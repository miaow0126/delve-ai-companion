#!/usr/bin/env python3
"""下矿 · 探险手帐 —— 只读展示台

跟 delve_mcp.py 同一目录部署，直接 import delve 复用它自己的 cmd() 逻辑
（status/museum/journal/titles 都是只读，不会碰存档），永远拿到游戏自己
算好的最新数据（评级/图鉴进度这些是运行时算的，不在存档里，靠这个办法
不用我们自己复刻一套规则表、也不会随着游戏更新过时）。

环境变量：
  DELVE_DISPLAY_PORT   展示台端口（默认 8901）
"""

import json
import os
import sys
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

PKG = os.path.dirname(os.path.abspath(__file__))
if PKG not in sys.path:
    sys.path.insert(0, PKG)

import delve

DISPLAY_PORT = int(os.environ.get("DELVE_DISPLAY_PORT", 8901))


# ── 读游戏自己算好的数据 ──────────────────────────────────

def safe_cmd(command):
    try:
        return delve.cmd(command)
    except Exception as e:
        return {"ok": False, "error": str(e)}


def load_overview():
    status = safe_cmd("status")
    st = status.get("state", {}) or {}
    rating = st.get("mining_rating", {}) or {}
    current = rating.get("current_rating", {}) or {}
    nxt = rating.get("next_rating") or {}
    return {
        "current_title": st.get("current_title"),
        "owned_title_count": st.get("owned_title_count", 0),
        "turn": st.get("turn", 0),
        "trip": st.get("trip", 1),
        "depth_m": st.get("depth_m", 0),
        "max_depth_m": st.get("max_depth_m", 0),
        "current_layer": st.get("current_layer"),
        "coins": st.get("coins", 0),
        "stamina": st.get("stamina"),
        "journal_count": st.get("journal_count", 0),
        "collection_total_value": st.get("collection_total_value", 0),
        "rating_icon": current.get("icon", ""),
        "rating_name": current.get("name", ""),
        "rating_tone": current.get("tone", ""),
        "next_rating_icon": nxt.get("icon", ""),
        "next_rating_name": nxt.get("name", ""),
        "remaining_to_next": rating.get("remaining_to_next"),
        "next_min_value": nxt.get("min_value"),
    }


JOURNAL_PAGE_SIZE = 20


def load_journal(page=1, page_size=JOURNAL_PAGE_SIZE):
    """journal_summary() 默认只给最近12页；这里直接调用底层函数（不走
    cmd() 的文本指令接口）传一个足够大的 limit，拿到全部手帐页再自己分页。"""
    try:
        j = delve.journal_summary(limit=100000)
    except Exception as e:
        return {"ok": False, "error": str(e)}
    pages = j.get("pages", []) or []
    pages = list(reversed(pages))  # 最新的在前面
    total = len(pages)
    start = (page - 1) * page_size
    slice_ = pages[start:start + page_size]
    out = [{
        "page_id": p.get("page_id"),
        "type": p.get("type"),
        "title": p.get("title"),
        "body": p.get("body"),
        "layer": p.get("layer"),
        "depth_m": p.get("depth_m"),
        "turn": p.get("turn"),
        "created_at": p.get("created_at"),
    } for p in slice_]
    return {
        "ok": True,
        "page": page,
        "page_size": page_size,
        "total": total,
        "has_more": start + page_size < total,
        "entries": out,
    }


CATEGORY_META = {
    "mineral": {"label": "矿物", "icon": "🪨"},
    "gem": {"label": "宝石", "icon": "💎"},
    "relic": {"label": "遗物", "icon": "🏺"},
    "fossil": {"label": "化石", "icon": "🦴"},
    "clue": {"label": "线索", "icon": "📜"},
}
RARITY_COLOR = {
    "普通": "#5a6b8c", "common": "#5a6b8c",
    "少见": "#3f8f6b", "uncommon": "#3f8f6b",
    "稀有": "#3f7ba6", "rare": "#3f7ba6",
    "史诗": "#8a5fc9", "epic": "#8a5fc9",
    "传说": "#d4a24e", "legendary": "#d4a24e",
}


_ITEM_LOOKUP = {it["id"]: it for it in delve.ITEMS}


