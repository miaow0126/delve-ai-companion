# 下矿｜Delve v0.2.21.6.1 Patch Notes

Target: RC Polish Patch

## Scope

This patch follows v0.2.21.6. It does not change the core value curve or add a large system. It polishes repeated text, repeat counters, clue-track summaries, and 82k-400k feedback after external AI playtest feedback.

## Key Changes

- Created `delve.py` with save file `mine_v0221_6_1_save.json`.
- Added legacy migration from `mine_v0221_6_save.json`.
- Updated `VERSION` to `0.2.21.6.1-rc-polish`.
- Added routine auto-return message rotation:
  - expands the template pool to 19 lines,
  - uses current layer,
  - current map target,
  - recent discovery,
  - sample-bag handling,
  - occasional companion bias / restraint,
  - skips the last 5 used template indices.
- Rewrote repeated item wording:
  - `first_seen=false` now says same-kind sample / repeat sample / 第 N 次,
  - avoids treating duplicates as new collection records,
  - displayed occurrence now uses lifetime `collection_seen_counts`, not trimmed log counts.
- Added lightweight transition titles:
  - `冷光追迹者`
  - `晶洞巡灯人`
  - `菌光记事人`
  - `回光辨识者`
  - `深层路标手`
- Updated clue-track research copy:
  - first completion is treated as a real拼合,
  - second/third completions say another piece was added,
  - fourth and later completions switch to summary wording.
- Connected clue-track research copy to `result_panel`:
  - player-visible result panels now prefer `tr["line"]`,
  - old hardcoded `📜 线索拼合：...｜图鉴研究估值 +...` remains fallback only.
- Differentiated several decision C options:
  - C can now abandon the current side opportunity and return to the main target,
  - no permanent punishment,
  - no free consolation item for every C choice.
- Added emotional decision prompt de-dupe so the same large prompt cannot repeat as a three-prompt run.
- Added `qa_v02_21_6_1_rc_polish.py` with RC polish checks.

## Guardrails

- No deep curve retune.
- No new route tree.
- No permanent missable punishment.
- Companion bias is occasional and restrained.

## Files

- Main implementation: `delve.py`
- QA harness: `qa_v02_21_6_1_rc_polish.py`
- Regression report: `REGRESSION.md`