def load_museum():
    raw = safe_cmd("museum")
    m = raw.get("museum") or raw
    cp = m.get("collection_progress") or {}
    progress = cp.get("categories", [])
    seen_ids = cp.get("seen_item_ids", []) or []
    seen_counts = cp.get("seen_counts", {}) or {}
    recent = m.get("recent_collection") or []

    # sections 只是引擎最近12次拾取的滚动窗口，不是去重藏品清单；
    # 真正完整的"每类发现了哪些藏品"要用 seen_item_ids 对照物品总表 ITEMS 自己拼。
    items_by_category = {}
    for iid in seen_ids:
        it = _ITEM_LOOKUP.get(iid)
        if not it:
            continue  # decision_*/track:* 这类动态生成的id不在静态总表里，图鉴分母也不算它们
        cid = it.get("category")
        items_by_category.setdefault(cid, []).append({
            "name": it.get("name"),
            "rarity": delve.RARITY_ZH.get(it.get("rarity"), it.get("rarity")),
            "seen_count": seen_counts.get(iid, 1),
            "description": it.get("description_seed") or "",
        })
    for cat_items in items_by_category.values():
        cat_items.sort(key=lambda x: -(x["seen_count"] or 0))

    categories = []
    for cat in progress:
        cid = cat.get("category")
        categories.append({
            "id": cid,
            "label": cat.get("label") or CATEGORY_META.get(cid, {}).get("label", cid),
            "icon": cat.get("icon") or CATEGORY_META.get(cid, {}).get("icon", "📦"),
            "seen": cat.get("seen", 0),
            "total": cat.get("total", 0),
            "items": items_by_category.get(cid, []),
        })
    recent_out = [{
        "name": r.get("name"), "category": r.get("category"),
        "rarity_zh": r.get("rarity_zh"), "value": r.get("value"),
        "first_seen": r.get("first_seen"), "turn": r.get("turn"),
    } for r in recent[-12:]]
    recent_out.reverse()
    return {"categories": categories, "recent": recent_out}


def load_titles():
    t = safe_cmd("titles")
    return t


# ── 展示页面 ──────────────────────────────────────────────

PAGE = r"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>下矿 · 探险手帐</title>
<style>
:root {
  --bg: #0a0e14;
  --surface: #0f1420;
  --card: #141a28;
  --card-hover: #1a2136;
  --border: #202940;
  --text: #dde3f0;
  --muted: #5a6b8c;
  --accent: #d4a24e;
  --accent-soft: #8a97b8;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: 'PingFang SC', 'Noto Sans SC', 'Helvetica Neue', sans-serif;
  height: 100vh;
  display: flex;
  flex-direction: column;
}
.header {
  padding: 16px 24px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 14px;
  background: var(--surface);
  flex-shrink: 0;
  flex-wrap: wrap;
}
.header h1 { font-size: 1.15rem; font-weight: 600; }
.header .rating { color: var(--accent); font-size: 0.85rem; }
.stats {
  margin-left: auto;
  display: flex;
  gap: 16px;
  font-size: 0.78rem;
  color: var(--muted);
  flex-wrap: wrap;
}
.stats b { color: var(--text); font-weight: 600; }
.progress-bar {
  width: 100%;
  height: 6px;
  background: var(--border);
  border-radius: 3px;
  overflow: hidden;
  margin-top: 6px;
}
.progress-bar-fill { height: 100%; background: var(--accent); }
.tabs {
  display: flex;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
  flex-shrink: 0;
}
.tab {
  padding: 10px 20px;
  font-size: 0.82rem;
  color: var(--muted);
  cursor: pointer;
  border-bottom: 2px solid transparent;
}
.tab.active { color: var(--accent); border-bottom-color: var(--accent); }
.main { flex: 1; overflow: hidden; display: flex; }
.panel { flex: 1; overflow-y: auto; display: none; }
.panel.active { display: block; }

/* 手帐流水账 */
.journal-feed { max-width: 720px; margin: 0 auto; padding: 24px 28px 60px; }
.journal-entry { padding: 18px 0; border-bottom: 1px solid var(--border); }
.journal-entry:first-child { padding-top: 0; }
.journal-entry-title { font-size: 1.02rem; font-weight: 700; margin-bottom: 6px; }
.journal-entry-meta { font-size: 0.72rem; color: var(--muted); margin-bottom: 10px; display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }
.journal-entry-body { font-size: 0.88rem; line-height: 1.9; white-space: pre-wrap; color: var(--text); }
.type-badge { display: inline-block; padding: 2px 8px; border-radius: 4px; background: var(--card); color: var(--accent); font-size: 0.68rem; }

/* 分页控件（手帐用） */
.pager { display: flex; align-items: center; justify-content: center; gap: 6px; margin-top: 20px; flex-wrap: wrap; }
.pager button {
  min-width: 34px; height: 34px; padding: 0 8px; border-radius: 6px; border: 1px solid var(--border);
  background: var(--card); color: var(--text); cursor: pointer; font-size: 0.8rem;
}
.pager button:hover:not(:disabled) { background: var(--card-hover); }
.pager button:disabled { opacity: 0.35; cursor: default; }
.pager button.current { border-color: var(--accent); color: var(--accent); }
.pager .ellipsis { color: var(--muted); padding: 0 4px; }

/* 藏品图鉴 */
.museum-body { padding: 24px 28px; }
.cat-row { margin-bottom: 28px; }
.cat-head { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; font-size: 0.9rem; font-weight: 600; }
.cat-head .count { margin-left: auto; color: var(--muted); font-size: 0.78rem; font-weight: 400; }
.card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }
.item-card {
  display: flex; flex-direction: column; height: 148px; padding: 12px 14px; border-radius: 8px;
  background: var(--card); border: 1px solid var(--border); border-left: 3px solid var(--rarity-color, var(--border));
}
.item-card-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 8px; margin-bottom: 6px; }
.item-card-name { font-size: 0.9rem; font-weight: 600; }
.item-card-rarity {
  flex-shrink: 0; font-size: 0.65rem; padding: 2px 7px; border-radius: 4px;
  background: color-mix(in srgb, var(--rarity-color, var(--muted)) 22%, transparent);
  color: var(--rarity-color, var(--muted));
}
.item-card-desc {
  flex: 1; font-size: 0.74rem; line-height: 1.55; color: var(--accent-soft);
  overflow: hidden; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical;
}
.item-card-foot { margin-top: 8px; font-size: 0.7rem; color: var(--muted); }
.empty-cat { color: var(--muted); font-size: 0.78rem; font-style: italic; }
.recent-list { margin-top: 28px; }
.recent-row { display: flex; gap: 10px; padding: 8px 0; border-bottom: 1px solid var(--border); font-size: 0.82rem; align-items: center; }
.recent-row .dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.recent-row .value { margin-left: auto; color: var(--accent); }

/* 称号簿 */
.titles-body { padding: 24px 28px; }
.title-card {
  display: flex; flex-direction: column; height: 128px; padding: 12px 14px; border-radius: 8px;
  background: var(--card); border: 1px solid var(--border);
}
.title-card.current { border-color: var(--accent); }
.title-card-name { font-size: 0.9rem; font-weight: 600; margin-bottom: 6px; display: flex; align-items: center; gap: 6px; }
.title-card.current .title-card-name { color: var(--accent); }
.title-card-desc {
  flex: 1; font-size: 0.74rem; line-height: 1.55; color: var(--accent-soft);
  overflow: hidden; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical;
}

.empty-state { display: flex; align-items: center; justify-content: center; height: 100%; color: var(--muted); font-size: 0.9rem; }
</style>
</head>
<body>
<div class="header">
  <span style="font-size:1.4rem">⛏️</span>
  <h1>下矿 · 探险手帐</h1>
  <span class="rating" id="rating-label">加载中…</span>
  <div class="stats" id="stats"></div>
</div>
<div style="padding: 0 24px; background: var(--surface); border-bottom: 1px solid var(--border);">
  <div class="progress-bar" id="rating-progress-bar" style="display:none"><div class="progress-bar-fill" id="rating-progress-fill"></div></div>
  <div style="font-size:0.68rem;color:var(--muted);padding:4px 0 8px" id="rating-progress-text"></div>
</div>
<div class="tabs">
  <div class="tab active" data-tab="journal" onclick="switchTab('journal')">📜 探险手帐</div>
  <div class="tab" data-tab="museum" onclick="switchTab('museum')">📚 藏品图鉴</div>
  <div class="tab" data-tab="titles" onclick="switchTab('titles')">🎖️ 称号簿</div>
</div>
<div class="main">
  <div class="panel active" id="panel-journal"><div class="journal-feed" id="journal-feed"></div></div>
  <div class="panel" id="panel-museum"><div class="museum-body" id="museum-body"></div></div>
  <div class="panel" id="panel-titles"><div class="titles-body" id="titles-body"></div></div>
</div>
<script>
function esc(s) { return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function fmtDate(iso) {
  if (!iso) return '';
  const d = new Date(iso.endsWith('Z') || iso.includes('+') ? iso : iso + 'Z');
  return d.toLocaleString('zh-CN', { month:'2-digit', day:'2-digit', hour:'2-digit', minute:'2-digit' });
}
function rarityColor(r) {
  const map = {"普通":"#5a6b8c","少见":"#3f8f6b","稀有":"#3f7ba6","史诗":"#8a5fc9","传说":"#d4a24e"};
  return map[r] || "#5a6b8c";
}

let journalData = [];

function switchTab(name) {
  document.querySelectorAll('.tab').forEach(t => t.classList.toggle('active', t.dataset.tab === name));
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.getElementById('panel-' + name).classList.add('active');
}

async function loadOverview() {
  const r = await fetch('/api/overview');
  const o = await r.json();
  document.getElementById('rating-label').textContent =
    `${o.rating_icon||''} ${o.rating_name||''}${o.current_title ? ' ｜ 🎖️ ' + o.current_title : ''}`;
  document.getElementById('stats').innerHTML = `
    <span>⛏️ 深度 <b>${o.depth_m||0}m</b></span>
    <span>🕯️ 灯火 <b>${esc(o.stamina||'')}</b></span>
    <span>🪙 金币 <b>${o.coins||0}</b></span>
    <span>💰 图鉴估值 <b>${o.collection_total_value||0}</b></span>
    <span>📜 手帐 <b>${o.journal_count||0}</b> 页</span>
  `;
  if (o.next_rating_name && o.remaining_to_next != null && o.next_min_value) {
    const cur = o.next_min_value - o.remaining_to_next;
    const pct = Math.max(2, Math.min(100, Math.round(cur / o.next_min_value * 100)));
    document.getElementById('rating-progress-bar').style.display = 'block';
    document.getElementById('rating-progress-fill').style.width = pct + '%';
    document.getElementById('rating-progress-text').textContent =
      `距「${o.next_rating_icon||''} ${o.next_rating_name}」还差 ${o.remaining_to_next}`;
  }
}

let journalPage = 1;
let journalTotalPages = 1;

function buildPager(current, total, onGoto) {
  if (total <= 1) return '';
  const pages = new Set([1, total, current, current - 1, current + 1]);
  const nums = [...pages].filter(p => p >= 1 && p <= total).sort((a, b) => a - b);
  let html = '<div class="pager">';
  html += `<button data-goto="${current - 1}" ${current <= 1 ? 'disabled' : ''}>‹ 上一页</button>`;
  let prev = 0;
  for (const p of nums) {
    if (prev && p - prev > 1) html += '<span class="ellipsis">…</span>';
    html += `<button data-goto="${p}" class="${p === current ? 'current' : ''}">${p}</button>`;
    prev = p;
  }
  html += `<button data-goto="${current + 1}" ${current >= total ? 'disabled' : ''}>下一页 ›</button>`;
  html += `<span style="color:var(--muted);font-size:0.75rem;margin-left:6px">共 ${total} 页</span>`;
  html += '</div>';
  return html;
}

function renderJournalEntries() {
  const feed = document.getElementById('journal-feed');
  if (!journalData.length) {
    feed.innerHTML = '<div class="empty-state">还没有手帐记录<br>下矿走一趟就有了</div>';
    return;
  }
  feed.innerHTML = journalData.map(p => `
    <div class="journal-entry">
      <div class="journal-entry-title">${esc(p.title)}</div>
      <div class="journal-entry-meta">
        <span class="type-badge">${esc(p.type||'')}</span>
        <span>${fmtDate(p.created_at)}</span>
        <span>📍 ${esc(p.layer||'')} · ${p.depth_m||0}m</span>
        <span>第 ${p.turn||'?'} 回合</span>
      </div>
      <div class="journal-entry-body">${esc(p.body)}</div>
    </div>
  `).join('') + buildPager(journalPage, journalTotalPages);
  feed.querySelectorAll('.pager button[data-goto]').forEach(btn => {
    btn.addEventListener('click', () => gotoJournalPage(parseInt(btn.dataset.goto, 10)));
  });
}

async function gotoJournalPage(page) {
  if (page < 1 || page > journalTotalPages) return;
  journalPage = page;
  const r = await fetch('/api/journal?page=' + page);
  const data = await r.json();
  if (data.ok) {
    journalData = data.entries;
    journalTotalPages = Math.max(1, Math.ceil(data.total / data.page_size));
  }
  renderJournalEntries();
  document.getElementById('panel-journal').scrollTo(0, 0);
}

async function loadJournal() {
  const r = await fetch('/api/journal?page=' + journalPage);
  const data = await r.json();
  if (!data.ok) {
    journalData = [];
    journalTotalPages = 1;
  } else {
    journalData = data.entries;
    journalTotalPages = Math.max(1, Math.ceil(data.total / data.page_size));
  }
  renderJournalEntries();
}

async function loadMuseum() {
  const r = await fetch('/api/museum');
  const m = await r.json();
  const body = document.getElementById('museum-body');
  let html = '';
  for (const cat of m.categories) {
    html += `<div class="cat-row">
      <div class="cat-head"><span>${cat.icon}</span><span>${esc(cat.label)}</span><span class="count">${cat.seen}/${cat.total}</span></div>
      <div class="card-grid">`;
    if (cat.items.length) {
      for (const it of cat.items) {
        const color = rarityColor(it.rarity);
        html += `<div class="item-card" style="--rarity-color:${color}">
          <div class="item-card-head">
            <span class="item-card-name">${esc(it.name)}</span>
            <span class="item-card-rarity">${esc(it.rarity||'')}</span>
          </div>
          <div class="item-card-desc">${esc(it.description || '暂无记录')}</div>
          <div class="item-card-foot">拾取 ×${it.seen_count||1}</div>
        </div>`;
      }
    } else {
      html += `<div class="empty-cat">还没发现</div>`;
    }
    html += `</div></div>`;
  }
  if (m.recent.length) {
    html += `<div class="recent-list"><div class="cat-head" style="margin-bottom:10px">🕒 最近入手</div>`;
    for (const r2 of m.recent) {
      html += `<div class="recent-row">
        <span class="dot" style="background:${rarityColor(r2.rarity_zh)}"></span>
        <span>${esc(r2.name)}</span>
        <span style="color:var(--muted)">${esc(r2.rarity_zh||'')}</span>
        <span class="value">+${r2.value||0}</span>
      </div>`;
    }
    html += `</div>`;
  }
  body.innerHTML = html || '<div class="empty-state">还没有藏品</div>';
}

async function loadTitles() {
  const r = await fetch('/api/titles');
  const t = await r.json();
  const body = document.getElementById('titles-body');
  const owned = t.owned_titles || t.titles || [];
  if (!owned.length) {
    body.innerHTML = '<div class="empty-state">还没有称号</div>';
    return;
  }
  const current = t.current_title;
  body.innerHTML = '<div class="card-grid">' + owned.map(item => {
    const isStr = typeof item === 'string';
    const label = isStr ? item : (item.name || JSON.stringify(item));
    const desc = isStr ? '' : (item.tone || '');
    const isCur = label === current;
    return `<div class="title-card ${isCur ? 'current' : ''}">
      <div class="title-card-name">${isCur ? '👑' : ''} ${esc(label)}</div>
      <div class="title-card-desc">${esc(desc || '暂无描述')}</div>
    </div>`;
  }).join('') + '</div>';
}

loadOverview();
loadJournal();
loadMuseum();
loadTitles();
setInterval(() => { loadOverview(); loadJournal(); loadMuseum(); loadTitles(); }, 30000);
</script>
</body>
</html>"""


class DisplayHandler(BaseHTTPRequestHandler):
    def _json(self, obj):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path, _, query = self.path.partition("?")
        if path == "/api/overview":
            self._json(load_overview())
        elif path == "/api/journal":
            qs = parse_qs(query)
            try:
                page = int(qs.get("page", ["1"])[0])
            except ValueError:
                page = 1
            self._json(load_journal(page=page))
        elif path == "/api/museum":
            self._json(load_museum())
        elif path == "/api/titles":
            self._json(load_titles())
        else:
            body = PAGE.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    print(f"[*] 下矿展示台启动  端口:{DISPLAY_PORT}")
    server = ThreadingHTTPServer(("0.0.0.0", DISPLAY_PORT), DisplayHandler)
    server.serve_forever()
