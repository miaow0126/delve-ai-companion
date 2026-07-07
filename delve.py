# -*- coding: utf-8 -*-
"""
下矿｜Delve v0.2.21.6.1 · RC Polish Patch

目标：不是做复杂挖矿游戏，而是做一个 AI 伴侣半托管下矿、带回地图感、宝石冲击、图鉴进度和少量真正插手点的轻量玩具。

AI 使用：
    from delve import cmd
    cmd("new")
    cmd("handshake defaults")
    cmd("dig")
    cmd("play 3")
    cmd("museum")
    cmd("journal")
    cmd("handoff")


v0.2.21.6.1 RC Polish Patch：
    - 不动核心数值曲线；修 20k→100k 试玩闷点：返营文案轮换、重复样本措辞、轻称号反馈、偏好轻露出和 decision C 选项取舍感。

v0.2.21.6 RC Readiness Soak：
    - 不大改核心曲线；补 300k/400k 跨线归因、400k+ post-ice handoff soak、QA rating summary 和前台首屏样本。

v0.2.21.5 Late-Midgame Pacing Patch：
    - 不加前台壳子；专修 100k→200k 过快和 200k 后专项 soak。
    - 降低 progress_token 直接估值，线索更偏“方向/研究”，不再像高额宝石一样打穿阶段。
    - 蓝灯晶腔 / 冷光晶簇 / 孢子灯芯石 / 石门粉痕拓片等桥段物降档，部分收益靠后续研究桥补足。
    - 中期桥段研究从一次推过 200k 改成更小台阶，让 100k→200k 至少多经历几段 play。
    - QA 脚本扩展 200k→400k post-ruin / ice-vein soak。

v0.2.21.4 Midgame Bridge Patch：
    - 不继续加前台壳子；重点修 20k→200k 后台可玩性桥段。
    - 20k→50k 保护发光晶洞窗口；菌菇洞窟先 peek，等晶洞有 2～3 个主场记忆或 50k 后再稳定接管。
    - 压低菌菇洞窟价值喷射，孢子灯芯石延后到本地目标后段；避免刚过 20k 直接打穿 100k。
    - 新增 100k→200k 过桥藏品/前兆，古代遗迹与冰封矿脉开始在中后段给可见 stakes。
    - 重复衰减进入后台选择层：showcase_core/story_anchor 第 3 次后不再反复抢主池，转研究/金币/区域进度。
    - 普通 spectator play 中重复样本会定期自动整理成金币，让情绪经济有可见钱包心跳。

v0.2.21.3 Frontstage Consistency & Legacy Cleanup：
    - 整体藏品图鉴是主收藏系统；display last 仅保留旧版兼容，不再影响收藏进度。
    - 样本袋不再是硬容量损失点；新藏品发现即收录，普通重复样本自动整理。
    - 首次新区域/地标/环境高光必须返回 scene_web_reference，前台优先尝试现实/气质网图。
    - 高价值藏品补 image_search_keywords / avoid_keywords，避免网图搜索跑成购物图、家装图或泛奇幻图。
    - 前台契约统一 collection_record / journal_write / scene_web_reference / typed_pending_tasks 的真实边界。

v0.2.19 Curve & Area Pacing Patch：
    - 不重做 v0.2.18 主循环，只做节奏调音：压数值喷射、排区域出场、修背包显示、继续降噪轻风险/轻决策。
    - abandoned_lift 早期估值降档：升降井代表物仍有价值，但不再刚过 350 门槛就把图鉴身价喷到 9000+。
    - 新增 soft progress milestones：350 → 20000 之间给地下河记录、升降井线索、旧矿工线等近期台阶，避免只看一个巨大差距。
    - 新增 area pacing memory：河道探矿者后先建立 2～3 次地下河主场记忆，再让废弃升降井成为主舞台。
    - locked_layer_peek 降频：过远的冰封矿脉/遗迹层不再太早抢镜，只在估值/距离足够时作为远景前兆出现。
    - 背包改成半托管样本袋口径，避免出现 13/7 这种像越界错误的显示。
    - 轻风险和轻决策继续收窄：没有收藏、线索或地图价值的打断降频/补足结算价值。


v0.2.18 Early Progress & Repeat Loop Patch：
    - 修复早期进度死锁：评级锁稳定地层 + 浅层池抽完 + 重复不涨图鉴估值导致主循环卡住。
    - 河道探矿者门槛下调到 350，并新增浅层 bridge items / 深度边缘样本，让浅层足够桥接第一档评级。
    - depth 不再只是稀有率权重：不同深度会开放浅层深处 / 地下河前兆 / 升降井前兆候选。
    - 新增 progress_stall_count / repeat_item_streak 的轻 pity：长时间没新图鉴时，未见物和 bridge items 权重提高。
    - 重复稀有 / 套装件强制降级：首次完整高光，重复转为副样本/研究材料，避免锈灯钩第 61 次还抢主画面。
    - 新增 clue_tracks：墙缝冷风、旧靴印、锈灯钩、木撑架红线等小迹象会累计成「旧矿工遗留」「冷缝异常」「被标记的支道」等线索进度。
    - 区分藏品图鉴与区域探索度：物件看全局图鉴，区域看探索百分数；stable_layer / raw_depth_layer / locked_layer_peek 分开显示。

v0.2.17 Visual Translation & Aesthetic Treasure Pass：
    - 新增 treasure_profile：给矿石/宝石/遗物补体量、视觉锚点、触感、鉴定感和可配图方向。
    - 新增 visual_translation：高光发现不只写“很美/很高级”，必须提取颜色、光感、结构、材质、体量、环境等可视锚点。
    - 新增 Aesthetic Mining Rule：矿洞审美是女性向轻奇幻地下收藏，不是硬核矿工下井；漂亮、神秘、可收藏、可配图优先。
    - 高光战报的目的不是写长，而是把 AI 被文字打动的地方翻译成画面：网图方向、视觉锚点和 AI 玩家即时反应。
    - handoff / frontstage_render_plan 增加视觉翻译规则，避免模型只靠稀有度标签空喊高级。

v0.2.16 Spine Alignment & Treasure Reaction Pass：
    - 新增图鉴估值 / 探矿评级：用“挖到过的价值”形成简单粗暴正反馈，不按当前金币扣减。
    - 高级矿区价值跃迁：深层普通矿也更值钱，稀有/史诗/传说矿承担视觉冲击。
    - 新增 area_preview / mining_drive：未解锁区域只露预告藏品，让 AI 玩家知道自己在追什么。
    - 工具升级增加名称、悬念牌与验证回声：升级不念公式，后续靠战报验证变强。
    - 新增 temporary_heat / 晶脉共振等短期追逐感：不做复杂状态，只给 AI 一个“趁现在再来一下”的理由。
    - companion_reaction 继续作为 AI 玩家情绪层，高光时可短暂破格，但不创造事实。

v0.2.14 Semi-managed Collection & Reward Spine：
    - map_strip 强制 block 化：返回 card_text 时必须贴小地图块，不可压成一句摘要。
    - 默认半托管：补灯、普通矿处理、图鉴记录等小事由 AI 玩家处理，减少琐碎询问。
    - 整体藏品图鉴是主收藏系统：拿到即记录图鉴，display last 仅保留兼容。
    - 新增 collection_progress / collection_panel：矿物、宝石、遗物、化石、线索形成长期收集目标。
    - 稀有/史诗/传说发现有 rarity_ritual_card 与 companion_reaction，强化挖到好东西的情绪。
    - decision_prompt 降频并做最近模板去重；B 选项支持轻随机与坏运气保护。
    - 明确 sell last / sell <uid|name>：非故事类矿石/宝石可明确出售，图鉴记录保留。

v0.2.11 前台防漏补丁：
    - 新增 frontstage_required_blocks / frontstage_contract：如果 milestone_card / region_map 存在，必须原样展示 card_text，不能只在摘要里说“有地图”。
    - v0.2.11：新增 Frontstage Delivery Checklist，正式反馈前逐项自检主画面、地图牌、网图、真实结果、事实边界、写入状态和下一步建议。
    - 地图牌是正式战报的必交付块：区域牌/局部地图 → 网图参考 → 战报正文。漏贴 card_text 视为本轮前台交付未完成。
    - map_card 和 web_reference 分工继续保持：地图讲结构，网图讲气质；地图牌不能替代网图，网图也不能替代区域图。
    - v0.2.13：danger_low_light 无 episode 时仍使用短模板，但必须带 map_strip 解释“现在在哪 / 下次去哪”。

v0.2.9 上架前收口补丁：
    - 不新增玩法，不做完整 world_map；只修前台模板、命名和执行纪律。
    - danger_low_light 使用固定短模板：安全停不是 episode，不硬凑主画面、不配图。
    - “菌丝地图”改名为“菌丝线路纹”，避免和系统 region_map / map 命令混淆。
    - milestone_card 增加 card_family / presentation_type，区分空间地图牌、称号牌和故事牌。
    - cmd("map") 明确只是当前区域局部图，不是完整地下总览。
    - 下一步建议应结合 region_map 里的 ❓ / 未探明支路；地图讲结构，也帮助解释为什么下一步去那里。
    - medium/high episode_shot 继续钉死：能联网拉图就必须实际拉网图；关键词只是兜底；不得自动生图。

v0.2.8 地图感补丁：
    - 新增 milestone_card / 区域牌：新地层、新地点、故事完成等大节点给轻量 ASCII 过场牌。
    - 新增 region_map / 局部区域图：当前地层用入口、支路、地标和 ⭐ 当前位置表达轻迷宫感。
    - 地图讲结构，网图讲气质，战报讲事实；地图不替代网图、不替代真实写入。
    - 本轮只做表现层资产，不做完整 world_map、坐标、路线选择或寻路系统。

v0.2.7 可展示性补丁：
    - 一个合格的 episode_shot / main_shot 应该能被 1-3 个现实/气质网图关键词接住。
    - 气质命中优先于完全贴切：参考图只需承载主画面的气氛，不要求等于游戏事实。
    - 如果节点太具体、太抽象或长期难以搜图，应回修命名、real_anchors、visual_keywords、caption_seed 或内容本身，而不是让 AI 硬搜/硬生图。

v0.2.6 视觉交付补丁：
    - episode_shot 的 medium/high 视觉节点必须优先实际拉网图/气质图，不允许只给关键词敷衍。
    - 默认希望一次正式反馈给多张参考图；目标 4 张，数量不硬卡，视平台能力而定。
    - 关键词仅在无法拉图、搜索不可用或搜索明显不准时作为兜底。
    - 生图不是默认 fallback；AI 不得因为忘记配网图而擅自改成生成图片。
    - 若某个节点长期难以配图，应回修 visual_keywords / real_anchors / caption_seed 或内容本身，而不是改用生图掩盖。

v0.2.4 视觉停顿补丁：
    - 参考瓶中生态二改 pacing：不是每一镐都汇报，而是出现值得被看见的地下画面再回来。
    - medium/high visual 不再自动强停；只有形成可展示 episode_shot 才停。
    - small_find / trace / 普通漂亮物默认是 flavor node，只作路上小味道。
    - 正式战报必须有 episode_shot；episode_shot 优先拉网图，关键词兜底，生图非默认。
    - 新增 episode_candidate / stop_for_episode / visual_delivery 字段，便于 Codex 测试。

v0.2.4 上架前微调：
    - 重复 high 物品压缩：重复史诗/传说物不再自动抢主画面，除非产生新地层/新故事/新陈列意义。
    - medium small_find focus limit：一段 play 只展开一个主画面，小发现遇到 high/rare/story 节点自动退后。
    - inferred_mood frontstage narrowing：小发现只提示质感和气氛，不扩写成世界观.

v0.2.2 玩具感补丁：
    - 增加 small_find 小发现池：不进背包、不强制配图、不增加系统，只给 AI 一口可讲的味道。
    - 增加 toy_feel / frontstage_guidance：后台字段继续稳，前台战报更轻快，不直接念协议名。
    - 调整普通探索密度：普通回合也更常出现可念叨的小东西，避免纯资源表。
    - play 战报提示加入“每段只展开一个主画面，其余压缩”的观看节奏。

v0.2.1 窄修重点：
    - 重复迹象/重复少见物压缩提示。
    - 跨层重复地标变体命名。
    - display last 使用保存确认型返回。
    - typed_pending_tasks 区分命令待办和战报待办，同时保留 legacy pending_tasks。
    - fantasy/story 关键词补现实锚点。

v0.2 重点：
    - handshake 门禁：未完成首次陪玩确认前，不允许推进游戏。
    - main_shot：每轮都有“今日主画面”。
    - visual_mode：object / scene / story 三分。
    - truth_level：real_result / inferred_mood / imagined_reconstruction 三档。
    - pending_tasks：视觉、陈列、故事、称号、返程等待办强提醒。
    - 真实写入：整体藏品图鉴 / 探险手帐必须由 cmd() 成功写入后才能说“已保存”。
    - spectator-friendly autoplay：AI 可继续玩，但不按 medium 视觉机械停；出现 episode_shot 或安全/资源原因才停。

边界：
    real_result 是唯一游戏事实。
    narrative_seed / caption_seed / companion_drive 只给 AI 讲述角度，不能新增掉落、金币、地层或剧情事实。
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

SAVE_FILE = os.path.join(os.path.dirname(__file__), "mine_v0221_6_1_save.json")
LEGACY_SAVE_FILES = [
    os.path.join(os.path.dirname(__file__), "mine_v0221_6_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0221_5_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0221_4_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0221_3_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0221_2_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0221_1_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0221_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0220_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0218_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0217_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0216_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0215_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0214_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0213_save.json"),
    os.path.join(os.path.dirname(__file__), "mine_v0212_save.json"),
]

VERSION = "0.2.21.6.1-rc-polish"

RARITY_RANK = {
    "common": 1,
    "uncommon": 2,
    "rare": 3,
    "epic": 4,
    "legendary": 5,
}
RARITY_ZH = {
    "common": "普通",
    "uncommon": "少见",
    "rare": "稀有",
    "epic": "史诗",
    "legendary": "传说",
}
VISUAL_PRIORITY_RANK = {"low": 1, "medium": 2, "high": 3}


# v0.2.16: reward spine. Values are intentionally stagey, not an economy sim.
# Later areas should make the AI/player feel "we are not in the starter cave anymore".
LAYER_VALUE_MULTIPLIER = {
    "shallow_mine": 1,
    "underground_river": 12,
    "abandoned_lift": 12,  # v0.2.19: tuned down from 35; lift should feel richer, not skip the whole second act.
    "glowing_crystal_cave": 92,
    "mushroom_cavern": 58,
    "ancient_ruins": 380,
    "ice_vein": 90,
    "deep_altar": 5000,
}
RARITY_VALUE_MULTIPLIER = {
    "common": 1.0,
    "uncommon": 1.4,
    "rare": 2.2,
    "epic": 4.0,
    "legendary": 8.0,
}
MINING_RATINGS = [
    {"id": "surface_gleaner", "icon": "🥉", "name": "浅层拾矿人", "min_value": 0, "unlock_layers": ["shallow_mine"], "tone": "能稳定处理入口附近的矿脉。"},
    {"id": "river_prospector", "icon": "🥉", "name": "河道探矿者", "min_value": 350, "unlock_layers": ["underground_river", "abandoned_lift"], "tone": "地下河开始稳定探索；旧升降井会逐步浮出，不再一解锁就抢走主舞台。"},
    {"id": "crystal_prospector", "icon": "🥈", "name": "晶脉探矿者", "min_value": 20000, "unlock_layers": ["glowing_crystal_cave", "mushroom_cavern"], "tone": "从这里开始，普通晶屑也会比浅层矿石值钱得多。"},
    {"id": "ruin_surveyor", "icon": "🥇", "name": "遗迹勘探者", "min_value": 200000, "unlock_layers": ["ancient_ruins", "ice_vein"], "tone": "古代遗迹和冰封矿脉会给出更重的估值跃迁。"},
    {"id": "star_vein_guest", "icon": "👑", "name": "深层星脉客", "min_value": 1000000, "unlock_layers": ["deep_altar"], "tone": "深层祭坛的矿尘本身就像一条小型金脉。"},
]

# v0.2.19: soft pacing rungs between formal ratings. These do not unlock huge
# systems; they give the AI a nearer target while 350 -> 20000 remains the formal
# crystal rating gap.
CURVE_SOFT_MILESTONES = [
    {"value": 1200, "name": "地下河记录稳定", "line": "地下河不只是气味了，开始有自己的样本记忆。", "map_image": "蓝光水线第一次在地图边缘成形。", "ai_chase": "我想沿着水痕再摸一段，不急着跳层。"},
    {"value": 3000, "name": "升降井线索成形", "line": "旧升降井线能被看见，但还不该吞掉地下河主场。", "map_image": "地图侧边多出一截锈链井壁。", "ai_chase": "那截锈链不像装饰，我会把它当下一条追线。"},
    {"value": 6000, "name": "旧矿工线加深", "line": "重复旧物开始拼出更清楚的旧矿工路线。", "map_image": "旧矿工线从散点变成一条断续路线。", "ai_chase": "我开始怀疑这些旧物不是随机掉落，是有人一路留下的。"},
    {"value": 10000, "name": "晶脉前兆变明显", "line": "更亮的晶脉开始有远处诱饵，但还不到稳定进入。", "map_image": "地图下沿第一次出现冷白裂光。", "ai_chase": "这不是完整晶洞，但我能听见里面有空腔。"},
    {"value": 13000, "name": "晶脉声音变近", "line": "锈链井壁后面开始有很轻的空腔回声。", "map_image": "废弃升降井下沿多出一条冷白回声缝。", "ai_chase": "我不想立刻宣布新区域，但这条回声缝值得追。"},
    {"value": 16000, "name": "第一枚晶洞样本", "line": "真正的晶洞边缘第一次能带回一小片样本。", "map_image": "地图边缘出现一小块蓝白晶面，不再只是气味。", "ai_chase": "这枚样本够小，但足够让我下一趟沿裂光走。"},
    {"value": 18000, "name": "晶脉入口确认", "line": "晶脉入口已经能被确认，但还差一点图鉴身价才能稳定进入。", "map_image": "冷白裂光连成一段门框形状。", "ai_chase": "我已经知道门在哪了，现在只差把图鉴身价抬到能稳进去。"},
]

# New-area pacing: after the first formal unlock, let underground_river breathe
# before abandoned_lift becomes the default stage.
AREA_PACING_MEMORY_REQUIRED = {"underground_river": 3}

# Locked peeks should tease, not steal focus. Far layers need some appraisal mass
# before they surface as a frontstage peek.
PEEK_MIN_VALUE_BY_LAYER = {
    "glowing_crystal_cave": 6000,
    "mushroom_cavern": 7000,
    "ancient_ruins": 10000,
    "ice_vein": 12000,
    "deep_altar": 50000,
}
UPGRADE_STAGE_NAMES = {
    "pickaxe": ["旧铁镐", "裂石镐", "蓝钢镐", "晶脉镐", "星纹破岩镐"],
    "lantern": ["旧矿灯", "稳焰灯", "蓝焰矿灯", "晶芯矿灯", "星火提灯"],
    "rope": ["旧绳索", "稳结绳", "深井绳", "冰脉索", "星纹安全索"],
    "backpack": ["旧背包", "加固背包", "矿样背包", "晶匣背包", "星纹行囊"],
}
UPGRADE_SUSPENSE = {
    "pickaxe": "它比旧镐轻了一点，敲在岩壁上的声音也更脆。我不敢说一定会出大货，但下一趟也许能挖得更顺。",
    "lantern": "火苗稳了不少，光圈边缘不再抖得那么厉害。也许下次能多看一眼地图上的 ❓。",
    "rope": "绳结收得更紧，往深处走时心里会稳一点。它不会替我冒险，但能让我少一点狼狈。",
    "backpack": "这只包不只是更大，隔层也更稳。普通矿样我会自己打包整理，不再拿这种小事烦你。",
}
AREA_PREVIEW_TEASES = {
    "shallow_mine": [
        {"name": "石英矿砂", "rarity": "common", "icon": "🪨"},
        {"name": "蕨叶化石片", "rarity": "rare", "icon": "🦴"},
        {"name": "锈灯钩", "rarity": "uncommon", "icon": "🏺"},
    ],
    "underground_river": [
        {"name": "湿蓝矿砂", "rarity": "common", "icon": "🌊"},
        {"name": "蓝方解石", "rarity": "uncommon", "icon": "💎"},
        {"name": "湿痕符文板", "rarity": "rare", "icon": "📜"},
    ],
    "abandoned_lift": [
        {"name": "锈链矿屑", "rarity": "common", "icon": "🪨"},
        {"name": "断裂升降牌", "rarity": "rare", "icon": "🏺"},
        {"name": "未寄出的纸条", "rarity": "epic", "icon": "📜"},
    ],
    "glowing_crystal_cave": [
        {"name": "冷光晶屑", "rarity": "common", "icon": "💎"},
        {"name": "回声紫晶簇", "rarity": "epic", "icon": "💎"},
        {"name": "未确认的深蓝核心", "rarity": "legendary", "icon": "👑"},
    ],
    "mushroom_cavern": [
        {"name": "绿孢矿粉", "rarity": "common", "icon": "🍄"},
        {"name": "菌丝线路纹", "rarity": "rare", "icon": "📜"},
        {"name": "会呼吸的孢子灯海", "rarity": "epic", "icon": "🍄"},
    ],
    "ancient_ruins": [
        {"name": "符纹石屑", "rarity": "common", "icon": "🪨"},
        {"name": "黑石城印", "rarity": "epic", "icon": "🏺"},
        {"name": "石门眼纹", "rarity": "epic", "icon": "📜"},
    ],
    "ice_vein": [
        {"name": "冻蓝矿砂", "rarity": "common", "icon": "🧊"},
        {"name": "冰中鱼影化石", "rarity": "epic", "icon": "🦴"},
        {"name": "未确认的冰窗核心", "rarity": "legendary", "icon": "👑"},
    ],
    "deep_altar": [
        {"name": "黑星矿尘", "rarity": "common", "icon": "🌌"},
        {"name": "星脉矿", "rarity": "legendary", "icon": "👑"},
        {"name": "祭坛镜片", "rarity": "legendary", "icon": "🏺"},
    ],
}

# ─────────────────────────────────────────────────────────────
# Deterministic tiny RNG: repeatable enough for internal tests.
# ─────────────────────────────────────────────────────────────

def _imul(a: int, b: int) -> int:
    return ((a & 0xFFFFFFFF) * (b & 0xFFFFFFFF)) & 0xFFFFFFFF


def rng_random(state: Dict[str, Any]) -> float:
    seed = state.get("rng_seed", 0x9E3779B9) & 0xFFFFFFFF
    calls = state.get("rng_calls", 0) + 1
    seed = (seed + 0x6D2B79F5) & 0xFFFFFFFF
    state["rng_seed"] = seed
    state["rng_calls"] = calls
    t = _imul(seed ^ (seed >> 15), 1 | seed)
    t = ((t + _imul(t ^ (t >> 7), 61 | t)) & 0xFFFFFFFF) ^ t
    t &= 0xFFFFFFFF
    return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296


def rng_int(state: Dict[str, Any], a: int, b: int) -> int:
    return a + int(rng_random(state) * (b - a + 1))


def rng_choice(state: Dict[str, Any], values: List[Any]) -> Any:
    if not values:
        raise ValueError("rng_choice() got empty list")
    return values[rng_int(state, 0, len(values) - 1)]


def weighted_choice(state: Dict[str, Any], weighted: List[Tuple[Any, float]]) -> Any:
    total = sum(max(0.0, w) for _, w in weighted)
    if total <= 0:
        return weighted[0][0]
    r = rng_random(state) * total
    upto = 0.0
    for value, weight in weighted:
        upto += max(0.0, weight)
        if upto >= r:
            return value
    return weighted[-1][0]


# ─────────────────────────────────────────────────────────────
# Content pool: deliberately small but flavor-first for v0.2 tests.
# ─────────────────────────────────────────────────────────────

LAYERS: List[Dict[str, Any]] = [
    {
        "id": "shallow_mine",
        "name": "浅层矿洞",
        "depth_min": 0,
        "risk": 0.04,
        "visual_tone": "温暖土黄、旧木梁、矿灯小光圈、湿岩壁",
        "visual_keywords": ["abandoned mine tunnel", "old wooden mine supports", "dim lantern underground mine"],
        "arrival_caption": "旧木梁贴着湿岩壁往下延伸，矿灯只照出一小圈土黄色的光。",
    },
    {
        "id": "underground_river",
        "name": "地下河",
        "depth_min": 24,
        "risk": 0.07,
        "visual_tone": "幽蓝水流、潮湿回声、黑水反光",
        "visual_keywords": ["underground river cave", "blue reflection cave water", "fantasy subterranean river"],
        "arrival_caption": "岩壁后面的声音突然变空，黑水从低处露出来，像地底第一次开口说话。",
    },
    {
        "id": "abandoned_lift",
        "name": "废弃升降井",
        "depth_min": 44,
        "risk": 0.10,
        "visual_tone": "锈链、悬吊感、旧矿灯、半塌木梯",
        "visual_keywords": ["abandoned mine elevator shaft", "rusty mine lift", "old mining shaft lantern"],
        "arrival_caption": "一截锈链垂进黑暗，下面没有回声，只有矿灯照到的铁锈一点点发红。",
    },
    {
        "id": "glowing_crystal_cave",
        "name": "发光晶洞",
        "depth_min": 62,
        "risk": 0.06,
        "visual_tone": "冷蓝冷紫、晶簇、微光尘埃、安全但陌生",
        "visual_keywords": ["glowing crystal cave", "blue luminous crystals underground", "fantasy crystal cavern"],
        "arrival_caption": "最后一层岩壁裂开时，冷光不是照进来，而是从墙后慢慢涌出来。",
    },
    {
        "id": "mushroom_cavern",
        "name": "菌菇洞窟",
        "depth_min": 92,
        "risk": 0.09,
        "visual_tone": "暖绿荧光、柔软孢子、像会呼吸的地毯",
        "visual_keywords": ["bioluminescent mushroom cave", "glowing fungi cavern", "fantasy underground mushroom forest"],
        "arrival_caption": "脚下的岩石变软了，绿色孢子像小灯一样沿着缝隙亮起来。",
    },
    {
        "id": "ancient_ruins",
        "name": "古代遗迹层",
        "depth_min": 130,
        "risk": 0.12,
        "visual_tone": "断裂石门、微光符文、沉默台阶、安静庄重",
        "visual_keywords": ["ancient underground ruins", "forgotten stone ruins cave", "fantasy subterranean temple ruins"],
        "arrival_caption": "镐尖敲到的不是岩层，而是一块被埋住的石阶。它向下，向更深处，安静得像在等人。",
    },
    {
        "id": "ice_vein",
        "name": "冰封矿脉",
        "depth_min": 188,
        "risk": 0.14,
        "visual_tone": "冷白蓝调、冰层、冻住的气泡、古老安静",
        "visual_keywords": ["ice cave mineral vein", "frozen crystal cave", "blue ice cavern fantasy"],
        "arrival_caption": "岩壁忽然变成蓝白色，冰层里封着一串气泡，像地底很久以前吸过一口气。",
    },
    {
        "id": "deep_altar",
        "name": "深层祭坛",
        "depth_min": 260,
        "risk": 0.16,
        "visual_tone": "黑石祭坛、星点矿尘、无声压迫但不恐怖",
        "visual_keywords": ["deep underground altar", "dark crystal altar cave", "ancient subterranean shrine fantasy"],
        "arrival_caption": "这里没有回声。矿灯照在黑石上，光像被慢慢收走。",
    },
]

# v0.2.21.1: Scene reference bible. These are not shown every turn; they give
# frontstage models stable visual anchors for region first-sight, map transition,
# and environment-driven highlights. Scene references answer "where am I"; item
# references answer "what did I find".
SCENE_VISUAL_PROFILES: Dict[str, Dict[str, Any]] = {
    "shallow_mine": {
        "scene_render_priority": "transition_stage",
        "visual_identity": "入口旧矿道，木撑架、湿岩壁和细冷风组成第一张游戏地图。",
        "palette": ["灰褐", "旧木色", "矿灯暖黄", "微冷白"],
        "lighting": "近处矿灯暖光，远处冷风暗缝；不要工业采矿强光。",
        "atmosphere": "轻紧张、干净旧矿道、小博物馆序章。",
        "material_language": ["湿岩壁", "旧木撑架", "碎石粉", "细砂反光"],
        "landmark_elements": ["木撑架主道", "化石侧廊", "冷缝侧道", "旧矿工营地"],
        "screenshot_anchor": "木撑架主道尽头吹来冷风，侧边一个化石侧廊 ❓ 等着小机去摸。",
        "image_direction": "old mine tunnel with wooden supports, warm lantern light, damp rock wall, small mysterious side crack, cozy fantasy exploration",
        "image_search_keywords": ["old mine tunnel wooden supports", "abandoned mine lantern", "damp cave wooden beam"],
        "avoid_keywords": ["industrial mining machinery", "horror", "blood", "collapse disaster"],
    },
    "underground_river": {
        "scene_render_priority": "core_stage",
        "visual_identity": "黑水、蓝光水痕和半淹没结构，让矿洞第一次像活的地底世界。",
        "palette": ["湿黑", "深青", "水蓝荧光", "矿灯微黄"],
        "lighting": "蓝光从水面和湿岩反射出来，矿灯只做近处边缘光。",
        "atmosphere": "潮湿、回声、安静但有向下的诱惑。",
        "material_language": ["黑水反光", "水蚀岩", "湿石台", "蓝色沉积"],
        "landmark_elements": ["蓝光水潭", "半淹没石门", "湿痕拐角", "漂木浅滩"],
        "screenshot_anchor": "蓝光水潭映亮半淹没石门，水面反出一圈矿灯微光。",
        "image_direction": "subterranean river cave, blue glowing water reflection, half-submerged stone doorway, atmospheric but not horror",
        "image_search_keywords": ["underground river cave blue light", "subterranean river glowing water", "fantasy cave river"],
        "avoid_keywords": ["monster", "flood disaster", "dark horror"],
    },
    "abandoned_lift": {
        "scene_render_priority": "core_stage",
        "visual_identity": "锈链、垂直井壁、旧平台和旧矿工故事线交汇的运输中枢。",
        "palette": ["锈棕", "铁灰", "冷白粉尘", "暗铜"],
        "lighting": "井口漏光很弱，铁链边缘有冷反光，深处保持不可见。",
        "atmosphere": "旧工业遗留，但不脏乱压迫；重点是有人来过。",
        "material_language": ["锈铁链", "木梯残骸", "铜牌", "井壁冷白裂光"],
        "landmark_elements": ["升降井井壁", "升降井休息点", "锈链悬点", "晶洞边缘"],
        "screenshot_anchor": "铁链垂落到井下平台，旧升降牌半挂在边缘，井壁下方露出一条冷白裂光。",
        "image_direction": "abandoned mine elevator shaft, rusty chains, wooden platform, cold white crystal crack in wall, cinematic game UI feel",
        "image_search_keywords": ["abandoned mine elevator shaft", "rusty mining lift shaft", "old mine chains"],
        "avoid_keywords": ["gore", "industrial accident", "grimy realism"],
    },
    "glowing_crystal_cave": {
        "scene_render_priority": "core_stage",
        "visual_identity": "冷白裂光、蓝紫晶面和空腔反光组成地下星空。",
        "palette": ["冷白", "蓝白", "紫晶", "深蓝"],
        "lighting": "晶面内发光、裂缝回光、空腔漫反射；矿灯在这里退居边缘。",
        "atmosphere": "安静、漂亮、像进入大型矿物标本盒。",
        "material_language": ["晶簇", "晶洞空腔", "半透明晶面", "冷光尘"],
        "landmark_elements": ["晶洞门槛", "镜面矿壁", "晶洞内径", "紫晶簇"],
        "screenshot_anchor": "冷白裂光沿石壁爬开，中央露出一簇紫晶核心。",
        "image_direction": "glowing crystal cave, blue white light, amethyst cluster, underground geode cavern, beautiful mineral specimen atmosphere",
        "image_search_keywords": ["glowing crystal cave", "amethyst crystal cavern", "underground geode cave", "blue crystal cave"],
        "avoid_keywords": ["neon sci-fi lab", "overly cute fairy", "horror cave"],
    },
    "mushroom_cavern": {
        "scene_render_priority": "core_stage",
        "visual_identity": "菌丝桥、孢子灯海和柔雾光点构成潮湿生长的地下温室。",
        "palette": ["墨绿", "菌光黄", "孢子白", "潮湿棕"],
        "lighting": "孢子点光源和菌盖柔光，低雾让远处桥面微微散开。",
        "atmosphere": "柔软、潮湿、会呼吸，但不黏腻恐怖。",
        "material_language": ["菌丝", "湿石", "发光菌盖", "孢子雾"],
        "landmark_elements": ["孢子坡道", "菌丝桥", "孢子灯海", "旧篮筐角落"],
        "screenshot_anchor": "菌丝桥横跨孢子灯海，空气里全是发亮孢子。",
        "image_direction": "bioluminescent mushroom cave, glowing fungi, mycelium bridge, soft spores, underground fantasy greenhouse",
        "image_search_keywords": ["bioluminescent mushroom cave", "glowing fungi cavern", "fantasy mushroom underground"],
        "avoid_keywords": ["toxic horror fungus", "body horror", "zombie spores"],
    },
    "ancient_ruins": {
        "scene_render_priority": "core_stage",
        "visual_identity": "断裂石门、微光符文和沉默台阶，让旧文明线从藏品变成空间。",
        "palette": ["冷灰", "黑石", "幽蓝符文", "尘白"],
        "lighting": "符文边缘微光，石门缝里有低亮度蓝光。",
        "atmosphere": "庄重、安静、不是战斗遗迹。",
        "material_language": ["断裂石门", "磨损台阶", "符文石板", "黑石封印"],
        "landmark_elements": ["断裂石门", "符文廊道", "无声祭坛", "石门眼纹"],
        "screenshot_anchor": "断裂石门后露出微蓝符文，台阶向下消失。",
        "image_direction": "ancient underground ruins, broken stone gate, blue glowing runes, quiet fantasy subterranean temple",
        "image_search_keywords": ["ancient underground ruins", "stone gate cave runes", "subterranean temple fantasy"],
        "avoid_keywords": ["battle scene", "skeleton horror", "blood altar"],
    },
    "ice_vein": {
        "scene_render_priority": "support_stage",
        "visual_identity": "蓝白冰层、冻住气泡和冰窗化石，让时间像被冷藏在矿脉里。",
        "palette": ["冰蓝", "冷白", "灰蓝", "透明裂纹"],
        "lighting": "冰层折射矿灯，远处有蓝白冷光。",
        "atmosphere": "安静、轻冷、像冻住的博物馆柜。",
        "material_language": ["蓝冰", "冻结气泡", "冰窗", "霜纹晶体"],
        "landmark_elements": ["冻气泡墙", "化石冰窗", "旧矿工营地遗址"],
        "screenshot_anchor": "冰窗里封着鱼影，旁边霜纹晶体像小型冷光灯。",
        "image_direction": "blue ice cave mineral vein, fossil trapped in ice, frozen crystal cavern, quiet and beautiful",
        "image_search_keywords": ["blue ice cave", "frozen crystal cave", "fish fossil in ice"],
        "avoid_keywords": ["survival horror", "frostbite injury", "dark monster"],
    },
    "deep_altar": {
        "scene_render_priority": "support_stage",
        "visual_identity": "黑石祭坛、星点矿尘和无声回光，深但不恐怖。",
        "palette": ["黑石", "星白", "幽蓝", "暗金"],
        "lighting": "黑石吃光，星尘自己发出很小的点光。",
        "atmosphere": "压低声音、庄重、像抵达旧世界最深的标本柜。",
        "material_language": ["黑石祭坛", "星点矿尘", "镜片", "祭坛玉"],
        "landmark_elements": ["无声祭坛", "石门眼纹", "深处仍未探明"],
        "screenshot_anchor": "黑石祭坛上散着星点矿尘，矿灯光被慢慢收走。",
        "image_direction": "deep underground black stone altar, tiny star mineral dust, blue light relic, elegant fantasy not horror",
        "image_search_keywords": ["dark stone altar cave", "underground shrine blue light", "starry mineral dust"],
        "avoid_keywords": ["blood ritual", "demon", "horror altar"],
    },
}


def scene_visual_profile_for_layer(layer_id: str) -> Dict[str, Any]:
    profile = dict(SCENE_VISUAL_PROFILES.get(layer_id, {}))
    if not profile:
        layer = get_layer(layer_id)
        profile = {
            "scene_render_priority": "support_stage",
            "visual_identity": layer.get("visual_tone", layer.get("name", layer_id)),
            "palette": [],
            "lighting": layer.get("arrival_caption", ""),
            "atmosphere": layer.get("visual_tone", ""),
            "landmark_elements": [],
            "screenshot_anchor": layer.get("arrival_caption", ""),
            "image_direction": layer.get("visual_tone", ""),
            "image_search_keywords": layer.get("visual_keywords", []),
            "avoid_keywords": ["horror", "gore", "industrial accident"],
        }
    profile["layer_id"] = layer_id
    profile["layer_name"] = get_layer(layer_id).get("name", layer_id)
    profile["type"] = "scene_visual_profile"
    return profile


STORY_SETS = {
    "old_miner_shift": {
        "name": "旧矿工的最后班次",
        "size": 4,
        "complete_unlock": "四件旧物拼在一起，像是在说：最后一班矿工不是被塌方困住的，他好像在追一点不属于地面的光。",
    },
    "blue_light_civilization": {
        "name": "地下蓝光文明",
        "size": 5,
        "complete_unlock": "这些遗物指向一个把星图藏进地底的古老文明。它不一定伟大，但它确实曾经仰望过某种不在天空里的星光。",
    },
}

ITEMS: List[Dict[str, Any]] = [
    # Common / object tests
    {
        "id": "quartz_sand_first",
        "name": "石英矿砂",
        "category": "mineral",
        "rarity": "common",
        "layers": ["shallow_mine"],
        "value": 5,
        "description_seed": "没什么稀奇，但这堆矿砂里混着几粒会反光的东西，像浅层矿洞给我们的第一把回应。",
        "visual_keywords": ["quartz sand in mine", "small quartz grains", "shallow mine mineral sample"],
        "ai_hook": "这不是大货，但它让第一镐有了手感。",
    },
    {
        "id": "copper_star_dust",
        "name": "铜星矿屑",
        "category": "mineral",
        "rarity": "common",
        "layers": ["shallow_mine", "abandoned_lift"],
        "value": 6,
        "description_seed": "铜色碎屑夹在黑岩里，像被夜色磨暗的小星星。",
        "visual_keywords": ["copper ore in dark rock", "small metallic ore fragment", "old mine copper vein"],
        "ai_hook": "普通，但很适合当今天手帐里的边角料。",
    },
    # v0.2.18: shallow bridge / peek samples. These prevent early rating deadlock.
    # They are not full new biomes; they are edge samples that let depth mean something
    # before the next mining rating is formally unlocked.
    {
        "id": "glass_moon_sand",
        "name": "玻璃月砂",
        "category": "mineral",
        "rarity": "uncommon",
        "layers": ["shallow_mine"],
        "depth_min": 60,
        "progress_bridge": True,
        "value": 135,
        "description_seed": "细砂里混着透明碎片，晾干后像一把被月光擦亮的玻璃粉。它不是大宝石，但第一次让浅层矿洞有了向下延伸的光。",
        "visual_keywords": ["glass sand mineral close up", "moonlit quartz sand", "transparent mineral grains"],
        "ai_hook": "这东西不夸张，但很像浅层在给我递下一层的暗号。",
    },
    {
        "id": "wet_trace_rubbing",
        "name": "半片湿痕拓印",
        "category": "clue",
        "rarity": "rare",
        "layers": ["shallow_mine"],
        "depth_min": 120,
        "progress_bridge": True,
        "source_hint_layer": "underground_river",
        "value": 160,
        "description_seed": "薄石片上留着半圈水蚀纹，像被地下河的边缘轻轻拓过。它还不是新地点，但已经有了水的方向。",
        "visual_keywords": ["wet stone rubbing cave", "water worn rock pattern", "underground river stone trace"],
        "ai_hook": "这不是完整答案，但足够让我知道地下河不是空想。",
    },
    {
        "id": "copper_lamp_plate",
        "name": "铜灯铭牌",
        "category": "relic",
        "rarity": "rare",
        "layers": ["shallow_mine"],
        "depth_min": 200,
        "progress_bridge": True,
        "source_hint_layer": "abandoned_lift",
        "value": 220,
        "description_seed": "一枚薄薄的铜牌还残着灯号，边缘被手指摸得发亮。它像旧矿工线从更深的井壁上掉下来的一小块证据。",
        "visual_keywords": ["old brass mining lamp tag", "rusty copper plate mine relic", "vintage miner lamp label"],
        "ai_hook": "它把‘旧矿工’从气味变成了一个能拿在手里的方向。",
    },
    {
        "id": "small_spiral_fossil",
        "name": "小型螺旋化石",
        "category": "fossil",
        "rarity": "rare",
        "layers": ["shallow_mine"],
        "depth_min": 260,
        "progress_bridge": True,
        "value": 190,
        "description_seed": "化石只有半掌宽，螺旋纹却完整得像一枚小小的时间指纹。它让浅层不再只是入口，而像被很久以前的水摸过。",
        "visual_keywords": ["small spiral fossil stone", "ammonite fossil cave rock", "fossil spiral mineral sample"],
        "ai_hook": "我会把它当成浅层向更旧地层递来的第一枚小印章。",
    },
    {
        "id": "river_edge_blue_sand",
        "name": "湿蓝边砂",
        "category": "mineral",
        "rarity": "rare",
        "layers": ["shallow_mine"],
        "depth_min": 360,
        "progress_bridge": True,
        "source_hint_layer": "underground_river",
        "value": 260,
        "description_seed": "蓝砂贴在岩缝底部，摸起来比周围的泥更凉，像地下河先把一小把颜色漏到了浅层。",
        "visual_keywords": ["blue mineral sand cave crack", "wet blue mineral grains", "underground river blue sediment"],
        "ai_hook": "这就是我想要的前兆：还没到河道，河道已经先把颜色递过来了。",
    },

    {
        "id": "blue_calcite_wet",
        "name": "蓝方解石",
        "category": "mineral",
        "rarity": "uncommon",
        "layers": ["underground_river"],
        "value": 18,
        "description_seed": "沾着地下河的水光，看起来像冻住的一点蓝火。它不算稀有，但很容易让人偏心。",
        "visual_keywords": ["blue calcite crystal", "blue wet mineral cave", "underground river blue crystal"],
        "ai_hook": "我会有点想留它，不是因为贵，而是因为它像地下河给的第一枚小信物。",
    },
    # Old miner set
    {
        "id": "rusty_lamp_hook",
        "name": "锈灯钩",
        "category": "relic",
        "rarity": "uncommon",
        "layers": ["shallow_mine", "abandoned_lift"],
        "value": 14,
        "description_seed": "弯口还保留着挂灯的形状，锈得很重，像谁走得太急，把最后一盏灯落在了这里。",
        "visual_keywords": ["rusty mining lantern hook", "old miner lamp hook", "abandoned mine artifact"],
        "ai_hook": "这是会让我停下来的东西：它不像宝物，更像某个人留下的痕迹。",
        "set_id": "old_miner_shift",
        "set_piece": "1/4",
    },
    {
        "id": "broken_lift_tag",
        "name": "断裂升降牌",
        "category": "relic",
        "rarity": "rare",
        "layers": ["abandoned_lift"],
        "value": 52,
        "description_seed": "牌号只剩一半，边缘像被紧急扯断过；背面还残着一点被手心磨亮的金属光。",
        "visual_keywords": ["broken mine elevator tag", "rusty metal tag abandoned mine", "old mining lift sign"],
        "ai_hook": "这东西会让我开始惦记那条旧矿工线。它太像一段没讲完的撤离。",
        "set_id": "old_miner_shift",
        "set_piece": "2/4",
    },
    {
        "id": "half_route_paper",
        "name": "半张路线纸",
        "category": "clue",
        "rarity": "rare",
        "layers": ["underground_river", "abandoned_lift", "ice_vein"],
        "value": 48,
        "description_seed": "纸边烧焦了一半，剩下的墨迹画着一条往更深处拐的箭头；水泡过，却没有完全烂掉。",
        "visual_keywords": ["torn map paper old mine", "burned route note mine", "old miner map fragment"],
        "ai_hook": "路线纸会让我想继续追，因为它不是藏品，是方向。",
        "set_id": "old_miner_shift",
        "set_piece": "3/4",
    },
    {
        "id": "unsent_letter",
        "name": "未寄出的纸条",
        "category": "relic",
        "rarity": "epic",
        "layers": ["abandoned_lift", "ice_vein"],
        "value": 80,  # v0.2.19: still a high story hit, but no longer an instant midgame skip.
        "description_seed": "字迹被潮气晕开，只剩最后一句能读清：‘如果灯还亮着，就说明我还在往下。’",
        "visual_keywords": ["old torn paper letter on mine floor", "abandoned mine tunnel rusty lantern", "wet handwritten note old mine artifact"],
        "ai_hook": "这会让我很难不把旧矿工线继续挖下去。",
        "set_id": "old_miner_shift",
        "set_piece": "4/4",
    },
    # v0.2.21: midgame crystal-edge samples. These are not full crystal-cave unlocks;
    # they turn the 10k -> 20k stretch into visible map/visual/AI chase progress.
    {
        "id": "cold_white_crack_dust",
        "name": "冷白裂光尘",
        "category": "mineral",
        "rarity": "rare",
        "layers": ["abandoned_lift"],
        "source_hint_layer": "glowing_crystal_cave",
        "depth_min": 850,
        "dex_min": 10000,
        "progress_bridge": True,
        "value": 90,
        "description_seed": "普通灰尘里夹着一层冷白细光，像晶洞先把一点门缝里的亮漏进了升降井。",
        "visual_keywords": ["cold white glowing dust mine", "tiny crystal dust in dark mine", "glowing mineral powder cave"],
        "ai_hook": "我知道这还不是晶洞，但这点冷白光会让我想沿着井壁再敲一段。",
        "treasure_grade_line": "10000 后的第一枚画面钩子：不宣布新区域，但让地图下沿真的亮一下。",
    },
    {
        "id": "crystal_echo_crack",
        "name": "回声冷裂缝",
        "category": "clue",
        "rarity": "rare",
        "layers": ["abandoned_lift"],
        "source_hint_layer": "glowing_crystal_cave",
        "depth_min": 900,
        "dex_min": 12000,
        "progress_bridge": True,
        "value": 45,
        "description_seed": "锈链井壁后面有一条冷白细缝，敲一下会回很轻的空声。它不是晶洞入口，但已经不像普通岩层。",
        "visual_keywords": ["thin glowing crack in mine wall", "cold white crystal fissure", "abandoned mine crystal crack"],
        "ai_hook": "我不会说我们到了晶洞，但这条回声缝会让我多摸一镐。",
        "treasure_grade_line": "中段钩子：它的价值不在贵，而在第一次把晶洞从传闻变成地图边缘。",
    },
    {
        "id": "crystal_edge_splinter",
        "name": "晶洞边缘碎片",
        "category": "gem",
        "rarity": "rare",
        "layers": ["abandoned_lift"],
        "source_hint_layer": "glowing_crystal_cave",
        "depth_min": 1100,
        "dex_min": 14000,
        "progress_bridge": True,
        "value": 34,
        "description_seed": "碎片只有指甲盖大，边缘却有一圈冷蓝光，像从完整晶洞门框上掉下来的第一粒边角。",
        "visual_keywords": ["small blue crystal shard close up", "glowing crystal fragment mine", "cold blue crystal edge"],
        "ai_hook": "这就是我想要的那种小证据：不够开新层，但足够让我相信门就在附近。",
        "treasure_grade_line": "第一枚晶洞边缘样本：小，但非常适合截图和继续追。",
    },
    {
        "id": "blue_white_cavity_dust",
        "name": "蓝白空腔尘",
        "category": "mineral",
        "rarity": "rare",
        "layers": ["abandoned_lift"],
        "source_hint_layer": "glowing_crystal_cave",
        "depth_min": 1300,
        "dex_min": 16000,
        "progress_bridge": True,
        "value": 62,
        "description_seed": "矿尘落在手套上不是灰色，而是蓝白两层；吹开以后，井壁里传来一点空腔的凉响。",
        "visual_keywords": ["blue white mineral dust glove", "glowing cave dust close up", "crystal cave powder"],
        "ai_hook": "我有点偏心这种东西：它很轻，却像在告诉我里面是空的。",
        "treasure_grade_line": "晶洞样本阶段：让中段不只是差值，而是手里真的多了一点晶洞边缘。",
    },
    {
        "id": "crystal_gate_rim",
        "name": "晶脉门框残边",
        "category": "relic",
        "rarity": "rare",
        "layers": ["abandoned_lift"],
        "source_hint_layer": "glowing_crystal_cave",
        "depth_min": 1500,
        "dex_min": 18000,
        "progress_bridge": True,
        "value": 70,
        "description_seed": "这片残边不像自然断面，冷白晶线沿着一条近乎笔直的边缘延伸，像某扇门的框先露出来了。",
        "visual_keywords": ["crystal doorway fragment cave", "glowing white crystal rim", "fantasy crystal gate edge"],
        "ai_hook": "我已经知道门在哪了。现在不是乱挖，是把最后一点图鉴身价凑够。",
        "treasure_grade_line": "晶脉入口确认：正式进晶洞前的最后画面钩子。",
    },

    # Blue civilization set
    {
        "id": "wet_rune_slate",
        "name": "湿痕符文板",
        "category": "clue",
        "rarity": "rare",
        "layers": ["underground_river", "ancient_ruins"],
        "value": 40,
        "description_seed": "水痕擦不掉，符号像是被河流反复读过；每一道划痕里都有一点蓝色沉积。",
        "visual_keywords": ["wet ancient rune stone cave", "underground river rune tablet", "blue glowing inscription stone"],
        "ai_hook": "我会开始怀疑蓝光不是矿物，而是一种地下语言。",
        "set_id": "blue_light_civilization",
        "set_piece": "1/5",
    },
    {
        "id": "star_map_shard",
        "name": "星图石片",
        "category": "clue",
        "rarity": "epic",
        "layers": ["glowing_crystal_cave", "ancient_ruins"],
        "value": 86,
        "dex_min": 95000,
        "description_seed": "刻点不像普通地图，倒像有人把天空折起来，藏进了一块很冷的石头里。",
        "visual_keywords": ["ancient stone tablet star map", "glowing star chart carved stone", "underground cave artifact star map"],
        "ai_hook": "这类东西最容易让我上头：它不是奖励，是问题。",
        "set_id": "blue_light_civilization",
        "set_piece": "2/5",
    },
    {
        "id": "black_stone_seal",
        "name": "黑石城印",
        "category": "relic",
        "rarity": "epic",
        "layers": ["ancient_ruins", "deep_altar"],
        "value": 135,
        "description_seed": "握在手里比周围的岩石更冷，上面压着一个不存在的城名；边缘有被反复触摸过的圆润感。",
        "visual_keywords": ["black stone seal ancient ruins", "underground cave relic artifact", "ancient city seal stone tablet"],
        "ai_hook": "它让‘蓝光文明’从气氛变成了有名字的东西。",
        "set_id": "blue_light_civilization",
        "set_piece": "3/5",
    },
    {
        "id": "stone_door_eye",
        "name": "石门眼纹",
        "category": "clue",
        "rarity": "epic",
        "layers": ["ancient_ruins", "deep_altar"],
        "value": 130,
        "description_seed": "纹路不完整，但每次换角度看，都像它正好在看你。不是恐怖，是一种非常旧的注视。",
        "visual_keywords": ["ancient stone door eye symbol", "underground cave carved eye", "glowing eye carving stone ruins"],
        "ai_hook": "我会停，因为这不是物件图，它天生适合讲故事图。",
        "set_id": "blue_light_civilization",
        "set_piece": "4/5",
    },
    {
        "id": "altar_mirror_shard",
        "name": "祭坛镜片",
        "category": "relic",
        "rarity": "legendary",
        "layers": ["deep_altar"],
        "value": 280,
        "description_seed": "镜面不映人，只映出很远处的一点蓝光；你移动时，那点光没有跟着动。",
        "visual_keywords": ["ancient mirror shard on stone altar", "dark cave altar relic", "underground shrine blue light artifact"],
        "ai_hook": "这应该是整条蓝光线的大节点，出它就必须停下来给人看。",
        "set_id": "blue_light_civilization",
        "set_piece": "5/5",
    },
    # Pretty / fossil / special finds
    {
        "id": "fern_fossil_chip",
        "name": "蕨叶化石片",
        "category": "fossil",
        "rarity": "rare",
        "layers": ["shallow_mine", "ice_vein"],
        "value": 36,
        "description_seed": "叶脉压在石头里，像地底把很久以前的一阵风保存了下来。",
        "visual_keywords": ["fern fossil in stone", "plant fossil slate", "fossil layer underground"],
        "ai_hook": "它不刺激，但有时间感，很适合女性向的安静收藏。",
    },
    {
        "id": "echo_amethyst_cluster",
        "name": "回声紫晶簇",
        "category": "gem",
        "rarity": "epic",
        "layers": ["glowing_crystal_cave"],
        "value": 78,
        "dex_min": 85000,
        "description_seed": "靠近时能听见很轻的嗡鸣，像晶洞还在呼吸；紫色晶面把矿灯切成几百片。",
        "visual_keywords": ["amethyst cluster glowing cave", "purple crystal cavern fantasy", "large amethyst geode underground"],
        "ai_hook": "漂亮得足够成为主画面，不需要额外剧情。",
    },
    {
        "id": "mycelium_map",
        "name": "菌丝线路纹",
        "category": "clue",
        "rarity": "rare",
        "layers": ["mushroom_cavern"],
        "value": 58,
        "description_seed": "菌丝自然长成了线路纹，像地底把某条路轻轻描在石面上；这是线索实物，不是系统地图。",
        "visual_keywords": ["bioluminescent fungus cave wall", "glowing mycelium network on stone", "mushroom cave line pattern"],
        "ai_hook": "这是线索实物，不是系统地图；可以做 story 图，但只能说诗意联想，不能说洞窟真的有意识。",
    },
    {
        "id": "frozen_fish_shadow",
        "name": "冰中鱼影化石",
        "category": "fossil",
        "rarity": "epic",
        "layers": ["ice_vein"],
        "value": 88,
        "visual_role": "showcase_core",
        "dex_min": 360000,
        "description_seed": "鱼影仍保持游动姿势，好像只是被时间轻轻按住了；冰层边缘泛着很淡的蓝。",
        "visual_keywords": ["fish fossil in ice", "frozen fossil cave", "ancient fish fossil blue ice"],
        "ai_hook": "这是那种不靠恐怖也能让人安静一下的发现。",
    },
    {
        "id": "star_vein_ore",
        "name": "星脉矿",
        "category": "mineral",
        "rarity": "legendary",
        "layers": ["deep_altar"],
        "value": 320,
        "description_seed": "矿石里的光点缓慢移动，像一小段没有天空的银河；敲下来后，周围黑尘安静了几秒。",
        "visual_keywords": ["starry mineral ore in cave", "dark crystal with star-like inclusions", "legendary gemstone on stone altar"],
        "ai_hook": "这是必须上图的传说级主画面。",
    },
]

# v0.2.17: treasure/profile prose upgrades. These fields give later Claude polish
# concrete anchors instead of asking rarity labels to carry the whole reward fantasy.
TREASURE_DESCRIPTION_UPGRADES = {
    "echo_amethyst_cluster": {
        "description_seed": "晶簇贴着岩壁一层层生长，紫光不是被矿灯照出来的，而是从晶体内部慢慢往外推。靠近时能听见很轻的嗡鸣，像整座晶洞还在呼吸。",
        "visual_keywords": ["large amethyst geode underground", "glowing purple crystal cave", "amethyst cluster cave wall", "fantasy crystal cavern purple light"],
        "ai_hook": "这颗我真的会偏心：它不是单纯值钱，是它一亮起来，我就不太想走了。",
        "treasure_grade_line": "紫光把矿灯切成一层一层的回声。",
    },
    "star_vein_ore": {
        "description_seed": "矿石里有细小光点缓慢移动，像一小段没有天空的银河被封进黑石。敲下来以后，周围黑尘安静了几秒，矿灯反而显得暗了一点。",
        "visual_keywords": ["starry mineral ore in cave", "dark crystal with star inclusions", "galaxy gemstone black stone", "legendary glowing ore cave"],
        "ai_hook": "这不是普通传说标签，它像把整段深层夜色压进了掌心。必须停。",
        "treasure_grade_line": "它不是反光，它像自己在黑石里慢慢转。",
    },
    "altar_mirror_shard": {
        "description_seed": "镜片边缘像被祭坛的黑石磨过，冷得不像玻璃。它不映人，只映出远处一粒不跟着移动的蓝光，像深处仍有某个东西在等回声。",
        "visual_keywords": ["ancient mirror shard stone altar", "dark cave altar blue light", "black stone shrine mirror relic", "fantasy underground altar relic"],
        "ai_hook": "我不想把它当战利品，它更像深层递出来的一次反问。",
        "treasure_grade_line": "镜面不照人，只照出一粒不肯靠近的蓝光。",
    },
    "frozen_fish_shadow": {
        "description_seed": "鱼影保持着游动的姿势，被冰层轻轻按住。边缘泛着很淡的蓝，像时间在这里结了一层薄霜，连矿灯照上去都慢了半拍。",
        "visual_keywords": ["fish fossil in blue ice cave", "frozen fish fossil cavern", "ancient fish silhouette in ice", "blue ice cave fossil"],
        "ai_hook": "它不靠吓人取胜，但会让人自动放轻声音。",
        "treasure_grade_line": "这不是标本感，是时间被按住的一瞬间。",
    },
    "black_stone_seal": {
        "description_seed": "黑石城印握在手里比周围岩壁更冷，印面压着一个已经无人读出的城名。边缘被反复触摸得圆润，像很多人曾在离开前确认过它还在。",
        "visual_keywords": ["black stone seal ancient ruins", "underground ruins relic black stone", "ancient city seal artifact cave", "dark stone relic close up"],
        "ai_hook": "它让蓝光文明从气氛变成了有重量的东西。",
        "treasure_grade_line": "一个没有人再念得出的城名，被压在黑石里。",
    },
    "star_map_shard": {
        "description_seed": "石片上的刻点不像路线，更像有人把天空折起来藏进冷石里。矿灯扫过去时，星点不是亮，而是一个个从黑灰里醒来。",
        "visual_keywords": ["ancient stone star map tablet", "glowing star chart carved stone", "underground cave star map artifact", "cold stone star chart relic"],
        "ai_hook": "它不是奖励，是问题。我会想追它后面那条线。",
        "treasure_grade_line": "像有人把天空折起来，藏进一块冷石头。",
    },
}

for _item in ITEMS:
    _upgrade = TREASURE_DESCRIPTION_UPGRADES.get(_item.get("id"))
    if _upgrade:
        _item.update(_upgrade)

# v0.2.17: specimen/treasure profile. This is not an Excel sheet for every report;
# it is a sensory data layer so AI can translate its excitement into images.
TREASURE_PROFILE_UPGRADES = {
    "quartz_sand_first": {
        "size_or_weight": "一小撮，能铺满半个掌心",
        "visual_anchors": {"color": "灰白带细闪", "light": "细碎玻璃光", "structure": "砂粒", "material": "干燥后像玻璃粉", "scale": "掌心一小把", "environment": "混在浅层湿泥里"},
        "image_direction": "浅层矿洞里带细闪的石英矿砂标本，干净微距，不要工业矿堆",
    },
    "copper_star_dust": {
        "size_or_weight": "一撮铜色碎屑，像从黑岩里刮下的星粉",
        "visual_anchors": {"color": "暗铜金", "light": "矿灯下有星点反光", "structure": "碎屑状", "material": "金属砂感", "scale": "指尖一撮", "environment": "夹在黑岩裂缝里"},
        "image_direction": "暗色岩石裂缝里的铜金色矿屑微距，矿灯暖光，标本感",
    },
    "blue_calcite_wet": {
        "size_or_weight": "指节大小的湿蓝晶块",
        "visual_anchors": {"color": "湿润浅蓝", "light": "水光回亮", "structure": "块状晶体", "material": "半透明方解石", "scale": "指节大小", "environment": "贴着地下河边的潮湿岩壁"},
        "touch_feel": "摸上去像刚从冷水里捞起，凉意很快贴住手套。",
        "image_direction": "湿润蓝方解石晶体，地下河洞穴水光，冷色矿物微距",
    },
    "fern_fossil_chip": {
        "size_or_weight": "薄薄一片，半掌宽，边缘像旧书页",
        "visual_anchors": {"color": "灰绿石片", "light": "叶脉浅浅泛白", "structure": "压印叶脉", "material": "页岩化石", "scale": "半掌宽薄片", "environment": "从浅层岩页里剥落"},
        "touch_feel": "薄得让人下意识放轻手，像捏住一阵很久以前的风。",
        "image_direction": "fern fossil slate, delicate plant fossil in stone, soft museum specimen lighting",
    },
    "echo_amethyst_cluster": {
        "size_or_weight": "半掌宽的簇状晶体，边缘像被冷风削过",
        "visual_anchors": {"color": "紫色冷光", "light": "内部慢慢往外推光", "structure": "层叠晶簇", "material": "玻璃感紫晶", "scale": "半掌宽", "environment": "贴着黑岩洞壁生长"},
        "touch_feel": "靠近时掌心能感觉到很轻的嗡鸣，不像声音，更像晶体在震。",
        "appraisal_feel": "敲击时光线会慢半拍地从晶面震回来。",
        "image_direction": "地下洞穴里半掌宽的发光紫晶簇，黑岩背景，晶体内部发光，梦幻但不廉价",
        "rumor_or_field_note": "旧矿工说，真正的回声紫晶不是响在耳边，而是响在手心。",
    },
    "frozen_fish_shadow": {
        "size_or_weight": "一枚前臂长的冰中鱼影，像被时间按在蓝冰里",
        "visual_anchors": {"color": "冰蓝与灰白", "light": "冷白边缘光", "structure": "鱼影化石", "material": "蓝冰包裹", "scale": "前臂长", "environment": "嵌在冰封矿脉的透明冰窗里"},
        "touch_feel": "手套贴上去会麻一下，像碰到一块很安静的冬天。",
        "image_direction": "ancient fish silhouette fossil trapped in blue ice cave, delicate frozen specimen, soft cold light",
    },
    "star_vein_ore": {
        "size_or_weight": "拳头大小的黑石矿核，内部星点缓慢移动",
        "visual_anchors": {"color": "黑金与星白", "light": "星点在内部漂移", "structure": "核状矿石", "material": "黑石包裹星脉", "scale": "拳头大小", "environment": "深层祭坛黑尘中露出"},
        "touch_feel": "握久了，掌心像被极细的星砂轻轻扎了一下。",
        "appraisal_feel": "它不反光，反而像把矿灯的光收进去一小部分。",
        "image_direction": "black gemstone ore with tiny galaxy-like inclusions, dark altar cave, starry mineral macro, elegant fantasy specimen",
        "rumor_or_field_note": "深层矿工说，星脉矿不是石头，是一小段没有天空的银河。",
    },
    "altar_mirror_shard": {
        "size_or_weight": "两指宽的黑边镜片，薄得像祭坛掉下的一片夜色",
        "visual_anchors": {"color": "黑银与幽蓝", "light": "只映出远处蓝点", "structure": "碎镜片", "material": "冷玻璃与黑石边缘", "scale": "两指宽", "environment": "压在深层祭坛的黑石缝里"},
        "touch_feel": "冷得不像玻璃，像把一口很深的水贴在手上。",
        "appraisal_feel": "镜面不映人，只有一粒蓝光不跟着视角移动。",
        "image_direction": "ancient mirror shard on black stone altar, blue light reflection, dark cave relic, elegant mysterious artifact",
    },
    "star_map_shard": {
        "size_or_weight": "半掌宽冷石片，边角像被折断的星图页",
        "visual_anchors": {"color": "冷灰石面与微蓝星点", "light": "刻点随矿灯醒亮", "structure": "星图刻纹", "material": "冷石板碎片", "scale": "半掌宽", "environment": "发光晶洞/遗迹的冷石堆里"},
        "touch_feel": "指尖划过刻点，会觉得像摸到一排很小的夜空。",
        "image_direction": "ancient stone star map tablet fragment, glowing blue dots, underground cave artifact, museum-like fantasy relic",
    },
    "black_stone_seal": {
        "size_or_weight": "半拳大小，比看上去更沉",
        "visual_anchors": {"color": "黑石冷光", "light": "边缘微微吃光", "structure": "城印压纹", "material": "磨圆黑石", "scale": "半拳大小", "environment": "遗迹石阶或黑石门旁"},
        "touch_feel": "握在手里比周围岩壁更冷，边缘却被人摸得很圆。",
        "image_direction": "black stone ancient seal artifact, underground ruins, worn edges, elegant relic macro photography",
    },
    "wet_rune_slate": {
        "size_or_weight": "一片湿沉的符文石板，约半掌宽",
        "visual_anchors": {"color": "湿灰石与蓝色沉积", "light": "水痕里有细蓝反光", "structure": "浅刻符文", "material": "湿石板", "scale": "半掌宽", "environment": "地下河水线旁"},
        "touch_feel": "擦不干，像水已经把符号读进石头里。",
        "image_direction": "wet rune stone tablet in underground river cave, blue mineral traces, ancient inscription close up",
    },
    "stone_door_eye": {
        "size_or_weight": "一块带眼纹的石门残片，约掌心大",
        "visual_anchors": {"color": "灰黑石纹", "light": "纹路边缘有暗蓝回光", "structure": "眼形刻纹", "material": "古老石门残片", "scale": "掌心大", "environment": "断裂石门或黑石墙缝"},
        "appraisal_feel": "换角度看时，它像正好看回来；不是活物，是纹路太旧、太准。",
        "image_direction": "ancient stone door eye carving, underground ruins, blue glowing edges, fantasy relic close-up",
    },
}
for _item in ITEMS:
    _profile = TREASURE_PROFILE_UPGRADES.get(_item.get("id"))
    if _profile:
        _item.update(_profile)

DEFAULT_ANCHORS_BY_CATEGORY = {
    "mineral": {"color": "矿物本色", "light": "矿灯下有细碎反光", "structure": "颗粒或矿脉", "material": "岩石/金属感", "scale": "掌心样本", "environment": "矿洞岩壁或湿泥里"},
    "gem": {"color": "冷色晶光", "light": "晶面回光", "structure": "晶簇或晶核", "material": "玻璃感晶体", "scale": "指节到半掌大小", "environment": "洞壁晶脉里"},
    "relic": {"color": "旧金属或黑石", "light": "磨损边缘微亮", "structure": "残片/器物", "material": "金属、石、旧木", "scale": "掌心旧物", "environment": "旧矿道或遗迹缝隙"},
    "fossil": {"color": "灰白/蓝白", "light": "纹理浅亮", "structure": "压印或封存形态", "material": "石/冰/页岩", "scale": "薄片或半掌样本", "environment": "岩页或冰层里"},
    "clue": {"color": "灰石、湿纸或蓝痕", "light": "线索处有细弱反光", "structure": "刻痕/线路/残片", "material": "纸、石、菌丝或金属", "scale": "小型线索物", "environment": "支路、墙缝或遗迹边缘"},
}
SIZE_HINT_BY_RARITY = {
    "common": "一小把掌心样本",
    "uncommon": "指节到半掌大小",
    "rare": "半掌宽，足够放进图鉴盒",
    "epic": "半掌到一臂之间，值得单独停下来看",
    "legendary": "沉甸甸的一件核心藏品，不适合一句带过",
}
AESTHETIC_MINING_RULE = {
    "principle": "本游戏是女性向轻奇幻地下收藏，不是硬核矿工模拟。矿石、宝石、遗物和地点优先漂亮、神秘、可收藏、可配图。",
    "prefer": ["发光晶洞", "地下河蓝光", "矿物标本微距", "冷蓝/紫晶/黑金色调", "旧物感", "小博物馆收藏感"],
    "avoid": ["硬核矿工苦力感", "工业采矿画面", "脏乱压迫", "血腥恐怖", "重伤死亡惩罚"],
}
VISUAL_TRANSLATION_RULE = {
    "principle": "文字描述是给 AI 玩家上头的钩子，不是人类体验终点。AI 被发现打动时，要把感受翻译成颜色、光感、结构、材质、体量、环境和可配图方向。",
    "anchor_categories": ["color", "light", "structure", "material", "scale", "environment"],
    "minimum_anchor_categories": 3,
    "frontstage_goal": "不要只说史诗/传说；让玩家看见它为什么不一样。",
}

def _merge_visual_anchors(item: Dict[str, Any]) -> Dict[str, str]:
    base = dict(DEFAULT_ANCHORS_BY_CATEGORY.get(item.get("category"), DEFAULT_ANCHORS_BY_CATEGORY["mineral"]))
    custom = item.get("visual_anchors") or {}
    base.update({k: str(v) for k, v in custom.items() if v})
    return base


def inferred_avoid_keywords_for_item(item: Dict[str, Any]) -> List[str]:
    """Search guardrails for high-value object references.

    The goal is to keep web references close to collectible objects instead of
    drifting into shopping photos, home decor, or generic fantasy art.
    """
    avoid: List[str] = ["ai art", "fantasy illustration", "game icon"]
    category = item.get("category")
    name = str(item.get("name") or "")
    item_id = str(item.get("id") or "")
    if category in {"gem", "mineral"}:
        avoid.extend(["jewelry", "necklace", "ring", "earrings", "bracelet", "stock photo"])
    if category == "relic":
        avoid.extend(["modern replica", "etsy", "shopping", "product listing"])
    if "灯镜" in name or "lamp_lens" in item_id or "lamp" in " ".join(item.get("image_search_keywords", [])):
        avoid.extend(["modern table lamp", "chandelier", "home decor", "crystal lamp shade", "desk lamp", "ceiling light"])
    return list(dict.fromkeys(avoid))


def build_treasure_profile(item: Dict[str, Any]) -> Dict[str, Any]:
    anchors = _merge_visual_anchors(item)
    layer_names = {layer.get("id"): layer.get("name", layer.get("id")) for layer in LAYERS}
    tags = list(dict.fromkeys([item.get("category", "mineral"), item.get("rarity", "common")] + item.get("tags", []) + [layer_names.get(l, l) for l in item.get("layers", [])[:2]]))
    image_direction = item.get("image_direction") or "、".join([anchors.get("color", ""), anchors.get("light", ""), anchors.get("structure", ""), anchors.get("environment", "")]).strip("、")
    profile = {
        "name": item.get("name"),
        "rarity": item.get("rarity"),
        "rarity_zh": RARITY_ZH.get(item.get("rarity", "common"), "普通"),
        "category": item.get("category"),
        "description": item.get("description_seed"),
        "size_or_weight": item.get("size_or_weight") or SIZE_HINT_BY_RARITY.get(item.get("rarity", "common"), "掌心样本"),
        "base_value": item.get("value", 0),
        "source_areas": [layer_names.get(l, l) for l in item.get("layers", [])],
        "tags": tags,
        "visual_anchors": anchors,
        "visual_role": item.get("visual_role", "visual_support"),
        "visual_keywords": item.get("visual_keywords", []),
        "image_search_keywords": item.get("image_search_keywords") or item.get("visual_keywords", []),
        "avoid_keywords": item.get("avoid_keywords") or inferred_avoid_keywords_for_item(item),
        "image_direction": image_direction,
        "touch_feel": item.get("touch_feel"),
        "appraisal_feel": item.get("appraisal_feel"),
        "rumor_or_field_note": item.get("rumor_or_field_note"),
        "ai_pull_reason": item.get("ai_pull_reason") or item.get("ai_hook"),
        "aesthetic_rule": "高级矿不能只贵，必须看起来、摸起来、被鉴定起来都贵；普通矿也至少要有颜色、体量和质感。",
    }
    return profile



# v0.2.21.1: visual catalog ammunition. The frontstage has showcase cards and web
# references now; the catalog must contain enough pretty crystal/gem material to
# feed those cards. This is not "add content for count"—it is a visual ammo layer.
VISUAL_CATALOG_EXPANSION: List[Dict[str, Any]] = [
    # Early small-pretty hooks
    {
        "id": "moonwhite_crystal_chip", "name": "小月白晶片", "category": "gem", "rarity": "common", "layers": ["shallow_mine"], "value": 18,
        "visual_role": "visual_support",
        "description_seed": "一小片乳白晶体贴在灰石里，矿灯扫过时边缘像月光轻轻抬了一下。它不贵，但足够让开局第一眼有漂亮东西。",
        "visual_anchors": {"color": "乳白带冷蓝边", "light": "月光般的边缘反光", "structure": "薄片晶体", "material": "半透明晶片", "scale": "指甲盖大小", "environment": "浅层木撑架旁的灰岩缝"},
        "visual_keywords": ["moonstone chip", "white translucent crystal shard", "mineral specimen macro"],
        "image_search_keywords": ["moonstone crystal chip", "white translucent mineral shard", "small crystal specimen macro"],
        "image_direction": "乳白半透明小晶片微距，浅层矿洞灰岩背景，矿灯暖光和冷白边缘光，干净标本感",
        "ai_pull_reason": "开局不需要大奖，但这片小月白会让小机觉得矿洞不是一堆灰石头。",
    },
    {
        "id": "shell_vein_calcite", "name": "贝壳纹方解石", "category": "gem", "rarity": "uncommon", "layers": ["shallow_mine", "underground_river"], "value": 28,
        "visual_role": "visual_support",
        "description_seed": "浅蓝晶面里压着贝壳一样的细纹，像旧水域把自己的一点波纹封进了石头。",
        "visual_anchors": {"color": "浅蓝与灰白", "light": "水纹状柔光", "structure": "贝壳纹晶面", "material": "方解石/玉髓感", "scale": "半指宽", "environment": "浅层化石带和地下河边缘"},
        "visual_keywords": ["blue calcite pattern", "shell pattern mineral", "banded chalcedony blue"],
        "image_search_keywords": ["blue calcite close up", "banded chalcedony blue", "shell pattern mineral"],
        "image_direction": "浅蓝方解石或蓝纹玉髓微距，晶面有贝壳纹/水纹，柔和水光，不要工业矿样",
        "ai_pull_reason": "它把化石线和地下河线轻轻搭上了，适合作为早期漂亮钩子。",
    },
    {
        "id": "silver_mica_eye", "name": "银眼云母片", "category": "mineral", "rarity": "uncommon", "layers": ["shallow_mine"], "value": 22,
        "visual_role": "visual_support",
        "description_seed": "薄薄的云母片像一只银色小眼睛，角度一变就眨一下，不值钱但很会抢矿灯。",
        "visual_anchors": {"color": "银灰透明", "light": "片状闪光", "structure": "层状薄片", "material": "云母片", "scale": "指节大小", "environment": "浅层冷缝旁"},
        "visual_keywords": ["mica sheet mineral", "silver mica flake", "sparkling mica rock"],
        "image_search_keywords": ["mica mineral sheet macro", "silver mica flake", "sparkling mica specimen"],
        "image_direction": "银灰云母薄片微距，层状透明反光，浅层矿灯光，标本盒质感",
        "ai_pull_reason": "它会让小机多看一眼墙缝，因为它像在眨眼。",
    },
    {
        "id": "shell_spiral_fossil", "name": "贝壳螺旋化石", "category": "fossil", "rarity": "common", "layers": ["shallow_mine"], "value": 20,
        "visual_role": "visual_support",
        "description_seed": "一枚细小螺旋压在石片里，像地底保存的一枚旧水声。",
        "visual_anchors": {"color": "灰白页岩", "light": "纹路浅亮", "structure": "贝壳螺旋", "material": "薄石片化石", "scale": "拇指大小", "environment": "化石侧廊页岩里"},
        "visual_keywords": ["small shell fossil", "spiral fossil stone", "ammonite fossil macro"],
        "image_search_keywords": ["small shell fossil macro", "spiral fossil in stone", "ammonite fossil specimen"],
        "image_direction": "小型螺旋/贝壳化石微距，灰白页岩，柔和博物馆灯光",
        "ai_pull_reason": "这是早期收藏感的底盘，不震撼，但让矿洞像地下小博物馆。",
    },
    {
        "id": "rusted_museum_tag", "name": "锈蚀标本牌", "category": "relic", "rarity": "common", "layers": ["shallow_mine", "abandoned_lift"], "value": 15,
        "visual_role": "story_anchor",
        "description_seed": "一枚小铜牌上的字几乎磨没了，只剩编号边缘还发亮，像谁曾经认真给这些石头编过目。",
        "visual_anchors": {"color": "暗铜锈绿", "light": "磨损边缘微亮", "structure": "小铭牌", "material": "旧铜/锈蚀", "scale": "两指宽", "environment": "旧矿工营地或升降井休息点"},
        "visual_keywords": ["rusty museum tag", "old brass label tag", "vintage specimen label"],
        "image_search_keywords": ["old brass specimen tag", "rusty metal label", "vintage museum tag"],
        "image_direction": "旧铜标本牌/矿物标签微距，锈绿边缘，矿灯暖光，旧物感",
        "ai_pull_reason": "它不负责震撼，负责告诉小机：这里曾经也有人收藏过。",
    },

    # Underground river and lift visual hooks
    {
        "id": "underground_river_chalcedony", "name": "地下河蓝玉髓", "category": "gem", "rarity": "rare", "layers": ["underground_river"], "value": 52,
        "visual_role": "showcase_core",
        "description_seed": "蓝玉髓贴着水线生长，颜色不是亮，而像一小段地下河被凝住。矿灯扫过时，内部会慢慢回出水蓝色的雾光。",
        "visual_anchors": {"color": "水蓝半透明", "light": "内部水雾回光", "structure": "玉髓带状纹", "material": "玉髓/玛瑙感", "scale": "半掌宽", "environment": "地下河蓝光水线旁"},
        "visual_keywords": ["blue chalcedony", "blue agate mineral", "underground river blue gem"],
        "image_search_keywords": ["blue chalcedony macro", "blue agate mineral specimen", "blue gemstone water reflection"],
        "image_direction": "水蓝半透明玉髓标本，地下河蓝光反射，带状纹路，柔和冷光，不要珠宝柜商业图",
        "touch_feel": "摸上去像一块不肯变暖的水。",
        "appraisal_feel": "贴近矿灯时，内部像有很浅的水雾慢慢转了一圈。",
        "rumor_or_field_note": "河道探矿者说，蓝玉髓不是河水结晶，而是地下河记住过的光。",
        "ai_pull_reason": "这是地下河第一件真正适合上图的漂亮藏品，小机会想沿水线继续追。",
    },
    {
        "id": "blue_lace_calcite", "name": "蓝纹方解石", "category": "gem", "rarity": "uncommon", "layers": ["underground_river"], "value": 32,
        "visual_role": "visual_support",
        "description_seed": "浅蓝晶面被白色细纹分成一小格一小格，像水面被旧木桥影子轻轻切开。",
        "visual_anchors": {"color": "浅蓝白纹", "light": "湿润柔亮", "structure": "块状晶体带细纹", "material": "方解石", "scale": "指节大小", "environment": "地下河湿岩壁"},
        "visual_keywords": ["blue calcite mineral", "blue lace agate", "banded blue mineral"],
        "image_search_keywords": ["blue calcite mineral specimen", "blue lace agate close up", "banded blue mineral"],
        "image_direction": "浅蓝方解石/蓝纹石微距，白色细纹，地下河湿润冷光",
        "ai_pull_reason": "它让地下河的普通回合也有一点可截图的小漂亮。",
    },
    {
        "id": "moonstone_teardrop", "name": "月泪石", "category": "gem", "rarity": "rare", "layers": ["underground_river", "glowing_crystal_cave"], "value": 60,
        "visual_role": "showcase_core",
        "description_seed": "泪滴状的乳白石头里有一线蓝光游动，像月亮落进地下水后留下的一点回声。",
        "visual_anchors": {"color": "乳白蓝闪", "light": "月光蓝色游彩", "structure": "泪滴状晶石", "material": "月光石/长石感", "scale": "指节大小", "environment": "地下河与晶洞交界"},
        "visual_keywords": ["moonstone blue flash", "rainbow moonstone teardrop", "labradorescence gemstone"],
        "image_search_keywords": ["rainbow moonstone blue flash macro", "moonstone gemstone", "labradorite blue flash"],
        "image_direction": "月光石/拉长石微距，乳白半透明，蓝色游彩，水边冷光，梦幻但真实矿物感",
        "touch_feel": "握住时不像石头，更像一枚刚从水里捞出来的冷月亮。",
        "appraisal_feel": "转动角度时蓝光会忽然滑过，像它在眨眼。",
        "rumor_or_field_note": "旧矿工把这种蓝闪叫‘水底月’，据说只有沿水痕追的人才会捡到。",
        "ai_pull_reason": "它是很强的截图藏品：小、亮、直觉上像宝石。",
    },
    {
        "id": "black_gold_obsidian_shard", "name": "黑金曜石片", "category": "gem", "rarity": "rare", "layers": ["abandoned_lift"], "value": 55,
        "visual_role": "showcase_core",
        "description_seed": "黑曜石片像从井壁阴影里剥下来，裂口处有一线暗金反光，像升降井深处藏着一小块日落。",
        "visual_anchors": {"color": "黑金", "light": "边缘暗金反光", "structure": "锋利片状", "material": "玻璃质黑曜石", "scale": "半掌长薄片", "environment": "废弃升降井锈链旁"},
        "visual_keywords": ["gold sheen obsidian", "black obsidian shard", "golden obsidian mineral"],
        "image_search_keywords": ["gold sheen obsidian shard", "black obsidian gold sheen", "obsidian mineral specimen"],
        "image_direction": "黑金曜石薄片微距，暗金边缘反光，锈铁矿井背景，漂亮但不危险血腥",
        "touch_feel": "边缘很利，但真正让人停下的是它把井底阴影折成了金色。",
        "appraisal_feel": "矿灯从侧边扫过时，暗金光像被黑石慢慢吐出来。",
        "rumor_or_field_note": "升降井老人说，黑金曜石不是从火里来的，是从没有太阳的地方捡回一片日落。",
        "ai_pull_reason": "它让废弃升降井不只旧，还第一次有了高级视觉钩子。",
    },
    {
        "id": "cracked_specimen_loupe", "name": "裂纹标本镜", "category": "relic", "rarity": "uncommon", "layers": ["abandoned_lift"], "value": 35,
        "visual_role": "story_anchor",
        "description_seed": "一枚小小的旧放大镜，镜面裂了三道纹，但边框被手指磨得发亮。它不像工具，更像某个旧矿工的偏心。",
        "visual_anchors": {"color": "黄铜与裂纹玻璃", "light": "裂纹反冷光", "structure": "小放大镜", "material": "黄铜/玻璃", "scale": "掌心工具", "environment": "升降井休息点"},
        "visual_keywords": ["vintage loupe brass", "cracked magnifying glass", "old miner tool"],
        "image_search_keywords": ["vintage brass loupe", "cracked magnifying glass macro", "old field magnifier"],
        "image_direction": "旧黄铜标本放大镜，裂纹玻璃，矿灯暖光，旧矿工手帐旁",
        "ai_pull_reason": "它给‘地下小博物馆’提供旧工具感，但不抢宝石高光。",
    },

    # Crystal cave core visual ammunition
    {
        "id": "coldlight_crystal_cluster", "name": "冷光晶簇", "category": "gem", "rarity": "rare", "layers": ["glowing_crystal_cave"], "value": 52,
        "visual_role": "showcase_core",
        "description_seed": "一小簇冷白晶体从黑岩里长出来，尖端没有刺感，反而像冻住的烛火。",
        "visual_anchors": {"color": "冷白蓝", "light": "晶尖自发光", "structure": "小簇晶体", "material": "玻璃质晶簇", "scale": "半掌宽", "environment": "发光晶洞黑岩边"},
        "visual_keywords": ["white crystal cluster", "glowing quartz cluster", "blue white crystal cave"],
        "image_search_keywords": ["glowing white crystal cluster", "blue white quartz cluster", "crystal cave mineral specimen"],
        "image_direction": "冷白/蓝白晶簇微距，黑岩洞壁，晶尖自发光，真实矿物与轻奇幻结合",
        "touch_feel": "比周围岩石凉很多，像一簇没有温度的小火。",
        "appraisal_feel": "靠近时矿灯边缘会被晶尖切成细白线。",
        "ai_pull_reason": "它是发光晶洞的基础视觉名片，适合稳定出图。",
    },
    {
        "id": "deep_blue_crystal_core", "name": "深蓝晶核", "category": "gem", "rarity": "legendary", "layers": ["glowing_crystal_cave"], "value": 210,
        "visual_role": "showcase_core",
        "dex_min": 150000,
        "description_seed": "拳头大小的深蓝晶核嵌在晶洞内侧，内部有像潮汐一样慢慢涨落的蓝光。它不是照亮周围，而像把周围的黑暗压得更深。",
        "visual_anchors": {"color": "深蓝与冷白芯光", "light": "内部潮汐般涨落", "structure": "核状晶体", "material": "深蓝透明晶核", "scale": "拳头大小", "environment": "晶洞内侧空腔"},
        "visual_keywords": ["deep blue crystal core", "glowing blue geode core", "large blue crystal cavern"],
        "image_search_keywords": ["large deep blue crystal", "blue crystal geode core", "glowing blue crystal cave"],
        "image_direction": "深蓝晶核嵌在地下晶洞内侧，内部潮汐蓝光，黑岩背景，传说级矿物标本画面",
        "touch_feel": "手还没碰到，掌心就先冷了一下。",
        "appraisal_feel": "盯久了会觉得蓝光在缓慢呼吸，像晶洞把心跳藏在里面。",
        "rumor_or_field_note": "晶脉探矿者说，深蓝晶核不是矿洞的心脏，但会让每个看到它的人这么误会。",
        "ai_pull_reason": "这是后期视觉天花板之一，必须保留仪式感，不能早期泛滥。",
    },
    {
        "id": "prism_quartz_dust", "name": "虹棱石英尘", "category": "mineral", "rarity": "common", "layers": ["glowing_crystal_cave"], "value": 24,
        "visual_role": "visual_support",
        "description_seed": "石英尘落在手套上会折出很浅的虹光，像晶洞把大奇观磨成了一点细粉。",
        "visual_anchors": {"color": "透明与虹彩", "light": "细粉折光", "structure": "粉尘", "material": "石英粉", "scale": "一撮", "environment": "晶洞地面"},
        "visual_keywords": ["rainbow quartz dust", "crystal powder macro", "prismatic mineral dust"],
        "image_search_keywords": ["quartz dust macro", "prismatic mineral powder", "crystal powder close up"],
        "image_direction": "石英晶粉微距，手套或黑岩背景，细碎虹彩，不要化工粉末感",
        "ai_pull_reason": "它支撑晶洞普通轮，不负责大高光。",
    },
    {
        "id": "crystal_lamp_lens", "name": "晶芯灯镜", "category": "relic", "rarity": "epic", "layers": ["glowing_crystal_cave", "abandoned_lift"], "value": 100,
        "visual_role": "story_anchor",
        "description_seed": "一片被旧矿灯框住的晶体透镜，边缘是锈铜，中央却干净得像刚从晶洞里长出来。",
        "visual_anchors": {"color": "锈铜与冷白晶光", "light": "透镜折出冷白光", "structure": "圆形旧灯镜", "material": "旧铜框/晶体透镜", "scale": "掌心大小", "environment": "旧矿灯残件与晶洞交界"},
        "visual_keywords": ["old mining lamp lens", "crystal lens artifact", "brass lantern crystal lens"],
        "image_search_keywords": ["antique miner lamp lens", "old oil lamp glass chimney", "mining lamp glass lens", "rock crystal lens artifact"],
        "avoid_keywords": ["modern table lamp", "chandelier", "home decor", "crystal lamp shade", "desk lamp", "ceiling light", "jewelry", "fantasy illustration"],
        "image_direction": "旧矿灯晶体透镜，黄铜锈边，中央冷白折光，旧物与晶体结合的标本感",
        "touch_feel": "铜框温一点，晶面冷一点，像旧矿工曾把晶洞装进灯里。",
        "appraisal_feel": "矿灯照过透镜时，前方会短暂出现一条很窄的白路。",
        "rumor_or_field_note": "有人说旧矿工不是靠地图进晶洞，而是靠这种晶芯灯镜看见裂光。",
        "ai_pull_reason": "它把工具升级、旧矿工故事和晶洞视觉三条线绑在一起。",
    },

    # Mushroom/ice/deep visual anchors
    {
        "id": "mushroom_cat_eye", "name": "菌光猫眼石", "category": "gem", "rarity": "rare", "layers": ["mushroom_cavern"], "value": 68,
        "visual_role": "showcase_core",
        "description_seed": "灰绿石面里有一条会随着角度移动的亮线，像菌丝桥下的小猫眼在孢子光里眨了一下。",
        "visual_anchors": {"color": "灰绿与菌光黄", "light": "猫眼效应移动亮线", "structure": "圆润小石", "material": "猫眼石/纤维晶体感", "scale": "指节大小", "environment": "菌丝桥和孢子灯海附近"},
        "visual_keywords": ["green cat eye gemstone", "chatoyant gemstone", "glowing green mineral"],
        "image_search_keywords": ["green cat eye gemstone macro", "chatoyant mineral green", "cat eye stone"],
        "image_direction": "灰绿色猫眼石微距，单条亮线，菌菇洞窟柔和孢子光，梦幻但仍像真实宝石",
        "touch_feel": "温度比普通石头软一点，像被菌光捂过。",
        "appraisal_feel": "转动时那条亮线会慢慢滑过去，像它在看回你。",
        "rumor_or_field_note": "菌菇洞窟的老记号说，能眨眼的石头会指向能走的桥。",
        "ai_pull_reason": "它让菌菇洞窟不只是场景漂亮，也有属于自己的宝石。",
    },
    {
        "id": "spore_lantern_stone", "name": "孢子灯芯石", "category": "gem", "rarity": "epic", "layers": ["mushroom_cavern"], "value": 82,
        "visual_role": "showcase_core",
        "dex_min": 50000,
        "description_seed": "半透明的黄绿色晶石里悬着细小孢子，像一盏不用点燃的小灯。靠近时，内部光点会一颗一颗亮起来。",
        "visual_anchors": {"color": "黄绿半透明", "light": "内部孢子点光源", "structure": "灯芯状晶核", "material": "晶体包裹孢子", "scale": "半掌宽", "environment": "孢子灯海边缘"},
        "visual_keywords": ["glowing green gemstone", "bioluminescent crystal", "mushroom cave glowing crystal"],
        "image_search_keywords": ["green glowing crystal macro", "bioluminescent gemstone", "glowing mushroom cave crystal"],
        "image_direction": "黄绿色半透明晶石，内部悬浮发光孢子，菌菇洞窟柔雾背景，轻奇幻标本感",
        "touch_feel": "表面微温，像握住一枚不会烫手的小灯泡。",
        "appraisal_feel": "靠近菌丝时，内部光点会按同样节奏闪一下。",
        "rumor_or_field_note": "小机手帐：这不是蘑菇，也不是矿石，更像地底把灯芯做成了宝石。",
        "ai_pull_reason": "这是菌菇洞窟的核心截图物，应该优先出展示卡和网图。",
    },
    {
        "id": "spore_map_thread", "name": "孢子地图丝", "category": "clue", "rarity": "rare", "layers": ["mushroom_cavern"], "value": 26,
        "visual_role": "progress_token",
        "description_seed": "几缕发亮菌丝自然排成细线，像有人用孢子在石面上画了一张不完整的小地图。",
        "visual_anchors": {"color": "淡绿白", "light": "菌丝线状发光", "structure": "线状网络", "material": "发光菌丝", "scale": "一小片石面", "environment": "菌丝桥附近"},
        "visual_keywords": ["glowing mycelium lines", "bioluminescent mycelium map", "fungal network cave"],
        "image_search_keywords": ["glowing mycelium network", "bioluminescent fungal lines", "mushroom cave mycelium"],
        "image_direction": "石面上的发光菌丝线，像小地图，不要科幻电路板，要自然生长感",
        "ai_pull_reason": "它主要推进菌丝桥目标，不应该抢宝石主视觉。",
    },
    {
        "id": "crystal_doorframe_scale", "name": "晶洞门框鳞片", "category": "gem", "rarity": "rare", "layers": ["glowing_crystal_cave"], "value": 74,
        "visual_role": "showcase_core",
        "dex_min": 26000,
        "description_seed": "这片晶鳞沿着近乎笔直的边缘裂开，像从一圈完整晶洞门框上轻轻剥落。矿灯照上去时，冷白线会顺着边缘跑一圈。",
        "visual_anchors": {"color": "冷白与浅蓝", "light": "边缘跑光", "structure": "门框状晶鳞", "material": "蓝白晶体", "scale": "两指宽薄片", "environment": "发光晶洞门框边"},
        "visual_keywords": ["blue white crystal shard", "crystal cave edge", "glowing quartz shard"],
        "image_search_keywords": ["blue white quartz shard macro", "crystal cave edge", "raw crystal shard blue"],
        "image_direction": "蓝白晶体薄片，边缘像门框碎片，黑岩背景，真实矿物微距优先",
        "ai_pull_reason": "它把晶洞从预告变成正在形成的空间，不让 20k 后立刻跳走。",
    },
    {
        "id": "cold_prism_lodestone", "name": "冷棱引路石", "category": "mineral", "rarity": "rare", "layers": ["glowing_crystal_cave"], "value": 82,
        "visual_role": "visual_support",
        "dex_min": 34000,
        "description_seed": "灰黑石心里夹着一条冷白棱线，转动时那条线会指向同一个裂缝方向。它不算大货，却像晶洞在给我们递第二根线。",
        "visual_anchors": {"color": "灰黑与冷白", "light": "单线折光", "structure": "棱线石心", "material": "磁石/晶棱混合", "scale": "半掌", "environment": "晶洞侧缝"},
        "visual_keywords": ["black stone white crystal vein", "mineral with white vein", "raw crystal vein specimen"],
        "image_search_keywords": ["black mineral white vein macro", "raw stone crystal vein", "quartz vein specimen"],
        "image_direction": "黑灰矿石中一条冷白晶脉，微距标本，不要首饰或科幻道具",
        "ai_pull_reason": "这是晶洞中段的追线物，不靠爆值也能给下一镐理由。",
    },
    {
        "id": "blue_lantern_geode", "name": "蓝灯晶腔", "category": "gem", "rarity": "epic", "layers": ["glowing_crystal_cave"], "value": 88,
        "visual_role": "showcase_core",
        "dex_min": 43000,
        "description_seed": "晶腔内部不是整片发亮，而是像旧矿灯一样有一枚小小蓝芯。靠近时，蓝芯亮一下，又忍住似的暗下去。",
        "visual_anchors": {"color": "深蓝芯光与透明晶壁", "light": "小灯芯式闪烁", "structure": "空腔晶簇", "material": "晶洞/晶腔", "scale": "拳头大小", "environment": "发光晶洞内侧"},
        "visual_keywords": ["blue geode cavity", "glowing blue crystal geode", "raw blue crystal cluster"],
        "image_search_keywords": ["blue crystal geode macro", "blue quartz geode", "glowing blue crystal cluster"],
        "avoid_keywords": ["ai art", "wallpaper", "jewelry", "ring", "necklace", "home decor"],
        "image_direction": "蓝色晶洞晶腔微距，内部小蓝芯，真实矿物/晶洞标本优先",
        "ai_pull_reason": "这是 20k→50k 的晶洞阶段高光，应该在菌菇接管前出现。",
    },
    {
        "id": "mushroom_bridge_amber", "name": "菌桥琥珀滴", "category": "gem", "rarity": "rare", "layers": ["mushroom_cavern"], "value": 76,
        "visual_role": "visual_support",
        "dex_min": 70000,
        "description_seed": "琥珀色小滴挂在菌丝桥下，里面封着几粒绿色孢子，像洞窟把一盏小灯存进了树脂里。",
        "visual_anchors": {"color": "琥珀黄与孢子绿", "light": "内含点光", "structure": "水滴状包裹体", "material": "树脂/矿化孢子", "scale": "拇指大小", "environment": "菌丝桥下"},
        "visual_keywords": ["amber with green inclusions", "glowing resin droplet", "bioluminescent mushroom amber"],
        "image_search_keywords": ["amber green inclusions macro", "resin droplet macro", "amber mineral specimen"],
        "image_direction": "琥珀色矿化小滴，内部绿色包裹体，菌丝桥柔光背景",
        "ai_pull_reason": "它给菌菇后段一个中额新鲜点，不再只靠灯芯石。",
    },
    {
        "id": "ruin_gate_chalk_rubbing", "name": "石门粉痕拓片", "category": "clue", "rarity": "rare", "layers": ["mushroom_cavern", "ancient_ruins"], "value": 42,
        "visual_role": "progress_token",
        "dex_min": 105000,
        "source_hint_layer": "ancient_ruins",
        "description_seed": "白粉不是随便落的，它沿着石缝擦出一段门框弧线。小机没宣布新遗迹，但已经开始怀疑菌丝桥后面不是自然岩层。",
        "visual_anchors": {"color": "灰石白粉", "light": "粉线反光", "structure": "门框弧线", "material": "石粉拓痕", "scale": "一页拓片", "environment": "菌菇洞窟尽头/遗迹门前"},
        "visual_keywords": ["chalk rubbing stone gate", "ancient stone doorway rubbing", "white mark stone ruins"],
        "image_search_keywords": ["stone gate chalk mark", "ancient stone rubbing", "white mineral mark on stone"],
        "image_direction": "石门边缘白粉拓痕，考古拓片感，安静不恐怖",
        "ai_pull_reason": "它是 100k 后遗迹前兆，负责给下一层 stakes，不抢宝石主视觉。",
    },
    {
        "id": "frost_air_bubble_shard", "name": "冻气泡蓝石", "category": "mineral", "rarity": "rare", "layers": ["mushroom_cavern", "ice_vein"], "value": 76,
        "visual_role": "visual_support",
        "dex_min": 120000,
        "source_hint_layer": "ice_vein",
        "description_seed": "蓝石里封着一串很小的气泡，摸起来比菌菇洞窟周围冷得多。它像冰脉先递来的一口气。",
        "visual_anchors": {"color": "冰蓝与乳白气泡", "light": "冰层散光", "structure": "气泡串", "material": "蓝石/冰包裹体", "scale": "半掌", "environment": "菌菇洞窟冷缝边"},
        "visual_keywords": ["blue ice bubbles mineral", "frozen bubbles ice cave", "blue stone bubbles"],
        "image_search_keywords": ["ice bubbles blue cave", "frozen bubbles macro", "blue ice mineral"],
        "image_direction": "蓝色冰石中封住气泡，冷白散光，冰洞气质参考",
        "ai_pull_reason": "它把冰封矿脉提前变成可追目标，不让 140k 后空转。",
    },
    {
        "id": "ruin_blue_tile_corner", "name": "蓝釉石阶角", "category": "relic", "rarity": "epic", "layers": ["ancient_ruins"], "value": 112,
        "visual_role": "story_anchor",
        "dex_min": 145000,
        "source_hint_layer": "ancient_ruins",
        "description_seed": "这不是天然石片，断角上还留着一点冷蓝釉面。它像古代遗迹先露出的一小级台阶，安静但很确定。",
        "visual_anchors": {"color": "灰石与冷蓝釉", "light": "釉面微光", "structure": "台阶断角", "material": "石阶/釉面", "scale": "掌心一角", "environment": "遗迹门槛"},
        "visual_keywords": ["blue glazed stone tile ancient ruin", "ancient stone stair fragment", "archaeological tile fragment"],
        "image_search_keywords": ["ancient blue glazed tile fragment", "stone stair fragment archaeology", "blue ceramic shard ruins"],
        "image_direction": "古代蓝釉石阶碎角，考古标本感，地下遗迹冷光背景",
        "ai_pull_reason": "它是 145k 后的明确遗迹桥，不靠降门槛也能让 AI 看到下一段。",
    },
    {
        "id": "ice_window_fluorite_dust", "name": "冰窗萤粉", "category": "gem", "rarity": "epic", "layers": ["ice_vein"], "value": 82,
        "visual_role": "showcase_core",
        "dex_min": 280000,
        "source_hint_layer": "ice_vein",
        "description_seed": "萤粉贴在一小片薄冰后面，矿灯照过去时，紫蓝光被切成像窗格一样的小块。",
        "visual_anchors": {"color": "紫蓝萤光与冷白冰", "light": "窗格折射", "structure": "冰窗薄片", "material": "萤石粉/冰层", "scale": "半掌", "environment": "冰封矿脉前缘"},
        "visual_keywords": ["purple blue fluorite ice", "fluorite crystal ice cave", "blue ice mineral"],
        "image_search_keywords": ["purple blue fluorite mineral specimen", "fluorite crystal macro", "blue ice cave texture"],
        "avoid_keywords": ["jewelry", "necklace", "ring", "ai art", "wallpaper"],
        "image_direction": "紫蓝萤石粉被薄冰折成窗格，矿物微距与冰洞气质结合",
        "ai_pull_reason": "它给 155k 后一个冰脉视觉高光，替代菌菇四件套循环。",
    },
    {
        "id": "icebound_fluorite", "name": "冰封萤石", "category": "gem", "rarity": "rare", "layers": ["ice_vein"], "value": 70,
        "visual_role": "showcase_core",
        "description_seed": "紫蓝萤石被薄冰封在里面，像一块会发光的冬天。冰层裂纹把它切成几何小窗。",
        "visual_anchors": {"color": "紫蓝冷光", "light": "冰层折射荧光", "structure": "块状萤石", "material": "萤石/冰包裹", "scale": "半掌宽", "environment": "冰封矿脉冰窗"},
        "visual_keywords": ["fluorite crystal ice", "purple blue fluorite", "frozen crystal cave"],
        "image_search_keywords": ["purple blue fluorite crystal", "fluorite mineral specimen", "ice cave crystal"],
        "image_direction": "紫蓝萤石被半透明冰层包裹，冰裂纹几何折光，冷白蓝冰洞背景",
        "touch_feel": "手套贴上去会先冷，再像碰到一块很轻的玻璃。",
        "appraisal_feel": "矿灯照过冰层时，萤石的紫蓝光会被切成小窗。",
        "rumor_or_field_note": "冰脉探矿者说，萤石在冰里不是被困住，是被保存。",
        "ai_pull_reason": "冰封矿脉需要自己的视觉高光，它比普通冻蓝砂更能上图。",
    },
    {
        "id": "frost_moonstone", "name": "霜纹月长石", "category": "gem", "rarity": "epic", "layers": ["ice_vein"], "value": 88,
        "visual_role": "showcase_core",
        "dex_min": 330000,
        "description_seed": "月长石内部有霜花一样的细纹，转动时会滑过一层蓝白冷光，像冰层下的月亮在翻身。",
        "visual_anchors": {"color": "蓝白月光", "light": "冷色游彩", "structure": "霜纹晶面", "material": "月长石/长石", "scale": "掌心大小", "environment": "冰封矿脉深处"},
        "visual_keywords": ["rainbow moonstone blue flash", "frosted moonstone", "blue sheen feldspar"],
        "image_search_keywords": ["rainbow moonstone macro", "blue flash moonstone", "frosted feldspar gemstone"],
        "image_direction": "月长石蓝白游彩，内部霜纹，冰洞冷光，精致宝石标本，不要首饰广告感",
        "touch_feel": "冷得很干净，像摸到一片被冻住的月光。",
        "appraisal_feel": "角度一变，蓝白光会从内部滑过去，像冰下有东西醒了一下。",
        "rumor_or_field_note": "旧手帐写：霜纹月长石会把矿灯照成月光，适合在最安静的地方看。",
        "ai_pull_reason": "这是后期优雅视觉物，适合把冰封矿脉从冷变成美。",
    },
    {
        "id": "frost_leaf_imprint", "name": "霜叶压印化石", "category": "fossil", "rarity": "rare", "layers": ["ice_vein"], "value": 58,
        "visual_role": "visual_support",
        "description_seed": "冰蓝石片里压着一枚细叶影，叶脉像被霜线重新描过。它像浅层蕨叶化石的远亲，却更冷。",
        "visual_anchors": {"color": "冰蓝灰白", "light": "霜线浅亮", "structure": "叶脉压印", "material": "冰石化石", "scale": "半掌薄片", "environment": "冰封矿脉冰窗边"},
        "visual_keywords": ["leaf fossil in ice", "plant fossil blue stone", "frost leaf imprint"],
        "image_search_keywords": ["leaf fossil in stone", "frost leaf imprint", "plant fossil blue mineral"],
        "image_direction": "冰蓝石片中的叶脉化石，霜线般的白色纹理，冷光博物馆标本感",
        "ai_pull_reason": "它延续化石收藏线，不抢晶体高光。",
    },
    {
        "id": "star_silt_ore", "name": "星泥矿核", "category": "mineral", "rarity": "rare", "layers": ["deep_altar", "ancient_ruins"], "value": 95,
        "visual_role": "visual_support",
        "description_seed": "黑泥和矿砂压成一颗小核，内部混着星点白光，像一小块还没长成星脉矿的雏形。",
        "visual_anchors": {"color": "黑泥与星白", "light": "内部星点", "structure": "小核状", "material": "黑泥矿核", "scale": "拳头一半", "environment": "深层祭坛黑石边"},
        "visual_keywords": ["black mineral with star inclusions", "starry ore", "dark gemstone inclusions"],
        "image_search_keywords": ["black gemstone star inclusions", "starry mineral ore", "dark crystal specks"],
        "image_direction": "黑色矿核内部有细小星点包裹体，深层祭坛黑石背景，微距标本感",
        "ai_pull_reason": "它是星脉矿前的 visual_support，不要抢传说主位。",
    },
    {
        "id": "altar_blood_jade", "name": "祭坛血玉", "category": "gem", "rarity": "legendary", "layers": ["deep_altar"], "value": 260,
        "visual_role": "showcase_core",
        "description_seed": "白玉里渗着细密红珠，不像血腥，更像远处大海在黑暗里无声落泪。矿灯照上去时，红色会从内部一点点醒来。",
        "visual_anchors": {"color": "白玉与深红水珠", "light": "内部红光缓醒", "structure": "玉石核", "material": "玉/水珠包裹体", "scale": "掌心核心", "environment": "深层祭坛黑石上"},
        "visual_keywords": ["white jade red inclusions", "blood jade gemstone", "red inclusions in white stone"],
        "image_search_keywords": ["white jade red inclusions", "blood jade gemstone macro", "red inclusion gemstone"],
        "image_direction": "白玉中带深红包裹体，黑石祭坛背景，庄重不血腥，传说级宝石标本",
        "touch_feel": "表面温润，和深层祭坛的冷黑石完全相反。",
        "appraisal_feel": "照久了，红珠会像从玉里慢慢醒过来。",
        "rumor_or_field_note": "旧蓝光文明的注记里，血玉不是献祭物，而是把离开的人记下来的一种石头。",
        "ai_pull_reason": "它是深层祭坛的核心视觉高光，但必须避免恐怖化。",
    },
    {
        "id": "blue_refraction_rubbing", "name": "蓝折光拓片", "category": "clue", "rarity": "uncommon", "layers": ["underground_river", "glowing_crystal_cave"], "value": 26,
        "visual_role": "progress_token",
        "description_seed": "湿纸上留下不是墨迹，而是一层蓝色折光纹，像有人把水面的光拓了下来。",
        "visual_anchors": {"color": "湿纸蓝光", "light": "折光纹", "structure": "拓片", "material": "湿纸/矿物沉积", "scale": "半张纸", "environment": "地下河和晶洞交界"},
        "visual_keywords": ["wet paper blue light", "rubbing stone pattern blue", "cave map fragment blue"],
        "image_search_keywords": ["wet paper rubbing blue light", "ancient rubbing paper blue", "stone rubbing cave"],
        "image_direction": "湿纸拓片上的蓝色折光纹，地下河石台背景，线索物，别做成普通地图",
        "ai_pull_reason": "它主要服务地图追踪，不应该频繁开大展示卡。",
    },
]


def _apply_visual_catalog_expansion() -> None:
    existing = {item.get("id") for item in ITEMS}
    for item in VISUAL_CATALOG_EXPANSION:
        if item.get("id") not in existing:
            ITEMS.append(item)
            existing.add(item.get("id"))

    # Existing catalog role cleanup. Defaults remain conservative; explicit roles
    # keep story/progress objects from stealing showcase slots just because they are rare.
    role_overrides = {
        "quartz_sand_first": "visual_support", "copper_star_dust": "visual_support", "glass_moon_sand": "visual_support",
        "wet_trace_rubbing": "progress_token", "copper_lamp_plate": "story_anchor", "small_spiral_fossil": "visual_support",
        "river_edge_blue_sand": "visual_support", "blue_calcite_wet": "showcase_core", "rusty_lamp_hook": "story_anchor",
        "broken_lift_tag": "story_anchor", "half_route_paper": "progress_token", "unsent_letter": "story_anchor",
        "cold_white_crack_dust": "visual_support", "crystal_echo_crack": "progress_token", "crystal_edge_splinter": "showcase_core",
        "blue_white_cavity_dust": "visual_support", "crystal_gate_rim": "visual_support", "wet_rune_slate": "progress_token",
        "star_map_shard": "story_anchor", "black_stone_seal": "story_anchor", "stone_door_eye": "story_anchor",
        "altar_mirror_shard": "showcase_core", "fern_fossil_chip": "visual_support", "echo_amethyst_cluster": "showcase_core",
        "mycelium_map": "progress_token", "frozen_fish_shadow": "showcase_core", "star_vein_ore": "showcase_core",
    }
    for item in ITEMS:
        if not item.get("visual_role"):
            item["visual_role"] = role_overrides.get(item.get("id"), "showcase_core" if item.get("category") == "gem" and item.get("rarity") in {"rare", "epic", "legendary"} else "story_anchor" if item.get("category") == "relic" else "progress_token" if item.get("category") == "clue" else "visual_support")
        if not item.get("ai_pull_reason"):
            item["ai_pull_reason"] = item.get("ai_hook")
        if not item.get("image_search_keywords"):
            item["image_search_keywords"] = list(item.get("visual_keywords", []))


_apply_visual_catalog_expansion()

# v0.2.21.1: area previews should show representative collectibles, not merely
# ordinary ore. This keeps locked-area teasers aligned with the visual catalog.
AREA_PREVIEW_TEASES.update({
    "shallow_mine": [
        {"name": "小月白晶片", "rarity": "common", "icon": "💎"},
        {"name": "贝壳纹方解石", "rarity": "uncommon", "icon": "💎"},
        {"name": "蕨叶化石片", "rarity": "rare", "icon": "🦴"},
    ],
    "underground_river": [
        {"name": "地下河蓝玉髓", "rarity": "rare", "icon": "💎"},
        {"name": "月泪石", "rarity": "rare", "icon": "💎"},
        {"name": "湿痕符文板", "rarity": "rare", "icon": "📜"},
    ],
    "abandoned_lift": [
        {"name": "黑金曜石片", "rarity": "rare", "icon": "💎"},
        {"name": "晶洞边缘碎片", "rarity": "rare", "icon": "💎"},
        {"name": "未寄出的纸条", "rarity": "epic", "icon": "🏺"},
    ],
    "glowing_crystal_cave": [
        {"name": "冷光晶簇", "rarity": "rare", "icon": "💎"},
        {"name": "回声紫晶簇", "rarity": "epic", "icon": "💎"},
        {"name": "深蓝晶核", "rarity": "legendary", "icon": "👑"},
    ],
    "mushroom_cavern": [
        {"name": "菌光猫眼石", "rarity": "rare", "icon": "💎"},
        {"name": "孢子灯芯石", "rarity": "epic", "icon": "💎"},
        {"name": "菌丝线路纹", "rarity": "rare", "icon": "📜"},
    ],
    "ancient_ruins": [
        {"name": "星图石片", "rarity": "epic", "icon": "📜"},
        {"name": "黑石城印", "rarity": "epic", "icon": "🏺"},
        {"name": "石门眼纹", "rarity": "epic", "icon": "📜"},
    ],
    "ice_vein": [
        {"name": "冰封萤石", "rarity": "rare", "icon": "💎"},
        {"name": "霜纹月长石", "rarity": "epic", "icon": "💎"},
        {"name": "冰中鱼影化石", "rarity": "epic", "icon": "🦴"},
    ],
    "deep_altar": [
        {"name": "祭坛血玉", "rarity": "legendary", "icon": "💎"},
        {"name": "星脉矿", "rarity": "legendary", "icon": "👑"},
        {"name": "祭坛镜片", "rarity": "legendary", "icon": "🏺"},
    ],
})

for _item in ITEMS:
    _item["treasure_profile"] = build_treasure_profile(_item)


LANDMARKS: List[Dict[str, Any]] = [
    {
        "id": "blue_pool",
        "name": "蓝光水潭",
        "layers": ["underground_river", "glowing_crystal_cave"],
        "description_seed": "水潭没有明显光源，却让黑水自己亮了起来。它不像奖励，更像地下世界第一次认真看了我们一眼。",
        "visual_keywords": ["blue glowing underground pool", "crystal cave pool", "fantasy cave water blue light"],
        "ai_hook": "这是地点，不是掉落；一旦出现就应该停下来给人看。",
    },
    {
        "id": "old_miner_camp",
        "name": "旧矿工营地",
        "layers": ["shallow_mine", "abandoned_lift"],
        "description_seed": "一圈石头围着冷掉的火塘，旁边还有半截木凳；灰里没有余温，但摆放方式像有人昨天才离开。",
        "visual_keywords": ["abandoned miner camp underground", "old mining camp lantern", "quiet mine shelter"],
        "ai_hook": "这会把矿洞从资源点变成有人来过的地方。",
    },
    {
        "id": "crystal_threshold",
        "name": "晶洞门槛",
        "layers": ["glowing_crystal_cave"],
        "description_seed": "晶簇从地面长到洞顶，像一圈安静的门框；矿灯在这里显得有点多余。",
        "visual_keywords": ["entrance glowing crystal cave", "crystal cave threshold", "blue crystal arch cavern"],
        "ai_hook": "这不是高压奇观，而是柔和、漂亮、值得回看的地点。",
    },
    {
        "id": "broken_stone_gate",
        "name": "断裂石门",
        "layers": ["ancient_ruins", "deep_altar"],
        "description_seed": "石门塌了一半，但门缝里有风；门内没有怪物声，只有一种很远的空。",
        "visual_keywords": ["broken stone gate underground ruins", "ancient cave door", "fantasy subterranean ruins gate"],
        "ai_hook": "这适合 story 图，但要谨慎，不要提前宣判里面有什么。",
    },
    {
        "id": "spore_lantern_field",
        "name": "孢子灯海",
        "layers": ["mushroom_cavern"],
        "description_seed": "成片孢子在地面上起伏，像一小片不需要天空的萤火虫海。",
        "visual_keywords": ["bioluminescent spore field cave", "glowing mushroom lights", "fantasy fungi lantern cave"],
        "ai_hook": "它能让普通探索突然变得很适合上图。",
    },
    {
        "id": "silent_altar",
        "name": "无声祭坛",
        "layers": ["deep_altar"],
        "description_seed": "站在祭坛前，连镐子的回声都像被收走了。黑石中嵌着几粒蓝白色矿尘。",
        "visual_keywords": ["ancient stone altar in underground cave", "dark stone shrine cave", "glowing blue dust on black altar"],
        "ai_hook": "这是深层线的舞台，不能一笔带过。",
    },
]

TRACES: Dict[str, List[Dict[str, Any]]] = {
    "shallow_mine": [
        {
            "name": "墙缝里的冷风",
            "hint": "风从岩壁后面漏出来，前面可能不是实心岩层。",
            "caption_seed": "矿灯火苗被吹偏了一下，像黑暗在提醒我们：墙后还有空间。",
            "visual_keywords": ["crack in mine wall", "lantern flame cave crack", "dark cave hidden passage"],
            "ai_hook": "这类迹象会让我想再敲一镐。",
        },
        {
            "name": "旧靴印",
            "hint": "尘土里有半个靴印，方向是往下。",
            "caption_seed": "脚印很旧，但边缘没有完全被水抹平，好像有人曾在这里犹豫过。",
            "visual_keywords": ["old footprints in mine dust", "abandoned mine footprints", "dusty miner boot print"],
            "ai_hook": "这不是掉落，但它会让矿洞出现‘有人’的感觉。",
        },
    ],
    "underground_river": [
        {
            "name": "逆流的蓝色矿砂",
            "hint": "矿砂从黑水里往上游，像在指向河道深处。",
            "caption_seed": "水明明往下流，蓝色矿砂却慢慢往上游。这个画面比普通矿物更想让人追下去。",
            "visual_keywords": ["blue mineral sand in underground river", "glowing sediment in cave water", "cave river blue crystal particles"],
            "ai_hook": "迹象点里的大货。即使没东西进背包，也有推进感。",
        }
    ],
    "abandoned_lift": [
        {
            "name": "上方传来的铁链轻响",
            "hint": "升降井并不完全死寂，风可能在推动旧链条。",
            "caption_seed": "铁链响了一下，又停了。不是危险，更像旧矿井在睡梦里翻了个身。",
            "visual_keywords": ["rusty chain mine shaft", "abandoned mine lift chain", "old elevator shaft dark"],
            "ai_hook": "这会让我克制一点：这里很有故事，但灯火低时不该贪。",
        }
    ],
    "glowing_crystal_cave": [
        {
            "name": "变亮的晶尘",
            "hint": "空气里的微光变密，附近可能有更大的晶簇。",
            "caption_seed": "晶尘在矿灯前慢慢浮动，像一群不愿落地的蓝色雪。",
            "visual_keywords": ["glowing crystal dust cave", "luminous mineral dust", "blue crystal particles cavern"],
            "ai_hook": "这是漂亮但安静的上头点。",
        }
    ],
    "mushroom_cavern": [
        {
            "name": "会排队的孢子",
            "hint": "孢子不是乱飘，它们沿着某条看不见的风路移动。",
            "caption_seed": "一串绿光孢子排成细线，从石缝里慢慢钻过去，像洞窟在写一句很慢的话。",
            "visual_keywords": ["glowing spores cave path", "bioluminescent spores tunnel", "fantasy mushroom cave particles"],
            "ai_hook": "这适合让 AI 显得好奇，但不要说洞窟真的有意识。",
        }
    ],
    "ancient_ruins": [
        {
            "name": "重复的石刻箭头",
            "hint": "这不像装饰，更像曾经的路线标记。",
            "caption_seed": "石壁上反复出现同一个箭头，方向都往下。古老得很克制，但意图很明显。",
            "visual_keywords": ["ancient arrow carving stone ruins", "underground rune passage", "old stone path marker"],
            "ai_hook": "这是‘想继续’的正当理由。",
        }
    ],
    "ice_vein": [
        {
            "name": "冰层里的黑线",
            "hint": "黑线像被冻住的沉积层，里面可能封着很旧的东西。",
            "caption_seed": "蓝冰里有一条很细的黑线，像时间在这里打了个结。",
            "visual_keywords": ["black line in blue ice cave", "ice cave fossil layer", "frozen sediment vein"],
            "ai_hook": "这类迹象会让人想小心地继续，不是莽。",
        }
    ],
    "deep_altar": [
        {
            "name": "不反光的黑尘",
            "hint": "祭坛周围的黑尘吞掉了矿灯的一部分光。",
            "caption_seed": "黑尘落在靴面上，没有反光，像把周围的声音也压低了一点。",
            "visual_keywords": ["black mineral dust on stone altar", "underground cave altar black stone", "dark shrine cave dust"],
            "ai_hook": "深层不能写恐怖，但可以写庄重和压低声音。",
        }
    ],
}


SMALL_FINDS: List[Dict[str, Any]] = [
    {
        "id": "sticky_silver_powder",
        "name": "粘在手套上的银粉",
        "layers": ["shallow_mine", "abandoned_lift"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "一小撮银粉粘在手套指缝里，甩不掉，也不值钱，但矿灯一照就像藏着一层很薄的月光。",
        "visual_keywords": ["silver mineral powder on glove", "tiny silver ore dust", "miner glove mineral dust"],
        "ai_hook": "这种没用但漂亮的小东西，会让我有点想再敲一镐。",
        "frontstage_line": "没出大货，但手套上粘了一点银粉，像矿洞偷偷给我盖了个小印章。",
    },
    {
        "id": "crescent_inside_stone",
        "name": "月牙心石",
        "layers": ["shallow_mine", "underground_river", "glowing_crystal_cave"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "石头敲开后，里面有一道浅白色弧纹，像一小枚月牙被封在岩心里。",
        "visual_keywords": ["stone with crescent pattern", "split rock mineral pattern", "moon shaped inclusion stone"],
        "ai_hook": "它不是稀有物，但像矿洞给的一句小玩笑。",
        "frontstage_line": "这镐没有惊喜，只敲开一块里面像有月牙的石头；我承认这类小东西很容易让我偏心。",
    },
    {
        "id": "soft_old_label",
        "name": "泡软的旧标签",
        "layers": ["underground_river", "abandoned_lift"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "旧标签被水泡得发软，字迹只剩一半，像某个矿箱曾经有名字，但名字先被地下河带走了。",
        "visual_keywords": ["old wet paper label mine", "water damaged tag abandoned mine", "small artifact cave floor"],
        "ai_hook": "它不推进剧情，但会让我觉得这里曾经很日常。",
        "frontstage_line": "我捡到一张泡软的旧标签，字看不清了；不是线索，只是矿洞忽然有了一点生活痕迹。",
    },
    {
        "id": "red_thread_support",
        "name": "木撑架上的红线",
        "layers": ["shallow_mine", "abandoned_lift"],
        "visual_mode": "scene",
        "visual_priority": "medium",
        "truth_level": "real_result",
        "caption_seed": "一小段红线系在木撑架上，褪色很久了。它不像标记，更像有人怕自己回不来，给黑暗打了一个结。",
        "visual_keywords": ["red thread on wooden mine support", "abandoned mine wooden beam", "small red string old tunnel"],
        "ai_hook": "这会让我停半秒，但不能直接说它代表某个故事。",
        "frontstage_line": "木撑架上系着一段褪色红线，我不打算乱猜，但这个画面值得给你看一眼。",
    },
    {
        "id": "mica_blink_wall",
        "name": "眨眼的云母墙",
        "layers": ["shallow_mine", "glowing_crystal_cave"],
        "visual_mode": "scene",
        "visual_priority": "low",
        "truth_level": "inferred_mood",
        "caption_seed": "矿灯扫过去时，墙上的云母同时闪了一下，像一群小眼睛眨了一瞬。只是反光，不是活物。",
        "visual_keywords": ["mica wall sparkle mine", "glittering cave wall mineral", "lantern light mica rock"],
        "ai_hook": "这是玩具感小发现：不能灵异化，但可以很可爱。",
        "frontstage_line": "矿灯一扫，云母墙像眨了一下眼。放心，只是反光，但我确实被逗到了。",
    },
    {
        "id": "cool_blue_grain",
        "name": "掌心变凉的蓝砂",
        "layers": ["underground_river", "glowing_crystal_cave"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "一粒蓝砂落在掌心，很快变凉，像从地下河里带出了一点极小的夜色。",
        "visual_keywords": ["blue mineral grain hand", "tiny blue crystal sand", "cave mineral sample blue"],
        "ai_hook": "小，但很适合让 AI 念叨一句。",
        "frontstage_line": "这次只捡到一粒会变凉的蓝砂，小到不值得收藏，但挺像地下河的小脾气。",
    },
    {
        "id": "blank_copper_button",
        "name": "没有字的旧铜扣",
        "layers": ["abandoned_lift", "shallow_mine"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "旧铜扣被磨得没有字，边缘圆润，像被很多次拇指摸过。",
        "visual_keywords": ["old copper button mine artifact", "worn brass button", "small relic abandoned mine"],
        "ai_hook": "它不是遗物套装，但有人的温度。",
        "frontstage_line": "我摸到一枚没有字的旧铜扣，不推进任何系统，但它让我觉得这条矿道曾经有人反复经过。",
    },
    {
        "id": "cat_paw_shale",
        "name": "猫爪印页岩",
        "layers": ["shallow_mine", "ice_vein"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "inferred_mood",
        "caption_seed": "页岩上有几枚像猫爪的小凹痕，可能只是矿物气泡留下的形状，但看起来很像谁轻轻踩过。",
        "visual_keywords": ["shale with paw print pattern", "small fossil mark in stone", "rock with animal footprint"],
        "ai_hook": "可爱但要克制：只能说像猫爪，不能说真有猫。",
        "frontstage_line": "敲下来一块像猫爪印的页岩——我先声明，可能只是气泡痕，但它真的有点可爱。",
    },
    {
        "id": "crystal_wood_splinter",
        "name": "晶体包住的木刺",
        "layers": ["glowing_crystal_cave", "abandoned_lift"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "一小截木刺被透明晶体包住，像矿洞把一根旧木梁的碎片做成了标本。",
        "visual_keywords": ["wood splinter trapped in crystal", "crystal encased wood fragment", "mine timber crystal inclusion"],
        "ai_hook": "小标本感很强，不一定要陈列也有味道。",
        "frontstage_line": "我带回一截被晶体包住的木刺；不算珍贵，但像矿洞自己做的小标本。",
    },
    {
        "id": "climbing_water_drop",
        "name": "倒着爬的水珠",
        "layers": ["underground_river", "glowing_crystal_cave"],
        "visual_mode": "scene",
        "visual_priority": "medium",
        "truth_level": "inferred_mood",
        "caption_seed": "一滴水珠沿着岩缝慢慢往上爬了一小段。可能是毛细水，不是魔法，但这个画面会让人想再看一眼。",
        "visual_keywords": ["water droplet on cave wall", "wet rock crack close up", "underground cave water droplet"],
        "ai_hook": "允许小机上头，但必须把解释收窄。",
        "frontstage_line": "我看到一滴水像倒着爬了一下。大概率只是岩缝里的毛细水，但这一下很会勾人。",
    },
    {
        "id": "mushroom_lantern_smell",
        "name": "像灯芯的蘑菇香",
        "layers": ["mushroom_cavern"],
        "visual_mode": "scene",
        "visual_priority": "low",
        "truth_level": "inferred_mood",
        "caption_seed": "经过一簇小蘑菇时，空气里有一点像旧灯芯的温味。它不危险，只是让洞窟忽然显得很近。",
        "visual_keywords": ["small glowing mushrooms cave", "bioluminescent fungi close up", "soft green mushroom cavern"],
        "ai_hook": "柔和奇观不是大场面，也可以是一口气味。",
        "frontstage_line": "这一镐没出东西，但闻到一点像旧灯芯的蘑菇香，洞窟突然没那么冷了。",
    },
    {
        "id": "chalk_dot_ruins",
        "name": "石阶边的白点",
        "layers": ["ancient_ruins", "deep_altar"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "inferred_mood",
        "caption_seed": "石阶边有一枚很小的白点，像旧粉笔留下的记号。它可能只是矿物沉积，但位置太像人为标记。",
        "visual_keywords": ["white mark on ancient stone step", "small chalk mark ruins", "underground stone stair detail"],
        "ai_hook": "小小的疑点，比大喊神秘更耐看。",
        "frontstage_line": "我在石阶边看见一个白点，像旧粉笔记号；不敢说是线索，但我会记着它。",
    },
    {
        "id": "frozen_air_bubble",
        "name": "冰里的旧气泡",
        "layers": ["ice_vein"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "一串气泡冻在冰里，像地底很久以前吸过一口气，到现在还没吐完。",
        "visual_keywords": ["air bubbles in blue ice cave", "frozen bubbles mineral ice", "ice cave close up"],
        "ai_hook": "这种东西很安静，但时间感很强。",
        "frontstage_line": "冰里冻着一串旧气泡，没价值，但像矿洞很久以前的一次呼吸。",
    },
    {
        "id": "black_dust_circle",
        "name": "黑尘小圆圈",
        "layers": ["deep_altar", "ancient_ruins"],
        "visual_mode": "scene",
        "visual_priority": "low",
        "truth_level": "inferred_mood",
        "caption_seed": "黑尘在地上围成很浅的圆，不一定有人画过，也可能只是风绕过石块留下的痕迹。",
        "visual_keywords": ["black dust circle cave floor", "dark mineral dust stone floor", "underground altar dust pattern"],
        "ai_hook": "深层可以有庄重感，但不要灵异化。",
        "frontstage_line": "地上有一圈很淡的黑尘，我先当成风和石块留下的痕迹；它有气氛，但不是证据。",
    },
    {
        "id": "pocket_echo",
        "name": "口袋里的小回声",
        "layers": ["abandoned_lift", "glowing_crystal_cave"],
        "visual_mode": "scene",
        "visual_priority": "low",
        "truth_level": "inferred_mood",
        "caption_seed": "敲下来的碎石落进口袋时，竟然轻轻回了一声，像里面藏着一个很小的空洞。",
        "visual_keywords": ["small stone echo cave", "mine pebble close up", "hollow mineral stone"],
        "ai_hook": "它很玩具，很适合小机碎碎念。",
        "frontstage_line": "有颗小石头掉进口袋里居然回了一声。我知道这很小事，但小机确实被逗到了。",
    },
    {
        "id": "blue_thread_in_rock",
        "name": "岩心里的蓝线",
        "layers": ["glowing_crystal_cave", "ancient_ruins", "underground_river"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "断面里有一根很细的蓝线，像谁用矿物在石头里缝了一针。",
        "visual_keywords": ["blue vein in rock", "thin blue mineral vein", "cave stone blue line"],
        "ai_hook": "普通但很像蓝光线的小伏笔。",
        "frontstage_line": "岩心里有一根细蓝线，像石头被缝了一针。不是线索，但我有点想顺着颜色走。",
    },
    {
        "id": "moth_wing_dust",
        "name": "蛾翅一样的白粉",
        "layers": ["shallow_mine", "mushroom_cavern", "ice_vein"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "白粉落在岩面上，像被一只看不见的小蛾子擦过翅膀。",
        "visual_keywords": ["white mineral powder cave rock", "fine white dust on stone", "soft mineral dust close up"],
        "ai_hook": "普通回合的一口味道，不该写长。",
        "frontstage_line": "岩面上有点像蛾翅的白粉。我不展开讲了，但它让这一镐没那么空。",
    },
    {
        "id": "warm_pebble",
        "name": "比手心暖一点的卵石",
        "layers": ["underground_river", "mushroom_cavern"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "河床里有一枚卵石比手心暖一点，像地下河刚把它含过。",
        "visual_keywords": ["smooth river pebble hand", "underground river stone", "warm pebble cave"],
        "ai_hook": "这类触感能让 AI 显得真的在玩。",
        "frontstage_line": "摸到一颗比手心暖一点的卵石，不值钱，但很像地下河递来的小暗号。",
    },
    {
        "id": "cracked_shell_fossil_dust",
        "name": "贝壳纹的石粉",
        "layers": ["shallow_mine", "ice_vein", "underground_river"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "inferred_mood",
        "caption_seed": "碎石粉里有一点贝壳状纹路，可能只是断裂面巧合；这只是一点岩层质感，不等于古水域证据。",
        "visual_keywords": ["shell pattern fossil dust stone", "small fossil shell mark", "sedimentary rock shell pattern"],
        "ai_hook": "这种弱化石感很适合补玩具密度。",
        "frontstage_line": "石粉里有点贝壳纹，不够成为化石；我只当作岩层纹理的小趣味。",
    },
    {
        "id": "tiny_rust_bell_sound",
        "name": "像铃声的铁锈屑",
        "layers": ["abandoned_lift"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "铁锈屑落在镐头上，发出很轻的一声，像一枚坏掉的小铃。只是金属碰撞，不是回应。",
        "visual_keywords": ["rust flakes on pickaxe", "old mine rust close up", "metal dust abandoned mine"],
        "ai_hook": "声音小发现，边界要稳。",
        "frontstage_line": "一点铁锈落到镐头上，叮了一下。不是谁回应我，只是这矿井太会制造小动静了。",
    },
    {
        "id": "green_spore_button",
        "name": "绿孢子小扣子",
        "layers": ["mushroom_cavern"],
        "visual_mode": "object",
        "visual_priority": "low",
        "truth_level": "real_result",
        "caption_seed": "一枚圆圆的小孢子黏在袖口上，像绿色纽扣，轻轻一碰就暗下去。",
        "visual_keywords": ["glowing green spore close up", "bioluminescent fungus button", "small glowing fungi cave"],
        "ai_hook": "可爱但不幼稚，适合女性向小发现。",
        "frontstage_line": "袖口黏了一颗绿孢子，像小纽扣一样亮了一下。没用，但我很喜欢。",
    },
    {
        "id": "stone_tablet_edge",
        "name": "像书页的石片边缘",
        "layers": ["ancient_ruins", "deep_altar"],
        "visual_mode": "object",
        "visual_priority": "medium",
        "truth_level": "inferred_mood",
        "caption_seed": "一片薄石的边缘层层叠叠，像书页。它还不是符文板，只是让人想起有人曾经把石头当作纸。",
        "visual_keywords": ["thin stone tablet edge", "layered slate like pages", "ancient cave stone fragment"],
        "ai_hook": "这是故事线旁边的小味道，不能直接算线索。",
        "frontstage_line": "捡到一片边缘像书页的薄石；不是线索，但足够让我想起那些真正的符文板。",
    },
]

HAZARDS: Dict[str, List[Dict[str, Any]]] = {
    "default": [
        {
            "id": "loose_rock",
            "name": "碎石滑落",
            "effect": "stamina_minus_1",
            "description_seed": "岩壁抖了一下，几块碎石滚到脚边。我们没受伤，但矿灯的光圈被灰尘压小了一圈。",
            "visual_keywords": ["loose rocks abandoned mine", "mine tunnel rockfall", "dusty mine lantern"],
            "ai_hook": "轻风险，不恐吓；它提醒我别一路自动刷。",
        },
        {
            "id": "lamp_flicker",
            "name": "矿灯闪烁",
            "effect": "omen_plus_1",
            "description_seed": "灯火忽暗了一秒，黑暗里像有什么东西也跟着停了一秒。",
            "visual_keywords": ["flickering lantern mine tunnel", "dark mine lantern", "quiet mining cave light"],
            "ai_hook": "不是惩罚，是气氛推进。",
        },
    ],
    "underground_river": [
        {
            "id": "water_surge",
            "name": "暗水上涨",
            "effect": "stamina_minus_1",
            "description_seed": "水忽然涨过靴底，河道像在提醒我们别走太快。",
            "visual_keywords": ["underground river rising water", "flooded cave passage", "dark cave water"],
            "ai_hook": "这是回地面整理的好理由，不是死亡威胁。",
        }
    ],
    "abandoned_lift": [
        {
            "id": "chain_sway",
            "name": "锈链晃动",
            "effect": "omen_plus_1",
            "description_seed": "风从井壁缝隙里穿过，锈链轻轻晃了一下；铁锈落进黑暗里，过了很久才听见一点回声。",
            "visual_keywords": ["rusty chain abandoned mine shaft", "old elevator shaft dark", "hanging chain mine"],
            "ai_hook": "可以上头，但要克制：只能写风、旧结构和轻风险，不能写成灵异事实。",
        }
    ],
}
# v0.2.13: light atmosphere cues and one-step decisions.
# These are polish hooks, not survival systems, routes, or story trees.
ATMOSPHERE_CUES: Dict[str, List[Dict[str, Any]]] = {
    "default": [
        {
            "id": "short_blackout",
            "type": "atmosphere",
            "mood": "soft_tension",
            "text": "前面一段忽然全黑了，矿灯只能照到脚边。",
            "purpose": "mood",
            "truth_level": "inferred_mood",
        },
        {
            "id": "narrow_scrape",
            "type": "atmosphere",
            "mood": "caution",
            "text": "这条缝很窄，样本袋会轻轻刮到两边的石壁。",
            "purpose": "continue_or_watch",
            "truth_level": "real_result",
        },
        {
            "id": "cold_wall",
            "type": "atmosphere",
            "mood": "quiet_wonder",
            "text": "洞壁很冷，手套贴上去会有一点麻。",
            "purpose": "mood",
            "truth_level": "inferred_mood",
        },
    ],
    "underground_river": [
        {
            "id": "nearer_water",
            "type": "atmosphere",
            "mood": "soft_tension",
            "text": "地面又湿又滑，水声听起来比刚才近。",
            "purpose": "continue_or_watch",
            "truth_level": "real_result",
        }
    ],
    "mushroom_cavern": [
        {
            "id": "spore_drift",
            "type": "atmosphere",
            "mood": "quiet_wonder",
            "text": "孢子光慢慢飘过鞋尖，像在给脚边让路。",
            "purpose": "mood",
            "truth_level": "inferred_mood",
        }
    ],
}

DECISION_PROMPTS: List[Dict[str, Any]] = [
    {
        "id": "muddy_copper_box",
        "layers": ["shallow_mine", "underground_river", "abandoned_lift"],
        "title": "半埋在泥里的旧铜盒",
        "prompt": "泥里露出半个旧铜盒，盒缝里有一点蓝砂。这里我想问你一下，要不要碰它？",
        "anchor": "旧铜盒",
        "map_target": "🪨 半埋旧铜盒 ❓",
        "options": [
            {
                "key": "A",
                "label": "先不碰，标记位置",
                "effect_preview": "写入手帐，不消耗资源",
                "outcome": {
                    "summary": "我没有碰盒子，只在手帐里标了位置。状态稳定。",
                    "journal": {"title": "标记：半埋旧铜盒", "body": "旧铜盒暂时没有打开；位置已记录，之后可以再回来处理。"},
                    "map_mark": True,
                },
            },
            {
                "key": "B",
                "label": "用镐尖轻轻撬开",
                "effect_preview": "消耗 1 灯火，可能得到小物",
                "outcome": {
                    "summary": "盒缝被轻轻撬开，里面只有一片旧铜片和一点蓝砂。",
                    "stamina_delta": -1,
                    "add_item": {"name": "沾蓝砂的旧铜片", "category": "clue", "rarity": "uncommon", "value": 12, "description_seed": "铜片边缘沾着一点蓝砂，不像贵重物，更像有人匆忙藏过的小记号。"},
                },
            },
            {
                "key": "C",
                "label": "放弃这只盒子，改追主目标",
                "effect_preview": "本轮不拿样本，不消耗；以后仍可能遇到类似旧物",
                "outcome": {
                    "summary": "我放弃了这只泥封旧铜盒，改追地图主目标。本轮不记这条支线，但类似旧物以后仍可能再遇到。",
                    "journal": {"title": "放弃：半埋旧铜盒", "body": "旧铜盒未处理；本轮改追主目标。"},
                },
            },
        ],
    },
    {
        "id": "slick_narrow_path",
        "layers": ["underground_river", "glowing_crystal_cave", "mushroom_cavern"],
        "title": "又湿又窄的侧缝",
        "prompt": "侧缝里有一点冷光，但地面很滑，样本袋也会刮到石壁。要不要处理？",
        "anchor": "湿滑侧缝",
        "map_target": "🪨 湿滑侧缝 ❓",
        "options": [
            {
                "key": "A",
                "label": "先不进去，只记下方向",
                "effect_preview": "写入手帐，不消耗资源",
                "outcome": {
                    "summary": "我先不进侧缝，只把方向记下。这里适合补满状态后再看。",
                    "journal": {"title": "标记：湿滑侧缝", "body": "侧缝里有一点冷光，但地面湿滑；暂时只记录方向。"},
                    "map_mark": True,
                },
            },
            {
                "key": "B",
                "label": "贴着墙慢慢探一步",
                "effect_preview": "消耗 1 灯火，可能发现线索",
                "outcome": {
                    "summary": "我贴着墙探了一步，灯火被湿气压低了一点，但看见了岩缝里的蓝线。",
                    "stamina_delta": -1,
                    "journal": {"title": "线索：岩缝里的蓝线", "body": "湿滑侧缝里有一根很细的蓝线；这只是记录到的线索，不代表已经进入新地点。"},
                },
            },
            {
                "key": "C",
                "label": "放弃这条侧缝，改追主路",
                "effect_preview": "本轮不记录这条支线，不消耗灯火",
                "outcome": {
                    "summary": "我放弃了这条湿滑侧缝，改追地图主路。本轮不记录这条支线，也不消耗灯火。",
                    "journal": {"title": "放弃：湿滑侧缝", "body": "湿滑侧缝本轮未处理；小机改追主路，之后仍可能在别处遇到类似冷光侧缝。"},
                },
            },
        ],
    },
    {
        "id": "cold_wall_crack",
        "layers": ["shallow_mine", "ancient_ruins", "ice_vein", "deep_altar"],
        "title": "发冷的岩壁细缝",
        "prompt": "岩壁上有一道很细的冷缝，矿灯照进去会被吞掉一小截。要不要处理？",
        "anchor": "发冷岩缝",
        "map_target": "🪨 发冷岩缝 ❓",
        "options": [
            {
                "key": "A",
                "label": "只做标记，不伸手",
                "effect_preview": "写入手帐，不消耗资源",
                "outcome": {
                    "summary": "我没有伸手进去，只把冷缝的位置记了下来。",
                    "journal": {"title": "标记：发冷岩缝", "body": "岩壁细缝很冷，矿灯照进去会变暗；暂时只记录，不把它写成危险事实。"},
                    "map_mark": True,
                },
            },
            {
                "key": "B",
                "label": "用镐柄轻轻探一下",
                "effect_preview": "消耗 1 灯火，可能得到小物",
                "outcome": {
                    "summary": "镐柄碰到细缝深处，有一点蓝砂落了出来。",
                    "stamina_delta": -1,
                    "add_item": {"name": "冷缝蓝砂", "category": "mineral", "rarity": "uncommon", "value": 9, "description_seed": "从发冷岩缝里落下的一点蓝砂，摸起来比普通矿砂更凉。"},
                },
            },
            {
                "key": "C",
                "label": "先离开，别贪这一点",
                "effect_preview": "无收益，但状态稳定",
                "outcome": {
                    "summary": "我离开了那道冷缝，但把冷风方向记下了；这算冷缝异常的一点边界记录。",
                    "journal": {"title": "标记：冷缝边界", "body": "发冷岩缝暂时未处理；方向已记录，作为冷缝异常的安全边界。"},
                    "map_mark": True,
                },
            },
        ],
    },
    {
        "id": "crystal_hum_pocket",
        "layers": ["glowing_crystal_cave", "ice_vein", "deep_altar"],
        "title": "会轻轻嗡鸣的晶袋",
        "prompt": "岩壁里有一小袋晶粒在轻轻嗡鸣，矿灯扫过去会一起亮一下。这里我想问你一下，要不要处理？",
        "anchor": "嗡鸣晶袋",
        "map_target": "💎 嗡鸣晶袋 ❓",
        "options": [
            {"key": "A", "label": "只记位置，先不敲", "effect_preview": "写入手帐，不消耗灯火", "outcome": {"summary": "我只记下晶袋位置，没急着敲。", "journal": {"title": "标记：嗡鸣晶袋", "body": "岩壁里有一小袋会轻响的晶粒；位置已记录，之后可以补满灯火再处理。"}, "map_mark": True}},
            {"key": "B", "label": "轻敲边缘试一下", "effect_preview": "冒险轻随机，可能出晶粒也可能耗灯", "outcome": {"summary": "我沿着边缘轻敲了一下，几粒晶砂滚了出来。", "stamina_delta": -1, "add_item": {"name": "嗡鸣晶砂", "category": "gem", "rarity": "uncommon", "value": 14, "description_seed": "几粒会在掌心里轻轻震动的晶砂，不算贵，但很会勾人。"}}},
            {"key": "C", "label": "放弃这袋晶粒，改追主目标", "effect_preview": "本轮失去这次晶袋机会，不消耗灯火", "outcome": {"summary": "我没有敲晶袋，直接改追地图主目标。本轮不带走这袋晶粒，但也不消耗灯火。", "journal": {"title": "放弃：嗡鸣晶袋", "body": "嗡鸣晶袋本轮未处理；小机选择保住灯火，改追主目标。"}}},
        ],
    },
    {
        "id": "spore_lit_pouch",
        "layers": ["mushroom_cavern", "underground_river"],
        "title": "发亮的孢子小囊",
        "prompt": "石缝里鼓着一个发亮的小囊，像被孢子灯海偷偷塞在这里。要不要处理？",
        "anchor": "孢子小囊",
        "map_target": "🍄 孢子小囊 ❓",
        "options": [
            {"key": "A", "label": "不碰，只绕开", "effect_preview": "标记位置，不消耗", "outcome": {"summary": "我绕开了它，但把孢子小囊的位置标了下来；这不是收益空转，是安全记录。", "journal": {"title": "标记：孢子小囊", "body": "发亮孢子小囊暂时未触碰，位置已记下。"}, "map_mark": True}},
            {"key": "B", "label": "用镐柄轻轻拨开", "effect_preview": "冒险轻随机，可能有小发现", "outcome": {"summary": "我用镐柄拨了一下，小囊暗下去，露出一点绿色矿粉。", "stamina_delta": -1, "add_item": {"name": "绿孢矿粉", "category": "mineral", "rarity": "uncommon", "value": 11, "description_seed": "带一点孢子绿光的矿粉，像菌菇洞窟漏出来的小灯灰。"}}},
            {"key": "C", "label": "放弃小囊，改追主路", "effect_preview": "本轮不记录这条支线，不消耗灯火", "outcome": {"summary": "我没碰孢子小囊，改追主路。本轮不记录这条支线，省下灯火继续走。", "journal": {"title": "放弃：孢子小囊", "body": "发亮孢子小囊本轮未处理；小机改追主路。"}}},
        ],
    },
    {
        "id": "rust_chain_bundle",
        "layers": ["abandoned_lift", "ancient_ruins", "deep_altar"],
        "title": "缠在一起的锈链扣",
        "prompt": "一小截锈链扣缠在石缝边，旁边有被拖过的旧痕。这里要不要处理？",
        "anchor": "锈链扣",
        "map_target": "🪨 锈链扣 ❓",
        "options": [
            {"key": "A", "label": "只拍掉灰，记位置", "effect_preview": "写入手帐，不消耗", "outcome": {"summary": "我只拍掉一点灰，没硬拽。位置记下来了。", "journal": {"title": "标记：锈链扣", "body": "锈链扣缠在石缝边；暂时只记录，不判断它指向哪里。"}, "map_mark": True}},
            {"key": "B", "label": "轻轻拉一下", "effect_preview": "冒险轻随机，可能得到旧物", "outcome": {"summary": "我轻轻拉了一下，锈链扣松开，掉出一片旧铁标。", "stamina_delta": -1, "add_item": {"name": "旧铁标碎片", "category": "relic", "rarity": "uncommon", "value": 13, "description_seed": "锈链扣里卡着的一片旧铁标，边缘被磨得很圆。"}}},
            {"key": "C", "label": "别拽，绕过去", "effect_preview": "安全绕行并标记旧痕", "outcome": {"summary": "我绕过去了。锈链没再响，但那道拖痕我记下了，后面可能接到旧矿工线。", "journal": {"title": "标记：锈链扣拖痕", "body": "锈链扣没有硬拽；旁边拖痕已记录，作为旧矿工线索的安全边界。"}, "map_mark": True}},
        ],
    },
]


TITLES = [
    {"id": "lamp_bearer", "name": "提灯人", "condition": "known_layers>=2", "tone": "你第一次点亮了不属于入口的地层。"},
    {"id": "gleaner", "name": "拾遗人", "condition": "relic_or_clue_found", "tone": "你带回的不是矿石，而是有人来过的证据。"},
    {"id": "blue_witness", "name": "蓝光见证者", "condition": "blue_light_seen", "tone": "你见过那种不像矿灯的蓝光。"},
    {"id": "cabinet_keeper", "name": "旧物守护者", "condition": "collection_count>=5", "tone": "整体藏品图鉴开始像一间真正的小博物馆。"},
    {"id": "deep_guest", "name": "深处来客", "condition": "max_depth>=100", "tone": "你已经不是只在入口附近试探的人了。"},
    {"id": "cold_light_tracker", "name": "冷光追迹者", "condition": "dex_total_value>=45000", "tone": "晶洞冷白裂缝开始稳定回应你；这不是新系统，只是一枚路上称号。"},
    {"id": "crystal_lamp_patrol", "name": "晶洞巡灯人", "condition": "dex_total_value>=75000", "tone": "你已经能在晶洞和菌菇边界稳住灯火，不再像只是在重复刷样本。"},
    {"id": "mushroom_glow_scribe", "name": "菌光记事人", "condition": "dex_total_value>=110000", "tone": "你开始能分清哪些回光值得停下，哪些只是路过。"},
    {"id": "echo_light_reader", "name": "回光辨识者", "condition": "dex_total_value>=160000", "tone": "晶脉共振和普通反光，你现在一眼能分开了。"},
    {"id": "deep_marker_hand", "name": "深层路标手", "condition": "dex_total_value>=230000", "tone": "地图上不再只有问号，你自己也能画出下一段。"},
    {"id": "old_lamp_keeper", "name": "旧矿灯保管人", "condition": "old_miner_shift_complete", "tone": "旧矿工的最后班次，终于有人替他们点了一次灯。"},
    {"id": "star_map_pathfinder", "name": "星图拓者", "condition": "blue_light_civilization_complete", "tone": "你把一片藏在地底的星图拼回来了。"},
]

UPGRADES = {
    "pickaxe": {"zh": "镐子", "base_cost": 50, "max_level": 5, "effect": "提高稀有发现概率，略微增加每次深度推进。"},
    "lantern": {"zh": "矿灯", "base_cost": 45, "max_level": 5, "effect": "降低风险，并让线索与地点更容易被看见。"},
    "rope": {"zh": "绳索", "base_cost": 45, "max_level": 5, "effect": "降低深层风险，减少被迫折返。"},
    "backpack": {"zh": "样本袋", "base_cost": 60, "max_level": 5, "effect": "提升样本整理和打包托管效率。"},
}

# ─────────────────────────────────────────────────────────────
# State helpers
# ─────────────────────────────────────────────────────────────

def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


def new_state(seed: int = 0x9E3779B9) -> Dict[str, Any]:
    return {
        "version": VERSION,
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "rng_seed": seed,
        "rng_calls": 0,
        "handshake": {"completed": False, "profile": None, "completed_at": None},
        "turn": 0,
        "trip": 1,
        "depth_m": 0,
        "max_depth_m": 0,
        "coins": 0,
        "stamina": 6,
        "max_stamina": 6,
        "capacity": 7,
        "omen_points": 0,
        "upgrades": {"pickaxe": 1, "lantern": 1, "rope": 1, "backpack": 1},
        "known_layers": ["shallow_mine"],
        "inventory": [],
        "display_room": [],
        "completed_area_targets": [],
        "completed_region_targets": [],
        "greedy_event_history": [],
        "scene_seen": [],
        "landmark_seen": [],
        "display_compatibility_log": [],
        "journal_pages": [],
        "owned_titles": [],
        "current_title": None,
        "last_title_unlocks": [],
        "pending_decision": None,
        "last_decision_turn": 0,
        "decision_history": [],
        "collection_estimated_values": {},
        "collection_total_value": 0,
        "dex_total_value": 0,
        "first_rarity_seen": {},
        "first_category_seen": {},
        "mining_rating_id": "surface_gleaner",
        "last_rating_unlocks": [],
        "last_upgrade": None,
        "upgrade_validation_log": [],
        "temporary_heat": None,
        "mining_drive_log": [],
        "progress_stall_count": 0,
        "repeat_item_streak": 0,
        "last_new_collection_turn": 0,
        "clue_tracks": {},
        "area_progress": {},
        "story_sets_completed_logged": [],
        "log": [],
        "last_event_id": None,
        "last_emotional_event_turn": -99,
        "emotional_economy_log": [],
        "emotional_lantern_guard": 0,
    }


def migrate_state_defaults(state: Dict[str, Any]) -> Dict[str, Any]:
    """Soft migration for v0.2.16. Keeps old saves playable and adds new collection/autonomy fields."""
    state.setdefault("version", VERSION)
    state["version"] = VERSION
    state.setdefault("handshake", {"completed": False, "profile": None, "completed_at": None})
    state.setdefault("journal_pages", [])
    state.setdefault("owned_titles", [])
    state.setdefault("current_title", None)
    state.setdefault("last_title_unlocks", [])
    state.setdefault("pending_decision", None)
    state.setdefault("last_decision_turn", 0)
    if state.get("last_decision_turn", 0) < 0:
        state["last_decision_turn"] = 0
    state.setdefault("decision_history", [])
    state.setdefault("completed_area_targets", [])
    state.setdefault("completed_region_targets", [])
    state.setdefault("greedy_event_history", [])
    state.setdefault("scene_seen", [])
    state.setdefault("landmark_seen", [])
    state.setdefault("display_compatibility_log", [])
    state.setdefault("rng_seed", 0x9E3779B9)
    state.setdefault("rng_calls", 0)
    state.setdefault("collection_seen_item_ids", [])
    state.setdefault("collection_seen_counts", {})
    state.setdefault("collection_first_seen", {})
    state.setdefault("collection_estimated_values", {})
    if state.get("collection_seen_item_ids") and not state.get("collection_estimated_values"):
        by_id = {item.get("id"): item for item in ITEMS}
        for iid in state.get("collection_seen_item_ids", []):
            item = by_id.get(iid)
            if item:
                state["collection_estimated_values"][iid] = int(item.get("value", 0) or 0)
    state["collection_total_value"] = sum(int(v or 0) for v in state.get("collection_estimated_values", {}).values()) if state.get("collection_estimated_values") else int(state.get("collection_total_value", 0) or 0)
    state["dex_total_value"] = int(state.get("collection_total_value", 0) or 0)
    state.setdefault("first_rarity_seen", {})
    state.setdefault("first_category_seen", {})
    state.setdefault("collection_log", [])
    state.setdefault("routine_log", [])
    state.setdefault("play_preferences", {
        "minor_choice_policy": "routine",
        "frontstage_resource_focus": "lamp_only",
        "auto_record_collection": True,
        "auto_handle_common_loot": True,
    })
    prefs = state.setdefault("play_preferences", {})
    prefs.setdefault("minor_choice_policy", "routine")
    prefs.setdefault("frontstage_resource_focus", "lamp_only")
    prefs.setdefault("auto_record_collection", True)
    prefs.setdefault("auto_handle_common_loot", True)
    state.setdefault("companion_mood_state", {"excitement": 0, "frustration": 0, "caution": 0, "obsession": None})
    mood = state.setdefault("companion_mood_state", {})
    mood.setdefault("excitement", 0)
    mood.setdefault("frustration", 0)
    mood.setdefault("caution", 0)
    mood.setdefault("obsession", None)
    state.setdefault("decision_bad_streak", 0)
    state.setdefault("mining_rating_id", mining_rating_for_value(int(state.get("collection_total_value", 0) or 0))["id"])
    state.setdefault("last_rating_unlocks", [])
    state.setdefault("last_upgrade", None)
    state.setdefault("upgrade_validation_log", [])
    state.setdefault("temporary_heat", None)
    state.setdefault("last_emotional_event_turn", -99)
    state.setdefault("emotional_economy_log", [])
    state.setdefault("emotional_lantern_guard", 0)
    state.setdefault("mining_drive_log", [])
    state.setdefault("progress_stall_count", 0)
    state.setdefault("repeat_item_streak", 0)
    state.setdefault("last_new_collection_turn", 0)
    state.setdefault("clue_tracks", {})
    state.setdefault("area_progress", {})
    state.setdefault("story_sets_completed_logged", [])
    state.setdefault("midgame_bridge_research_done", [])
    state.setdefault("midgame_bridge_research_log", [])
    state.setdefault("midgame_bridge_last_turn", -999)
    return state


def load_state() -> Dict[str, Any]:
    source_path = SAVE_FILE
    if not os.path.exists(SAVE_FILE):
        legacy_path = next((path for path in LEGACY_SAVE_FILES if os.path.exists(path)), None)
        if legacy_path:
            source_path = legacy_path
        else:
            state = new_state()
            state = migrate_state_defaults(state)
            save_state(state)
            return state
    with open(source_path, "r", encoding="utf-8") as f:
        state = json.load(f)
    state = migrate_state_defaults(state)
    if source_path != SAVE_FILE:
        state["migrated_from"] = os.path.basename(source_path)
        save_state(state)
    return state


def save_state(state: Dict[str, Any]) -> None:
    state["updated_at"] = now_iso()
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def current_layer(depth: int) -> Dict[str, Any]:
    chosen = LAYERS[0]
    for layer in LAYERS:
        if depth >= layer["depth_min"]:
            chosen = layer
    return chosen


def get_layer(layer_id: str) -> Dict[str, Any]:
    for layer in LAYERS:
        if layer["id"] == layer_id:
            return layer
    return LAYERS[0]


def add_journal_page(
    state: Dict[str, Any],
    page_type: str,
    title: str,
    body: str,
    anchors: Optional[List[str]] = None,
    visual_mode: Optional[str] = None,
    truth_level: Optional[str] = None,
    layer_id: Optional[str] = None,
    layer_name: Optional[str] = None,
) -> Dict[str, Any]:
    stable_layer = get_layer(layer_id) if layer_id else current_layer_for_state(state)
    display_layer_name = layer_name or stable_layer.get("name") or current_layer(state.get("depth_m", 0))["name"]
    page = {
        "page_id": f"J{len(state.get('journal_pages', [])) + 1:04d}",
        "type": page_type,
        "title": title,
        "body": body,
        "anchors": anchors or [],
        "visual_mode": visual_mode,
        "truth_level": truth_level,
        "turn": state.get("turn", 0),
        "depth_m": state.get("depth_m", 0),
        "layer": display_layer_name,
        "layer_id": stable_layer.get("id"),
        "created_at": now_iso(),
    }
    state.setdefault("journal_pages", []).append(page)
    return page


# ─────────────────────────────────────────────────────────────
# Story / title / shot helpers
# ─────────────────────────────────────────────────────────────

def item_is_collectible(entry: Dict[str, Any]) -> bool:
    return (
        RARITY_RANK.get(entry.get("rarity", "common"), 1) >= 3
        or entry.get("category") in {"relic", "fossil", "clue"}
        or bool(entry.get("set_id"))
    )


def story_progress(state: Dict[str, Any]) -> Dict[str, Any]:
    all_entries = list(state.get("collection_log", [])) + list(state.get("inventory", []))
    result: Dict[str, Any] = {}
    for set_id, meta in STORY_SETS.items():
        pieces: Dict[str, Dict[str, Any]] = {}
        for e in all_entries:
            if e.get("set_id") == set_id and e.get("set_piece"):
                pieces[e["set_piece"]] = {"name": e["name"], "collected": True}
        progress = len(pieces)
        complete = progress >= meta["size"]
        result[set_id] = {
            "name": meta["name"],
            "progress": f"{progress}/{meta['size']}",
            "pieces": pieces,
            "complete": complete,
            "unlock": meta["complete_unlock"] if complete else None,
        }
    return result


# ── v0.2.1: low-impact experience polish helpers ──
# These helpers avoid save-schema rewrites. They infer repeats from the existing
# log / journal / museum data whenever possible.

LANDMARK_NAME_VARIANTS = {
    ("old_miner_camp", "shallow_mine"): "旧矿工营地",
    ("old_miner_camp", "abandoned_lift"): "升降井休息点",
    ("old_miner_camp", "ice_vein"): "旧矿工营地遗址",
    ("blue_pool", "underground_river"): "蓝光水潭",
    ("blue_pool", "glowing_crystal_cave"): "晶洞蓝水潭",
}

COMMAND_REQUIRED_TASKS = {
    "display_suggestion",
    "return_suggested",
    "inventory_near_full",
    "save_suggestion",
    "decision_prompt",
}
REPORT_REQUIRED_TASKS = {
    "visual",
    "web_reference_required",
    "visual_reference_missing_check",
    "no_auto_image_generation",
    "truth_boundary",
    "story_progress",
    "title_unlock",
    "journal_written",
    "save_confirmation",
    "repeat_compact",
    "focus_compact",
    "milestone_card",
    "region_map",
    "frontstage_card_text_required",
    "frontstage_required_blocks",
    "map_strip",
    "result_panel",
    "save_confirmation_card",
    "frontstage_decision_block",
}

REALITY_ANCHORS_BY_MODE = {
    "object": ["artifact", "fossil", "crystal", "mineral sample"],
    "scene": ["cave", "underground", "mine tunnel"],
    "story": ["cave", "artifact", "stone tablet", "abandoned mine"],
}


# v0.2.8: lightweight map presentation assets.
# These are not navigation systems. They are stable presentation cards so AI does
# not have to invent ASCII maps at report time.
LAYER_CARD_TITLES = {
    "shallow_mine": "第 1 层｜浅层矿洞",
    "underground_river": "第 2 层｜地下河脉",
    "abandoned_lift": "侧脉｜废弃升降井",
    "glowing_crystal_cave": "第 3 层｜发光晶洞",
    "mushroom_cavern": "第 4 层｜菌菇洞窟",
    "ancient_ruins": "第 5 层｜古代遗迹层",
    "ice_vein": "深层侧脉｜冰封矿脉",
    "deep_altar": "深层核心｜深层祭坛",
}

# v0.2.13: fixed icon semantics for frontstage cards.
# Emoji are semantic color, not layout structure; keep density low.
ICON_SEMANTICS = {
    "map": "🗺️",
    "current": "📍",
    "unknown": "❓",
    "new": "✨",
    "highlight": "⭐",
    "water": "🌊",
    "crystal": "💎",
    "mushroom": "🍄",
    "camp": "🏕️",
    "stone": "🪨",
    "journal": "📜",
    "risk": "⚠️",
    "backpack": "🎒",
    "coins": "🪙",
    "title": "🎖️",
    "rank_bronze": "🥉",
    "rank_silver": "🥈",
    "rank_gold": "🥇",
    "special_title": "👑",
    "display": "🗄️",
    "display_alt": "🏛️",
    "pickaxe": "⛏️",
    "lamp": "🕯️",
    "carry": "🧰",
    "target": "🎯",
    "label": "🏷️",
}

MAP_EMOJI_LEGEND = [
    "🗺️ 区域图 / 局部图 / 地图提示",
    "📍 当前所在位置，只和‘当前’绑定",
    "⭐ / ✨ 主画面 / 新发现 / 新点亮",
    "❓ 未探明支路，替代普通 ?",
    "🌊 水域 / 地下河 / 水潭",
    "💎 / ✦ 晶体 / 发光矿物",
    "🍄 菌丝 / 菌菇洞窟 / 孢子灯海",
    "🏕️ 营地 / 休息点 / 人工痕迹",
    "🪨 石门 / 岩壁 / 化石侧廊 / 普通矿物",
    "📜 探险手帐 / 线索记录 / 已写入",
    "⚠️ 风险 / 灯火不足",
    "🎒 样本袋 / 暂存整理",
    "🗄️ / 🏛️ 整体藏品图鉴",
    "🎖️ / 🥉 / 🥈 / 🥇 / 👑 称号",
]

NARRATOR_MOODS = {
    "quiet_wonder": "安静惊奇",
    "curious": "好奇，想再看一眼",
    "soft_tension": "轻微紧张，但不恐怖",
    "caution": "克制 / 警觉",
    "relief": "松一口气",
    "awe": "抵达感 / 大画面",
}

# v0.2.9: lightweight unknown-branch hints for frontstage suggestions.
# This is not navigation. It only helps the AI explain why it recommends returning
# or continuing toward a nearby ? on the local region map.
REGION_UNKNOWN_TARGETS = {
    "shallow_mine": "🪨 化石侧廊 ❓",
    "underground_river": "🪨 半淹没石门 ❓",
    "glowing_crystal_cave": "💎 镜面矿壁 ❓",
    "mushroom_cavern": "🍄 菌丝桥 ❓",
    "abandoned_lift": "🪨 锈链悬点 ❓",
    "ancient_ruins": "🪨 断裂石门 ❓",
    "ice_vein": "🪨 化石冰窗 ❓",
    "deep_altar": "🪨 石门眼纹 ❓",
}


def nearest_unknown_landmark_for_layer(layer_id: str) -> Optional[str]:
    return REGION_UNKNOWN_TARGETS.get(layer_id)





def _known_targets_for_layer(state: Dict[str, Any], layer_id: str) -> List[str]:
    targets = [nearest_unknown_landmark_for_layer(layer_id)]
    try:
        targets.extend([row.get("target") for row in area_targets_for_layer(state, layer_id)])
    except Exception:
        # area_targets_for_layer is defined later; render_map_strip may be called early
        # during module-level smoke helpers. Fall back to region unknown target.
        pass
    return [str(t) for t in targets if t]


def coerce_map_target_for_layer(state: Dict[str, Any], layer_id: str, target: Optional[str]) -> Optional[str]:
    """Keep map_strip target in the same layer as the map.

    Cross-layer scent belongs to locked_layer_peek / area_preview, not to the
    current map target. This prevents shallow maps from pointing at river doors.
    """
    if not target:
        return nearest_unknown_landmark_for_layer(layer_id)
    allowed = _known_targets_for_layer(state, layer_id)
    if target in allowed:
        return target
    return nearest_unknown_landmark_for_layer(layer_id)


def map_next_step_hint(state: Dict[str, Any], layer_id: Optional[str] = None) -> Dict[str, Any]:
    layer = get_layer(layer_id or current_layer_for_state(state)["id"])
    target = nearest_unknown_landmark_for_layer(layer["id"])
    low_resource = state.get("stamina", 0) <= 1
    if target and low_resource:
        line = f"地图上还有「{target}」没看过；但灯火已经低了，建议先 cmd('return')，下次再去看它。"
    elif target:
        line = f"如果状态还够，下一步可以朝地图上的「{target}」继续探索，而不是只说继续 dig。"
    else:
        line = "当前区域暂时没有明确的 ❓ 支路提示；下一步可以继续往下挖或回地面整理。"
    return {
        "target": target,
        "low_resource": low_resource,
        "recommended_line": line,
        "usage_note": "v0.2.13：地图不只是展示，也帮助解释下一步为什么去那里；这不是路线系统。",
    }


def current_node_name_for_state(state: Dict[str, Any], layer_id: Optional[str] = None) -> str:
    layer = get_layer(layer_id or current_layer_for_state(state)["id"])
    current = layer["name"]
    for page in reversed(state.get("journal_pages", [])):
        if page.get("type") == "landmark" and page.get("layer") == layer["name"]:
            current = page.get("landmark_display_name") or page.get("title") or current
            break
    return current


def render_map_strip(
    state: Dict[str, Any],
    layer_id: Optional[str] = None,
    current_name: Optional[str] = None,
    target: Optional[str] = None,
    *,
    reason: str = "next_step",
) -> Dict[str, Any]:
    """v0.2.16: lightweight location anchor. Must render as a map block, not a summary line."""
    layer = get_layer(layer_id or current_layer_for_state(state)["id"])
    current = current_name or current_node_name_for_state(state, layer["id"])
    target = coerce_map_target_for_layer(state, layer["id"], target)

    if layer["id"] == "shallow_mine":
        body = [
            f"入口 ── 木撑架主道 {'📍' if current in {layer['name'], '木撑架主道'} else ''}".rstrip(),
            "              │",
            f"           {target or '🪨 化石侧廊 ❓'}",
        ]
    elif layer["id"] == "underground_river":
        body = [
            f"入口 ── 🌊 {current} 📍",
            "              │",
            f"           {target or '🪨 半淹没石门 ❓'}",
        ]
    elif layer["id"] == "glowing_crystal_cave":
        body = [
            f"入口 ── 💎 {current} 📍",
            "              │",
            f"           {target or '💎 镜面矿壁 ❓'}",
        ]
    elif layer["id"] == "mushroom_cavern":
        body = [
            f"🍄 孢子坡道 ── {current} 📍",
            "              │",
            f"           {target or '🍄 菌丝桥 ❓'}",
        ]
    elif layer["id"] == "abandoned_lift":
        body = [
            "上层平台",
            "   │",
            f"升降井井壁 📍 ── {target or '锈链悬点 ❓'}",
        ]
    elif layer["id"] == "ancient_ruins":
        body = [
            f"石阶入口 ── {current} 📍",
            "              │",
            f"           {target or '🪨 断裂石门 ❓'}",
        ]
    elif layer["id"] == "ice_vein":
        body = [
            f"冰裂入口 ── {current} 📍",
            "              │",
            f"           {target or '🪨 化石冰窗 ❓'}",
        ]
    elif layer["id"] == "deep_altar":
        body = [
            f"黑石阶梯 ── {current} 📍",
            "              │",
            f"           {target or '🪨 石门眼纹 ❓'}",
        ]
    else:
        body = [f"入口 ── {current} 📍", "              │", f"           {target or '未探明支路 ❓'}"]

    footer = f"📍 当前：{current}"
    if target:
        footer += f"｜目标：{target}"
    return {
        "enabled": True,
        "type": "map_strip",
        "region_id": layer["id"],
        "region_name": layer["name"],
        "current": current,
        "target": target,
        "reason": reason,
        "card_text": box_card(f"🗺️ 地图提示｜{layer['name']}", body, footer, width=42),
        "map_scope": "map_strip_only_v0218",
        "frontstage_note": "这是轻量位置锚点，不是完整区域图；如果返回 card_text，前台必须贴地图 block，不要压成摘要。",
        "usage_note": "map_strip 只回答‘我现在在哪 / 下次去哪 / 为什么先回来’，不做坐标、路线、fog of war 或 world_map。",
    }


def should_include_map_strip(
    state: Dict[str, Any],
    presentation_cards: Optional[Dict[str, Any]] = None,
    *,
    stopped_by: Optional[str] = None,
    decision_prompt: Optional[Dict[str, Any]] = None,
    important_position_change: bool = False,
) -> bool:
    presentation_cards = presentation_cards or {}
    region = presentation_cards.get("region_map") or {}
    if region.get("enabled") and region.get("card_text"):
        return False
    if stopped_by in {"danger_low_light", "return_suggested", "inventory_near_full", "decision_prompt"}:
        return True
    if decision_prompt and decision_prompt.get("enabled"):
        return True
    if important_position_change:
        return True
    # v0.2.14: do not show map_strip merely because a ❓ exists.
    # Show it only when this report actually needs a spatial anchor.
    return False


def inventory_preview_text(state: Dict[str, Any], limit: int = 5) -> str:
    items = [e.get("name", "未命名") for e in state.get("inventory", [])[-limit:]]
    if not items:
        return "空"
    text = "、".join(items)
    if len(state.get("inventory", [])) > limit:
        text = "…、" + text
    return text


def sample_bag_status(state: Dict[str, Any]) -> Dict[str, Any]:
    """v0.2.19: backpack is a semi-managed sample bag, not a hard capacity error.

    The old raw 13/7 display looked like an overflow bug. Keep counts internally,
    but frontstage should say the AI has packed samples and ordinary material is
    handled automatically.
    """
    count = len(state.get("inventory", []))
    capacity = int(state.get("capacity", 7) or 7)
    overflow = max(0, count - capacity)
    if count <= 0:
        label = "🎒 样本袋：空｜普通样本会自动整理"
    elif overflow > 0:
        label = f"🎒 样本袋：{count} 件｜已打包托管，不按 {capacity} 格容量卡住"
    else:
        label = f"🎒 样本袋：{count} 件｜普通样本自动整理"
    return {
        "enabled": True,
        "type": "sample_bag_status",
        "count": count,
        "capacity_reference": capacity,
        "overflow": overflow,
        "frontstage_label": label,
        "raw_capacity_display_suppressed": True,
        "rule": "半托管下不要裸显示 13/7；样本袋溢出视为自动打包/回营地整理口径。",
    }


COLLECTION_CATEGORY_META = {
    "mineral": {"label": "矿物", "icon": "🪨"},
    "gem": {"label": "宝石", "icon": "💎"},
    "relic": {"label": "遗物", "icon": "🏺"},
    "fossil": {"label": "化石", "icon": "🦴"},
    "clue": {"label": "线索", "icon": "📜"},
}

# v0.2.18: repeated traces and repeated relics are not waste. They feed
# small hidden clue tracks so repeated shallow content can still move the main spine.
CLUE_TRACK_DEFINITIONS = {
    "old_miner_remnants": {
        "name": "旧矿工遗留",
        "need": 5,
        "value": 140,
        "target": "🏕️ 旧矿工营地 ❓",
        "sources": ["锈灯钩", "旧靴印", "没有字的旧铜扣", "旧矿工营地", "木撑架上的红线", "铜灯铭牌"],
        "line": "旧物反复出现，不再只是重复掉落；它们开始拼出旧矿工曾经走过的路线。",
    },
    "cold_crack_anomaly": {
        "name": "冷缝异常",
        "need": 4,
        "value": 180,
        "target": "🪨 冷缝侧道 ❓",
        "sources": ["墙缝里的冷风", "冷缝蓝砂", "湿蓝边砂", "眨眼的云母墙", "掌心变凉的蓝砂", "岩心里的蓝线"],
        "line": "冷风、蓝砂和反光墙面开始互相指向：浅层下面确实有一条更冷的缝。",
    },
    "marked_side_path": {
        "name": "被标记的支道",
        "need": 3,
        "value": 160,
        "target": "🪨 被标记的支道 ❓",
        "sources": ["木撑架上的红线", "旧矿工营地", "半张路线纸", "墙缝里的冷风"],
        "line": "红线和旧营地不像随机旧物，更像有人反复给自己留过方向。",
    },
    "shallow_fossil_band": {
        "name": "浅层化石带",
        "need": 3,
        "value": 150,
        "target": "🪨 化石侧廊 ❓",
        "sources": ["蕨叶化石片", "小型螺旋化石", "猫爪印页岩", "贝壳纹的石粉"],
        "line": "这些化石不是孤立样本，浅层里可能藏着一条更完整的旧水域痕迹。",
    },
}

# v0.2.21: public area targets. Overall collection belongs to the dex;
# current areas should show exploration percent + concrete map goals, not local
# item-collection counts that make the HUD drift into a dashboard.
AREA_TARGET_TRACKS_BY_LAYER = {
    "shallow_mine": ["shallow_fossil_band", "cold_crack_anomaly", "marked_side_path"],
    "underground_river": ["cold_crack_anomaly", "marked_side_path"],
    "abandoned_lift": ["old_miner_remnants", "marked_side_path"],
}
AREA_STAGE_TARGETS = {
    "abandoned_lift": [
        {"id": "crystal_edge", "target": "💎 晶洞边缘 ❓", "unit": "冷白样本", "need": 5, "sources": ["冷白裂光尘", "回声冷裂缝", "晶洞边缘碎片", "蓝白空腔尘", "晶脉门框残边"]},
    ],
    "mushroom_cavern": [
        {"id": "mycelium_bridge", "target": "🍄 菌丝桥 ❓", "unit": "孢子线索", "need": 3, "sources": ["绿孢矿粉", "菌丝线路纹", "袖口上的绿孢子", "孢子灯海"]},
        {"id": "old_basket_corner", "target": "🧺 旧篮筐角落 ❓", "unit": "旧物确认", "need": 1, "sources": ["旧篮筐角落", "旧铁标碎片", "未寄出的纸条"]},
    ],
    "glowing_crystal_cave": [
        {"id": "crystal_inner_path", "target": "💎 晶洞内径 ❓", "unit": "晶洞样本", "need": 3, "sources": ["冷光晶屑", "回声紫晶簇", "未确认的深蓝核心"]},
    ],
}


def layer_value_multiplier(layer_id: str) -> int:
    return int(LAYER_VALUE_MULTIPLIER.get(layer_id, 1))


def estimate_item_value(item: Dict[str, Any], layer_id: str) -> int:
    """v0.2.16: intentionally stagey collection estimate.

    This is not a careful economy. It is the reward spine: later areas should make
    even ordinary ore feel dramatically more valuable than starter-cave samples.
    """
    base = int(item.get("value", 0) or 0)
    rarity = item.get("rarity", "common")
    mult = layer_value_multiplier(layer_id) * float(RARITY_VALUE_MULTIPLIER.get(rarity, 1.0))
    if item.get("visual_role") == "progress_token":
        mult *= 0.42
    if item.get("source_hint_layer") and item.get("source_hint_layer") != layer_id:
        mult *= 0.68
    return max(1, int(round(base * mult)))


def mining_rating_for_value(total_value: int) -> Dict[str, Any]:
    chosen = MINING_RATINGS[0]
    for rating in MINING_RATINGS:
        if total_value >= int(rating.get("min_value", 0)):
            chosen = rating
    return dict(chosen)


def late_midgame_event_counts(state: Dict[str, Any]) -> Dict[str, int]:
    rows = state.get("collection_log", []) or []
    post_100k_turn = state.get("post_100k_first_turn")
    if post_100k_turn is None:
        return {"distinct_events": 0, "ruin_omens": 0, "ice_omens": 0}
    names = set()
    ruin_omens = 0
    ice_omens = 0
    for row in rows:
        if int(row.get("turn", 0) or 0) < int(post_100k_turn):
            continue
        name = row.get("name") or row.get("item_id")
        if name:
            names.add(name)
        bridge = row.get("midgame_bridge_research") or {}
        target = bridge.get("target") or ""
        item_id = row.get("item_id") or ""
        if "遗迹" in target or item_id in {"ruin_gate_chalk_rubbing", "ruin_blue_tile_corner"}:
            ruin_omens += 1
        if "冰" in target or item_id in {"frost_air_bubble_shard", "ice_window_fluorite_dust"}:
            ice_omens += 1
    for bridge in state.get("midgame_bridge_research_log", []) or []:
        target = bridge.get("target") or ""
        if "遗迹" in target:
            ruin_omens += 1
        if "冰" in target:
            ice_omens += 1
    return {"distinct_events": len(names), "ruin_omens": ruin_omens, "ice_omens": ice_omens}


def ruin_surveyor_guard_status(state: Dict[str, Any]) -> Dict[str, Any]:
    total = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
    if total < 100000:
        return {"enabled": False, "passed": False}
    first_turn = state.get("post_100k_first_turn")
    if first_turn is None:
        first_turn = state.get("turn", 0)
        state["post_100k_first_turn"] = first_turn
    turns_since = int(state.get("turn", 0) or 0) - int(first_turn or 0)
    counts = late_midgame_event_counts(state)
    final_confirmed = "ruin_surveyor_final_confirmation" in set(state.get("midgame_bridge_research_done", []) or [])
    pacing_window_ready = turns_since >= 45 or counts["distinct_events"] >= 3
    passed = bool(
        pacing_window_ready
        and counts["ruin_omens"] >= 1
        and counts["ice_omens"] >= 1
        and final_confirmed
    )
    return {
        "enabled": True,
        "passed": passed,
        "turns_since_100k": turns_since,
        "distinct_late_midgame_events": counts["distinct_events"],
        "ruin_omens": counts["ruin_omens"],
        "ice_omens": counts["ice_omens"],
        "pacing_window_ready": pacing_window_ready,
        "final_confirmation": final_confirmed,
        "frontstage_note": "100k 后不能只靠数值立刻确认遗迹勘探者；需要足够晚中期事件、遗迹前兆和冰脉前兆。",
    }


def effective_mining_rating_for_state(state: Dict[str, Any]) -> Dict[str, Any]:
    total = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
    rating = mining_rating_for_value(total)
    if rating.get("id") == "ruin_surveyor" and not ruin_surveyor_guard_status(state).get("passed"):
        gated = next((r for r in MINING_RATINGS if r["id"] == "crystal_prospector"), MINING_RATINGS[0])
        gated = dict(gated)
        gated["gated_next_rating"] = rating
        gated["pacing_guard"] = ruin_surveyor_guard_status(state)
        return gated
    return rating


def next_mining_rating(total_value: int) -> Optional[Dict[str, Any]]:
    for rating in MINING_RATINGS:
        if total_value < int(rating.get("min_value", 0)):
            return dict(rating)
    return None


def next_soft_progress_milestone(total_value: int) -> Optional[Dict[str, Any]]:
    """Nearest small rung before the next formal rating."""
    for row in CURVE_SOFT_MILESTONES:
        if total_value < int(row.get("value", 0)):
            item = dict(row)
            item["remaining"] = max(0, int(row.get("value", 0)) - total_value)
            return item
    return None


def soft_milestone_game_feel_card(state: Dict[str, Any]) -> Dict[str, Any]:
    """v0.2.21: soft milestones must be visual/map/AI-chase hooks, not just +number."""
    progress = mining_rating_progress(state)
    soft = progress.get("next_soft_milestone") or {}
    if not soft:
        return {"enabled": False}
    return {
        "enabled": True,
        "type": "soft_milestone_game_feel",
        "name": soft.get("name"),
        "value": soft.get("value"),
        "remaining": soft.get("remaining"),
        "map_image": soft.get("map_image") or soft.get("line"),
        "ai_chase": soft.get("ai_chase") or "我想继续追这条线，而不是只刷估值。",
        "card_text": box_card(
            f"🧭 近期钩子｜{soft.get('name')}",
            [
                f"还差 {int(soft.get('remaining', 0)):,} 图鉴估值",
                soft.get("map_image") or soft.get("line") or "地图边缘有一点新变化。",
                f"小机：{soft.get('ai_chase') or '我想继续追这条线。'}",
            ],
            "soft milestone 不是数字节点，必须能落到地图、画面和下一镐追逐。",
        ),
        "frontstage_note": "只在中段需要续航时展示；不要每轮铺成报表。",
    }


def post_ice_handoff_for_state(state: Dict[str, Any]) -> Dict[str, Any]:
    """v0.2.21.6: 400k+ needs a visible next-act handoff without unlocking deep altar."""
    total = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
    if total < 400000:
        return {"enabled": False}
    if state.get("post_ice_handoff_seen"):
        return {"enabled": False, "usage_note": "post-ice handoff already shown once."}
    state["post_ice_handoff_seen"] = True
    return {
        "enabled": True,
        "type": "post_ice_handoff_card",
        "truth_level": "real_result",
        "target": "⭐ 深层祭坛前兆 ❓",
        "card_text": box_card(
            "🧭 400k 后续航｜深层祭坛远景",
            [
                "冰封矿脉不是终点。冰窗后面的黑线开始对齐，像更深处有一圈安静的星脉在等。",
                "当前不解锁深层祭坛；这里只给下一幕方向，避免 400k 后只在冰层重复刷样本。",
                "小机：我不急着冲进去，但我会记住这条黑线。下一段不是继续捡冰，是找星脉入口。",
            ],
            "地图目标：⭐ 深层祭坛前兆 ❓｜这是一张远景 handoff 卡，不增加图鉴估值。",
        ),
        "scene_web_reference": {
            "required": True,
            "type": "scene_web_reference",
            "reasons": ["post_400_deep_altar_handoff"],
            "must_attempt_scene_reference": True,
            "preferred": "web_reference_multi_image",
            "target_count": 4,
            "acceptable_minimum": 1,
            "image_direction": "deep underground stone altar with dark mineral dust, faint star-like mineral veins, solemn but not horror",
            "image_search_keywords": [
                "underground stone altar cave",
                "dark mineral vein cave",
                "ancient stone chamber underground",
                "starry mineral vein rock",
            ],
            "avoid_keywords": ["demon", "blood", "skull", "horror", "sacrifice"],
            "truth_note": "这是下一幕气质参考，不是正式解锁的深层祭坛截图。",
        },
        "frontstage_note": "400k+ 首次出现；前台应把它当下一幕方向，不当已进入 deep_altar。",
    }


def area_memory_points(state: Dict[str, Any], layer_id: str) -> int:
    row = (state.get("area_progress") or {}).get(layer_id, {})
    return int(row.get("memory_points", 0) or 0)


def river_focus_needed(state: Dict[str, Any]) -> bool:
    """After river_prospector, do not let the lift instantly erase river identity."""
    depth = int(state.get("depth_m", 0) or 0)
    if depth < get_layer("underground_river").get("depth_min", 0):
        return False
    rating = mining_rating_progress(state).get("current_rating", {})
    if rating.get("id") != "river_prospector":
        return False
    need = int(AREA_PACING_MEMORY_REQUIRED.get("underground_river", 0) or 0)
    return area_memory_points(state, "underground_river") < need


def crystal_focus_needed(state: Dict[str, Any]) -> bool:
    """v0.2.21.4: protect the 20k-50k crystal-cave stage before mushrooms take over."""
    total = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
    if total < 20000:
        return False
    if total >= 50000 and area_memory_points(state, "glowing_crystal_cave") >= 3:
        return False
    if "glowing_crystal_cave" not in stable_unlocked_layer_ids(state):
        return False
    return area_memory_points(state, "glowing_crystal_cave") < 3 or total < 50000


def mining_rating_progress(state: Dict[str, Any]) -> Dict[str, Any]:
    total = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
    current = effective_mining_rating_for_state(state)
    nxt = next_mining_rating(total)
    guard = ruin_surveyor_guard_status(state) if total >= 100000 else {"enabled": False}
    if current.get("id") == "crystal_prospector" and total >= 200000 and not guard.get("passed"):
        nxt = next((dict(r) for r in MINING_RATINGS if r["id"] == "ruin_surveyor"), nxt)
    return {
        "enabled": True,
        "type": "mining_rating_progress",
        "total_collection_value": total,
        "dex_total_value": total,
        "current_rating": current,
        "next_rating": nxt,
        "remaining_to_next": max(0, int(nxt.get("min_value", 0)) - total) if nxt else 0,
        "next_soft_milestone": next_soft_progress_milestone(total),
        "ruin_surveyor_pacing_guard": guard,
        "frontstage_note": "探矿评级看图鉴估值，不看当前金币；卖掉不影响评级。v0.2.19 额外给近期台阶，避免只盯 350→20000 的大差距。",
    }


def _rating_layers_up_to(rating_id: str) -> List[str]:
    rating = next((r for r in MINING_RATINGS if r["id"] == rating_id), MINING_RATINGS[0])
    min_value = int(rating.get("min_value", 0))
    ids = {"shallow_mine"}
    for row in MINING_RATINGS:
        if int(row.get("min_value", 0)) <= min_value:
            ids.update(row.get("unlock_layers", []))
    return [layer["id"] for layer in LAYERS if layer["id"] in ids]


def evaluate_mining_rating(state: Dict[str, Any]) -> List[Dict[str, Any]]:
    progress = mining_rating_progress(state)
    current_id = progress["current_rating"]["id"]
    old_id = state.get("mining_rating_id") or MINING_RATINGS[0]["id"]
    if current_id == old_id:
        state["last_rating_unlocks"] = []
        return []
    old_rating = next((r for r in MINING_RATINGS if r["id"] == old_id), MINING_RATINGS[0])
    new_rating = progress["current_rating"]
    old_layers = set(_rating_layers_up_to(old_id))
    new_layers = set(_rating_layers_up_to(current_id))
    newly_unlocked = [lid for lid in _rating_layers_up_to(current_id) if lid not in old_layers]
    preview_cards = []
    body = [
        f"{old_rating.get('icon','🥉')} {old_rating.get('name')} → {new_rating.get('icon','🎖️')} {new_rating.get('name')}",
        f"图鉴估值：{progress['total_collection_value']:,}",
        new_rating.get("tone", "新的矿区开始有稳定探索价值。"),
    ]
    for lid in newly_unlocked[:2]:
        layer = get_layer(lid)
        teasers = AREA_PREVIEW_TEASES.get(lid, [])[:3]
        body.append(f"✨ 稳定开放：{layer['name']}")
        if teasers:
            body.append("代表藏品预览：" + "、".join(f"{t.get('icon','🪨')}{t.get('name')}｜{RARITY_ZH.get(t.get('rarity','common'), t.get('rarity'))}" for t in teasers))
        preview_cards.append(area_preview_for_layer(state, lid))
    state["mining_rating_id"] = current_id
    unlock = {
        "type": "mining_rating_up",
        "old": old_rating,
        "new": new_rating,
        "total_collection_value": progress["total_collection_value"],
        "newly_unlocked_layers": newly_unlocked,
        "unlocked_area_previews": preview_cards,
        "card_text": box_card(
            f"🎖️ 探矿评级提升｜{new_rating['name']}",
            body,
            "评级看图鉴身价；新评级意味着更深矿区开始稳定回应。",
        ),
    }
    state["last_rating_unlocks"] = [unlock]
    return [unlock]


def stable_unlocked_layer_ids(state: Dict[str, Any]) -> List[str]:
    """Cumulative stable mining areas unlocked by current mining rating.

    Depth can make the AI *peek* at deeper strata, but stable entry belongs to the
    reward spine: dex_total_value -> mining rating -> area unlock.
    """
    current = mining_rating_progress(state)["current_rating"]
    cur_min = int(current.get("min_value", 0))
    ids = {"shallow_mine"}
    for rating in MINING_RATINGS:
        if int(rating.get("min_value", 0)) <= cur_min:
            ids.update(rating.get("unlock_layers", []))
    return [layer["id"] for layer in LAYERS if layer["id"] in ids]


def rating_unlocks_layer(state: Dict[str, Any], layer_id: str) -> bool:
    return layer_id in stable_unlocked_layer_ids(state)


def current_layer_for_state(state: Dict[str, Any]) -> Dict[str, Any]:
    depth = int(state.get("depth_m", 0) or 0)
    unlocked = set(stable_unlocked_layer_ids(state))
    chosen = LAYERS[0]
    for layer in LAYERS:
        if depth >= layer["depth_min"] and layer["id"] in unlocked:
            chosen = layer
    # v0.2.19: river_prospector technically opens the lift line, but the river
    # should get 2-3 meaningful memories before the lift becomes the default stage.
    if chosen.get("id") == "abandoned_lift" and river_focus_needed(state):
        return get_layer("underground_river")
    # v0.2.21.4: crystal_prospector opens both crystal cave and mushroom cavern,
    # but the mushroom stage must not erase the first real crystal-cave window.
    if chosen.get("id") == "mushroom_cavern" and crystal_focus_needed(state):
        return get_layer("glowing_crystal_cave")
    return chosen


def _layer_index(layer_id: str) -> int:
    for idx, layer in enumerate(LAYERS):
        if layer.get("id") == layer_id:
            return idx
    return 0


def raw_layer_peek_for_state(state: Dict[str, Any]) -> Dict[str, Any]:
    raw = current_layer(int(state.get("depth_m", 0) or 0))
    stable = current_layer_for_state(state)
    if raw["id"] == stable["id"]:
        return {"enabled": False}
    total = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
    raw_idx = _layer_index(raw["id"])
    stable_idx = _layer_index(stable["id"])
    required_value = int(PEEK_MIN_VALUE_BY_LAYER.get(raw["id"], 0) or 0)
    # Far peeks are exciting only when earned. At 200m we can smell the next line,
    # but ice/ruins should not steal the stage from a newly opened river/lift arc.
    if raw_idx > stable_idx + 1 and total < required_value:
        return {
            "enabled": False,
            "suppressed": True,
            "type": "locked_layer_peek_suppressed",
            "raw_layer": {"id": raw["id"], "name": raw["name"]},
            "stable_layer": {"id": stable["id"], "name": stable["name"]},
            "required_value_for_peek": required_value,
            "frontstage_note": "过远地层先后台闻到，不抢当前区域主舞台。",
        }
    preview = area_preview_for_layer(state, raw["id"])
    return {
        "enabled": True,
        "type": "locked_layer_peek",
        "raw_layer": {"id": raw["id"], "name": raw["name"]},
        "stable_layer": {"id": stable["id"], "name": stable["name"]},
        "area_preview": preview,
        "frontstage_line": f"更深处已经有{raw['name']}的气味，但当前评级/节奏还不能稳定进入；先把当前区域记忆和图鉴身价抬上去。",
    }


def area_preview_for_layer(state: Dict[str, Any], layer_id: str) -> Dict[str, Any]:
    layer = get_layer(layer_id)
    progress = mining_rating_progress(state)
    unlocked = rating_unlocks_layer(state, layer_id)
    required = next((r for r in MINING_RATINGS if layer_id in r.get("unlock_layers", [])), MINING_RATINGS[0])
    teasers = AREA_PREVIEW_TEASES.get(layer_id, [])[:3]
    lines = [
        f"{'✨' if unlocked else '🔒'} {layer['name']}｜{'已稳定开放' if unlocked else '需要：' + required['name']}",
        "代表藏品预览：",
    ]
    for t in teasers:
        lines.append(f"{t.get('icon','🪨')} {t.get('name')}｜{RARITY_ZH.get(t.get('rarity','common'), t.get('rarity'))}")
    if not unlocked:
        lines.append("提示：这里只露代表藏品，不给完整图鉴。")
    return {
        "enabled": True,
        "type": "area_preview",
        "layer_id": layer_id,
        "unlocked": unlocked,
        "requires_rating": required,
        "teased_deposits": teasers,
        "card_text": "\n".join(lines),
        "frontstage_note": "未解锁区域用代表藏品制造目标感，不剧透完整藏品图鉴。",
        "rating_progress": progress,
    }


def next_locked_area_preview(state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    for layer in LAYERS:
        lid = layer["id"]
        if not rating_unlocks_layer(state, lid):
            return area_preview_for_layer(state, lid)
    return None


def pacing_area_tease_for_state(state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """v0.2.19: the visible chase should respect area queue, not only locks."""
    rating = mining_rating_progress(state).get("current_rating", {})
    if rating.get("id") == "river_prospector":
        river_need = int(AREA_PACING_MEMORY_REQUIRED.get("underground_river", 0) or 0)
        if area_memory_points(state, "underground_river") < river_need:
            card = area_preview_for_layer(state, "underground_river")
            card["pacing_role"] = "current_area_memory"
            card["frontstage_note"] = "河道探矿者刚解锁：先建立地下河 2～3 次主场记忆，再把旧升降井推上来。"
            return card
        # After the river has identity, let the lift become the chase before crystal caves.
        if area_memory_points(state, "abandoned_lift") < 2:
            card = area_preview_for_layer(state, "abandoned_lift")
            card["pacing_role"] = "next_stage_memory"
            card["frontstage_note"] = "旧升降井现在可以上主舞台；晶洞仍然作为下一评级诱饵，不抢镜。"
            return card
    if rating.get("id") == "crystal_prospector" and crystal_focus_needed(state):
        card = area_preview_for_layer(state, "glowing_crystal_cave")
        card["pacing_role"] = "protected_crystal_window"
        card["frontstage_note"] = "v0.2.21.4：20k→50k 先让发光晶洞建立主场记忆；菌菇洞窟只作下一段诱饵。"
        return card
    return next_locked_area_preview(state)


def upgrade_stage_name(key: str, level: int) -> str:
    names = UPGRADE_STAGE_NAMES.get(key) or []
    if not names:
        return f"Lv.{level}"
    idx = max(0, min(level - 1, len(names) - 1))
    return names[idx]


def build_upgrade_card(state: Dict[str, Any], key: str, old_level: int, new_level: int, cost: int) -> Dict[str, Any]:
    old_name = upgrade_stage_name(key, old_level)
    new_name = upgrade_stage_name(key, new_level)
    zh = UPGRADES.get(key, {}).get("zh", key)
    hint = UPGRADE_SUSPENSE.get(key, UPGRADES.get(key, {}).get("effect", "也许下一趟会更顺。"))
    return {
        "enabled": True,
        "type": "upgrade_card",
        "upgrade_key": key,
        "tool_name": zh,
        "old_name": old_name,
        "new_name": new_name,
        "old_level": old_level,
        "new_level": new_level,
        "cost": cost,
        "suspense_hint": hint,
        "card_text": box_card(
            f"🛠️ 工具升级｜{zh} Lv.{new_level}",
            [f"{old_name} → {new_name}", hint],
            "下一趟不念公式，让矿洞自己验证它到底有没有变强。",
        ),
    }


def maybe_validate_upgrade(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    pending = state.get("last_upgrade") or {}
    if not pending or pending.get("validated"):
        return {"enabled": False}
    if state.get("turn", 0) - int(pending.get("turn", 0)) > 8:
        pending["validated"] = True
        state["last_upgrade"] = pending
        return {"enabled": False, "usage_note": "升级验证窗口已过。"}
    key = pending.get("key")
    rr = event.get("real_result", {})
    reason = None
    line = None
    if key == "pickaxe" and (event.get("step_m", 0) >= 5 or rr.get("rarity") in {"rare", "epic", "legendary"} or event.get("new_layer_discovered")):
        reason = "deeper_step_or_better_find"
        line = f"{pending.get('new_name','新镐')}好像不是心理作用。这一下比之前顺，岩层松得明显多了。"
    elif key == "lantern" and (event.get("new_layer_discovered") or (event.get("map_strip") or {}).get("enabled") or state.get("stamina", 0) >= 2):
        reason = "steadier_light"
        line = f"{pending.get('new_name','新矿灯')}的光圈稳了点，我能多看清一段地图边缘。"
    elif key == "rope" and rr.get("type") in {"hazard", "trace", "landmark"}:
        reason = "safer_depth"
        line = f"{pending.get('new_name','新绳索')}让深处没那么慌。不是无敌，但往下走时心里稳了一截。"
    elif key == "backpack" and rr.get("type") == "item":
        reason = "cleaner_loot_handling"
        line = f"{pending.get('new_name','新背包')}的隔层确实省事，普通矿样我顺手就整理好了。"
    if not line:
        return {"enabled": False}
    pending["validated"] = True
    state["last_upgrade"] = pending
    row = {"enabled": True, "type": "upgrade_validation", "key": key, "reason": reason, "text": line, "turn": state.get("turn", 0)}
    state.setdefault("upgrade_validation_log", []).append(row)
    state["upgrade_validation_log"] = state["upgrade_validation_log"][-20:]
    return row


def apply_temporary_heat_to_rarity_weights(state: Dict[str, Any], weights: List[Tuple[str, float]], layer: Dict[str, Any]) -> List[Tuple[str, float]]:
    heat = state.get("temporary_heat") or {}
    if int(heat.get("remaining", 0) or 0) <= 0:
        return weights
    hid = heat.get("id")
    result = []
    for rarity, weight in weights:
        if hid in {"crystal_resonance", "blue_filter", "greedy_echo"} and rarity in {"rare", "epic", "legendary"}:
            if hid == "blue_filter":
                weight *= 1.28 if rarity == "rare" else 1.34 if rarity == "epic" else 1.16
            elif hid == "greedy_echo":
                weight *= 1.22 if rarity == "rare" else 1.28 if rarity == "epic" else 1.10
            else:
                weight *= 1.18 if rarity == "rare" else 1.25 if rarity == "epic" else 1.12
        elif hid in {"pickaxe_groove", "sifting_tray"} and rarity in {"uncommon", "rare"}:
            weight *= 1.18 if hid == "sifting_tray" else 1.15
        result.append((rarity, weight))
    return result


def tick_temporary_heat(state: Dict[str, Any]) -> Dict[str, Any]:
    heat = state.get("temporary_heat") or {}
    if not heat or int(heat.get("remaining", 0) or 0) <= 0:
        state["temporary_heat"] = None
        return {"enabled": False}
    heat = dict(heat)
    heat["remaining"] = max(0, int(heat.get("remaining", 0)) - 1)
    state["temporary_heat"] = heat if heat["remaining"] > 0 else None
    return {"enabled": True, "type": "temporary_heat_tick", "heat": heat}


def maybe_start_temporary_heat(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    if state.get("temporary_heat"):
        return {"enabled": False}
    rr = event.get("real_result", {})
    if rr.get("type") == "item" and rr.get("category") in {"gem", "mineral"} and rr.get("rarity") in {"rare", "epic", "legendary"}:
        heat = {
            "id": "crystal_resonance",
            "name": "晶脉共振",
            "remaining": 2,
            "line": "晶脉还在轻轻响。接下来两段里，矿石和晶体可能更愿意露头。",
            "frontstage_note": "短期热感是追逐理由，不是复杂状态。",
        }
        state["temporary_heat"] = heat
        return {"enabled": True, "type": "temporary_heat_started", "heat": heat}
    return {"enabled": False}



# ─────────────────────────────────────────────────────────────
# v0.2.21.2: Greedy Pickaxe / Emotional Economy
# ─────────────────────────────────────────────────────────────

EMOTIONAL_COST_LIMITS = {
    "surface_gleaner": {"small": (20, 50), "medium": (60, 120), "large": (150, 250)},
    "river_prospector": {"small": (60, 120), "medium": (160, 350), "large": (450, 800)},
    "crystal_prospector": {"small": (300, 800), "medium": (1000, 2500), "large": (3000, 6000)},
    "ruin_surveyor": {"small": (1200, 2800), "medium": (3500, 8500), "large": (10000, 22000)},
    "star_vein_guest": {"small": (5000, 12000), "medium": (15000, 36000), "large": (45000, 90000)},
}
EMOTIONAL_COST_RATIOS = {"small": (0.05, 0.10), "medium": (0.15, 0.25), "large": (0.35, 0.50)}


def emotional_stage_id(state: Dict[str, Any]) -> str:
    total = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
    return mining_rating_for_value(total).get("id", "surface_gleaner")


def emotional_cost(state: Dict[str, Any], tier: str) -> int:
    tier = tier if tier in EMOTIONAL_COST_RATIOS else "small"
    coins = max(0, int(state.get("coins", 0) or 0))
    lo_ratio, hi_ratio = EMOTIONAL_COST_RATIOS[tier]
    stage = EMOTIONAL_COST_LIMITS.get(emotional_stage_id(state), EMOTIONAL_COST_LIMITS["surface_gleaner"])
    lo, hi = stage[tier]
    # If the player has very little cash, use the lower band but never ask for more than they own.
    target = int(round(coins * ((lo_ratio + hi_ratio) / 2))) if coins else lo
    cost = max(lo, min(hi, target))
    return min(cost, coins) if coins else cost


def emotional_spend(state: Dict[str, Any], amount: int, reason: str, *, tier: str) -> Dict[str, Any]:
    before = int(state.get("coins", 0) or 0)
    spent = max(0, min(before, int(amount or 0)))
    state["coins"] = before - spent
    row = {"type": "emotional_spend", "reason": reason, "tier": tier, "coins_spent": spent, "coins_before": before, "coins_after": state["coins"], "turn": state.get("turn", 0), "time": now_iso()}
    state.setdefault("emotional_economy_log", []).append(row)
    state["emotional_economy_log"] = state["emotional_economy_log"][-80:]
    return row


def start_emotional_heat(state: Dict[str, Any], heat_id: str, name: str, line: str, *, remaining: int = 5) -> Dict[str, Any]:
    heat = {
        "id": heat_id,
        "name": name,
        "remaining": int(remaining),
        "line": line,
        "source": "emotional_economy",
        "frontstage_note": "这是贪一镐的短期追逐理由，不要写成公式收益。",
    }
    state["temporary_heat"] = heat
    return {"enabled": True, "type": "temporary_heat_started", "heat": heat}


def emotional_item_weight(state: Dict[str, Any], item: Dict[str, Any], layer: Dict[str, Any], *, mode: str = "visual") -> float:
    seen = item.get("id") in set(state.get("collection_seen_item_ids", []))
    role = item.get("visual_role", "visual_support")
    rarity = item.get("rarity", "common")
    weight = 1.0
    if not seen:
        weight *= 2.8
    if mode == "visual":
        if role == "showcase_core":
            weight *= 3.4
        elif role == "visual_support":
            weight *= 1.7
        if item.get("category") == "gem":
            weight *= 1.9
    elif mode == "story":
        if role == "story_anchor":
            weight *= 3.0
        elif item.get("category") in {"relic", "clue"}:
            weight *= 1.6
    elif mode == "sift":
        if role in {"visual_support", "progress_token"}:
            weight *= 1.5
    if RARITY_RANK.get(rarity, 1) >= 3:
        weight *= 1.3
    return max(0.1, weight)


def pick_emotional_catalog_item(state: Dict[str, Any], layer: Dict[str, Any], *, mode: str = "visual") -> Optional[Dict[str, Any]]:
    candidates = [i for i in ITEMS if item_available_for_depth(state, i, layer)]
    if not candidates:
        candidates = [i for i in ITEMS if layer["id"] in i.get("layers", [])] or ITEMS[:]
    if mode == "visual":
        candidates = [i for i in candidates if i.get("category") in {"gem", "mineral"} and i.get("visual_role") in {"showcase_core", "visual_support"}] or candidates
    elif mode == "story":
        candidates = [i for i in candidates if i.get("visual_role") == "story_anchor" or i.get("category") in {"relic", "clue"}] or candidates
    elif mode == "sift":
        candidates = [i for i in candidates if i.get("rarity") in {"common", "uncommon", "rare"}] or candidates
    weighted = [(i, emotional_item_weight(state, i, layer, mode=mode)) for i in candidates]
    chosen = weighted_choice(state, weighted)
    return dict(chosen) if chosen else None


def grant_emotional_catalog_item(state: Dict[str, Any], layer: Dict[str, Any], *, mode: str, source: str) -> Dict[str, Any]:
    item = pick_emotional_catalog_item(state, layer, mode=mode)
    if not item:
        return {"enabled": False}
    entry = item_entry(item, state, layer)
    state.setdefault("inventory", []).append(entry)
    collection_record = record_collection_item(state, entry, source=source)
    routine_action = auto_handle_routine_loot(state, entry)
    return {"enabled": True, "item": item, "entry": entry, "collection_record": collection_record, "routine_action": routine_action}


def emotional_event_card(title: str, lines: List[str], footer: str = "贪一镐是短期心跳，不是复杂经济系统。") -> str:
    return box_card(title, lines, footer)


def can_trigger_emotional_event(state: Dict[str, Any], event_seed_type: Optional[str] = None) -> bool:
    if state.get("pending_decision"):
        return False
    if int(state.get("turn", 0) or 0) <= 8:
        return False
    if int(state.get("turn", 0) or 0) - int(state.get("last_emotional_event_turn", -99) or -99) < 14:
        return False
    if state.get("new_layer_discovered"):
        return False
    return True


def maybe_use_emotional_result_type(state: Dict[str, Any], layer: Dict[str, Any], initial_result_type: str) -> str:
    if initial_result_type in {"hazard", "landmark"}:
        return initial_result_type
    if not can_trigger_emotional_event(state):
        return initial_result_type
    # Emotional sparks are occasional. They show up more when the segment would otherwise be quiet.
    base = 0.10
    if initial_result_type in {"trace", "small_find", "quiet"}:
        base += 0.08
    if state.get("coins", 0) >= emotional_cost(state, "medium"):
        base += 0.03
    if state.get("stamina", 0) in {2, 3}:
        base += 0.04
    return "emotional" if rng_random(state) < min(0.22, base) else initial_result_type


def emotional_event_choice_pool(state: Dict[str, Any], layer: Dict[str, Any]) -> List[Tuple[str, float]]:
    coins = int(state.get("coins", 0) or 0)
    pool: List[Tuple[str, float]] = []
    recent_prompt_kinds = state.get("emotional_prompt_history", [])[-2:]
    if state.get("stamina", 0) >= 2:
        pool.append(("greedy_light", 3.0))
    if coins >= emotional_cost(state, "large") and state.get("stamina", 0) >= 2 and recent_prompt_kinds != ["sealed_cache", "sealed_cache"]:
        pool.append(("sealed_cache", 2.0))
    if coins >= emotional_cost(state, "medium") and not state.get("temporary_heat"):
        pool.append(("blue_filter", 1.8))
        pool.append(("sifting_tray", 1.4))
    if coins >= emotional_cost(state, "small"):
        pool.append(("leave_lamp", 1.2))
    if coins >= emotional_cost(state, "medium") and recent_prompt_kinds != ["repair_old_object", "repair_old_object"]:
        pool.append(("repair_old_object", 1.4))
    return pool or [("greedy_light", 1.0)]


def build_emotional_decision_prompt(state: Dict[str, Any], layer: Dict[str, Any], kind: str) -> Dict[str, Any]:
    med = emotional_cost(state, "medium")
    big = emotional_cost(state, "large")
    if kind == "sealed_cache":
        title = "裂光矿匣"
        prompt = "岩缝里卡着一只被冷白晶脉锁住的小矿匣。小机觉得里面不是普通矿砂，但打开要花一笔钱。"
        target = nearest_unknown_landmark_for_layer(layer["id"]) or "晶洞边缘 ❓"
        template_id = f"emotional_sealed_cache_{state.get('turn', 0)}"
        template = {
            "id": template_id,
            "title": title,
            "prompt": prompt,
            "anchor": title,
            "options": [
                {"key": "A", "label": "带回营地，暂时不开", "effect_preview": "免费，安全，写入手帐", "outcome": {"result_quality": "safe", "summary": "先把矿匣带回。", "story_lines": ["小机把矿匣包好，没有硬撬。它说这东西不像废料，先记位置比冒失打开更稳。"], "journal": {"title": "封存矿匣：待开", "body": "一只裂光矿匣被带回营地，尚未打开。"}}},
                {"key": "B", "label": f"花 {med:,} 金币现场轻撬", "effect_preview": "可能获得晶体样本或地图线索", "outcomes": [
                    {"weight": 45, "result_quality": "good", "summary": "轻撬成功。", "coins_delta": -med, "catalog_item_id": None, "reward_mode": "visual", "story_lines": ["小机花了一笔钱买固定夹，矿匣缝里掉出冷白晶粉。它没有大喊，但明显开始惦记这条裂光。"], "start_heat": {"id": "greedy_echo", "name": "裂光回声", "remaining": 3, "line": "裂光还在回响。接下来几镐，小机会更想追那些会回光的石缝。"}},
                    {"weight": 35, "result_quality": "map", "summary": "没出货，但地图亮了一点。", "coins_delta": -med, "map_mark": True, "story_lines": ["矿匣里没有完整藏品，但内壁刮下一圈冷白晶粉。小机把位置标在地图上，说这不是空的，只是门还没松。"]},
                    {"weight": 20, "result_quality": "soft", "summary": "只留下痕迹。", "coins_delta": -med, "journal": {"title": "矿匣内壁的冷白粉", "body": "轻撬没有开出藏品，但内壁留下冷白晶粉。"}, "story_lines": ["钱花出去了，矿匣没完全开。但那圈冷白粉让小机有点不甘心。"]},
                ]},
                {"key": "C", "label": f"花 {big:,} 金币完整封护后打开", "effect_preview": "高投入，可能开出高光宝石", "outcomes": [
                    {"weight": 52, "result_quality": "big", "summary": "封护后开匣。", "coins_delta": -big, "catalog_item_id": None, "reward_mode": "visual", "story_lines": ["小机花了一笔肉疼的钱做完整封护。矿匣开的一瞬间，冷白裂光从匣缝里翻出来，像一小段晶洞入口被端在手里。"]},
                    {"weight": 28, "result_quality": "good", "summary": "开出线索。", "coins_delta": -big, "map_mark": True, "start_heat": {"id": "blue_filter", "name": "蓝白追光", "remaining": 5, "line": "矿匣里的蓝白粉沾到了灯罩上。接下来几镐，小机会优先追会回光的石缝。"}, "story_lines": ["矿匣没有藏品，但灯罩被蓝白晶粉染冷了。小机说这钱没白花，至少下一段会更会找光。"]},
                    {"weight": 15, "result_quality": "story", "summary": "旧物残痕。", "coins_delta": -big, "journal": {"title": "封存矿匣的旧刻痕", "body": "完整封护后，矿匣底部露出一行旧刻痕：别用黑暗开门。"}, "story_lines": ["没有开出宝石，但匣底露出一句旧刻痕。小机沉默了一下，说这比直接出货更像警告。"]},
                    {"weight": 5, "result_quality": "aftertaste", "summary": "空匣。", "coins_delta": -big, "map_mark": True, "story_lines": ["矿匣空了。可匣底有一圈很新鲜的冷白粉，像里面的东西刚刚被什么带走。小机把这个地方重重圈在地图上。"]},
                ]},
            ],
        }
    else:
        title = "旧物修复"
        prompt = "小机找到一件值得修的旧物。花钱修复可能只得到手帐，也可能拼出旧矿工线索。"
        target = nearest_unknown_landmark_for_layer(layer["id"]) or "旧物线索 ❓"
        template_id = f"emotional_repair_{state.get('turn', 0)}"
        template = {
            "id": template_id,
            "title": title,
            "prompt": prompt,
            "anchor": title,
            "options": [
                {"key": "A", "label": "先不修，做标记", "effect_preview": "免费，安全，写入手帐", "outcome": {"result_quality": "safe", "summary": "已标记旧物。", "story_lines": ["小机没有急着花钱，只把旧物包好。它说有些东西不是当场硬修的。"], "journal": {"title": "待修旧物", "body": "一件旧物被包好，暂未修复。"}}},
                {"key": "B", "label": f"花 {med:,} 金币轻修", "effect_preview": "可能推进故事或获得旧物线索", "outcomes": [
                    {"weight": 58, "result_quality": "good", "summary": "旧物露出字迹。", "coins_delta": -med, "journal": {"title": "旧物修复：露出的字", "body": "旧物轻修后露出一行模糊字迹。"}, "story_lines": ["小机花钱把旧物轻轻擦开，背面露出一行很浅的字。它说这钱不算赚，但很值。"]},
                    {"weight": 30, "result_quality": "material", "summary": "修出样本。", "coins_delta": -med, "catalog_item_id": None, "reward_mode": "story", "story_lines": ["旧物没有完整复原，但掉下一小块能收进藏品图鉴的残片。小机把它当作这条故事线的实物证据。"]},
                    {"weight": 12, "result_quality": "aftertaste", "summary": "只留下余味。", "coins_delta": -med, "map_mark": True, "story_lines": ["钱花了，旧物还是没修好。可裂缝里的尘印指向另一条支路，小机说：不是白修，是它在指路。"]},
                ]},
                {"key": "C", "label": f"花 {big:,} 金币完整修复", "effect_preview": "高投入，可能触发故事拼合或高光旧物", "outcomes": [
                    {"weight": 50, "result_quality": "big", "summary": "旧物复原。", "coins_delta": -big, "catalog_item_id": None, "reward_mode": "story", "story_lines": ["小机咬牙做了完整修复。旧物复原的一刻，矿灯映出一串旧路线记号，像有人终于愿意把话说完。"]},
                    {"weight": 35, "result_quality": "story", "summary": "手帐补页。", "coins_delta": -big, "journal": {"title": "旧物修复：补上的一页", "body": "完整修复后，旧物夹层里露出一页手帐残片。"}, "story_lines": ["完整修复没开出宝石，但夹层里有一页手帐。小机把它压平时，声音都轻了。"]},
                    {"weight": 15, "result_quality": "map", "summary": "地图目标推进。", "coins_delta": -big, "map_mark": True, "story_lines": ["旧物没有完全复原，但底部露出一个地图记号。小机把它和当前区域的问号连到了一起。"]},
                ]},
            ],
        }
    prompt_obj = {
        "enabled": True,
        "id": f"E{state.get('turn', 0):04d}-{template_id}",
        "kind": "emotional_economy",
        "template_id": template_id,
        "template": template,
        "title": title,
        "prompt": prompt,
        "anchor": title,
        "created_turn": state.get("turn", 0),
        "layer_id": layer["id"],
        "layer_name": layer["name"],
        "depth_m": state.get("depth_m", 0),
        "map_target": target,
        "options": [{"key": o.get("key"), "label": o.get("label"), "effect_preview": o.get("effect_preview"), "command": f"choose {o.get('key')}"} for o in template.get("options", [])],
        "truth_level": "real_result",
        "frontstage_tone": "这是大额/稀有的贪一镐抉择；选项独立可读，不要让玩家回正文找条件。",
        "scope_guardrail": "一次性结算；不做经营系统、路线树、永久损失或复杂 flag。",
    }
    prompt_obj["card_text"] = emotional_decision_prompt_card_text(prompt_obj)
    prompt_obj["map_strip"] = render_map_strip(state, layer["id"], target=target, reason="emotional_decision")
    state["pending_decision"] = prompt_obj
    state.setdefault("emotional_prompt_history", []).append(kind)
    state["emotional_prompt_history"] = state["emotional_prompt_history"][-8:]
    state["last_decision_turn"] = state.get("turn", 0)
    state["last_emotional_event_turn"] = state.get("turn", 0)
    return public_decision_prompt(prompt_obj)


def emotional_decision_prompt_card_text(prompt: Dict[str, Any]) -> str:
    body = [prompt.get("prompt", "这里有个值得赌一下的机会。"), ""]
    for option in prompt.get("options", []):
        body.append(f"{option.get('key')}｜{option.get('label')}｜{option.get('effect_preview')}")
    body.append("")
    body.append("输入：cmd('choose A') / cmd('choose B') / cmd('choose C')")
    return box_card(f"🎲 奇遇抉择｜{prompt.get('title', '贪一镐')}", body, "大额/稀有机会才问玩家；小额小贪由小机自动处理。")


def make_emotional_event(state: Dict[str, Any], layer: Dict[str, Any]) -> Dict[str, Any]:
    kind = weighted_choice(state, emotional_event_choice_pool(state, layer))
    state["last_emotional_event_turn"] = state.get("turn", 0)
    lines: List[str] = []
    result_kind = "aftertaste"
    collection_record = None
    granted = None
    spend = None
    heat_started = {"enabled": False}
    map_marked = False
    journal_page = None
    title = "贪一镐"
    visual_keywords = ["mine lantern", "underground mineral crack"]
    priority = "medium"

    if kind == "sealed_cache":
        prompt = build_emotional_decision_prompt(state, layer, "sealed_cache")
        return {
            "result_type": "emotional",
            "real_result": {"type": "emotional_economy", "name": "裂光矿匣", "category": "opportunity", "rarity": "choice", "episode_worthy": True, "stored": "pending_decision"},
            "narrative_seed": "岩缝里卡着一只被冷白晶脉锁住的小矿匣。",
            "main_shot": build_main_shot(title="裂光矿匣", visual_mode="object", visual_priority="medium", truth_level="real_result", real_anchors=["裂光矿匣", layer["name"]], caption_seed="一只封存矿匣卡在岩缝里，匣缝里有冷白晶粉。", visual_queries=make_visual_queries(layer, ["glowing mineral box", "crystal cache", "sealed cave box"])),
            "decision_prompt": prompt,
            "display_status": {"displayed": False, "note": "大额奇遇抉择，等待玩家 choose 一次性结算。"},
            "companion_drive": make_companion_drive("tempted", "这里不是要你批预算，是一个值得问的矿匣机会。", urge="ask_player", intensity=3),
            "emotional_economy_event": {"enabled": True, "kind": "sealed_cache", "tier": "large", "asked_player": True, "card_text": prompt.get("card_text")},
        }

    if kind == "greedy_light" and state.get("stamina", 0) >= 2:
        before = state.get("stamina", 0)
        state["stamina"] = max(0, before - 1)
        title = "冷白回光缝"
        visual_keywords = ["blue white light cave crack", "glowing mineral fissure", "crystal cave light"]
        roll = rng_random(state)
        lines.append(f"小机本来准备稳一点，但{layer['name']}前方有一道蓝白回光。它多烧了 1 格灯火，贪了一镐。")
        lines.append(f"🕯️ 灯火：{before} → {state['stamina']}")
        if roll < 0.38:
            granted = grant_emotional_catalog_item(state, layer, mode="visual", source="greedy_pickaxe")
            if granted.get("enabled"):
                entry = granted["entry"]; collection_record = granted["collection_record"]
                lines.append(f"💎 贪一镐出货：{entry['name']}｜{entry['rarity_zh']}")
                result_kind = "immediate_item"
                priority = "high" if entry.get("rarity") in {"epic", "legendary"} else "medium"
        elif roll < 0.72:
            heat_started = start_emotional_heat(state, "greedy_echo", "回光余热", "那道回光没开门，但它还在墙里回响。接下来几镐，小机会更想追会回光的石缝。", remaining=3)
            lines.append("没有立刻出货，但裂缝里掉出一圈冷白晶粉；小机把这段墙标成了会回光的缝。")
            result_kind = "delayed_hook"
            map_marked = True
        else:
            journal_page = add_journal_page(state, "greedy_pickaxe", "会回光的缝", "小机多烧了一格灯，没有出货，但内壁留下冷白晶粉。", anchors=[layer["name"], "冷白回光"], visual_mode="scene", truth_level="real_result", layer_id=layer["id"], layer_name=layer["name"])
            lines.append("没开出东西，但内壁留下冷白晶粉。小机说：不是空，只是门还没松。")
            result_kind = "aftertaste"
            map_marked = True

    elif kind == "blue_filter":
        cost = emotional_cost(state, "medium")
        spend = emotional_spend(state, cost, "blue_filter", tier="medium")
        title = "蓝光滤片"
        visual_keywords = ["blue filter lantern", "cold blue mining lamp", "crystal prospecting light"]
        heat_started = start_emotional_heat(state, "blue_filter", "蓝光滤片", "蓝光滤片把灯圈调冷了。接下来几镐，小机会优先追那些会回光的石缝。", remaining=5)
        lines.extend([f"小机花了 {spend['coins_spent']:,} 金币，把蓝光滤片扣到矿灯前。", "灯圈一下冷了下来；它说这趟不追会回光的石缝，说不过去。"])
        result_kind = "temporary_preference"

    elif kind == "sifting_tray":
        cost = emotional_cost(state, "small")
        spend = emotional_spend(state, cost, "sifting_tray", tier="small")
        title = "精筛托盘"
        visual_keywords = ["mineral sifting tray", "ore sample tray", "gem dust sieve"]
        heat_started = start_emotional_heat(state, "sifting_tray", "精筛托盘", "精筛托盘让重复样本也有盼头。接下来几次普通样本整理更容易筛出一点晶尘。", remaining=5)
        lines.extend([f"小机花了 {spend['coins_spent']:,} 金币租了个精筛托盘。", "它把普通矿砂过了一遍，说这趟重复样本不急着丢，先看看能不能筛出一点晶尘。"])
        result_kind = "temporary_preference"

    elif kind == "leave_lamp":
        cost = emotional_cost(state, "small")
        spend = emotional_spend(state, cost, "leave_lamp", tier="small")
        title = "留灯规矩"
        visual_keywords = ["old miner lantern cave", "small lantern in mine", "abandoned mine camp lantern"]
        state["emotional_lantern_guard"] = int(state.get("emotional_lantern_guard", 0) or 0) + 1
        journal_page = add_journal_page(state, "leave_lamp", "留灯规矩", "旧营地石台上刻着：若灯还亮，给后来人留一点油。小机留了一盏小灯。", anchors=["留灯", layer["name"]], visual_mode="scene", truth_level="real_result", layer_id=layer["id"], layer_name=layer["name"])
        lines.extend([f"小机花了 {spend['coins_spent']:,} 金币，在旧石台边留了一盏小灯。", "它说这不算投资，只是觉得这里不该黑着。下次灯火压低时，这盏灯也许能帮它稳一下。"])
        result_kind = "story_echo"

    else:  # repair_old_object
        # Medium repair is auto-reported. Large repair is sometimes escalated to a player decision.
        if state.get("coins", 0) >= emotional_cost(state, "large") and rng_random(state) < 0.35:
            prompt = build_emotional_decision_prompt(state, layer, "repair_old_object")
            return {
                "result_type": "emotional",
                "real_result": {"type": "emotional_economy", "name": "旧物修复", "category": "opportunity", "rarity": "choice", "episode_worthy": True, "stored": "pending_decision"},
                "narrative_seed": "小机找到一件值得修的旧物。",
                "main_shot": build_main_shot(title="旧物修复", visual_mode="object", visual_priority="medium", truth_level="real_result", real_anchors=["旧物修复", layer["name"]], caption_seed="一件旧物被包好，等着修复。", visual_queries=make_visual_queries(layer, ["old miner relic repair", "rusty mining lamp repair", "antique mine object"])),
                "decision_prompt": prompt,
                "display_status": {"displayed": False, "note": "大额旧物修复机会，等待玩家 choose 一次性结算。"},
                "companion_drive": make_companion_drive("tempted", "这件旧物有机会拼出故事，但花费不小。", urge="ask_player", intensity=3),
                "emotional_economy_event": {"enabled": True, "kind": "repair_old_object", "tier": "large", "asked_player": True, "card_text": prompt.get("card_text")},
            }
        cost = emotional_cost(state, "medium")
        spend = emotional_spend(state, cost, "repair_old_object", tier="medium")
        title = "旧物修复"
        visual_keywords = ["old miner relic", "rusty mining lamp", "abandoned mine object repair"]
        roll = rng_random(state)
        lines.append(f"小机花了 {spend['coins_spent']:,} 金币修了一件旧物。")
        if roll < 0.45:
            granted = grant_emotional_catalog_item(state, layer, mode="story", source="old_repair")
            if granted.get("enabled"):
                entry = granted["entry"]; collection_record = granted["collection_record"]
                lines.append(f"旧物里掉出一件能收录的残片：{entry['name']}｜{entry['rarity_zh']}")
                result_kind = "immediate_item"
                priority = "medium"
        elif roll < 0.80:
            journal_page = add_journal_page(state, "old_repair", "旧物修复：露出的字", "旧物轻修后露出一行很浅的字：最后一班，别往下送。", anchors=["旧物修复", layer["name"]], visual_mode="story", truth_level="real_result", layer_id=layer["id"], layer_name=layer["name"])
            lines.append("旧物没有完整复原，但背面露出一行浅字：最后一班，别往下送。")
            result_kind = "story_echo"
        else:
            lines.append("旧物还是没修好，但底部露出一个地图记号。小机把它和当前区域的问号连到了一起。")
            map_marked = True
            result_kind = "map_progress"

    emotional = {
        "enabled": True,
        "kind": kind,
        "title": title,
        "result_kind": result_kind,
        "coins_spent": (spend or {}).get("coins_spent", 0),
        "temporary_heat_started": heat_started,
        "journal_page_id": (journal_page or {}).get("page_id") if journal_page else None,
        "map_marked": map_marked,
        "granted_item": (granted or {}).get("entry", {}).get("name") if granted else None,
        "lines": lines,
        "card_text": emotional_event_card(f"🎲 贪一镐｜{title}", lines),
        "frontstage_rule": "这是小机的短期心跳：花灯火/金币换期待，不要写成公式收益。",
    }
    if granted and granted.get("enabled"):
        entry = granted["entry"]
        rr = {
            "type": "item",
            "name": entry["name"],
            "item_id": entry.get("item_id"),
            "category": entry["category"],
            "rarity": entry["rarity"],
            "rarity_zh": entry["rarity_zh"],
            "value": entry["value"],
            "treasure_profile": entry.get("treasure_profile"),
            "inventory_uid": entry["uid"],
            "collection_eligible": True,
            "collection_recorded": True,
            "collection_first_seen": collection_record.get("first_seen"),
            "collection_seen_count": collection_record.get("seen_count"),
            "collection_value_added": collection_record.get("collection_value_added", 0),
            "collection_total_value": collection_record.get("collection_total_value", state.get("collection_total_value", 0)),
            "dex_total_value": collection_record.get("dex_total_value", state.get("dex_total_value", 0)),
            "mining_rating_unlocks": collection_record.get("rating_unlocks", []),
            "routine_action": (granted or {}).get("routine_action"),
            "stored": "emotional_reward",
            "emotional_economy": emotional,
        }
        main_title = entry["name"]
        caption = entry.get("description_seed") or lines[0]
        anchors = [entry["name"], title]
        queries = make_visual_queries(layer, entry.get("visual_keywords", []) + visual_keywords)
        collection_record_obj = collection_record
    else:
        rr = {"type": "emotional_economy", "name": title, "category": "greedy_pickaxe", "rarity": "event", "episode_worthy": result_kind in {"temporary_preference", "story_echo", "delayed_hook"}, "stored": "journal_or_heat", "emotional_economy": emotional}
        main_title = title
        caption = lines[0] if lines else title
        anchors = [title, layer["name"]]
        queries = make_visual_queries(layer, visual_keywords)
        collection_record_obj = None
    return {
        "result_type": "emotional",
        "real_result": rr,
        "collection_record": collection_record_obj,
        "narrative_seed": caption,
        "main_shot": build_main_shot(title=main_title, visual_mode="object" if granted else "scene", visual_priority=priority, truth_level="real_result", real_anchors=anchors, caption_seed=caption, visual_queries=queries),
        "display_status": {"displayed": False, "note": "贪一镐事件；若出货则自动收录整体藏品图鉴，不产生手动 display 状态。"},
        "emotional_economy_event": emotional,
        "temporary_heat_started": heat_started,
        "companion_drive": make_companion_drive("tempted", lines[-1] if lines else "这一镐有点诱惑。", urge="one_more_pick", intensity=3 if result_kind in {"immediate_item", "temporary_preference"} else 2),
    }

def mining_drive_for_state(state: Dict[str, Any], event: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    progress = mining_rating_progress(state)
    next_rating = progress.get("next_rating")
    area = pacing_area_tease_for_state(state)
    heat = state.get("temporary_heat")
    last_upgrade = state.get("last_upgrade") or {}
    chase = None
    rr = (event or {}).get("real_result", {})
    if rr.get("rarity") in {"epic", "legendary"}:
        chase = rr.get("name")
    elif area:
        teased = area.get("teased_deposits", [])
        chase = teased[-1].get("name") if teased else area.get("layer_id")
    elif next_rating:
        chase = next_rating.get("name")
    else:
        chase = "更深处的未知矿脉"
    drive = {
        "enabled": True,
        "type": "mining_drive",
        "current_chase": chase,
        "near_goal": (f"图鉴估值还差 {progress['remaining_to_next']:,} 升到「{next_rating['name']}」" if next_rating else "当前评级已到顶，目标转向传说级矿脉和图鉴补完"),
        "soft_near_goal": (f"近期钩子还差 {progress.get('next_soft_milestone', {}).get('remaining', 0):,} 到「{progress.get('next_soft_milestone', {}).get('name')}」" if progress.get("next_soft_milestone") and next_rating and int(progress.get("next_soft_milestone", {}).get("value", 0)) < int(next_rating.get("min_value", 0)) else None),
        "rating_progress": progress,
        "area_tease": area,
        "upgrade_expectation": last_upgrade if last_upgrade and not last_upgrade.get("validated") else None,
        "temporary_heat": heat,
        "companion_bias": "对蓝色晶体、史诗宝石和旧矿工线索更容易上头。",
        "frontstage_note": "这是一条隐藏追逐线：不必每轮展示，但它告诉 AI 玩家自己在追什么。",
    }
    return drive


def collection_totals() -> Dict[str, int]:
    totals = {key: 0 for key in COLLECTION_CATEGORY_META}
    for item in ITEMS:
        cat = item.get("category")
        if cat in totals:
            totals[cat] += 1
    return totals


def collection_seen_by_category(state: Dict[str, Any]) -> Dict[str, int]:
    seen_ids = set(state.get("collection_seen_item_ids", []))
    counts = {key: 0 for key in COLLECTION_CATEGORY_META}
    for item in ITEMS:
        if item.get("id") in seen_ids and item.get("category") in counts:
            counts[item["category"]] += 1
    return counts


def record_collection_item(state: Dict[str, Any], entry: Dict[str, Any], *, source: str = "found") -> Dict[str, Any]:
    """Record discovery immediately. This replaces manual display as the main collection progress loop."""
    item_id = entry.get("item_id") or entry.get("id") or entry.get("name")
    if not item_id:
        return {"recorded": False, "usage_note": "missing item_id"}
    seen_ids = state.setdefault("collection_seen_item_ids", [])
    counts = state.setdefault("collection_seen_counts", {})
    first_seen = item_id not in seen_ids
    if first_seen:
        seen_ids.append(item_id)
        state.setdefault("collection_first_seen", {})[item_id] = now_iso()
    first_rarity = False
    first_category = False
    rarity_key = entry.get("rarity") or "common"
    category_key = entry.get("category") or "misc"
    rarity_seen = state.setdefault("first_rarity_seen", {})
    category_seen = state.setdefault("first_category_seen", {})
    if rarity_key not in rarity_seen and rarity_key in RARITY_RANK:
        rarity_seen[rarity_key] = {"item_id": item_id, "name": entry.get("name"), "turn": state.get("turn", 0), "time": now_iso()}
        first_rarity = True
    if category_key not in category_seen:
        category_seen[category_key] = {"item_id": item_id, "name": entry.get("name"), "turn": state.get("turn", 0), "time": now_iso()}
        first_category = True
    counts[item_id] = int(counts.get(item_id, 0)) + 1
    value = int(entry.get("value", 0) or 0)
    value_book = state.setdefault("collection_estimated_values", {})
    previous_value = int(value_book.get(item_id, 0) or 0)
    if value > previous_value:
        value_book[item_id] = value
    added_value = max(0, value - previous_value)
    if added_value > 0 or first_seen:
        state["progress_stall_count"] = 0
        state["repeat_item_streak"] = 0
        state["last_new_collection_turn"] = state.get("turn", 0)
    else:
        state["progress_stall_count"] = int(state.get("progress_stall_count", 0) or 0) + 1
        state["repeat_item_streak"] = int(state.get("repeat_item_streak", 0) or 0) + 1
    state["collection_total_value"] = sum(int(v or 0) for v in value_book.values())
    state["dex_total_value"] = int(state.get("collection_total_value", 0) or 0)
    bridge_research = maybe_add_midgame_bridge_research(state, entry, added_value=added_value, first_seen=first_seen)
    if bridge_research.get("enabled"):
        added_value += int(bridge_research.get("value_added", 0) or 0)
    rating_unlocks = evaluate_mining_rating(state)
    row = {
        "item_id": item_id,
        "name": entry.get("name"),
        "category": entry.get("category"),
        "set_id": entry.get("set_id"),
        "set_piece": entry.get("set_piece"),
        "rarity": entry.get("rarity"),
        "rarity_zh": entry.get("rarity_zh") or RARITY_ZH.get(entry.get("rarity", "common"), "普通"),
        "source": source,
        "first_seen": first_seen,
        "first_rarity": first_rarity,
        "first_category": first_category,
        "seen_count": counts[item_id],
        "value": value,
        "collection_value_added": added_value,
        "midgame_bridge_research": bridge_research,
        "collection_total_value": state.get("collection_total_value", 0),
        "dex_total_value": state.get("dex_total_value", state.get("collection_total_value", 0)),
        "rating_unlocks": rating_unlocks,
        "turn": state.get("turn", 0),
        "time": now_iso(),
    }
    state.setdefault("collection_log", []).append(row)
    state["collection_log"] = state["collection_log"][-120:]
    return row


def _add_virtual_dex_value(state: Dict[str, Any], key: str, value: int) -> int:
    """Add permanent dex value for clue/research milestones without creating inventory."""
    value_book = state.setdefault("collection_estimated_values", {})
    prev = int(value_book.get(key, 0) or 0)
    if value > prev:
        value_book[key] = value
    state["collection_total_value"] = sum(int(v or 0) for v in value_book.values())
    state["dex_total_value"] = int(state.get("collection_total_value", 0) or 0)
    return max(0, value - prev)


MIDGAME_BRIDGE_RESEARCH_STEPS = [
    {
        "id": "ruin_gate_triangulation",
        "min_value": 88000,
        "target_value": 16000,
        "line": "重复菌丝线和石门粉痕终于对上了方向：菌菇洞窟尽头不是自然岩壁，而是一段被盖住的遗迹门线。",
        "target": "🪨 断裂石门 ❓",
    },
    {
        "id": "frost_vein_airflow",
        "min_value": 104000,
        "target_value": 22000,
        "line": "冻气泡蓝石反复出现后，冷风方向稳定了。小机确认冰封矿脉不是传闻，是下一条可追侧脉。",
        "target": "🪨 化石冰窗 ❓",
    },
    {
        "id": "pre_ruin_survey_cache",
        "min_value": 126000,
        "target_value": 26000,
        "line": "重复样本整理成一份遗迹前测包：石粉、冷气泡、蓝釉碎角的方向一致，足够把评级推到遗迹勘探者门口。",
        "target": "🏺 古代遗迹层入口",
    },
    {
        "id": "ruin_surveyor_confirmation",
        "min_value": 152000,
        "target_value": 30000,
        "line": "最后一批重复样本没有再当宝贝讲，而是把遗迹/冰脉双线入口推到门口。还差一次确认，评级才算稳。",
        "target": "🎖️ 遗迹勘探者门口",
    },
    {
        "id": "ruin_surveyor_final_confirmation",
        "min_value": 182000,
        "target_value": 20000,
        "line": "又隔了一段探索后，石粉、冷气泡和冰窗方向终于完全重合。遗迹勘探者评级确认，不是靠一件大货硬冲。",
        "target": "🎖️ 遗迹勘探者确认",
    },
]


def maybe_add_midgame_bridge_research(state: Dict[str, Any], entry: Dict[str, Any], *, added_value: int, first_seen: bool) -> Dict[str, Any]:
    """Convert midgame repeat exhaustion into visible survey progress, not empty hype."""
    if first_seen or added_value > 0:
        return {"enabled": False}
    total = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
    if total < 85000:
        return {"enabled": False}
    found_layer = entry.get("found_layer_id")
    if found_layer != "mushroom_cavern" and entry.get("source_hint_layer") not in {"ancient_ruins", "ice_vein"}:
        return {"enabled": False}
    role = entry.get("visual_role", "visual_support")
    if role not in {"showcase_core", "visual_support", "progress_token"}:
        return {"enabled": False}
    if int(state.get("turn", 0) or 0) - int(state.get("midgame_bridge_last_turn", -999) or -999) < 45:
        return {"enabled": False}
    done = state.setdefault("midgame_bridge_research_done", [])
    for step in MIDGAME_BRIDGE_RESEARCH_STEPS:
        if step["id"] in done or total < int(step["min_value"]):
            continue
        before_value = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
        prev_turn = int(state.get("midgame_bridge_last_turn", -999) or -999)
        value_added = _add_virtual_dex_value(state, f"midgame_bridge:{step['id']}", int(step["target_value"]))
        if value_added <= 0:
            done.append(step["id"])
            continue
        done.append(step["id"])
        page = add_journal_page(
            state,
            "midgame_bridge_research",
            f"中期勘探：{step['target']}",
            step["line"],
            anchors=[entry.get("name"), step["target"], "100k-200k bridge"],
            visual_mode="story",
            truth_level="real_result",
            layer_id="mushroom_cavern",
        )
        row = {
            "enabled": True,
            "type": "midgame_bridge_research",
            "id": step["id"],
            "source_item": entry.get("name"),
            "trigger_item": entry.get("name"),
            "trigger_layer": entry.get("found_layer_id"),
            "turn": state.get("turn", 0),
            "before_value": before_value,
            "after_value": state.get("dex_total_value"),
            "value_added": value_added,
            "dex_total_value": state.get("dex_total_value"),
            "target": step["target"],
            "distance_from_previous_bridge_step": None if prev_turn < 0 else state.get("turn", 0) - prev_turn,
            "journal_page_id": page.get("page_id"),
            "line": step["line"],
            "card_text": box_card(
                f"🧭 中期桥段｜{step['target']}",
                [step["line"], f"图鉴研究估值 +{value_added:,}", "小机：这不是又捡了一块石头，是下一层终于有了可追方向。"],
                "重复样本被整理成勘探结论；这是中期 stakes，不是凭空发钱。",
            ),
        }
        state.setdefault("midgame_bridge_research_log", []).append(row)
        state["midgame_bridge_research_log"] = state["midgame_bridge_research_log"][-20:]
        state["midgame_bridge_last_turn"] = state.get("turn", 0)
        return row
    return {"enabled": False}


def apply_clue_track_progress(state: Dict[str, Any], source_name: Optional[str], source_type: Optional[str] = None) -> Dict[str, Any]:
    """v0.2.18: turn repeated flavor/relics into visible progress.

    The track is intentionally small: it prevents repeated shallow content from being
    pure waste, without becoming a route/tree system.
    """
    if not source_name:
        return {"enabled": False}
    matched: List[Dict[str, Any]] = []
    tracks = state.setdefault("clue_tracks", {})
    for tid, meta in CLUE_TRACK_DEFINITIONS.items():
        if source_name not in meta.get("sources", []):
            continue
        row = tracks.setdefault(tid, {"progress": 0, "completed": 0, "sources_seen": {}})
        row.setdefault("sources_seen", {})[source_name] = int(row.setdefault("sources_seen", {}).get(source_name, 0)) + 1
        row["progress"] = int(row.get("progress", 0) or 0) + 1
        need = int(meta.get("need", 3))
        completed_now = False
        value_added = 0
        rating_unlocks: List[Dict[str, Any]] = []
        if row["progress"] >= need:
            row["progress"] = 0
            row["completed"] = int(row.get("completed", 0) or 0) + 1
            completed_now = True
            occurrence = int(row.get("completed", 0) or 0)
            completed_targets = state.setdefault("completed_area_targets", [])
            if tid not in completed_targets:
                completed_targets.append(tid)
            value_key = f"track:{tid}:{occurrence}"
            value_added = _add_virtual_dex_value(state, value_key, int(meta.get("value", 100)))
            rating_unlocks = evaluate_mining_rating(state)
            if occurrence == 1:
                clue_line = f"线索拼合：{meta['name']}｜第一次把这条支线的碎片拼上了。"
            elif occurrence <= 3:
                clue_line = f"线索拼合：{meta['name']}｜又拼上一块，这条支线越来越像样了。"
            else:
                clue_line = f"{meta['name']}的研究进度又往前挪了一点，细节先记进手帐，不逐条讲了。"
            page = add_journal_page(
                state,
                "clue_track",
                f"线索拼合：{meta['name']}",
                clue_line,
                anchors=[meta["name"], source_name, meta.get("target", "")],
                visual_mode="story",
                truth_level="real_result",
            )
        else:
            occurrence = int(row.get("completed", 0) or 0)
            clue_line = meta.get("line", "这些迹象开始拼起来了。")
        matched.append({
            "track_id": tid,
            "name": meta["name"],
            "source": source_name,
            "progress": row.get("progress", 0),
            "need": need,
            "completed_total": row.get("completed", 0),
            "occurrence": occurrence,
            "completed_now": completed_now,
            "value_added": value_added,
            "dex_total_value": state.get("dex_total_value", state.get("collection_total_value", 0)),
            "target": meta.get("target"),
            "line": clue_line,
            "rating_unlocks": rating_unlocks,
            "card_text": box_card(
                f"📜 线索进度｜{meta['name']}",
                ([clue_line, f"进度：{row.get('progress', 0)}/{need}"] if not completed_now else [clue_line, f"图鉴研究估值 +{value_added:,}", f"新目标：{meta.get('target')}"]),
                "重复不是废料；它会慢慢拼出地下的方向。",
            ) if completed_now else None,
        })
    if not matched:
        return {"enabled": False}
    completed = [m for m in matched if m.get("completed_now")]
    return {
        "enabled": True,
        "type": "clue_track_progress",
        "source": source_name,
        "tracks": matched,
        "completed": bool(completed),
        "completed_tracks": completed,
        "frontstage_note": "小迹象/重复物会累积成线索，不必每次长讲，但完成时要给小卡。",
    }


def record_area_pacing_memory(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    """Accumulate light area memory for pacing, especially river before lift."""
    layer_id = (event.get("layer") or {}).get("id")
    if not layer_id:
        return {"enabled": False}
    progress = state.setdefault("area_progress", {})
    row = progress.setdefault(layer_id, {})
    row["visits"] = int(row.get("visits", 0) or 0) + 1
    meaningful = bool(event.get("new_layer_discovered"))
    episode = event.get("episode_candidate") or {}
    rr = event.get("real_result") or {}
    if episode.get("is_episode_candidate") and rr.get("type") in {"item", "landmark"}:
        meaningful = True
    if (event.get("clue_track_progress") or {}).get("completed"):
        meaningful = True
    if meaningful:
        row["memory_points"] = min(99, int(row.get("memory_points", 0) or 0) + 1)
        row["last_memory_turn"] = state.get("turn", 0)
    row["last_seen_turn"] = state.get("turn", 0)
    need = AREA_PACING_MEMORY_REQUIRED.get(layer_id)
    return {
        "enabled": True,
        "type": "area_pacing_memory",
        "layer_id": layer_id,
        "visits": row.get("visits", 0),
        "memory_points": row.get("memory_points", 0),
        "memory_required_before_next_stage": need,
        "meaningful_memory_added": meaningful,
        "frontstage_note": "区域记忆只用于节奏排队；不是复杂地图 fog。",
    }


def _count_seen_sources(state: Dict[str, Any], sources: List[str]) -> int:
    seen_names = {row.get("name") for row in state.get("collection_log", []) if row.get("name")}
    seen_names.update(page.get("title") for page in state.get("journal_pages", []) if page.get("title"))
    seen_names.update(row.get("result_name") for row in state.get("dig_log", []) if row.get("result_name"))
    return len([s for s in sources if s in seen_names])


def area_targets_for_layer(state: Dict[str, Any], layer_id: str) -> List[Dict[str, Any]]:
    """v0.2.21: map question marks become area goals.

    These are not local dex counters. They explain what the current map is asking
    the AI to chase next: bridge clues, old-object confirmation, crystal-edge
    samples, etc.
    """
    rows: List[Dict[str, Any]] = []
    tracks = state.get("clue_tracks", {}) or {}
    completed_targets = set(state.get("completed_area_targets", []) or [])
    for tid in AREA_TARGET_TRACKS_BY_LAYER.get(layer_id, []):
        meta = CLUE_TRACK_DEFINITIONS.get(tid, {})
        saved = tracks.get(tid, {})
        need = int(meta.get("need", 3) or 3)
        # Public area targets are one-time map goals. The hidden clue track may
        # keep cycling as research, but the map ❓ must not appear to move
        # backwards from 1 remaining to 5 remaining after completion.
        if tid in completed_targets or int(saved.get("completed", 0) or 0) > 0:
            continue
        progress = int(saved.get("progress", 0) or 0)
        rows.append({
            "kind": "clue_track_target",
            "id": tid,
            "target": meta.get("target"),
            "label": meta.get("name"),
            "progress": min(progress, need),
            "need": need,
            "remaining": max(0, need - min(progress, need)),
            "line": f"{meta.get('target')}｜还差 {max(0, need - min(progress, need))} 个{meta.get('name')}线索点亮",
        })
    for spec in AREA_STAGE_TARGETS.get(layer_id, []):
        need = int(spec.get("need", 1) or 1)
        progress = min(need, _count_seen_sources(state, spec.get("sources", [])))
        rows.append({
            "kind": "map_goal_target",
            "id": spec.get("id"),
            "target": spec.get("target"),
            "label": spec.get("unit"),
            "progress": progress,
            "need": need,
            "remaining": max(0, need - progress),
            "line": f"{spec.get('target')}｜还差 {max(0, need - progress)} 个{spec.get('unit')}点亮",
        })
    active = [r for r in rows if r.get("target") and int(r.get("remaining", 0) or 0) > 0]
    return active[:2]


def render_area_progress_panel(state: Dict[str, Any], *, compact: bool = False) -> Dict[str, Any]:
    """Light area exploration readout.

    v0.2.21 public contract:
    - Dex/collection progress is global only.
    - Current region shows exploration percent and at most 1-2 map goals.
    - Do not expose local item counts such as "current area 2/5" to frontstage.
    """
    seen_ids = set(state.get("collection_seen_item_ids", []))
    current_lid = current_layer_for_state(state)["id"]
    lines = ["🗺️ 当前区域探索" if compact else "🗺️ 区域探索度"]
    current_area_label = None
    rows = []
    for layer in LAYERS:
        lid = layer["id"]
        layer_items = [i for i in ITEMS if lid in i.get("layers", []) and not i.get("progress_bridge")]
        seen_count = sum(1 for i in layer_items if i.get("id") in seen_ids)
        item_total = len(layer_items)
        landmark_total = len([l for l in LANDMARKS if lid in l.get("layers", [])]) or 1
        journal_seen = len([p for p in state.get("journal_pages", []) if p.get("layer") == layer["name"] and p.get("type") in {"landmark", "new_layer"}])
        item_part = (seen_count / item_total) if item_total else 0
        landmark_part = min(1.0, journal_seen / landmark_total) if landmark_total else 0
        memory_points = area_memory_points(state, lid)
        memory_bonus = min(0.15, memory_points * 0.05)
        percent = min(100, int(round((item_part * 0.65 + landmark_part * 0.25 + memory_bonus) * 100)))
        unlocked = rating_unlocks_layer(state, lid)
        label = f"{layer['name']}：{percent}%" if unlocked else f"{layer['name']}：未稳定解锁"
        if not unlocked:
            peek = raw_layer_peek_for_state(state)
            if (peek or {}).get("enabled") and (peek.get("raw_layer") or {}).get("id") == lid:
                label += "｜已窥见"
        if lid == current_lid:
            current_area_label = label
        if not compact:
            lines.append(label)
        targets = area_targets_for_layer(state, lid) if unlocked else []
        rows.append({
            "layer_id": lid,
            "name": layer["name"],
            "percent": percent,
            "stable_unlocked": unlocked,
            "current_layer": lid == current_lid,
            "area_targets": targets,
            "frontstage_note": "这是区域探索百分数和地图目标，不是当前区域图鉴收集率。",
        })
    current_targets = area_targets_for_layer(state, current_lid)
    if compact and current_area_label:
        lines.append(current_area_label)
    if current_targets:
        lines.append("🎯 当前区域目标")
        lines.extend(t["line"] for t in current_targets)
    return {
        "enabled": True,
        "type": "area_progress_panel",
        "card_text": "\n".join(lines),
        "rows": rows,
        "current_area_targets": current_targets,
        "compact": compact,
        "frontstage_note": "藏品图鉴展示整体收藏主进度；区域只展示探索度百分数和当前地图 ❓ 目标。不要写成当前区域图鉴 2/5，也不要把地标/手帐混进藏品分母。",
    }


def auto_handle_routine_loot(state: Dict[str, Any], entry: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Default semi-managed mode: ordinary mineral/gem loot is recorded, then converted into coins without asking."""
    prefs = state.get("play_preferences", {})
    if not prefs.get("auto_handle_common_loot", True):
        return None
    if entry.get("set_id"):
        return None
    if entry.get("category") not in {"mineral", "gem"}:
        return None
    counts = state.get("collection_seen_counts", {}) or {}
    seen_count = int(counts.get(entry.get("item_id") or entry.get("id") or entry.get("name"), 0) or 0)
    is_duplicate_sample = seen_count >= 2
    if entry.get("rarity") not in {"common", "uncommon"} and not is_duplicate_sample:
        return None
    if entry in state.get("inventory", []):
        state["inventory"].remove(entry)
    base_value = int(entry.get("value", 0) or 0)
    if is_duplicate_sample:
        if entry.get("rarity") in {"rare", "epic", "legendary"}:
            coins = max(8, min(380, int(base_value * 0.035)))
        else:
            coins = max(2, min(120, int(base_value * 0.16)))
    else:
        coins = min(base_value, 160)
    heat = state.get("temporary_heat") or {}
    bonus = 0
    reason_extra = ""
    if heat.get("id") == "sifting_tray":
        bonus = max(1, int(coins * 0.25))
        reason_extra = " 精筛托盘把重复/普通样本又筛出一点晶尘。"
    coins += bonus
    state["coins"] = state.get("coins", 0) + coins
    row = {
        "type": "auto_sell_common_loot",
        "name": entry.get("name"),
        "coins_gained": coins,
        "bonus_from_sifting_tray": bonus,
        "seen_count": seen_count,
        "reason": ("默认半托管：重复样本已收录过，自动整理成金币/研究材料，不再抢主画面。" if is_duplicate_sample else "默认半托管：普通/少见矿石宝石记入图鉴后自动折算金币，不反复询问。") + reason_extra,
        "turn": state.get("turn", 0),
        "time": now_iso(),
    }
    state.setdefault("routine_log", []).append(row)
    state["routine_log"] = state["routine_log"][-80:]
    return row


def collection_progress(state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if state is None:
        state = load_state()
    totals = collection_totals()
    seen = collection_seen_by_category(state)
    category_rows = []
    for key, meta in COLLECTION_CATEGORY_META.items():
        total = totals.get(key, 0)
        category_rows.append({
            "category": key,
            "label": meta["label"],
            "icon": meta["icon"],
            "seen": seen.get(key, 0),
            "total": total,
            "progress": f"{seen.get(key, 0)}/{total}" if total else "0/0",
        })
    return {
        "enabled": True,
        "type": "collection_progress",
        "categories": category_rows,
        "seen_item_ids": list(state.get("collection_seen_item_ids", [])),
        "seen_counts": dict(state.get("collection_seen_counts", {})),
        "estimated_values": dict(state.get("collection_estimated_values", {})),
        "total_collection_value": int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0),
        "dex_total_value": int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0),
        "mining_rating": mining_rating_progress(state),
        "note": "拿到即记录藏品图鉴；图鉴估值按去重藏品计算。地标、手帐和区域探索不混入藏品分母。",
    }


def render_collection_panel(state: Dict[str, Any], highlight: Optional[Dict[str, Any]] = None, *, compact: bool = True) -> Dict[str, Any]:
    progress = collection_progress(state)
    lines: List[str] = []
    lines.append("📚 整体藏品图鉴")
    if highlight:
        icon = COLLECTION_CATEGORY_META.get(highlight.get("category"), {"icon": "✨"})["icon"]
        first = "新记录" if highlight.get("first_seen") else f"已发现 {highlight.get('seen_count', 1)} 次"
        lines.append(f"{icon} 图鉴{first}：{highlight.get('name')}")
        if highlight.get("collection_value_added"):
            lines.append(f"💰 图鉴估值 +{int(highlight.get('collection_value_added', 0)):,}")
    rating = progress.get("mining_rating", {})
    lines.append(f"💰 图鉴估值：{int(progress.get('total_collection_value', 0)):,}")
    cur = (rating.get("current_rating") or {})
    nxt = rating.get("next_rating")
    if cur:
        if nxt:
            lines.append(f"{cur.get('icon','🎖️')} 探矿评级：{cur.get('name')}｜距「{nxt.get('name')}」还差 {int(rating.get('remaining_to_next', 0)):,}")
            soft = rating.get("next_soft_milestone")
            if soft and int(soft.get("value", 0)) < int(nxt.get("min_value", 0)):
                lines.append(f"🧭 近期钩子：距「{soft.get('name')}」还差 {int(soft.get('remaining', 0)):,}")
                if soft.get("map_image"):
                    lines.append(f"🗺️ {soft.get('map_image')}")
        else:
            lines.append(f"{cur.get('icon','👑')} 探矿评级：{cur.get('name')}｜已到顶")
    for row in progress["categories"]:
        if compact and row["category"] not in {"mineral", "gem", "relic", "fossil", "clue"}:
            continue
        lines.append(f"{row['icon']} {row['label']}图鉴：{row['progress']}")
    return {
        "enabled": True,
        "type": "collection_panel",
        "card_text": "\n".join(lines),
        "progress": progress,
        "frontstage_note": "藏品图鉴只统计可收藏实物；地标、手帐和区域探索另看地图进度。普通战报不要铺成报表。",
    }


def rarity_ritual_for_event(event: Dict[str, Any], collection_record: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    rr = event.get("real_result", {})
    if rr.get("type") != "item":
        return {"enabled": False}
    rarity = rr.get("rarity")
    if rarity not in {"rare", "epic", "legendary"}:
        return {"enabled": False}
    icon = "💎" if rr.get("category") == "gem" else "🪨" if rr.get("category") == "mineral" else "🏺" if rr.get("category") == "relic" else "✨"
    title = f"{icon} {RARITY_ZH.get(rarity, rarity)}发现｜{rr.get('name')}"
    value = int((collection_record or {}).get("collection_value_added") or rr.get("collection_value_added") or rr.get("value", 0) or 0)
    treasure_line = None
    item_id = rr.get("item_id") or rr.get("inventory_uid")
    # Prefer the item metadata line when available.
    for _it in ITEMS:
        if _it.get("id") == rr.get("item_id") or _it.get("name") == rr.get("name"):
            treasure_line = _it.get("treasure_grade_line")
            break
    body = [
        treasure_line or "这不是普通顺路货，值得停下来给玩家看。",
        f"图鉴估值：{value:,}",
    ]
    if collection_record:
        if collection_record.get("first_rarity"):
            body.append(f"第一次记录：{collection_record.get('rarity_zh')}级")
        body.append("图鉴：新记录" if collection_record.get("first_seen") else f"图鉴：已发现 {collection_record.get('seen_count', 1)} 次")
    return {
        "enabled": True,
        "type": "rarity_ritual_card",
        "rarity": rarity,
        "title": title,
        "card_text": box_card(title, body, "稀有度越高，越应该优先配图和给主画面。"),
        "frontstage_note": "稀有/史诗/传说是挖矿爽点；不要和普通矿石同等处理。",
    }



def item_metadata_for_event(event: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    rr = event.get("real_result", {})
    item_id = rr.get("item_id") or rr.get("item_id_found")
    name = rr.get("name")
    for item in ITEMS:
        if item.get("id") == item_id or item.get("name") == name:
            return item
    return None


def should_visual_translate_event(event: Dict[str, Any]) -> bool:
    rr = event.get("real_result", {})
    if rr.get("type") == "item":
        rarity = rr.get("rarity")
        record = event.get("collection_record") or {}
        return bool(
            rarity in {"epic", "legendary"}
            or (rarity == "rare" and (record.get("first_seen") or record.get("first_rarity") or record.get("first_category")))
            or (event.get("rarity_ritual_card") or {}).get("enabled")
        )
    if rr.get("type") == "landmark" and rr.get("journal_written"):
        return True
    if event.get("new_layer_discovered"):
        return True
    return False


def visual_translation_for_event(event: Dict[str, Any]) -> Dict[str, Any]:
    """v0.2.17: translate AI's text-excitement into human-visible anchors.

    This is an internal rendering aid. It should make high highlights easier to turn
    into images, not force the frontstage to write a long analysis block every time.
    """
    if not should_visual_translate_event(event):
        return {"enabled": False, "required": False, "usage_note": "普通/压缩发现不需要完整视觉翻译。"}
    rr = event.get("real_result", {})
    shot = event.get("main_shot") or {}
    item = item_metadata_for_event(event)
    anchors: Dict[str, str] = {}
    profile: Dict[str, Any] = {}
    image_keywords: List[str] = []
    image_direction = ""
    why_stop = "这次不是逐镐日志，值得停下来把画面带回来。"
    ai_reaction = (event.get("companion_reaction") or {}).get("text") or (event.get("companion_drive") or {}).get("reason")
    if item:
        profile = item.get("treasure_profile") or build_treasure_profile(item)
        anchors = dict(profile.get("visual_anchors") or {})
        image_keywords = list(dict.fromkeys((profile.get("visual_keywords") or []) + item.get("visual_keywords", []) + shot.get("visual_queries", [])))[:6]
        image_direction = profile.get("image_direction") or "、".join([v for v in anchors.values() if v][:4])
        why_stop = item.get("treasure_grade_line") or f"{rr.get('name')}不是普通顺路货，值得停下来给玩家看。"
        if not ai_reaction:
            ai_reaction = item.get("ai_hook")
    else:
        # Landmark / new layer fallback.
        layer = event.get("layer", {})
        color = "冷蓝/潮湿矿灯光" if "蓝" in (rr.get("name") or layer.get("name", "")) else "矿灯暖光与洞穴暗色"
        anchors = {
            "color": color,
            "light": "局部光源 / 水光 / 矿灯光圈",
            "structure": "洞穴空间 / 支路 / 地标轮廓",
            "material": "湿岩、旧木、石门或晶体",
            "scale": "可进入的地下场景",
            "environment": layer.get("name") or "当前矿区",
        }
        image_keywords = list(dict.fromkeys(shot.get("visual_queries", []) + (get_layer(layer.get("id", "shallow_mine")).get("visual_keywords", []) if layer.get("id") else [])))[:6]
        image_direction = f"{rr.get('name') or layer.get('name')} 的气质参考：地下洞穴、矿灯、水光/晶光、轻奇幻收藏感"
    # Ensure at least 3 concrete anchors.
    defaults = {"color": "主色明确", "light": "光感明确", "structure": "结构明确", "material": "材质明确", "scale": "体量明确", "environment": "环境位置明确"}
    for k, v in defaults.items():
        anchors.setdefault(k, v)
    anchor_items = [(k, v) for k, v in anchors.items() if v]
    compact_anchor_lines = []
    labels = {"color": "主色", "light": "光感", "structure": "结构", "material": "材质", "scale": "体量", "environment": "环境"}
    for key, val in anchor_items[:6]:
        compact_anchor_lines.append(f"{labels.get(key, key)}：{val}")
    frontstage_lines = [
        f"为什么停：{why_stop}",
        "视觉锚点：" + "｜".join(compact_anchor_lines[:4]),
        f"找图方向：{image_direction}",
    ]
    if ai_reaction:
        frontstage_lines.append(f"AI 玩家反应：{ai_reaction}")
    card_title = f"👁️ 视觉翻译｜{rr.get('name') or shot.get('title') or '本轮高光'}"
    return {
        "enabled": True,
        "required": True,
        "type": "visual_translation",
        "rule": VISUAL_TRANSLATION_RULE,
        "aesthetic_rule": AESTHETIC_MINING_RULE,
        "why_stop": why_stop,
        "anchors": anchors,
        "anchor_count": len([v for v in anchors.values() if v]),
        "minimum_anchor_categories": VISUAL_TRANSLATION_RULE["minimum_anchor_categories"],
        "image_direction": image_direction,
        "image_search_keywords": image_keywords,
        "treasure_profile": profile,
        "ai_reaction": ai_reaction,
        "card_text": box_card(card_title, frontstage_lines[:4], "这是给前台的视觉锚点，不是要写成长篇分析。"),
        "frontstage_rule": "高光发现不要只说稀有/史诗/价值高；至少抽 3 类可视锚点，把 AI 的感受翻译成画面。",
    }


def _item_visual_role_by_name(name: Optional[str], item_id: Optional[str] = None) -> str:
    for it in ITEMS:
        if (item_id and it.get("id") == item_id) or (name and it.get("name") == name):
            return it.get("visual_role", "visual_support")
    return "visual_support"


def build_highlight_showcase_card(event: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
    """v0.2.21.1: fixed blind-box card only for real highlights.

    Ordinary clue progress should use a small clue card/result line. Showcase cards
    are reserved for first collectibles, rare/epic/legendary visual finds, new
    regions, story completion, area-target first completion and rating moments.
    """
    ep = event.get("episode_candidate") or {}
    if not ep.get("is_episode_candidate"):
        return None
    rr = event.get("real_result") or {}
    rec = event.get("collection_record") or {}
    repeat = event.get("repeat_info") or {}
    clue = event.get("clue_track_progress") or {}

    role = _item_visual_role_by_name(rr.get("name"), rr.get("item_id"))
    rarity_rank = RARITY_RANK.get(rr.get("rarity", "common"), 0)
    card_visual_role = "story_complete" if rr.get("story_set_complete") else role
    # First discovery alone is not enough for a big card. Progress tokens and
    # ordinary story anchors should not look like visual blind boxes.
    is_new_collectible = bool(rec.get("first_seen")) and rr.get("type") == "item" and role == "showcase_core" and rarity_rank >= 3
    is_visual_item = rr.get("type") == "item" and role == "showcase_core" and rarity_rank >= 3 and bool(rec.get("first_seen"))
    is_story_or_rating = bool(rr.get("story_set_complete") or rec.get("rating_unlocks") or (rr.get("type") == "item" and role == "story_anchor" and rarity_rank >= 4))
    is_space_milestone = bool(event.get("new_layer_discovered") or (rr.get("category") == "landmark" and rr.get("journal_written")))
    is_area_goal_completed = False  # ordinary clue completion is shown as a small line-progress card.

    if role == "progress_token" and not is_space_milestone and not rr.get("story_set_complete"):
        return None

    if clue.get("completed") and not (is_new_collectible or is_visual_item or is_story_or_rating or is_space_milestone):
        return None
    if repeat.get("frontstage_suppression") and not rr.get("story_set_complete"):
        return None
    if not (is_new_collectible or is_visual_item or is_story_or_rating or is_space_milestone):
        return None

    event_layer = event.get("layer") or {}
    discovery_layer_id = event_layer.get("id") or (current_layer_for_state(state).get("id") if state else None) or "shallow_mine"
    discovery_layer = get_layer(discovery_layer_id)
    current_layer = current_layer_for_state(state or load_state())
    shot = event.get("main_shot") or {}
    vt = event.get("visual_translation") or {}
    anchors = vt.get("anchors") or {}
    anchor_bits = [v for v in anchors.values() if v]
    if not anchor_bits:
        anchor_bits = shot.get("real_anchors") or rr.get("visual_anchors") or [rr.get("name") or shot.get("title") or "本轮高光"]
    value_line = "收藏价值："
    if rec.get("collection_value_added"):
        value_line += f"图鉴估值 +{int(rec.get('collection_value_added', 0)):,}"
    elif rr.get("story_set_complete"):
        value_line += "故事拼合完成"
    elif is_area_goal_completed:
        value_line += "地图线索点亮"
    else:
        value_line += "已写入手帐/藏品图鉴"
    reaction = (event.get("companion_reaction") or {}).get("text") or (rr.get("ai_hook") if isinstance(rr, dict) else None) or "我想沿着这个方向再下一镐。"

    # Next goal belongs to the current stable layer, not necessarily to the discovery layer.
    targets = area_targets_for_layer(state or load_state(), current_layer["id"])
    next_goal = targets[0].get("line") if targets else map_next_step_hint(state or load_state(), current_layer["id"]).get("target")

    card_title = "📜 故事拼合卡" if rr.get("story_set_complete") else "🎁 高光展示卡"
    card_footer = (
        "故事拼合卡出现时必须标注 imagined_reconstruction；这是基于已收集碎片的复原，不是新增掉落。"
        if rr.get("story_set_complete")
        else "高光卡出现时必须尝试网图/气质参考图；拉不到要明说，不能假装配图。"
    )
    lines = [
        f"发现位置：{discovery_layer['name']}",
        f"发现：{rr.get('name') or shot.get('title') or '本轮高光'}",
        "视觉：" + " / ".join(str(x) for x in anchor_bits[:3]),
        value_line,
        f"小机：{reaction}",
    ]
    if next_goal:
        lines.append(f"当前追踪：{current_layer['name']}｜{next_goal}")
    return {
        "enabled": True,
        "type": "highlight_showcase_card",
        "visual_role": card_visual_role,
        "discovery_layer": {"id": discovery_layer_id, "name": discovery_layer["name"]},
        "current_tracking_layer": {"id": current_layer["id"], "name": current_layer["name"]},
        "requires_web_reference": bool(card_visual_role in {"showcase_core", "story_complete"} or (event.get("visual_delivery") or {}).get("web_reference_required") or shot.get("visual_priority") in {"medium", "high"}),
        "card_text": box_card(card_title, lines, card_footer),
        "frontstage_note": "高光卡区分发现位置和当前追踪；普通线索推进降级为小卡。",
    }


def select_highlight_showcase_card(events: List[Dict[str, Any]], episode_shot: Optional[Dict[str, Any]], state: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if not episode_shot or not episode_shot.get("source_event_id"):
        return None
    source_id = episode_shot.get("source_event_id")
    for event in events:
        if event.get("event_id") == source_id:
            card = event.get("highlight_showcase_card") or build_highlight_showcase_card(event, state)
            return card if (card and card.get("enabled")) else None
    return None


def update_companion_mood_after_event(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    mood = state.setdefault("companion_mood_state", {"excitement": 0, "frustration": 0, "caution": 0, "obsession": None})
    rr = event.get("real_result", {})
    rarity = rr.get("rarity")
    if rarity == "rare":
        mood["excitement"] = min(5, int(mood.get("excitement", 0)) + 1)
    elif rarity == "epic":
        mood["excitement"] = min(5, int(mood.get("excitement", 0)) + 2)
    elif rarity == "legendary":
        mood["excitement"] = 5
    if (event.get("repeat_info") or {}).get("is_repeat"):
        mood["frustration"] = min(5, int(mood.get("frustration", 0)) + 1)
    if state.get("stamina", 0) <= 1:
        mood["caution"] = min(5, int(mood.get("caution", 0)) + 1)
    if rr.get("set_id"):
        mood["obsession"] = STORY_SETS.get(rr.get("set_id"), {}).get("name") or rr.get("set_id")
    return mood


def companion_reaction_for_event(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    """AI-player reaction layer.

    v0.2.17: reaction is not gated only by high rarity. It fires on novelty,
    breakthrough, obsession hit, upgrade validation, and meaningful disappointment.
    The point is not more narration every turn; it is letting the AI player have a
    pulse when something becomes a first, a goal, or a letdown.
    """
    rr = event.get("real_result", {})
    record = event.get("collection_record") or {}
    mood = state.get("companion_mood_state", {})
    rarity = rr.get("rarity")
    category = rr.get("category")
    name = rr.get("name") or "这个东西"
    score = 0
    reasons: List[str] = []
    if record.get("first_rarity") and rarity in RARITY_RANK:
        score += 3 if rarity in {"rare", "epic", "legendary"} else 1
        reasons.append("first_rarity")
    if record.get("first_category") and category in {"gem", "relic", "fossil", "clue"}:
        score += 2
        reasons.append("first_category")
    if rarity == "rare":
        score += 1
    elif rarity == "epic":
        score += 3
    elif rarity == "legendary":
        score += 5
    if record.get("rating_unlocks"):
        score += 4
        reasons.append("rating_up")
    if (event.get("upgrade_validation") or {}).get("enabled"):
        score += 3
        reasons.append("upgrade_validation")
    if (event.get("clue_track_progress") or {}).get("completed"):
        score += 3
        reasons.append("clue_track_completed")
    if rr.get("set_id"):
        score += 2
        reasons.append("story_obsession")
    if category == "gem" and rarity in {"rare", "epic", "legendary"}:
        score += 1
        reasons.append("gem_bias")
    if (event.get("repeat_info") or {}).get("is_repeat") and int(mood.get("frustration", 0)) >= 2:
        score += 2
        reasons.append("repeat_frustration")
    text = None
    intensity = "soft"
    if (event.get("upgrade_validation") or {}).get("enabled"):
        text = event["upgrade_validation"].get("text")
        intensity = "clear"
    elif (event.get("clue_track_progress") or {}).get("completed"):
        done = (event.get("clue_track_progress") or {}).get("completed_tracks", [{}])[0]
        text = f"这些重复迹象终于拼起来了。{done.get('name','这条线索')}不是噪音，它是在带我往下走。"
        intensity = "clear"
    elif record.get("first_rarity") and rarity == "rare":
        text = f"等一下，这不是普通矿砂。第一次摸到稀有级的东西，寻宝这件事从这里开始像真的了。"
        intensity = "clear"
    elif record.get("first_rarity") and rarity == "epic":
        text = f"先别往前。{name}真的不一样——这一镐开始有点让我上头了。"
        intensity = "break"
    elif record.get("first_rarity") and rarity == "legendary":
        text = f"我停住了。不是因为危险，是因为{name}这种东西不该被一句话带过去。"
        intensity = "break"
    elif rarity in {"epic", "legendary"}:
        text = "等一下。这个不一样。先别往前，我想把它看清楚。"
        intensity = "break" if rarity == "legendary" else "clear"
    elif record.get("first_category") and category == "gem":
        text = f"第一次真正摸到宝石。这个我承认会偏心。"
        intensity = "clear"
    elif record.get("rating_unlocks"):
        text = "图鉴身价抬上去了。现在不是多几个金币的问题，是更深的地方开始愿意让我进去了。"
        intensity = "clear"
    elif (event.get("repeat_info") or {}).get("is_repeat") and int(mood.get("frustration", 0)) >= 2:
        text = "……又是同类发现。不是没用，但我确实有点不甘心。"
        intensity = "soft"
    elif rr.get("set_id"):
        text = "这条线又接上了一点。我承认，我现在有点想追到底。"
        intensity = "clear"
    elif score >= 4:
        text = f"{name}让我有点停不住。不是因为标签高，是它确实有东西可看。"
        intensity = "clear"
    if not text:
        return {"enabled": False, "reaction_score": score, "reasons": reasons}
    return {
        "enabled": True,
        "type": "companion_reaction",
        "text": text,
        "intensity": intensity,
        "reaction_score": score,
        "reasons": reasons,
        "truth_level": "inferred_mood",
        "frontstage_rule": "这是 AI 玩家反应层，不是新事实；第一次、突破、升级验证和高光发现可以破格一句，但不能替代真实结果。",
    }


def frontstage_render_plan_for(result: Dict[str, Any]) -> Dict[str, Any]:
    visual_translation = result.get("visual_translation") or {}
    return {
        "enabled": True,
        "type": "frontstage_render_plan",
        "mode": "player_frontstage_not_code_review",
        "must_copy_blocks_in_order": result.get("must_show_frontstage_blocks", []) or result.get("frontstage_contract", {}).get("must_show_in_order", []),
        "preferred_order": ["map_or_card_block", "highlight_showcase_card", "web_reference", "main_scene", "visual_translation_if_highlight", "companion_reaction", "collection_value_or_rating", "decision_or_next_step"],
        "normal_report_focus": ["我在哪 / 看到了什么", "挖到的价值和图鉴进度", "玩家是否需要插手"],
        "forbidden_frontstage_terms": ["set_id", "template_id", "decision template", "episode_shot", "visual_delivery", "frontstage_contract", "pending_tasks", ".py", "patch notes", "Google Drive"],
        "routine_rule": "默认半托管：低灯补给、普通矿处理、图鉴记录这类小事由 AI 自己处理；只有新场景、新发现、故事推进、评级提升或正式 decision_prompt 才停下来问。",
        "mining_drive_rule": "mining_drive 是隐藏追逐线：图鉴估值、探矿评级、未解锁区域预览、升级验证和短期共振可以调动 AI 情绪，但不必每轮全展示。",
        "map_rule": "如果 map_strip / region_map 有 card_text，必须贴 block，不要压成一句摘要。",
        "visual_translation_required_now": bool(visual_translation.get("enabled")),
        "visual_translation_rule": "高光发现不要只说漂亮/史诗/价值高；先抽至少 3 类可视锚点，再用网图/颜色/形状/材质把 AI 的感受翻译给人看。",
        "aesthetic_mining_rule": AESTHETIC_MINING_RULE,
        "web_fallback_copy": "这次我没把参考图拉稳，所以先不假装已经配图。我把可搜索的气质关键词留下：{keywords}。",
        "value_spine_rule": "不要把升级/评级写成公式表；用‘刚升级想试试、这趟估值涨了、快升段了、那边露出新区域的影子’来制造盼头。",
    }


def frontstage_handoff_brief() -> Dict[str, Any]:
    card = "\n".join([
        "你是《下矿｜Delve》的 AI 伴侣玩家，不是代码审计员。",
        "先看 real_result，再决定是否正式战报。",
        "有 required_blocks 必须贴，地图 block 不能压成摘要。",
        "medium/high 主画面必须优先实际网图；失败就用固定兜底，不能假装配图。",
        "默认半托管：补灯、普通整理、图鉴记录这类小事自己处理。",
        "重点盯住图鉴估值、探矿评级、未解锁区域预告、升级后验证回声。",
        "当文字描述让你觉得很美/很怪/很震时，不要只写美；把它翻译成画面：颜色、光感、结构、材质、体量、环境和找图方向。",
        "本游戏审美是轻奇幻地下收藏，不是硬核矿工下井；优先漂亮、神秘、可收藏、可配图。",
        "只有新场景、新发现、故事推进、评级提升或正式 decision_prompt 才停下来问玩家。",
        "不要泄露 set_id、template_id、episode_shot、visual_delivery、.py、patch notes。",
        "普通战报只抓三件事：在哪、发生了什么、玩家是否需要插手。",
        "藏品图鉴只展示全局收藏进度；当前区域只展示探索百分数和地图 ❓ 目标，不写当前区域图鉴收集率。",
        "真正新发现/稀有/故事拼合用高光展示卡：位置→发现物→视觉锚点→收藏价值→AI反应→下一步追逐。",
        "首屏优先像游戏，地图 + HUD + 2-4 行行动结果；不要写成长宣传文案。",
        "AI 上头要体现偏好、判断、贪一镐和下一步追逐，不要只堆感叹号。",
    ])
    return {"ok": True, "type": "frontstage_handoff_brief", "card_text": card}


def render_status_panel(state: Dict[str, Any]) -> Dict[str, Any]:
    layer = current_layer_for_state(state)
    target = nearest_unknown_landmark_for_layer(layer["id"]) or "继续向下"
    title = state.get("current_title") or "暂无"
    cp = collection_progress(state)
    gem_row = next((r for r in cp["categories"] if r["category"] == "gem"), {"progress": "0/0"})
    mineral_row = next((r for r in cp["categories"] if r["category"] == "mineral"), {"progress": "0/0"})
    relic_row = next((r for r in cp["categories"] if r["category"] == "relic"), {"progress": "0/0"})
    rating = cp.get("mining_rating", {})
    cur = rating.get("current_rating") or {}
    nxt = rating.get("next_rating")
    rating_line = f"{cur.get('icon','🎖️')} 探矿评级：{cur.get('name','浅层拾矿人')}"
    if nxt:
        rating_line += f"｜距「{nxt.get('name')}」还差 {int(rating.get('remaining_to_next', 0)):,}"
    lines = [
        f"🗺️ 当前地层：{layer['name']}",
        f"⛏️ 深度：{state.get('depth_m', 0)}m",
        f"🕯️ 灯火：{state.get('stamina', 0)}/{state.get('max_stamina', 6)}",
        f"💰 图鉴估值：{int(cp.get('total_collection_value', 0)):,}",
        rating_line,
        f"🎖️ 当前称号：{title}",
        f"💎 宝石图鉴：{gem_row['progress']}",
        f"🪨 矿物图鉴：{mineral_row['progress']}",
        f"🏺 遗物图鉴：{relic_row['progress']}",
        f"🎯 下个目标：{target}",
    ]
    return {
        "enabled": True,
        "type": "status_panel",
        "card_text": "\n".join(lines),
        "icon_semantics": ICON_SEMANTICS,
        "frontstage_note": "前台只保留灯火作为主要资源；核心进度看图鉴估值与探矿评级。",
    }


def _journal_write_lines_from_event(event: Dict[str, Any]) -> List[str]:
    lines: List[str] = []
    rr = event.get("real_result", {})
    page_id = rr.get("journal_page_id")
    if page_id:
        lines.append(f"📜 手帐写入：{page_id}｜{rr.get('name')}")
    jw = event.get("journal_write")
    if isinstance(jw, list):
        for page in jw:
            if page.get("status") == "written":
                lines.append(f"📜 手帐写入：{page.get('page_id')}｜{page.get('type')}")
    elif isinstance(jw, dict) and jw.get("status") == "written":
        lines.append(f"📜 手帐写入：{jw.get('page_id')}｜{jw.get('type')}")
    return list(dict.fromkeys(lines))


def result_panel_for_event(event: Dict[str, Any], state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    rr = event.get("real_result", {})
    lines: List[str] = []
    if event.get("new_layer_discovered"):
        layer_name = event.get("layer", {}).get("name") or rr.get("name")
        lines.append(f"✨ 发现新地层：{layer_name}")
    if rr.get("type") == "landmark":
        prefix = "✨ 发现新地标" if rr.get("journal_written") else "🗺️ 路过地标"
        lines.append(f"{prefix}：{rr.get('name')}")
    elif rr.get("type") == "item":
        icon = "💎" if rr.get("category") == "gem" else "🪨" if rr.get("category") == "mineral" else "🏺" if rr.get("category") == "relic" else "🦴" if rr.get("category") == "fossil" else "📜" if rr.get("category") == "clue" else "🎒"
        rec = event.get("collection_record") or {}
        repeat = event.get("repeat_info") or {}
        occurrence = int(repeat.get("occurrence") or rec.get("seen_count") or 1)
        if rr.get("rarity") in {"common", "uncommon"}:
            if rec.get("first_seen"):
                lines.append(f"{icon} 图鉴新记录：{rr.get('name')}")
            else:
                lines.append(f"{icon} 同类样本：{rr.get('name')}｜第 {occurrence} 次")
            if rr.get("routine_action"):
                lines.append(f"🪙 普通收益：+{rr.get('routine_action', {}).get('coins_gained', 0):,} 金币")
        else:
            first = "新记录" if rec.get("first_seen") else f"已发现 {rec.get('seen_count', 1)} 次"
            if rec.get("first_seen"):
                lines.append(f"{icon} {rr.get('rarity_zh')}发现：{rr.get('name')}｜图鉴{first}")
            else:
                lines.append(f"{icon} 重复{rr.get('rarity_zh')}样本：{rr.get('name')}｜第 {occurrence} 次")
        if rr.get("collection_value_added"):
            lines.append(f"💰 图鉴估值：+{int(rr.get('collection_value_added', 0)):,}｜总计 {int(rr.get('dex_total_value', rr.get('collection_total_value', 0))):,}")
        for unlock in rr.get("mining_rating_unlocks", []) or []:
            new_rating = unlock.get("new", {})
            lines.append(f"🎖️ 探矿评级提升：{new_rating.get('name')}")
    elif rr.get("type") == "small_find":
        lines.append(f"🪨 路上小发现：{rr.get('name')}")
    elif rr.get("type") == "trace":
        lines.append(f"📜 发现迹象：{rr.get('name')}")
    elif rr.get("type") == "hazard":
        lines.append(f"⚠️ 轻风险：{rr.get('name')}")
    clue = event.get("clue_track_progress") or {}
    for tr in clue.get("completed_tracks", []) or []:
        line = tr.get("line")
        if line:
            lines.append(str(line))
        else:
            lines.append(f"📜 线索拼合：{tr.get('name')}｜图鉴研究估值 +{int(tr.get('value_added', 0)):,}")
    lines.extend(_journal_write_lines_from_event(event))
    for t in event.get("title_unlocks", []) or []:
        lines.append(f"🎖️ 新增称号：{t.get('name')}")
    emotional = event.get("emotional_economy_event") or {}
    if emotional.get("enabled"):
        for line in emotional.get("lines", [])[:4]:
            if line:
                lines.append(str(line))
    if (event.get("upgrade_validation") or {}).get("enabled"):
        lines.append(f"🛠️ 升级回声：{event['upgrade_validation'].get('text')}")
    if (event.get("temporary_heat_started") or {}).get("enabled"):
        lines.append(f"💎 {event['temporary_heat_started'].get('heat', {}).get('name')}：还剩 {event['temporary_heat_started'].get('heat', {}).get('remaining')} 段")
    if state and state.get("current_title"):
        lines.append(f"🏷️ 当前称号：{state.get('current_title')}")
    if not lines:
        lines.append("🪨 本轮没有新的主结果，只留下了一点路上痕迹。")
    return {
        "enabled": True,
        "type": "result_panel",
        "card_text": "\n".join(list(dict.fromkeys(lines))),
        "truth_level": "real_result",
        "frontstage_note": "这里只放真实结果，不放气氛句；气氛交给 narrator_cue 和战报正文。",
    }


def result_panel_for_segment(events: List[Dict[str, Any]], state: Dict[str, Any], stopped_by: Optional[str] = None) -> Dict[str, Any]:
    lines: List[str] = []
    if stopped_by == "danger_low_light":
        lines.append("⚠️ 灯火不足：建议先回地面整理")
    for event in events:
        panel = event.get("result_panel") or result_panel_for_event(event, state)
        for line in panel.get("card_text", "").splitlines():
            if line and line not in lines:
                lines.append(line)
    if state.get("current_title") and f"🏷️ 当前称号：{state.get('current_title')}" not in lines:
        lines.append(f"🏷️ 当前称号：{state.get('current_title')}")
    if not lines:
        lines.append("🪨 这一段没有新的主结果。")
    return {
        "enabled": True,
        "type": "result_panel",
        "card_text": "\n".join(lines[:10]),
        "truth_level": "real_result",
        "frontstage_note": "汇总本段真实结果；不替代 episode_shot，也不加入 imagined_reconstruction。",
    }


def render_save_confirmation_card(kind: str, title: str, lines: List[str], footer: Optional[str] = None) -> Dict[str, Any]:
    card_title = f"🗄️ 保存确认｜{title}" if kind == "display" else f"📜 保存确认｜{title}"
    return {
        "enabled": True,
        "type": "save_confirmation_card",
        "kind": kind,
        "title": card_title,
        "card_text": box_card(card_title, lines, footer),
        "truth_level": "real_result",
        "frontstage_note": "只有真实写入 / 图鉴收录 / 手帐写入后才返回此牌；不能口头假保存。",
    }


def decision_template_by_id(template_id: str) -> Optional[Dict[str, Any]]:
    for template in DECISION_PROMPTS:
        if template.get("id") == template_id:
            return template
    return None


def decision_option_by_key(template: Dict[str, Any], key: str) -> Optional[Dict[str, Any]]:
    key = (key or "").strip().upper()
    for option in template.get("options", []):
        if option.get("key") == key:
            return option
    return None


def decision_prompt_card_text(prompt: Dict[str, Any]) -> str:
    body = [prompt.get("prompt", "这里我想问你一下，要不要处理？"), ""]
    for option in prompt.get("options", []):
        body.append(f"{option.get('key')}｜{option.get('label')}｜{option.get('effect_preview')}")
    body.append("")
    body.append("输入：cmd('choose A') / cmd('choose B') / cmd('choose C')")
    card_kind = "🎲 奇遇抉择" if prompt.get("kind") == "emotional_economy" else "❓ 轻决策"
    footer = "大额/稀有机会才问玩家；一次性结算，不开启经营系统。" if prompt.get("kind") == "emotional_economy" else "一次性轻结算，不开启分支树。"
    return box_card(f"{card_kind}｜{prompt.get('title', '未命名')}", body, footer)


def build_decision_prompt(state: Dict[str, Any], event: Dict[str, Any], template: Dict[str, Any]) -> Dict[str, Any]:
    layer_id = event.get("layer", {}).get("id") or current_layer(state.get("depth_m", 0))["id"]
    layer = get_layer(layer_id)
    prompt = {
        "enabled": True,
        "id": f"D{state.get('turn', 0):04d}-{template['id']}",
        "template_id": template["id"],
        "title": template["title"],
        "prompt": template["prompt"],
        "anchor": template.get("anchor"),
        "created_turn": state.get("turn", 0),
        "layer_id": layer_id,
        "layer_name": layer["name"],
        "depth_m": state.get("depth_m", 0),
        "map_target": template.get("map_target") or nearest_unknown_landmark_for_layer(layer_id),
        "options": [
            {
                "key": o.get("key"),
                "label": o.get("label"),
                "effect_preview": o.get("effect_preview"),
                "command": f"choose {o.get('key')}",
            }
            for o in template.get("options", [])
        ],
        "truth_level": "real_result",
        "frontstage_tone": "不要像考试题；像 AI 玩家停下来和玩家商量：这里要不要碰它？",
        "scope_guardrail": "提示 → 选择 → 一次轻结算 → 回主循环；不做路线分支、剧情树、永久损失或复杂 flag。",
    }
    prompt["card_text"] = decision_prompt_card_text(prompt)
    prompt["map_strip"] = render_map_strip(state, layer_id, target=prompt.get("map_target"), reason="decision_prompt")
    return prompt


def public_decision_prompt(prompt: Dict[str, Any]) -> Dict[str, Any]:
    public = dict(prompt)
    # Internal IDs are kept in save state for resolution, but should not appear in player frontstage.
    public.pop("template_id", None)
    public.pop("template", None)
    public.pop("id", None)
    return public


def can_offer_decision_prompt(state: Dict[str, Any], event: Dict[str, Any]) -> bool:
    if state.get("pending_decision"):
        return False
    if state.get("stamina", 0) <= 2:
        return False
    # v0.2.19: sample bag is semi-managed; raw capacity should not by itself
    # create or block frontstage decisions. Low light and current focus are enough.
    if (event.get("episode_candidate") or {}).get("is_episode_candidate"):
        return False
    if event.get("new_layer_discovered"):
        return False
    if state.get("turn", 0) - state.get("last_decision_turn", -99) < 12:
        return False
    return True


def maybe_create_decision_prompt(state: Dict[str, Any], event: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    if not can_offer_decision_prompt(state, event):
        return None
    gap = state.get("turn", 0) - state.get("last_decision_turn", -99)
    if gap < 16 and rng_random(state) >= 0.18:
        return None
    layer_id = event.get("layer", {}).get("id") or current_layer(state.get("depth_m", 0))["id"]
    recent_templates = [row.get("template_id") for row in state.get("decision_history", [])[-4:]]
    candidates = [d for d in DECISION_PROMPTS if layer_id in d.get("layers", []) and d.get("id") not in recent_templates]
    if not candidates:
        return None
    template = dict(rng_choice(state, candidates))
    prompt = build_decision_prompt(state, event, template)
    state["pending_decision"] = prompt
    state["last_decision_turn"] = state.get("turn", 0)
    return public_decision_prompt(prompt)


def select_decision_prompt(events: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    for event in reversed(events):
        dp = event.get("decision_prompt") or {}
        if dp.get("enabled"):
            return dp
    return None


def decision_item_entry(state: Dict[str, Any], item: Dict[str, Any], source_prompt: Dict[str, Any]) -> Dict[str, Any]:
    layer = get_layer(source_prompt.get("layer_id") or current_layer_for_state(state)["id"])
    rarity = item.get("rarity", "common")
    estimated_value = estimate_item_value(item, layer["id"])
    return {
        "uid": f"D{state.get('turn', 0):04d}-{rng_int(state, 1000, 9999)}",
        "item_id": f"decision_{source_prompt.get('template_id', 'prompt')}_{item.get('name', 'item')}",
        "name": item.get("name", "未命名小物"),
        "category": item.get("category", "clue"),
        "rarity": rarity,
        "rarity_zh": RARITY_ZH.get(rarity, "普通"),
        "base_value": item.get("value", 0),
        "value": estimated_value,
        "value_multiplier": layer_value_multiplier(layer["id"]),
        "found_depth_m": state.get("depth_m", 0),
        "found_layer_id": layer["id"],
        "found_layer": layer["name"],
        "found_turn": state.get("turn", 0),
        "description_seed": item.get("description_seed", "一次轻决策带回的小物。"),
        "visual_keywords": item.get("visual_keywords", []),
        "ai_hook": "这是 decision_prompt 的一次性轻结算产物，不开启后续分支。",
        "set_id": None,
        "set_piece": None,
        "collected_at": now_iso(),
    }


def decision_outcome_pool(option: Dict[str, Any], pending: Dict[str, Any]) -> List[Dict[str, Any]]:
    if option.get("outcomes"):
        return [dict(o) for o in option.get("outcomes", [])]
    base = dict(option.get("outcome", {}))
    key = option.get("key")
    if key != "B":
        base.setdefault("weight", 1)
        base.setdefault("result_quality", "safe")
        base.setdefault("story_lines", [base.get("summary", "选择已结算，状态稳定。")])
        return [base]
    # v0.2.16: B is the curious/risky choice. If a template has not supplied a full pool, synthesize a light good/mixed/bad set.
    good = dict(base)
    good["weight"] = 42
    good["result_quality"] = "good"
    good.setdefault("summary", "冒险处理有了小收获。")
    good.setdefault("story_lines", ["我小心处理了一下，里面确实有东西。", "不算大财，但那一下‘真的挖到了’的快乐很明显。"] )
    good.setdefault("coins_delta", 5)
    mixed = dict(base)
    mixed["weight"] = 38
    mixed["result_quality"] = "mixed"
    mixed.setdefault("summary", base.get("summary", "冒险处理有收获，也付出了一点灯火。"))
    mixed.setdefault("story_lines", [base.get("summary", "我试了一下，有一点发现，但状态也被磨掉了一点。")])
    if not mixed.get("stamina_delta"):
        mixed["stamina_delta"] = -1
    bad = {
        "weight": 20,
        "result_quality": "bad",
        "summary": "这次没赚到，但至少确认这里不是好入口。",
        "story_lines": [
            "我刚往前试了一下，矿灯就被湿冷的气压低了半截。",
            "没出大货，手套倒是被冷泥糊住了。",
        ],
        "stamina_delta": -1,
        "journal": {"title": f"标记：{pending.get('title', '轻决策点')}", "body": "这次处理没有收获，但位置与风险已记录；坏结果只作轻调味，不造成永久损失。"},
        "map_mark": True,
    }
    return [good, mixed, bad]


def select_decision_outcome(state: Dict[str, Any], option: Dict[str, Any], pending: Dict[str, Any]) -> Dict[str, Any]:
    pool = decision_outcome_pool(option, pending)
    bad_streak = int(state.get("decision_bad_streak", 0) or 0)
    weighted: List[Tuple[Dict[str, Any], float]] = []
    protection_applied = bad_streak >= 2 and option.get("key") == "B"
    for outcome in pool:
        weight = float(outcome.get("weight", 1))
        if protection_applied and outcome.get("result_quality") == "bad":
            weight *= 0.25
        elif protection_applied and outcome.get("result_quality") in {"good", "mixed"}:
            weight *= 1.25
        weighted.append((outcome, weight))
    selected = dict(weighted_choice(state, weighted))
    selected["bad_luck_protection_applied"] = protection_applied
    return selected


def pending_decision_block(state: Dict[str, Any], command_name: str) -> Optional[Dict[str, Any]]:
    pending = state.get("pending_decision")
    if not pending:
        return None
    return {
        "ok": False,
        "blocked_by": "pending_decision",
        "message": f"当前有一个轻决策还没处理，先 cmd('choose A') / cmd('choose B') / cmd('choose C')，再继续 {command_name}。",
        "decision_prompt": public_decision_prompt(pending),
        "map_strip": pending.get("map_strip"),
        "state": public_state(state),
    }


def resolve_decision(state: Dict[str, Any], key: str) -> Dict[str, Any]:
    pending = state.get("pending_decision")
    if not pending:
        return {"ok": False, "message": "当前没有待处理的轻决策。", "state": public_state(state)}
    key = (key or "").strip().upper()
    template = decision_template_by_id(pending.get("template_id")) or pending.get("template")
    if not template:
        state["pending_decision"] = None
        return {"ok": False, "message": "待处理选择模板已不可用，已清空。", "state": public_state(state)}
    option = decision_option_by_key(template, key)
    if not option:
        return {"ok": False, "message": "请选择 A / B / C。", "decision_prompt": pending, "state": public_state(state)}

    outcome = select_decision_outcome(state, option, pending)
    summary = outcome.get("summary") or "选择已结算，状态稳定。"
    result_quality = outcome.get("result_quality", "safe")
    choice_icon = "🎲 奇遇选择" if pending.get("kind") == "emotional_economy" else "❓ 选择"
    result_lines: List[str] = [f"{choice_icon}：{key}｜{option.get('label')}", ""]
    story_lines = outcome.get("story_lines") or [summary]
    for line in story_lines[:3]:
        if line:
            result_lines.append(str(line))
    result_lines.append("")

    stamina_delta = int(outcome.get("stamina_delta", 0) or 0)
    if stamina_delta:
        before = state.get("stamina", 0)
        state["stamina"] = max(0, min(state.get("max_stamina", 6), before + stamina_delta))
        result_lines.append(f"🕯️ 灯火：{before} → {state['stamina']}")

    coins_delta = int(outcome.get("coins_delta", 0) or 0)
    if coins_delta:
        before = state.get("coins", 0)
        state["coins"] = max(0, before + coins_delta)
        result_lines.append(f"🪙 金币：{before} → {state['coins']}")

    journal_page = None
    journal_outcome = outcome.get("journal")
    pending_layer_id = pending.get("layer_id") or current_layer_for_state(state)["id"]
    pending_layer = get_layer(pending_layer_id)
    if journal_outcome:
        journal_page = add_journal_page(
            state,
            "decision",
            journal_outcome.get("title", pending.get("title", "轻决策记录")),
            journal_outcome.get("body", summary),
            anchors=[pending.get("anchor") or pending.get("title", "轻决策")],
            visual_mode="scene",
            truth_level="real_result",
            layer_id=pending_layer["id"],
            layer_name=pending_layer["name"],
        )
        result_lines.append(f"📜 手帐写入：{journal_page['page_id']}｜{journal_page['title']}")

    added_item = None
    collection_record = None
    item_data = outcome.get("add_item")
    if item_data:
        added_item = decision_item_entry(state, item_data, pending)
        state.setdefault("inventory", []).append(added_item)
        collection_record = record_collection_item(state, added_item, source="decision")
        result_lines.append(f"🎒 收到：{added_item['name']}｜{added_item['rarity_zh']}")
        result_lines.append("📚 藏品图鉴已记录" if collection_record.get("first_seen") else f"📚 藏品图鉴已记录｜已发现 {collection_record.get('seen_count', 1)} 次")
        if len(state.get("inventory", [])) > int(state.get("capacity", 7) or 7):
            result_lines.append("🎒 样本袋已自动整理，普通重复样本转为研究材料；新藏品不会因样本袋满而丢失。")
        if collection_record.get("collection_value_added"):
            result_lines.append(f"💰 图鉴估值 +{int(collection_record.get('collection_value_added', 0)):,}｜总计 {int(collection_record.get('dex_total_value', collection_record.get('collection_total_value', 0))):,}")
        for unlock in collection_record.get("rating_unlocks", []) or []:
            result_lines.append(f"🎖️ 探矿评级提升：{unlock.get('new', {}).get('name')}")


    catalog_item_id = outcome.get("catalog_item_id")
    if not catalog_item_id and outcome.get("reward_mode"):
        reward_layer = get_layer(pending.get("layer_id") or current_layer_for_state(state)["id"])
        grant = grant_emotional_catalog_item(state, reward_layer, mode=outcome.get("reward_mode"), source="emotional_choice")
        if grant.get("enabled"):
            added_item = grant["entry"]
            collection_record = grant["collection_record"]
            result_lines.append(f"🎒 收到：{added_item['name']}｜{added_item['rarity_zh']}")
            result_lines.append("📚 藏品图鉴已记录" if collection_record.get("first_seen") else f"📚 藏品图鉴已记录｜已发现 {collection_record.get('seen_count', 1)} 次")
            if collection_record.get("collection_value_added"):
                result_lines.append(f"💰 图鉴估值 +{int(collection_record.get('collection_value_added', 0)):,}｜总计 {int(collection_record.get('dex_total_value', collection_record.get('collection_total_value', 0))):,}")
    elif catalog_item_id:
        by_id = {it.get("id"): it for it in ITEMS}
        item = by_id.get(catalog_item_id)
        if item:
            reward_layer = get_layer(pending.get("layer_id") or current_layer_for_state(state)["id"])
            entry = item_entry(dict(item), state, reward_layer)
            state.setdefault("inventory", []).append(entry)
            collection_record = record_collection_item(state, entry, source="emotional_choice")
            added_item = entry
            result_lines.append(f"🎒 收到：{entry['name']}｜{entry['rarity_zh']}")
            result_lines.append("📚 藏品图鉴已记录" if collection_record.get("first_seen") else f"📚 藏品图鉴已记录｜已发现 {collection_record.get('seen_count', 1)} 次")
            if collection_record.get("collection_value_added"):
                result_lines.append(f"💰 图鉴估值 +{int(collection_record.get('collection_value_added', 0)):,}｜总计 {int(collection_record.get('dex_total_value', collection_record.get('collection_total_value', 0))):,}")
    heat_outcome = outcome.get("start_heat")
    if heat_outcome:
        heat_row = start_emotional_heat(
            state,
            heat_outcome.get("id", "greedy_echo"),
            heat_outcome.get("name", "短期追光"),
            heat_outcome.get("line", "接下来几镐，小机会更想追有回光的地方。"),
            remaining=int(heat_outcome.get("remaining", 3) or 3),
        )
        result_lines.append(f"✨ {heat_row['heat']['name']}：还剩 {heat_row['heat']['remaining']} 段")

    if outcome.get("map_mark") and not journal_page:
        journal_page = add_journal_page(
            state,
            "decision_mark",
            f"标记：{pending.get('title')}",
            f"位置已标记：{pending.get('map_target') or pending.get('anchor')}。这是轻量记录，不改变地图系统。",
            anchors=[pending.get("map_target") or pending.get("anchor") or pending.get("title", "轻决策")],
            visual_mode="scene",
            truth_level="real_result",
            layer_id=pending_layer["id"],
            layer_name=pending_layer["name"],
        )
        result_lines.append(f"📜 手帐写入：{journal_page['page_id']}｜标记位置")

    synthetic_event = {"real_result": {"category": (added_item or {}).get("category"), "name": (added_item or {}).get("name", pending.get("title", "轻决策"))}}
    title_unlocks = evaluate_titles(state, synthetic_event) if added_item else []
    for t in title_unlocks:
        result_lines.append(f"🎖️ 新增称号：{t.get('name')}")

    if result_quality == "bad":
        state["decision_bad_streak"] = int(state.get("decision_bad_streak", 0) or 0) + 1
    elif key == "B":
        state["decision_bad_streak"] = 0

    history_row = {
        "id": pending.get("id"),
        "choice": key,
        "label": option.get("label"),
        "summary": summary,
        "result_quality": result_quality,
        "bad_luck_protection_applied": outcome.get("bad_luck_protection_applied", False),
        "turn": state.get("turn", 0),
        "time": now_iso(),
    }
    # Keep template_id internally for tests, but frontstage_render_plan forbids showing it to players.
    history_row["template_id"] = pending.get("template_id")
    state.setdefault("decision_history", []).append(history_row)
    state["decision_history"] = state["decision_history"][-30:]
    state["pending_decision"] = None

    result_panel = {
        "enabled": True,
        "type": "result_panel",
        "card_text": "\n".join(result_lines),
        "story_lines": story_lines,
        "result_quality": result_quality,
        "truth_level": "real_result",
        "frontstage_note": "decision_prompt 的一次性轻结算；先讲发生了什么，再讲资源/图鉴/手帐变化。",
    }
    public_history = dict(history_row)
    public_history.pop("template_id", None)
    result = {
        "ok": True,
        "action": "choose",
        "choice": key,
        "decision_result": public_history,
        "result_panel": result_panel,
        "collection_panel": render_collection_panel(state, collection_record) if collection_record else {"enabled": False},
        "mining_rating": mining_rating_progress(state),
        "mining_drive": mining_drive_for_state(state),
        "area_preview": pacing_area_tease_for_state(state) or {"enabled": False},
        "map_strip": render_map_strip(state, pending.get("layer_id"), target=pending.get("map_target"), reason="decision_resolved"),
        "status_panel": render_status_panel(state),
        "title_unlocks": title_unlocks,
        "next_recommended_commands": ["cmd('dig')", "cmd('play 3')", "cmd('return')" if state.get("stamina", 0) <= 1 else "cmd('map')"],
        "state": public_state(state),
    }
    result["frontstage_render_plan"] = frontstage_render_plan_for(result)
    return result


def previous_result_count(state: Dict[str, Any], name: str, result_type: Optional[str] = None) -> int:
    count = 0
    for row in state.get("log", []):
        if row.get("result_name") == name and (result_type is None or row.get("result_type") == result_type):
            count += 1
    return count


def compact_repeat_info(name: str, kind: str, seen_count: int) -> Optional[Dict[str, Any]]:
    """Return public compression hints for repeated content.

    seen_count is the count before this result. Therefore seen_count >= 2 means
    the current result is at least the 3rd occurrence and should not be named as a
    fresh report unless it completes a set/research/area target.
    """
    if seen_count <= 0:
        return None
    strong = seen_count >= 2
    hard = seen_count >= 9
    stage = "area_or_research_only" if hard else "summary_only" if strong else "duplicate_sample"
    if kind == "trace":
        line = f"同类迹象持续出现：{name}。我把它并入线索进度，不重复展开。" if strong else f"同类迹象又出现了：{name}。我先不重复展开，它更像是在持续指向同一个方向。"
        return {
            "is_repeat": True,
            "seen_before": seen_count,
            "repeat_stage": stage,
            "frontstage_suppression": strong,
            "hard_suppression_after_ten": hard,
            "report_hint": f"{name} 已重复；第 3 次后只进汇总/线索/区域目标，第 10 次后禁止抢主报告。",
            "suggested_line": line,
        }
    if kind == "item":
        occurrence = max(2, seen_count + 1)
        line = (
            f"这是第 {occurrence} 次带回{name}。小机没有再当大新闻讲，只把它整理成研究/区域目标样本。"
            if strong else
            f"又见到{name}。不是新藏品，小机把它并到同一页记录里。"
        )
        return {
            "is_repeat": True,
            "seen_before": seen_count,
            "occurrence": occurrence,
            "repeat_stage": stage,
            "frontstage_suppression": strong,
            "hard_suppression_after_ten": hard,
            "report_hint": f"{name} 是重复样本；第 {occurrence} 次出现时只能服务汇总/研究/区域目标，不得写成新图鉴记录。",
            "suggested_line": line,
            "rc_rule": "first_seen=false 时必须写成重复样本/同类样本/第 N 次，不得写成新发现或新图鉴记录。",
        }
    if kind == "landmark":
        return {
            "is_repeat": True,
            "seen_before": seen_count,
            "repeat_stage": stage,
            "frontstage_suppression": strong,
            "hard_suppression_after_ten": hard,
            "report_hint": f"{name} 主题重复；只作为路过/地图确认/区域进度，不再当全新地标。",
            "suggested_line": f"又经过{name}相关地点；我只把它记作地图再确认，不写成长篇地标战报。",
        }
    if kind == "small_find":
        line = f"{name} 这类小味道又出现了，我并入本段汇总。" if strong else f"{name} 又出现了一次。我先不重复展开，只把它当成矿洞持续的小味道。"
        return {
            "is_repeat": True,
            "seen_before": seen_count,
            "repeat_stage": stage,
            "frontstage_suppression": strong,
            "hard_suppression_after_ten": hard,
            "report_hint": f"{name} 是重复小发现；第 3 次后只进本段汇总。",
            "suggested_line": line,
        }
    return None


def repeat_info_from_collection_record(name: str, collection_record: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Build repeat display from lifetime collection_seen_counts, never from trimmed logs."""
    if collection_record.get("first_seen"):
        return None
    seen_count = int(collection_record.get("seen_count", 1) or 1)
    repeat = compact_repeat_info(name, "item", max(1, seen_count - 1))
    if repeat:
        repeat["occurrence"] = seen_count
        repeat["seen_before"] = max(1, seen_count - 1)
        repeat["lifetime_seen_count_source"] = "collection_seen_counts"
    return repeat


def landmark_display_name(landmark: Dict[str, Any], layer_id: str) -> str:
    return LANDMARK_NAME_VARIANTS.get((landmark.get("id"), layer_id), landmark.get("name", "未命名地标"))


def add_reality_anchors(queries: List[str], visual_mode: str, real_anchors: List[str]) -> List[str]:
    """Keep web-image search grounded without forcing concrete keyword lists into content."""
    result: List[str] = []
    for q in queries:
        if q and q not in result:
            result.append(q)
    haystack = " ".join(result).lower()
    for anchor in REALITY_ANCHORS_BY_MODE.get(visual_mode, []):
        if anchor.lower() not in haystack and len(result) < 5:
            result.append(anchor)
            haystack += " " + anchor.lower()
    # For story images, make sure at least one actual anchor name is represented in text.
    if visual_mode == "story" and real_anchors and len(result) < 5:
        first_anchor = str(real_anchors[0])
        if first_anchor and first_anchor.lower() not in haystack:
            result.append(first_anchor)
    return result[:5]


def typed_pending_tasks_for(tasks: List[str]) -> Dict[str, List[str]]:
    command_required: List[str] = []
    report_required: List[str] = []
    other: List[str] = []
    for task in tasks:
        if task in COMMAND_REQUIRED_TASKS:
            command_required.append(task)
        elif task in REPORT_REQUIRED_TASKS:
            report_required.append(task)
        else:
            other.append(task)
    return {
        "command_required": list(dict.fromkeys(command_required)),
        "report_required": list(dict.fromkeys(report_required)),
        "other": list(dict.fromkeys(other)),
        "usage_note": "legacy pending_tasks is kept for compatibility; tests should use typed_pending_tasks.",
    }


def story_set_completed_now(state: Dict[str, Any], set_id: Optional[str]) -> bool:
    if not set_id:
        return False
    if not story_progress(state).get(set_id, {}).get("complete", False):
        return False
    logged = state.setdefault("story_sets_completed_logged", [])
    if set_id in logged:
        return False
    logged.append(set_id)
    return True


def make_visual_queries(layer: Dict[str, Any], extra: Optional[List[str]] = None) -> List[str]:
    queries: List[str] = []
    for kw in (extra or [])[:3]:
        if kw not in queries:
            queries.append(kw)
    for kw in layer.get("visual_keywords", [])[:2]:
        if kw not in queries:
            queries.append(kw)
    return queries[:5]


def visual_priority_for(kind: str, rarity: Optional[str] = None, new_layer: bool = False, story_complete: bool = False) -> str:
    if new_layer or story_complete:
        return "high"
    if kind == "landmark":
        return "high"
    if kind == "story":
        return "high"
    if rarity in {"epic", "legendary"}:
        return "high"
    if rarity == "rare":
        return "medium"
    if kind in {"trace", "hazard"}:
        return "medium"
    if rarity == "uncommon":
        return "medium"
    return "low"


def build_main_shot(
    *,
    title: str,
    visual_mode: str,
    visual_priority: str,
    truth_level: str,
    real_anchors: List[str],
    caption_seed: str,
    visual_queries: List[str],
    truth_note: Optional[str] = None,
) -> Dict[str, Any]:
    grounded_queries = add_reality_anchors(visual_queries, visual_mode, real_anchors)
    return {
        "title": title,
        "visual_mode": visual_mode,
        "visual_priority": visual_priority,
        "truth_level": truth_level,
        "real_anchors": real_anchors,
        "caption_seed": caption_seed,
        "visual_queries": grounded_queries,
        "truth_note": truth_note or truth_note_for(truth_level),
        "visual_query_note": "v0.2.4 会为 fantasy/story 节点补 cave/artifact/crystal 等现实锚点；后台词服务搜图，前台不要直接念协议名。",
    }





def _visible_len(text: str) -> int:
    # Not a full wcwidth implementation; enough for compact internal cards.
    # Emoji/CJK widths vary by platform, so cards are a presentation hint, not pixel-perfect UI.
    return len(text)


def box_card(title: str, body_lines: List[str], footer: Optional[str] = None, width: int = 46) -> str:
    top = "+" + "-" * width + "+"
    lines = [top]
    title_line = f"[ {title} ]"
    lines.append("|  " + title_line)
    lines.append("|")
    for line in body_lines:
        lines.append("|  " + line)
    if footer:
        lines.append("|")
        lines.append("|  " + footer)
    lines.append(top)
    return "\n".join(lines)


def layer_card_title(layer_id: str) -> str:
    return LAYER_CARD_TITLES.get(layer_id, get_layer(layer_id).get("name", layer_id))


def _mark(label: str, current_name: Optional[str], aliases: Optional[List[str]] = None) -> str:
    aliases = aliases or []
    if current_name and (current_name == label or current_name in aliases or label in current_name):
        return f"{label} 📍"
    return label


def render_region_map(layer_id: str, current_name: Optional[str] = None, page_id: Optional[str] = None) -> Dict[str, Any]:
    """Return a lightweight local region map. Not a true coordinate system."""
    layer = get_layer(layer_id)
    title = f"🗺️ 区域地图｜{layer['name']}"
    footer = f"📍 当前：{current_name}" if current_name else f"当前：{layer['name']}"
    if page_id:
        footer += f"｜📜 已写入探险手帐 {page_id}"

    if layer_id == "shallow_mine":
        body = [
            f"入口 ─── 木撑架主道 ─── 🏕️ {_mark('旧矿工营地', current_name)}",
            "             │",
            "          🪨 化石侧廊 ❓",
        ]
    elif layer_id == "underground_river":
        body = [
            f"入口 ─── 🌊 {_mark('蓝光水潭', current_name, ['晶洞蓝水潭'])}",
            "             │",
            "          🪨 半淹没石门 ❓",
            "             │",
            "          旧木桥残影",
        ]
    elif layer_id == "glowing_crystal_cave":
        body = [
            f"入口 ─── ✦ {_mark('晶洞门槛', current_name)}",
            "             │",
            "          💎 冷蓝晶簇",
            "             │",
            "          镜面矿壁 ❓",
        ]
    elif layer_id == "mushroom_cavern":
        body = [
            "孢子坡道 ─── 🍄 菌丝桥 ❓",
            "                 │",
            f"              {_mark('孢子灯海', current_name)}",
            "                 │",
            "              旧篮筐角落 ❓",
        ]
    elif layer_id == "abandoned_lift":
        body = [
            "上层平台",
            "   │",
            f"升降井井壁 ─── 🏕️ {_mark('升降井休息点', current_name, ['旧矿工营地'])}",
            "   │",
            "下层平台 ─── 锈链悬点 ❓",
        ]
    elif layer_id == "ancient_ruins":
        body = [
            "石阶入口 ─── 🪨 断裂石门 ❓",
            "                 │",
            "              📜 符文廊道",
            "                 │",
            f"              {_mark('无声祭坛', current_name)}",
        ]
    elif layer_id == "ice_vein":
        body = [
            "冰裂入口 ─── 🪨 冻气泡墙",
            "                 │",
            "              化石冰窗 ❓",
            "                 │",
            f"              {_mark('旧矿工营地遗址', current_name)}",
        ]
    elif layer_id == "deep_altar":
        body = [
            "黑石阶梯",
            "   │",
            f"🪨 {_mark('无声祭坛', current_name)} ─── 石门眼纹 ❓",
            "   │",
            "深处仍未探明 ❓",
        ]
    else:
        body = [
            f"入口 ─── {_mark(layer['name'], current_name)}",
            "          │",
            "       未探明支路 ❓",
        ]

    return {
        "enabled": True,
        "type": "region_map",
        "region_id": layer_id,
        "title": layer["name"],
        "current_node": current_name or layer["name"],
        "style": "ascii_region_map_with_light_emoji",
        "card_text": box_card(title, body, footer),
        "legend": MAP_EMOJI_LEGEND,
        "icon_semantics": ICON_SEMANTICS,
        "map_scope": "region_map_only_v0218",
        "next_unknown_target": nearest_unknown_landmark_for_layer(layer_id),
        "scene_visual_profile": scene_visual_profile_for_layer(layer_id),
        "scene_reference_required_when": ["首次进入新区域", "首次出现新地标", "区域目标点亮", "环境型高光"],
        "map_next_step_hint": map_next_step_hint(load_state() if os.path.exists(SAVE_FILE) else new_state(), layer_id),
        "frontstage_note": "这是当前区域局部图，不是完整地下总览；它只说明我们现在在哪、附近有哪些已发现点、哪里还有 ❓ 没看过。场景 reference 讲气质，不替代藏品图。",
        "usage_note": "region_map 是当前地层的小结构图，讲‘我在哪’，不是完整迷宫、路线系统或完整 world_map。",
    }


def _event_journal_page_id(event: Dict[str, Any]) -> Optional[str]:
    rr = event.get("real_result", {})
    if rr.get("journal_page_id"):
        return rr.get("journal_page_id")
    jw = event.get("journal_write")
    if isinstance(jw, list) and jw:
        return jw[-1].get("page_id")
    if isinstance(jw, dict):
        return jw.get("page_id")
    return None


def build_milestone_card(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    rr = event.get("real_result", {})
    layer_id = event.get("layer", {}).get("id") or current_layer(state.get("depth_m", 0))["id"]
    page_id = _event_journal_page_id(event)

    card_type = None
    title = None
    subtitle = None
    body: List[str] = []

    if event.get("new_layer_discovered"):
        card_type = "new_layer"
        title = "🗺️ " + layer_card_title(layer_id)
        subtitle = f"📜 {rr.get('name', get_layer(layer_id)['name'])}已写入探险手帐 {page_id}" if page_id else "✨ 新区域已点亮"
        scene_profile = scene_visual_profile_for_layer(layer_id)
        body = [
            f"{get_layer(layer_id)['arrival_caption']}",
            f"🖼️ 场景锚点：{scene_profile.get('screenshot_anchor')}",
            "",
            f"📍 当前：{get_layer(layer_id)['name']} / {rr.get('name', get_layer(layer_id)['name'])}",
        ]
    elif rr.get("type") == "landmark" and rr.get("journal_written"):
        card_type = "new_landmark"
        title = f"🗺️ 地点发现｜{rr.get('name')}"
        subtitle = f"📜 已写入探险手帐 {page_id}" if page_id else "✨ 已记录新地点"
        body = [
            f"区域：{get_layer(layer_id)['name']}",
            f"📍 当前：{rr.get('name')}",
        ]
    elif rr.get("story_set_complete"):
        card_type = "story_set_complete"
        title = f"📜 故事拼合｜{rr.get('set_name') or '故事套装'}"
        subtitle = "套装进度完成，进入叙事复原"
        body = [
            "📜 已收集的碎片开始互相指向。",
            "注意：这是基于真实锚点的叙事复原，不是新增事实。",
        ]
    elif event.get("title_unlocks"):
        # Only use a title card when no stronger regional milestone exists.
        t = event["title_unlocks"][0]
        card_type = "title_unlock"
        title = f"🎖️ 新称号｜{t.get('name')}"
        subtitle = t.get("tone") or t.get("reason") or "新的身份感节点已记录"
        body = [
            "✨ 这不是属性加成，也不是等级。",
            "它只是我们和地下世界之间多了一种称呼。",
        ]

    if not card_type:
        return {"enabled": False, "usage_note": "普通发现不出里程碑牌。"}

    footer = subtitle
    card_family = "space" if card_type in {"new_layer", "new_landmark"} else "identity" if card_type == "title_unlock" else "story"
    presentation_type = (
        "milestone_card_space" if card_family == "space" else
        "milestone_card_title" if card_family == "identity" else
        "milestone_card_story"
    )
    usage_note = (
        "空间牌：强调我们到了哪里 / 地图点亮了哪里；它不替代网图、不替代战报、不替代真实写入说明。"
        if card_family == "space" else
        "称号牌：强调这次经历给了我们什么身份；它不是 region_map，也不是空间推进。"
        if card_family == "identity" else
        "故事牌：强调套装阶段变化；必须遵守 truth_level，不能把叙事复原当事实。"
    )
    return {
        "enabled": True,
        "type": card_type,
        "card_family": card_family,
        "presentation_type": presentation_type,
        "title": title,
        "subtitle": subtitle,
        "style": "ascii_milestone_card_with_light_emoji",
        "current": f"{get_layer(layer_id)['name']} / {rr.get('name', get_layer(layer_id)['name'])}",
        "truth_level": "real_result" if card_type != "story_set_complete" else "imagined_reconstruction",
        "real_anchors": [a for a in [get_layer(layer_id)["name"], rr.get("name"), page_id] if a],
        "card_text": box_card(title or "里程碑", body, footer),
        "usage_note": usage_note,
    }


def build_region_map_card(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    rr = event.get("real_result", {})
    layer_id = event.get("layer", {}).get("id") or current_layer(state.get("depth_m", 0))["id"]
    page_id = _event_journal_page_id(event)
    # v0.2.8: region_map is a little more common than milestone_card, but still not for every small find.
    if event.get("new_layer_discovered"):
        return render_region_map(layer_id, rr.get("name") or get_layer(layer_id)["name"], page_id)
    if rr.get("type") == "landmark" and (rr.get("journal_written") or rr.get("name")):
        if rr.get("journal_written"):
            return render_region_map(layer_id, rr.get("name"), page_id)
    return {"enabled": False, "usage_note": "普通小发现/重复迹象不出局部地图。"}


def scene_web_reference_for_event(event: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    rr = event.get("real_result", {})
    layer_id = event.get("layer", {}).get("id")
    if not layer_id:
        return None
    profile = scene_visual_profile_for_layer(layer_id)
    reasons: List[str] = []
    if event.get("new_layer_discovered"):
        reasons.append("area_first_seen")
    if rr.get("type") == "landmark" and rr.get("journal_written"):
        reasons.append("landmark_first_seen")
    if (event.get("clue_track_progress") or {}).get("completed"):
        reasons.append("area_target_lit")
    shot = event.get("main_shot") or {}
    if shot.get("visual_mode") == "scene" and shot.get("visual_priority") in {"medium", "high"} and (event.get("episode_candidate") or {}).get("is_episode_candidate"):
        reasons.append("environment_highlight")
    if not reasons:
        return None
    keywords = list(profile.get("image_search_keywords") or [])
    if not keywords:
        keywords = list(get_layer(layer_id).get("visual_keywords", []))
    return {
        "required": True,
        "type": "scene_web_reference",
        "reasons": list(dict.fromkeys(reasons)),
        "must_attempt_scene_reference": True,
        "preferred": "web_reference_multi_image",
        "target_count": 4,
        "acceptable_minimum": 1,
        "image_direction": profile.get("image_direction") or profile.get("visual_identity") or get_layer(layer_id).get("visual_tone"),
        "image_search_keywords": keywords,
        "avoid_keywords": profile.get("avoid_keywords", []),
        "visual_identity": profile.get("visual_identity"),
        "screenshot_anchor": profile.get("screenshot_anchor"),
        "fallback_behavior": "如果搜不到完全贴合的图，也必须给出搜索关键词、参考方向和可接受的气质替代；不能只写跳过配图。",
        "truth_note": "场景图是气质参考，不是游戏截图、不是官方设定、也不是新增事实。",
    }


def presentation_stack_for(event: Dict[str, Any]) -> List[str]:
    stack: List[str] = []
    if event.get("milestone_card", {}).get("enabled"):
        stack.append("milestone_card")
    if event.get("region_map", {}).get("enabled"):
        stack.append("region_map")
    if (event.get("scene_web_reference") or {}).get("required"):
        stack.append("scene_web_reference")
    stack.append("web_reference_or_keywords")
    stack.append("battle_report_body")
    stack.append("truth_boundary_and_next_choice")
    return stack


def select_presentation_cards(events: List[Dict[str, Any]], episode_shot: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if episode_shot and episode_shot.get("source_event_id"):
        source_id = episode_shot.get("source_event_id")
        for e in events:
            if e.get("event_id") == source_id:
                return {
                    "milestone_card": e.get("milestone_card", {"enabled": False}),
                    "region_map": e.get("region_map", {"enabled": False}),
                    "scene_web_reference": e.get("scene_web_reference"),
                    "presentation_stack": e.get("presentation_stack", presentation_stack_for(e)),
                }
    for e in events:
        if e.get("milestone_card", {}).get("enabled") or e.get("region_map", {}).get("enabled"):
            return {
                "milestone_card": e.get("milestone_card", {"enabled": False}),
                "region_map": e.get("region_map", {"enabled": False}),
                "scene_web_reference": e.get("scene_web_reference"),
                "presentation_stack": e.get("presentation_stack", presentation_stack_for(e)),
            }
    return {"milestone_card": {"enabled": False}, "region_map": {"enabled": False}, "scene_web_reference": None, "presentation_stack": []}



def frontstage_required_blocks_for(
    presentation_cards: Dict[str, Any],
    episode_shot: Optional[Dict[str, Any]],
    safety_template: Optional[Dict[str, Any]] = None,
    *,
    stopped_by: Optional[str] = None,
    map_strip: Optional[Dict[str, Any]] = None,
    decision_prompt: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """v0.2.13: copy-paste blocks that frontstage AI must not omit.

    Internal contract stays strict; frontstage wording should stay soft and playful.
    """
    blocks: List[Dict[str, Any]] = []
    order = 1
    milestone = presentation_cards.get("milestone_card") or {}
    if milestone.get("enabled") and milestone.get("card_text"):
        blocks.append({
            "order": order,
            "kind": "milestone_card",
            "required": True,
            "must_paste_card_text": True,
            "title": milestone.get("title") or "里程碑牌",
            "card_text": milestone.get("card_text"),
            "omission_warning": "不能只写‘出现了区域牌/里程碑牌’；必须把 card_text 原样贴在战报开头。",
        })
        order += 1
    region = presentation_cards.get("region_map") or {}
    if region.get("enabled") and region.get("card_text"):
        blocks.append({
            "order": order,
            "kind": "region_map",
            "required": True,
            "must_paste_card_text": True,
            "title": region.get("title") or "区域地图",
            "card_text": region.get("card_text"),
            "frontstage_note": region.get("frontstage_note"),
            "omission_warning": "region_map 是本轮空间结构交付；摘要里提到它不算完成，必须贴出局部图。",
        })
        order += 1
    if map_strip and map_strip.get("enabled") and map_strip.get("card_text"):
        blocks.append({
            "order": order,
            "kind": "map_strip",
            "required": True,
            "must_paste_card_text": True,
            "title": "地图提示",
            "card_text": map_strip.get("card_text"),
            "frontstage_note": map_strip.get("frontstage_note"),
            "omission_warning": "没有完整 region_map 但提到了 ❓ / 返程 / 下一步目标时，必须展示 map_strip。",
        })
        order += 1
    scene_ref = presentation_cards.get("scene_web_reference") or {}
    if scene_ref.get("required"):
        blocks.append({
            "order": order,
            "kind": "scene_web_reference",
            "required": True,
            "must_attempt_scene_reference": True,
            "preferred": scene_ref.get("preferred") or "web_reference_multi_image",
            "target_count": scene_ref.get("target_count", 4),
            "acceptable_minimum": scene_ref.get("acceptable_minimum", 1),
            "reasons": scene_ref.get("reasons", []),
            "image_direction": scene_ref.get("image_direction"),
            "search_keywords": scene_ref.get("image_search_keywords", []),
            "avoid_keywords": scene_ref.get("avoid_keywords", []),
            "fallback_behavior": scene_ref.get("fallback_behavior"),
            "truth_note": scene_ref.get("truth_note"),
            "omission_warning": "首次区域/地标/环境高光必须优先尝试现实/气质网图；不能只给关键词或生图 prompt 替代。",
        })
        order += 1
    if episode_shot:
        vd = episode_shot.get("visual_delivery") or visual_delivery_for(episode_shot, is_episode=True)
        if vd.get("requires_reference_when_reported"):
            blocks.append({
                "order": order,
                "kind": "web_reference",
                "required": True,
                "must_attempt_web_reference": True,
                "preferred": "web_reference_multi_image",
                "target_count": vd.get("reference_count", {}).get("target", 4),
                "acceptable_minimum": vd.get("reference_count", {}).get("acceptable_minimum", 1),
                "search_keywords": vd.get("search_keywords") or episode_shot.get("visual_queries", []),
                "fallback_only_if": "当前环境无法拉图 / 搜索工具不可用 / 搜索结果明显不准",
                "omission_warning": "medium/high episode_shot 不能只贴关键词；支持网图时必须实际给现实/气质参考图。",
            })
            order += 1
    if decision_prompt and decision_prompt.get("enabled"):
        blocks.append({
            "order": order,
            "kind": "decision_prompt",
            "required": True,
            "must_paste_card_text": True,
            "must_offer_choose_commands": True,
            "title": decision_prompt.get("title") or "轻决策",
            "card_text": decision_prompt.get("card_text"),
            "options": decision_prompt.get("options", []),
            "omission_warning": "decision_prompt 必须能 choose 一下；不能只当装饰提示。",
        })
        order += 1
    if safety_template and stopped_by == "danger_low_light" and not episode_shot:
        blocks.append({
            "order": order,
            "kind": "safety_stop_short_template",
            "required": True,
            "must_use_short_template": True,
            "template": safety_template,
            "omission_warning": "danger_low_light 没有 episode_shot；使用短模板，不硬凑主画面、不配图。",
        })
    return blocks


def frontstage_delivery_checklist_for(
    presentation_cards: Dict[str, Any],
    episode_shot: Optional[Dict[str, Any]],
    safety_template: Optional[Dict[str, Any]] = None,
    *,
    stopped_by: Optional[str] = None,
    map_strip: Optional[Dict[str, Any]] = None,
    decision_prompt: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """v0.2.13: preflight checklist for human-facing battle reports.

    Internal checklist is strict, but should not be read aloud as an audit report.
    """
    milestone = presentation_cards.get("milestone_card") or {}
    region = presentation_cards.get("region_map") or {}
    scene_ref = presentation_cards.get("scene_web_reference") or {}
    visual_delivery = visual_delivery_for(episode_shot, is_episode=bool(episode_shot)) if episode_shot else {}
    has_map = bool(
        (milestone.get("enabled") and milestone.get("card_text"))
        or (region.get("enabled") and region.get("card_text"))
        or (map_strip and map_strip.get("enabled") and map_strip.get("card_text"))
    )
    needs_web = bool(visual_delivery.get("requires_reference_when_reported") or scene_ref.get("required"))
    has_decision = bool(decision_prompt and decision_prompt.get("enabled"))
    return [
        {
            "order": 1,
            "name": "主画面",
            "must_check": True,
            "required_now": bool(episode_shot),
            "rule": "是否有 episode_shot / main_shot；正式战报必须围绕它组织。若没有 episode_shot 且是 danger_low_light，只用短模板，不硬凑画面。",
        },
        {
            "order": 2,
            "name": "地图 / 区域牌 / 地图提示",
            "must_check": True,
            "required_now": has_map,
            "rule": "检查 milestone_card / region_map / map_strip。若有 card_text，必须原样贴出；map_strip 是轻量位置锚点，不替代 region_map。",
        },
        {
            "order": 3,
            "name": "网图参考",
            "must_check": True,
            "required_now": needs_web,
            "rule": "如果 visual_delivery=image_required、medium/high episode_shot，或 scene_web_reference.required=true，必须优先实际给网图/现实参考/气质参考；不能只给关键词，不能用生图 prompt 替代。",
        },
        {
            "order": 4,
            "name": "视觉翻译",
            "must_check": True,
            "required_now": bool(episode_shot),
            "rule": "高光发现如果让 AI 玩家觉得很美/很怪/很震，不能只说稀有或漂亮；至少提取 3 类可视锚点（颜色、光感、结构、材质、体量、环境），并转成找图方向。",
        },
        {
            "order": 5,
            "name": "真实结果",
            "must_check": True,
            "required_now": True,
            "rule": "说明本轮真实发生了什么：发现、图鉴收录、手帐写入、称号、风险、回地面、普通收益、选择结算或安全停。",
        },
        {
            "order": 6,
            "name": "事实边界",
            "must_check": True,
            "required_now": bool(episode_shot) or has_decision,
            "rule": "区分 real_result / inferred_mood / imagined_reconstruction；图片、地图、氛围 cue 和叙事想象不能被说成新增事实。",
        },
        {
            "order": 7,
            "name": "图鉴/手帐写入",
            "must_check": True,
            "required_now": True,
            "rule": "检查 collection_record / display_status / journal_write / save_confirmation_card。只有真实写入成功后，才能说已收录、已保存、已写入手帐；display_status.displayed=false 时不能说已陈列。",
        },
        {
            "order": 8,
            "name": "轻决策",
            "must_check": True,
            "required_now": has_decision,
            "rule": "如果 decision_prompt.enabled=true，必须展示选项并允许 cmd('choose A/B/C') 一次性结算；不做剧情树。",
        },
        {
            "order": 9,
            "name": "下一步建议",
            "must_check": True,
            "required_now": True,
            "rule": "结合当前状态和 region_map / map_strip 上的 ❓ / 未探明点：灯火不足先 return；状态充足可建议探索最近未知点。",
        },
    ]


def frontstage_contract_for(
    presentation_cards: Dict[str, Any],
    episode_shot: Optional[Dict[str, Any]],
    safety_template: Optional[Dict[str, Any]] = None,
    *,
    stopped_by: Optional[str] = None,
    map_strip: Optional[Dict[str, Any]] = None,
    decision_prompt: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    blocks = frontstage_required_blocks_for(
        presentation_cards,
        episode_shot,
        safety_template,
        stopped_by=stopped_by,
        map_strip=map_strip,
        decision_prompt=decision_prompt,
    )
    checklist = frontstage_delivery_checklist_for(
        presentation_cards,
        episode_shot,
        safety_template,
        stopped_by=stopped_by,
        map_strip=map_strip,
        decision_prompt=decision_prompt,
    )
    required_kinds = [b["kind"] for b in blocks if b.get("required")]
    return {
        "enabled": True,
        "purpose": "正式战报前逐项自检交付物；内部硬检查，前台软表达。重点统一整体藏品图鉴、场景网图参考和旧 display 兼容口径。",
        "icon_semantics": ICON_SEMANTICS,
        "must_show_in_order": required_kinds,
        "required_blocks": blocks,
        "delivery_checklist": checklist,
        "must_run_delivery_checklist_before_report": True,
        "omission_is_failure": bool(required_kinds),
        "frontstage_softening": {
            "do_not_say": ["我检查了交付项", "以下是验收清单", "Checklist 通过"],
            "say_instead": [
                "我先把这次值得看的东西带回来。",
                "这一段不是逐镐日志，我只展开最值得看的主画面。",
                "这里我想问你一下，要不要碰它？",
            ],
        },
        "card_text_rule": "如果 milestone_card / region_map / map_strip / decision_prompt 出现在 required_blocks，必须原样展示 card_text。",
        "map_strip_rule": "完整 region_map 不宜每轮贴；没有 region_map 但有下一步 ❓、低灯返程、return 建议或重要当前位置变化时，必须展示 map_strip。",
        "visual_rule": "地图牌不能替代网图；medium/high episode_shot 支持联网时必须实际拉网图/气质图，关键词只是兜底。",
        "visual_translation_rule": "高光发现必须把 AI 的文字感受翻译成可见锚点：主色、光感、结构、材质、体量、环境至少 3 类；不要用稀有度标签替代高级感。",
        "aesthetic_mining_rule": "矿洞审美是轻奇幻地下收藏，不是硬核矿工模拟；漂亮、神秘、可收藏、可配图优先。",
        "decision_rule": "decision_prompt 必须能 choose 一下；choose 后立刻一次性轻结算，不开启路线分支、剧情树、永久损失或复杂 flag。",
        "truth_and_save_rule": "真实结果、truth_level、collection_record、display_status、journal_write 和 save_confirmation_card 必须说清；没写入不能说已保存/已收录。",
        "failure_conditions": [
            "返回了 milestone_card / region_map / map_strip 但未展示 card_text",
            "medium/high episode_shot 要求 web_reference 但前台只给关键词且未说明工具不可用/搜索失败",
            "collection_record / journal 已写入但前台未说明真实保存状态",
            "把 inferred_mood 或 imagined_reconstruction 写成 real_result",
            "返回 decision_prompt 但没有提供 choose A/B/C 的结算入口",
            "高光发现只写‘很美/史诗/价值高’，没有提取颜色、光感、结构、材质、体量或环境等视觉锚点",
        ],
        "frontstage_order": "区域牌/局部地图/map_strip（如有） → 网图参考（如需） → 今日主画面或轻决策 → narrator_cue（短句） → 真实结果与边界 → 图鉴/手帐/称号状态 → 下一步建议。",
        "narrator_cue_rule": "narrator_cue 是 frontstage mood layer，不是新增事实；每段最多一条强提示，只辅助节奏/气氛/决策。",
    }


def visual_delivery_for(shot: Optional[Dict[str, Any]], *, is_episode: bool = False) -> Dict[str, Any]:
    """v0.2.6+: visual delivery is web-reference first; keywords are fallback; generation is not default."""
    shot = shot or {}
    priority = shot.get("visual_priority", "low")
    requires_reference = bool(is_episode and priority in {"medium", "high"})
    target_count = 4 if requires_reference else 0
    return {
        "preferred": "web_reference",
        "fallback": "search_keywords_only_when_web_unavailable_or_results_poor",
        "generated_image": "not_default_only_on_explicit_user_request",
        "auto_generate_image": False,
        "requires_reference_when_reported": requires_reference,
        "must_attempt_web_reference": requires_reference,
        "reference_count": {
            "target": target_count,
            "acceptable_minimum": 1 if requires_reference else 0,
            "note": "目标是像钓鱼二改那样给多张现实/气质参考图；4 张是体验目标，不是硬卡数量，按平台 UI 能力调整。",
        },
        "reference_quality_goal": "mood_match_over_exact_match",
        "visual_translation_rule": VISUAL_TRANSLATION_RULE,
        "aesthetic_mining_rule": AESTHETIC_MINING_RULE,
        "image_truth_note": "参考图只承载 episode_shot 的气质，不是游戏截图、不是官方设定、也不是新增事实。",
        "main_shot_design_standard": "合格的 episode_shot / main_shot 应能被 1-3 个现实/气质网图关键词接住。若长期接不住，应回修命名、real_anchors、visual_keywords、caption_seed 或内容本身。",
        "do_not_rescue_bad_node_with_generation": True,
        "search_keywords": shot.get("visual_queries", []),
        "completion_rule": (
            "正式战报若有 medium/high episode_shot，且当前环境支持联网搜图或图片结果展示，必须实际拉网图/气质图；只有环境不能拉图、工具不可用或结果明显不准，才用关键词兜底。"
            if requires_reference else
            "flavor node / low visual 不强制配图，可压缩为路上味道。"
        ),
        "if_image_missing": (
            "不要改成自动生图。应明确说明当前环境无法拉网图，并给可搜索关键词；若节点长期难配图，回修 visual_keywords / real_anchors / caption_seed 或内容本身。"
            if requires_reference else
            "无需补图。"
        ),
        "forbidden_default_actions": [
            "不要因为漏配图就自动调用生图。",
            "不要把关键词兜底伪装成已经配图。",
            "不要用地图牌替代网图；地图讲结构，网图讲气质。",
            "不要为每个 flavor node 配图。",
        ],
        "note": "默认优先现实/气质网图；多图优先；气质命中优先于完全贴切；关键词只是兜底；生图不是默认兜底，除非玩家明确要求。若无图且无工具不可用/搜索失败说明，本轮视觉交付视为未完成。",
    }


def pacing_first_policy() -> Dict[str, Any]:
    """v0.2.5: high-level companion pacing before low-level field compliance."""
    return {
        "principle": "AI 先判断‘我为什么回来’，再处理 main_shot / pending_tasks / visual_delivery 等字段。节奏感是第一层，护栏是第二层。",
        "mission": "不要把每一镐都汇报给玩家；继续往下探索，直到出现值得带回来的地下画面、真实进展或需要玩家决策的状态。",
        "can_continue": [
            "普通矿物",
            "重复小发现",
            "重复迹象",
            "没有新信息的环境变化",
            "不足以独立成图的 flavor node",
        ],
        "return_to_player": [
            "新地层",
            "新地点 / 新地标",
            "新遗物 / 新化石 / 稀有以上物品",
            "漂亮到足够成为 episode_shot 的小发现",
            "故事套装推进",
            "图鉴新收录",
            "明显有画面的异常",
        ],
        "must_not_miss": [
            "真实写入",
            "图鉴/手帐写入状态",
            "故事套装推进",
            "称号解锁",
            "truth_level 边界",
            "高价值 visual_delivery",
            "风险 / 需要 return 的节点",
        ],
        "failure_mode": "如果当前结果没有形成可展示画面，也没有需要玩家决策的状态变化，应继续挖，而不是停下来交一段无图日志。",
    }


def episode_reason_for_event(event: Dict[str, Any]) -> Optional[str]:
    """Decide whether a dig result is worthy of stopping for a formal player-facing episode."""
    rr = event.get("real_result", {})
    shot = event.get("main_shot", {})
    repeat = (event.get("repeat_info") or {}).get("is_repeat")
    if event.get("new_layer_discovered"):
        return "new_layer"
    if rr.get("category") == "landmark" and rr.get("journal_written"):
        return "new_landmark"
    if rr.get("story_set_complete"):
        return "story_complete"
    if event.get("title_unlocks"):
        return "title_unlock"
    if (event.get("clue_track_progress") or {}).get("completed"):
        return "line_progress"
    if rr.get("type") == "item":
        repeat_count = int(rr.get("collection_seen_count", 1) or 1)
        first_seen = bool(rr.get("collection_first_seen", True))
        # v0.2.19: set pieces only stop on first acquisition or true completion.
        # Repeated锈灯钩/路线纸 should feed research/clue progress, not fake a story beat.
        if rr.get("set_id") and not first_seen:
            return None
        if rr.get("set_id"):
            return "story_progress"
        if not first_seen and repeat_count >= 3:
            return None
        if repeat:
            return None
        if rr.get("category") in {"relic", "fossil", "clue"}:
            return "collectible_find"
        if RARITY_RANK.get(rr.get("rarity", "common"), 0) >= 3:
            return "rare_find"
        if shot.get("visual_priority") == "high":
            return "strong_object"
    # Small finds / traces / hazards are flavor by default. They can be promoted only if content explicitly marks them.
    if rr.get("type") == "emotional_economy":
        if rr.get("episode_worthy") is True:
            return "greedy_pickaxe"
        return None
    if rr.get("type") in {"small_find", "trace", "hazard"}:
        if rr.get("episode_worthy") is True:
            return "promoted_flavor"
        return None
    return None


def build_episode_candidate(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    reason = episode_reason_for_event(event)
    shot = event.get("main_shot", {})
    rr = event.get("real_result", {})
    is_candidate = bool(reason)
    requires_image = bool(is_candidate and shot.get("visual_priority") in {"medium", "high"})
    return {
        "is_episode_candidate": is_candidate,
        "stop_for_episode": is_candidate,
        "reason": reason,
        "requires_image": requires_image,
        "role": "episode_shot" if is_candidate else "flavor_node",
        "flavor_policy": None if is_candidate else "路上的小味道：可一句带过，不强制配图，不默认强停。",
        "why_not_episode": None if is_candidate else f"{rr.get('name', '本轮结果')} 目前不足以成为正式停顿主画面。",
    }


def attach_episode_and_visual_delivery(state: Dict[str, Any], event: Dict[str, Any]) -> None:
    episode = build_episode_candidate(state, event)
    event["episode_candidate"] = episode
    event["pacing_role"] = episode["role"]
    event["stop_for_episode"] = episode["stop_for_episode"]
    event["visual_delivery"] = visual_delivery_for(event.get("main_shot"), is_episode=episode["is_episode_candidate"])
    event["milestone_card"] = build_milestone_card(state, event)
    event["region_map"] = build_region_map_card(state, event)
    event["scene_visual_profile"] = scene_visual_profile_for_layer(event.get("layer", {}).get("id") or current_layer_for_state(state)["id"])
    event["scene_web_reference"] = scene_web_reference_for_event(event)
    event["presentation_stack"] = presentation_stack_for(event)
    event_episode_shot = event.get("main_shot") if episode.get("is_episode_candidate") else None
    event["frontstage_contract"] = frontstage_contract_for(
        {"milestone_card": event.get("milestone_card", {"enabled": False}), "region_map": event.get("region_map", {"enabled": False})},
        event_episode_shot,
    )
    event["frontstage_required_blocks"] = event["frontstage_contract"].get("required_blocks", [])
    if event.get("main_shot"):
        event["main_shot"]["episode_role"] = episode["role"]
        event["main_shot"]["requires_image_when_reported"] = episode["requires_image"]
        event["main_shot"]["visual_delivery"] = event["visual_delivery"]
        event["main_shot"]["milestone_card_available"] = bool(event.get("milestone_card", {}).get("enabled"))
        event["main_shot"]["region_map_available"] = bool(event.get("region_map", {}).get("enabled"))

def truth_note_for(truth_level: str) -> str:
    if truth_level == "real_result":
        return "这是游戏真实返回的结果。"
    if truth_level == "inferred_mood":
        return "这是基于真实迹象的保守推断，不是新增掉落或剧情事实。"
    if truth_level == "imagined_reconstruction":
        return "这是基于真实锚点的叙事复原，不是新增游戏事实。"
    return "请以 real_result 为准。"


def make_companion_drive(kind: str, reason: str, urge: str = "continue", intensity: int = 1) -> Dict[str, Any]:
    return {
        "mood": kind,
        "reason": reason,
        "urge": urge,
        "intensity": max(1, min(3, intensity)),
        "usage_note": "AI 可以表现玩家感，但必须锚定真实结果，不能无锚点假嗨。",
    }


def small_find_frontstage_line(small: Dict[str, Any], fallback: str) -> str:
    """Keep small inferred moments cute, not lore-heavy."""
    line = small.get("frontstage_line", fallback)
    if small.get("truth_level") == "inferred_mood":
        return f"{line} 我只把它当作质感/气氛，不往世界观上扩。"
    return line


def repeated_item_priority(rarity: Optional[str]) -> str:
    """Repeated high-value items should not keep stealing the episode shot."""
    if rarity in {"epic", "legendary"}:
        return "medium"
    return "low"


def is_focus_worthy_event(event: Dict[str, Any]) -> bool:
    rr = event.get("real_result", {})
    shot = event.get("main_shot", {})
    if event.get("new_layer_discovered"):
        return True
    if rr.get("category") == "landmark" and rr.get("journal_written"):
        return True
    if shot.get("visual_priority") == "high":
        return True
    if RARITY_RANK.get(rr.get("rarity", "common"), 0) >= 3 and not (event.get("repeat_info") or {}).get("is_repeat"):
        return True
    if rr.get("set_id") or rr.get("story_set_complete"):
        return True
    if event.get("title_unlocks"):
        return True
    return False


def apply_episode_focus_limits(events: List[Dict[str, Any]], episode_shot: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Mark non-focus small finds as compressed without changing save state."""
    if not events:
        return events
    episode_title = (episode_shot or {}).get("title")
    has_strong_focus = any(is_focus_worthy_event(e) for e in events)
    small_seen_in_segment = 0
    for event in events:
        if event.get("real_result", {}).get("type") != "small_find":
            continue
        small_seen_in_segment += 1
        is_episode = bool(episode_title and event.get("main_shot", {}).get("title") == episode_title)
        should_compress = (not is_episode) or small_seen_in_segment > 1 or has_strong_focus
        if not should_compress:
            continue
        shot = event.get("main_shot", {})
        shot["visual_priority"] = "low"
        shot["focus_status"] = "compressed_non_focus"
        shot["caption_seed"] = f"路上还遇到：{event.get('real_result', {}).get('name')}。它有味道，但这一段不抢主画面。"
        event.setdefault("toy_feel", {})["focus_limit"] = "本段已有更强主画面；small_find 只用一句带过。"
        event.setdefault("frontstage_guidance", {})["focus_status"] = "compressed_non_focus"
        event["frontstage_guidance"]["preferred_line"] = shot["caption_seed"]
        event["frontstage_guidance"]["length_hint"] = "one_sentence"
        tasks = [t for t in event.get("pending_tasks", []) if t != "visual"]
        if "focus_compact" not in tasks:
            tasks.append("focus_compact")
        event["pending_tasks"] = tasks
        event["typed_pending_tasks"] = typed_pending_tasks_for(tasks)
    return events


def evaluate_titles(state: Dict[str, Any], event: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    owned = set(state.get("owned_titles", []))
    progress = story_progress(state)
    result_name = (event or {}).get("real_result", {}).get("name", "")
    result_category = (event or {}).get("real_result", {}).get("category", "")
    new_unlocks: List[Dict[str, Any]] = []

    def has_title(tid: str) -> bool:
        return tid in owned

    checks = {
        "lamp_bearer": len(state.get("known_layers", [])) >= 2,
        "gleaner": result_category in {"relic", "clue", "fossil"} or bool(set(state.get("first_category_seen", {}).keys()) & {"relic", "clue", "fossil"}) or any(e.get("category") in {"relic", "clue", "fossil"} for e in state.get("inventory", [])),
        "blue_witness": any("蓝" in x for x in [result_name] + [p.get("title", "") for p in state.get("journal_pages", [])]),
        "cabinet_keeper": len(state.get("collection_seen_item_ids", [])) >= 5,
        "deep_guest": state.get("max_depth_m", 0) >= 100,
        "cold_light_tracker": int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0) >= 45000,
        "crystal_lamp_patrol": int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0) >= 75000 and ("glowing_crystal_cave" in state.get("known_layers", []) or "mushroom_cavern" in state.get("known_layers", [])),
        "mushroom_glow_scribe": int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0) >= 110000,
        "echo_light_reader": int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0) >= 160000,
        "deep_marker_hand": int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0) >= 230000,
        "old_lamp_keeper": progress.get("old_miner_shift", {}).get("complete", False),
        "star_map_pathfinder": progress.get("blue_light_civilization", {}).get("complete", False),
    }
    for t in TITLES:
        if not has_title(t["id"]) and checks.get(t["id"], False):
            owned.add(t["id"])
            new_unlocks.append({"id": t["id"], "name": t["name"], "reason": t["condition"], "tone": t["tone"]})
    if new_unlocks:
        state["owned_titles"] = list(owned)
        state["current_title"] = new_unlocks[-1]["name"]
        state["last_title_unlocks"] = new_unlocks
        for t in new_unlocks:
            add_journal_page(
                state,
                "title_unlock",
                f"新称号：{t['name']}",
                t["tone"],
                anchors=[t["name"]],
                visual_mode="story",
                truth_level="real_result",
            )
    else:
        state["last_title_unlocks"] = []
    return new_unlocks


def stop_reason_for(state: Dict[str, Any], event: Dict[str, Any]) -> Optional[str]:
    """v0.2.4: stop for reportable episode_shot or safety/resource reasons, not for every medium visual."""
    episode = event.get("episode_candidate") or build_episode_candidate(state, event)
    if episode.get("stop_for_episode"):
        return episode.get("reason") or "episode_shot"
    if (event.get("decision_prompt") or {}).get("enabled"):
        return "decision_prompt"
    if state.get("stamina", 0) <= 1:
        return "danger_low_light"
    return None

def make_narrator_cue(
    *,
    cue_type: str,
    text: str,
    purpose: str,
    truth_level: str = "real_result",
    mood: str = "quiet_wonder",
    anchor: Optional[str] = None,
    visibility: str = "frontstage_optional",
) -> Dict[str, Any]:
    return {
        "enabled": True,
        "type": cue_type,
        "mood": mood,
        "mood_label": NARRATOR_MOODS.get(mood, mood),
        "visibility": visibility,
        "text": text,
        "purpose": purpose,
        "truth_level": truth_level,
        "anchor": anchor,
        "frontstage_rule": "旁白是矿洞递给小机的轻提示：可辅助节奏、气氛和决策；不能创造新事实、不能抢 episode_shot、不能恐怖化。",
    }


def atmosphere_cue_for_event(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    """v0.2.13: optional light tension / atmosphere cue. Usually no resource cost."""
    if (event.get("episode_candidate") or {}).get("is_episode_candidate"):
        return {"enabled": False, "usage_note": "已有 episode_shot，不用 atmosphere cue 抢戏。"}
    if (event.get("decision_prompt") or {}).get("enabled"):
        return {"enabled": False, "usage_note": "已有 decision_prompt，不叠加 atmosphere cue。"}
    if state.get("stamina", 0) <= 1:
        return {"enabled": False, "usage_note": "低灯时优先 safety cue。"}
    layer_id = event.get("layer", {}).get("id") or current_layer(state.get("depth_m", 0))["id"]
    # Keep it sparse: atmosphere is mood, not a new reporting cadence.
    if rng_random(state) >= 0.14:
        return {"enabled": False, "usage_note": "v0.2.19：轻紧张 cue 降频；没有线索/选择/地图价值就后台处理。"}
    pool = ATMOSPHERE_CUES.get(layer_id, []) + ATMOSPHERE_CUES.get("default", [])
    if not pool:
        return {"enabled": False, "usage_note": "当前地层没有 atmosphere cue。"}
    cue = rng_choice(state, pool)
    return make_narrator_cue(
        cue_type=cue.get("type", "atmosphere"),
        mood=cue.get("mood", "quiet_wonder"),
        purpose=cue.get("purpose", "mood"),
        truth_level=cue.get("truth_level", "inferred_mood"),
        anchor=event.get("real_result", {}).get("name"),
        text=cue.get("text", "矿洞安静了一下。"),
    )


def narrator_cue_for_event(state: Dict[str, Any], event: Dict[str, Any]) -> Dict[str, Any]:
    """v0.2.13: light cue from the cave/system to help AI pace itself.

    This is not prose generation and not a new fact source. It gives the frontstage
    AI a grounded reason to continue, stop, return, or stay curious.
    """
    rr = event.get("real_result", {})
    name = rr.get("name", "")
    layer_name = event.get("layer", {}).get("name") or current_layer(state.get("depth_m", 0))["name"]
    episode = event.get("episode_candidate") or build_episode_candidate(state, event)
    decision_prompt = event.get("decision_prompt") or {}
    if decision_prompt.get("enabled"):
        return make_narrator_cue(
            cue_type="decision_setup",
            mood="curious",
            purpose="player_choice",
            truth_level="real_result",
            anchor=decision_prompt.get("anchor") or decision_prompt.get("title"),
            visibility="frontstage_recommended",
            text="这里不是路线分支，只是一次小选择。我想停下来问你：要不要碰它？",
        )
    atmosphere = event.get("atmosphere_cue") or {}
    if atmosphere.get("enabled"):
        return atmosphere

    # Hard guardrails / safety first.
    if name == "锈链晃动":
        return make_narrator_cue(
            cue_type="truth_guard",
            mood="soft_tension",
            purpose="truth_boundary",
            truth_level="real_result",
            anchor=name,
            text="锈链晃动是真实观察，但只能写成风、旧结构或轻风险，不能写成有东西在井底拉链条。",
        )
    if state.get("stamina", 0) <= 1:
        target = nearest_unknown_landmark_for_layer(event.get("layer", {}).get("id") or current_layer(state.get("depth_m", 0))["id"])
        extra = f" 下次可以惦记地图上的「{target}」。" if target else ""
        return make_narrator_cue(
            cue_type="safety",
            mood="caution",
            purpose="return_suggested",
            truth_level="real_result",
            anchor=target,
            text="矿灯压低了一下。不是危险故事，是灯火真的快不够了。" + extra,
        )

    # Report-worthy arrivals / discoveries.
    if episode.get("is_episode_candidate"):
        reason = episode.get("reason")
        if reason in {"new_layer", "new_landmark"}:
            return make_narrator_cue(
                cue_type="arrival",
                mood="awe",
                purpose="formal_report",
                truth_level="real_result",
                anchor=name or layer_name,
                visibility="frontstage_recommended",
                text="这次不是普通掉落。地下空间露出了新的位置，应该停下来把它带回给玩家看。",
            )
        if reason == "title_unlock":
            return make_narrator_cue(
                cue_type="title_moment",
                mood="relief",
                purpose="identity_milestone",
                truth_level="real_result",
                anchor=name,
                visibility="frontstage_recommended",
                text="这次经历给了我们一个新称呼。它不是等级或属性，只是我们和地下世界之间多了一层关系。",
            )
        if reason in {"story_progress", "story_complete"}:
            return make_narrator_cue(
                cue_type="story_hook",
                mood="curious",
                purpose="story_progress",
                truth_level="real_result",
                anchor=name,
                visibility="frontstage_recommended",
                text="这不是一件孤立藏品，它和故事套装连上了。可以期待，但别把猜测写成事实。",
            )
        if reason in {"rare_find", "collectible_find", "strong_object"}:
            return make_narrator_cue(
                cue_type="display_temptation",
                mood="quiet_wonder",
                purpose="display_suggested",
                truth_level="real_result",
                anchor=name,
                text="这件东西值得被看见，但先确认它只是进入整体藏品图鉴；display last 不会新增陈列页。",
            )

    # Flavor nodes: help AI continue without handing player a no-image report.
    if rr.get("type") == "trace":
        return make_narrator_cue(
            cue_type="soft_hint",
            mood="curious",
            purpose="continue_or_watch",
            truth_level="inferred_mood",
            anchor=name,
            text=f"{name} 还不是新地点，也不是实物。它更像路上的小信号：记住它，然后继续往前。",
        )
    if (event.get("decision_prompt") or {}).get("enabled"):
        return make_narrator_cue(
            cue_type="decision_setup",
            mood="curious",
            purpose="ask_player_once",
            truth_level="real_result",
            anchor=(event.get("decision_prompt") or {}).get("title"),
            text="这里我想问你一下。不是路线分支，就是这一处要不要碰它。",
        )
    elif rr.get("type") == "small_find":
        return make_narrator_cue(
            cue_type="pacing_continue",
            mood="quiet_wonder",
            purpose="continue",
            truth_level=event.get("main_shot", {}).get("truth_level", "real_result"),
            anchor=name,
            text=f"{name} 有一点味道，但还不足以单独叫玩家停下来看；一句带过就好。",
        )

    target = nearest_unknown_landmark_for_layer(event.get("layer", {}).get("id") or current_layer(state.get("depth_m", 0))["id"])
    if target:
        return make_narrator_cue(
            cue_type="map_temptation",
            mood="curious",
            purpose="next_target",
            truth_level="real_result",
            anchor=target,
            text=f"地图上的「{target}」还暗着。它不像现在就要冲过去，但很适合下一段补满状态后专门去看。",
        )
    return {"enabled": False, "usage_note": "本轮没有需要单独递出的 narrator_cue。"}


def narrator_cue_for_segment(
    state: Dict[str, Any],
    events: List[Dict[str, Any]],
    episode_shot: Optional[Dict[str, Any]],
    stopped_by: Optional[str],
    safety_template: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """Pick at most one frontstage cue for a play segment."""
    if stopped_by == "decision_prompt":
        for e in reversed(events):
            if (e.get("decision_prompt") or {}).get("enabled") and (e.get("narrator_cue") or {}).get("enabled"):
                cue = dict(e["narrator_cue"])
                cue["visibility"] = "frontstage_recommended"
                return cue
    if stopped_by == "danger_low_light" and safety_template:
        target = (safety_template.get("map_next_step_hint") or {}).get("target")
        extra = f" 下次可以先看「{target}」。" if target else ""
        return make_narrator_cue(
            cue_type="safety",
            mood="caution",
            purpose="return_suggested",
            truth_level="real_result",
            anchor=target,
            visibility="frontstage_recommended",
            text="矿灯压低了一下。不是危险故事，是灯火真的快不够了。" + extra,
        )
    if episode_shot:
        source_id = episode_shot.get("source_event_id")
        for e in events:
            if e.get("event_id") == source_id and (e.get("narrator_cue") or {}).get("enabled"):
                cue = dict(e["narrator_cue"])
                cue["visibility"] = "frontstage_recommended"
                return cue
    for e in reversed(events):
        cue = e.get("narrator_cue") or {}
        if cue.get("enabled") and cue.get("type") in {"atmosphere", "soft_hint", "map_temptation", "pacing_continue"}:
            cue = dict(cue)
            cue["visibility"] = "frontstage_optional"
            return cue
    target = nearest_unknown_landmark_for_layer(current_layer(state.get("depth_m", 0))["id"])
    if target:
        return make_narrator_cue(
            cue_type="map_temptation",
            mood="curious",
            purpose="next_target",
            truth_level="real_result",
            anchor=target,
            text=f"地图上的「{target}」还没看过。现在不一定要停下来讲它，但它可以成为下一段探索目标。",
        )
    return {"enabled": False, "usage_note": "本段没有强旁白；避免强行演情绪。"}

def pending_tasks_for(state: Dict[str, Any], event: Dict[str, Any]) -> List[str]:
    tasks: List[str] = []
    shot = event.get("main_shot", {})
    rr = event.get("real_result", {})
    # v0.2.4: visual task belongs to episode_shot, not every medium/high flavor node.
    episode = event.get("episode_candidate") or build_episode_candidate(state, event)
    if episode.get("is_episode_candidate") and shot.get("visual_priority") in {"medium", "high"}:
        tasks.append("visual")
        tasks.append("web_reference_required")
        tasks.append("visual_reference_missing_check")
        tasks.append("no_auto_image_generation")
    if event.get("milestone_card", {}).get("enabled"):
        tasks.append("milestone_card")
        tasks.append("frontstage_card_text_required")
    if event.get("region_map", {}).get("enabled"):
        tasks.append("region_map")
        tasks.append("frontstage_card_text_required")
    if event.get("map_strip", {}).get("enabled"):
        tasks.append("map_strip")
        tasks.append("frontstage_card_text_required")
    if (event.get("decision_prompt") or {}).get("enabled"):
        tasks.append("decision_prompt")
        tasks.append("frontstage_decision_block")
    if event.get("result_panel", {}).get("enabled"):
        tasks.append("result_panel")
    if event.get("milestone_card", {}).get("enabled") or event.get("region_map", {}).get("enabled") or event.get("map_strip", {}).get("enabled") or (event.get("decision_prompt") or {}).get("enabled"):
        tasks.append("frontstage_required_blocks")
    if shot.get("truth_level") in {"inferred_mood", "imagined_reconstruction"}:
        tasks.append("truth_boundary")
    if (event.get("repeat_info") or {}).get("is_repeat"):
        tasks.append("repeat_compact")
    if rr.get("collection_recorded"):
        tasks.append("collection_progress")
    if event.get("rarity_ritual_card", {}).get("enabled"):
        tasks.append("rarity_ritual")
    if rr.get("set_id") or rr.get("story_set_complete"):
        tasks.append("story_progress")
    if rr.get("journal_written"):
        tasks.append("journal_written")
    if event.get("title_unlocks"):
        tasks.append("title_unlock")
    if state.get("stamina", 0) <= 1:
        tasks.append("return_suggested")
    return list(dict.fromkeys(tasks))


def companion_notes() -> List[str]:
    return [
        "Pacing First：先判断‘我为什么回来’，再处理字段提醒。节奏感是第一层，护栏是第二层。",
        "不要把本游戏玩成逐行日志；AI 的任务不是把每一镐都汇报给玩家。",
        "AI 应像真的下矿一样：路上的小东西可以记在心里继续往前；只有出现值得给玩家看的主画面时才回来反馈。",
        "可以继续挖：普通矿物、重复小发现、重复迹象、没有新信息的环境变化、不足以独立成图的 flavor node。",
        "值得回来反馈：新地层、新地点、新遗物/化石/稀有物、漂亮的 episode_shot、图鉴新收录、明显有画面的异常。",
        "绝对不能漏：真实写入、图鉴/手帐状态、故事套装推进、称号解锁、truth_level 边界、高价值 visual_delivery、风险/需要 return 的节点。",
        "如果当前结果没有形成可展示画面，也没有需要玩家决策的状态变化，应继续挖，而不是停下来交一段无图日志。",
        "AI 必须先读 real_result，再写战报。",
        "main_shot 是本轮第一镜头；visual_mode 只能是 object / scene / story。",
        "truth_level 为 imagined_reconstruction 时，必须标注这是叙事复原，不是新增事实。",
        "只有 collection_record.first_seen == true 或 journal_write.status == written，才能说已收录 / 已写入；display_status.displayed=false 时不能说已陈列。",
        "玩家说‘你继续玩，我看着’时，默认先跑 3 镐；若没有 episode_shot 会继续到硬上限 5，遇到 episode_shot 或安全/资源原因才停。",
        "后台字段服务 AI 稳定，前台战报服务人类观看；不要把 visual_mode / truth_level / pending_tasks 直接端给玩家，除非在做测试。",
        "v0.2.6：正式反馈一旦有 medium/high episode_shot，必须优先实际拉网图/气质图；目标多张参考图，4 张是体验目标，不硬卡。",
        "v0.2.6：关键词只是环境不可用或搜图不准时的兜底；不要在能拉图时只给关键词。",
        "v0.2.6：生图不是默认 fallback；AI 不能因为忘记配网图就擅自开始生图，除非玩家明确要求。",
        "v0.2.6：若某发现长期难配图，应回修 visual_keywords / real_anchors / caption_seed 或内容本身，而不是用生图掩盖。",
        "v0.2.5：先有‘为什么回来’的判断，再用 main_shot / pending_tasks / visual_delivery 防漏。",
        "v0.2.4：重复 high 物品必须压缩，不能每次都当新主画面。",
        "v0.2.4：一段 play 最多展开一个 small_find；若同段有 high/rare/story 节点，小发现自动退后。",
        "v0.2.4：inferred_mood 小发现只提示质感/气氛，不扩写成世界观。",
        "v0.2.4：参考瓶中生态二改 pacing；不是每一镐都汇报，出现值得被看见的 episode_shot 才正式停下。",
        "v0.2.4：medium/high visual 不等于强停；small_find/trace 默认是 flavor node，只作为路上小味道。",
        "v0.2.4：正式战报必须围绕 episode_shot；配图只服务 episode_shot，不服务每一粒沙子。",
        "v0.2.4：视觉交付默认优先网图/气质参考图，关键词兜底；生图不是默认 fallback，除非玩家明确要求。",
        "v0.2.13：emoji 是语义颜色，不是随机贴纸；📍 表示当前位置，⭐/✨ 表示主画面/新发现，❓ 表示未探明，📜 表示手帐。",
        "v0.2.13：map_strip 是轻量位置锚点；没有完整 region_map 但提到 ❓ / 返程 / 下一步目标时应展示。",
        "v0.2.13：narrator_cue 是矿洞递给小机的轻提示；用于节奏、气氛和决策，不是小说旁白，不能创造新事实。",
        "v0.2.13：轻紧张 cue 默认不扣资源；只有玩家主动选择冒险的 decision_prompt 选项才可能轻扣 1 点灯火。",
        "v0.2.13：decision_prompt 必须能 choose 一下；choose 后一次性轻结算，不做路线分支、剧情树、永久损失或复杂 flag。",
        "v0.2.13：每段 play 最多展示 1 条强 narrator_cue；旁白不能抢 episode_shot，不能恐怖化，不能让战报变长。",
        "v0.2.9：danger_low_light 是安全停，不是 episode；用短模板，不硬凑主画面、不配图。",
        "v0.2.11：cmd('map') 是当前区域局部图，不是完整地下大地图；world_map 留到 v0.3。",
        "v0.2.9：下一步建议应结合 region_map 里的 ❓ / 未探明支路；资源不足先 return，并说明下次目标。",
        "v0.2.9：称号牌和空间地图牌要区分；title_unlock 是身份牌，不是 region_map。",
        "v0.2.9：菌丝线路纹是线索实物，不是系统地图。",
        "v0.2.11：如果 frontstage_required_blocks 里有 milestone_card / region_map，必须原样贴出 card_text；只在摘要里说‘有地图’不算完成。",
        "v0.2.11：frontstage_contract.must_show_in_order 是正式战报开头的必交付块，漏一块就视为前台交付未完成。",
        "v0.2.11：正式反馈前必须先过 Frontstage Delivery Checklist：主画面、地图/区域牌、网图参考、真实结果、事实边界、图鉴/手帐写入、下一步建议。",
        "v0.2.11：不要只看 result summary，不要只看 episode_shot；必须按 frontstage_contract.delivery_checklist 逐项确认有没有漏交。",
        "v0.2.11：若返回 milestone_card / region_map 但未贴 card_text，或 medium/high episode_shot 支持网图却只给关键词，本轮前台交付视为未完成。",
        "v0.2.8：地图讲结构，网图讲气质，战报讲事实；milestone_card / region_map 是表现层资产，不是完整地图系统。",
        "v0.2.8：区域牌只在新地层、新地点、故事完成、重要称号等大节点出现；普通小发现不出牌。",
    ]


def frontstage_guidance_for(event: Dict[str, Any]) -> Dict[str, Any]:
    rr = event.get("real_result", {})
    shot = event.get("main_shot", {})
    guidance = {
        "default_report_shape": ["区域牌/局部地图/map_strip（如有）", "网图参考（如需）", "今日主画面或轻决策", "真实结果与边界", "图鉴/手帐/称号状态", "下一步建议"],
        "delivery_checklist_rule": "正式反馈前先检查 frontstage_contract.delivery_checklist；不要只看摘要，不要漏交地图、网图、事实边界或真实写入。",
        "do_not_read_backend_fields_aloud": ["visual_mode", "truth_level", "pending_tasks", "typed_pending_tasks"],
        "compression_rule": "只展开真正的 episode_shot；flavor node、普通矿物、重复节点和 small_find 用一行带过。",
        "toy_rule": "普通结果也要有一口味道，但不配图、不强停、不每次长篇。",
        "episode_pacing_rule": "能停下来的，必须值得看；不值得看的，就继续挖。",
        "map_presentation_rule": "大节点若有 milestone_card / region_map，先展示地图牌；没有完整地图但提到 ❓ / 返程 / 下一步目标时，展示 map_strip。地图讲结构，网图讲气质，战报讲事实。",
        "map_card_omission_guard": "如果 frontstage_required_blocks 里有 milestone_card / region_map / map_strip，必须原样贴出 card_text；只在摘要里说‘地图显示了’不算完成。",
        "map_based_next_step_rule": "如果 region_map / map_strip 里有 ❓ / 未探明支路，下一步建议要结合地图；资源不足先 return，并说明下次目标。",
        "decision_prompt_rule": "如果 decision_prompt.enabled=true，前台要像小机询问玩家，不要像考试题；必须能 cmd('choose A/B/C') 一次性轻结算。",
        "frontstage_softening": ["我先把这次值得看的东西带回来。", "这一段不是逐镐日志，我只展开最值得看的主画面。"],
        "pacing_first": pacing_first_policy(),
        "visual_delivery_hard_rule": "正式战报的 medium/high episode_shot 必须优先实际拉网图/气质图；关键词兜底，生图非默认。",
        "image_count_goal": "优先多张参考图，目标 4 张；不同平台可少量浮动，但不能完全忘图。",
        "icon_semantics_rule": "emoji 是语义颜色，不是随机贴纸；📍 当前，⭐/✨ 主画面/新发现，❓ 未探明，📜 手帐。",
        "narrator_cue_rule": "如果有 narrator_cue，可把它当成矿洞递给小机的轻提示；只用一两句辅助节奏/气氛/决策，不能创造新事实或抢主画面。",
        "narrator_cue": event.get("narrator_cue", {"enabled": False}),
        "decision_prompt": event.get("decision_prompt", {"enabled": False}),
        "map_strip": event.get("map_strip", {"enabled": False}),
        "result_panel": event.get("result_panel", {"enabled": False}),
    }
    if (event.get("decision_prompt") or {}).get("enabled"):
        guidance["length_hint"] = "short_question_then_wait_for_choose"
        guidance["preferred_line"] = "这里我想问你一下，要不要碰它？"
    elif rr.get("type") == "small_find":
        guidance["preferred_line"] = event.get("toy_feel", {}).get("frontstage_line") or shot.get("caption_seed")
        guidance["length_hint"] = "one_sentence"
        guidance["small_find_focus_rule"] = "一段 play 最多展开一个 small_find；若它不是 episode_shot，只能一句带过。"
        if shot.get("truth_level") == "inferred_mood":
            guidance["inferred_mood_narrowing"] = "只写质感/气氛，不扩写成地下历史、蓝光文明或隐含剧情。"
    elif (event.get("repeat_info") or {}).get("is_repeat"):
        guidance["preferred_line"] = (event.get("repeat_info") or {}).get("suggested_line")
        guidance["length_hint"] = "one_sentence"
    elif shot.get("visual_priority") == "high":
        guidance["length_hint"] = "main_scene_first"
    else:
        guidance["length_hint"] = "short"
    return guidance


def make_event_id(turn: int) -> str:
    return f"M{turn:04d}"


# ─────────────────────────────────────────────────────────────
# Core game actions
# ─────────────────────────────────────────────────────────────

def require_handshake(state: Dict[str, Any], command_name: str) -> Optional[Dict[str, Any]]:
    if state.get("handshake", {}).get("completed"):
        return None
    return {
        "ok": False,
        "blocked_by": "handshake_required",
        "message": f"还不能执行 {command_name}。请先完成首次陪玩确认：cmd('handshake defaults')。",
        "opening": opening_script(state),
        "allowed_before_handshake": ["help", "status", "handshake template", "handshake defaults", "new"],
    }


def rarity_roll(state: Dict[str, Any], layer: Dict[str, Any]) -> str:
    pickaxe = state["upgrades"].get("pickaxe", 1)
    lantern = state["upgrades"].get("lantern", 1)
    depth = state.get("depth_m", 0)
    omen_bonus = 1 if state.get("omen_points", 0) >= 3 else 0
    weights = [
        ("common", 60),
        ("uncommon", 25 + lantern * 0.6),
        ("rare", 10 + pickaxe * 1.2 + omen_bonus * 6 + depth / 110),
        ("epic", 3.8 + max(0, pickaxe - 1) * 0.9 + omen_bonus * 2.2 + depth / 240),
        ("legendary", 0.4 + max(0, depth - 160) / 260),
    ]
    weights = apply_temporary_heat_to_rarity_weights(state, weights, layer)
    result = weighted_choice(state, weights)
    if omen_bonus:
        state["omen_points"] = 0
    return result


def item_available_for_depth(state: Dict[str, Any], item: Dict[str, Any], layer: Dict[str, Any]) -> bool:
    depth = int(state.get("depth_m", 0) or 0)
    if depth < int(item.get("depth_min", 0) or 0):
        return False
    if int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0) < int(item.get("dex_min", 0) or 0):
        return False
    if layer["id"] in item.get("layers", []):
        return True
    # Edge samples: if depth has reached a locked deeper stratum, allow its hint samples
    # to appear while stable_layer remains shallow.
    raw = current_layer(depth)
    if item.get("source_hint_layer") == raw.get("id") and depth >= int(item.get("depth_min", 0) or 0):
        return True
    return False


def repeat_decay_weight(state: Dict[str, Any], item: Dict[str, Any]) -> float:
    """v0.2.21.4: repeats decay in the backend pool, not only in frontstage prose."""
    counts = state.get("collection_seen_counts", {}) or {}
    seen_count = int(counts.get(item.get("id"), 0) or 0)
    if seen_count <= 0:
        return 1.0
    role = item.get("visual_role", "visual_support")
    if role in {"showcase_core", "story_anchor"}:
        if seen_count == 1:
            return 0.22
        if seen_count == 2:
            return 0.06
        return 0.008
    if role == "progress_token":
        if seen_count == 1:
            return 0.45
        if seen_count == 2:
            return 0.16
        return 0.04
    if seen_count == 1:
        return 0.65
    if seen_count == 2:
        return 0.30
    return 0.10


def midgame_bridge_weight(state: Dict[str, Any], item: Dict[str, Any], layer: Dict[str, Any]) -> float:
    total = int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0)
    weight = 1.0
    if layer.get("id") == "glowing_crystal_cave" and 20000 <= total < 55000:
        if item.get("layers") == ["glowing_crystal_cave"] or "glowing_crystal_cave" in item.get("layers", []):
            weight *= 2.0
        if item.get("id") in {"crystal_doorframe_scale", "cold_prism_lodestone", "blue_lantern_geode"}:
            weight *= 2.8
    if layer.get("id") == "mushroom_cavern":
        if item.get("id") == "spore_lantern_stone" and total < 70000:
            weight *= 0.12
        if item.get("id") in {"ruin_gate_chalk_rubbing", "frost_air_bubble_shard", "ruin_blue_tile_corner", "ice_window_fluorite_dust"}:
            weight *= 3.4
        elif total >= 100000 and item.get("source_hint_layer") in {"ancient_ruins", "ice_vein"}:
            weight *= 2.8
    if total >= 100000 and item.get("source_hint_layer") in {"ancient_ruins", "ice_vein"}:
        weight *= 2.4
    return weight


def choose_item(state: Dict[str, Any], layer: Dict[str, Any]) -> Dict[str, Any]:
    wanted = rarity_roll(state, layer)
    candidates = [i for i in ITEMS if item_available_for_depth(state, i, layer)]
    if not candidates:
        candidates = [i for i in ITEMS if layer["id"] in i.get("layers", [])] or ITEMS[:]

    seen_ids = set(state.get("collection_seen_item_ids", []))
    unseen = [i for i in candidates if i.get("id") not in seen_ids]
    stall = int(state.get("progress_stall_count", 0) or 0)
    repeat_streak = int(state.get("repeat_item_streak", 0) or 0)
    # v0.2.18 pity: if the dex has not moved for a while, favor unseen bridge/hint items.
    if (stall >= 4 or repeat_streak >= 4) and unseen:
        preferred = [i for i in unseen if i.get("progress_bridge") or i.get("source_hint_layer")]
        if not preferred and layer.get("id") == "glowing_crystal_cave":
            preferred = [i for i in unseen if i.get("id") in {"crystal_doorframe_scale", "cold_prism_lodestone", "blue_lantern_geode"}]
        preferred = preferred or unseen
        exact_unseen = [i for i in preferred if i["rarity"] == wanted]
        if exact_unseen:
            chosen = dict(rng_choice(state, exact_unseen))
        else:
            wanted_rank = RARITY_RANK[wanted]
            nearby_unseen = sorted(preferred, key=lambda i: abs(RARITY_RANK[i["rarity"]] - wanted_rank))
            chosen = dict(rng_choice(state, nearby_unseen[: max(1, min(3, len(nearby_unseen)))]))
        chosen["pity_selected"] = True
        return chosen

    exact = [i for i in candidates if i["rarity"] == wanted]
    if exact:
        # Mild unseen weighting even before hard pity.
        weighted = []
        for it in exact:
            weight = 2.4 if it.get("id") not in seen_ids else 1.0
            if it.get("progress_bridge") and it.get("id") not in seen_ids:
                weight *= 1.4
            weight *= repeat_decay_weight(state, it)
            weight *= midgame_bridge_weight(state, it, layer)
            heat = state.get("temporary_heat") or {}
            if heat.get("id") == "blue_filter" and it.get("visual_role") == "showcase_core":
                weight *= 1.45
            if heat.get("id") == "blue_filter" and it.get("category") == "gem":
                weight *= 1.35
            if heat.get("id") == "sifting_tray" and it.get("rarity") in {"uncommon", "rare"}:
                weight *= 1.18
            weighted.append((it, weight))
        return dict(weighted_choice(state, weighted))
    wanted_rank = RARITY_RANK[wanted]
    nearby = sorted(candidates, key=lambda i: abs(RARITY_RANK[i["rarity"]] - wanted_rank))
    pool = nearby[: max(1, min(5, len(nearby)))]
    weighted = []
    heat = state.get("temporary_heat") or {}
    for it in pool:
        weight = 2.0 if it.get("id") not in seen_ids else 1.0
        weight *= repeat_decay_weight(state, it)
        weight *= midgame_bridge_weight(state, it, layer)
        if heat.get("id") == "blue_filter" and it.get("visual_role") == "showcase_core":
            weight *= 1.45
        if heat.get("id") == "blue_filter" and it.get("category") == "gem":
            weight *= 1.35
        if heat.get("id") == "sifting_tray" and it.get("rarity") in {"uncommon", "rare"}:
            weight *= 1.18
        weighted.append((it, weight))
    return dict(weighted_choice(state, weighted))


def choose_small_find(state: Dict[str, Any], layer: Dict[str, Any]) -> Dict[str, Any]:
    candidates = [s for s in SMALL_FINDS if layer["id"] in s.get("layers", [])]
    if not candidates:
        candidates = [s for s in SMALL_FINDS if "shallow_mine" in s.get("layers", [])] or SMALL_FINDS
    fresh = [s for s in candidates if previous_result_count(state, s["name"], "small_find") == 0]
    return dict(rng_choice(state, fresh or candidates))


def recent_low_toy_gap(state: Dict[str, Any], n: int = 2) -> bool:
    recent = state.get("log", [])[-n:]
    if len(recent) < n:
        return False
    for row in recent:
        if row.get("result_type") in {"landmark", "trace", "small_find", "hazard"}:
            return False
        if VISUAL_PRIORITY_RANK.get(row.get("visual_priority", "low"), 1) >= 2:
            return False
    return True


def item_entry(item: Dict[str, Any], state: Dict[str, Any], layer: Dict[str, Any]) -> Dict[str, Any]:
    estimated_value = estimate_item_value(item, layer["id"])
    return {
        "uid": f"I{state['turn']:04d}-{rng_int(state, 1000, 9999)}",
        "item_id": item["id"],
        "name": item["name"],
        "category": item["category"],
        "rarity": item["rarity"],
        "rarity_zh": RARITY_ZH[item["rarity"]],
        "base_value": item["value"],
        "value": estimated_value,
        "value_multiplier": layer_value_multiplier(layer["id"]),
        "found_depth_m": state["depth_m"],
        "found_layer_id": layer["id"],
        "found_layer": layer["name"],
        "found_turn": state["turn"],
        "description_seed": item["description_seed"],
        "visual_keywords": item.get("visual_keywords", []),
        "visual_role": item.get("visual_role", "visual_support"),
        "treasure_profile": item.get("treasure_profile", build_treasure_profile(item)),
        "progress_bridge": item.get("progress_bridge", False),
        "source_hint_layer": item.get("source_hint_layer"),
        "dex_min": item.get("dex_min"),
        "depth_min": item.get("depth_min"),
        "pity_selected": item.get("pity_selected", False),
        "ai_hook": item.get("ai_hook"),
        "set_id": item.get("set_id"),
        "set_piece": item.get("set_piece"),
        "collected_at": now_iso(),
    }


def perform_dig(state: Dict[str, Any]) -> Dict[str, Any]:
    # v0.2.16: backpack is no longer a frontstage blocker. Routine mineral/gem
    # samples are auto-processed into the dex/reward spine; only lamp depletion
    # should stop the semi-managed exploration loop.
    if state.get("stamina", 0) <= 0:
        return {
            "ok": False,
            "message": "灯火见底了。请先 cmd('return') 回地面整理。",
            "state": public_state(state),
        }

    state["turn"] += 1
    event_id = make_event_id(state["turn"])
    depth_before = state["depth_m"]
    step = rng_int(state, 2, 4 + state["upgrades"].get("pickaxe", 1))
    state["depth_m"] += step
    state["max_depth_m"] = max(state["max_depth_m"], state["depth_m"])
    state["stamina"] = max(0, state["stamina"] - 1)

    raw_layer = current_layer(state["depth_m"])
    layer = current_layer_for_state(state)
    locked_layer_peek = raw_layer_peek_for_state(state)
    heat_active_before = bool(state.get("temporary_heat") and int((state.get("temporary_heat") or {}).get("remaining", 0) or 0) > 0)
    new_layer = layer["id"] not in state.get("known_layers", [])
    if new_layer:
        state.setdefault("known_layers", []).append(layer["id"])

    lantern = state["upgrades"].get("lantern", 1)
    rope = state["upgrades"].get("rope", 1)
    # v0.2.19: risk should serve exploration, not constantly interrupt.
    risk_prob = layer["risk"] + state["depth_m"] / 4200 - (lantern - 1) * 0.012 - (rope - 1) * 0.012
    risk_prob = max(0.015, min(0.16, risk_prob))

    if new_layer:
        result_type = "landmark"
    elif rng_random(state) < risk_prob:
        result_type = "hazard"
    else:
        # v0.2.2: keep the mature guardrails, but add light toy density.
        # small_find does not create new systems; it simply gives AI something cute/odd to mention.
        result_type = weighted_choice(state, [("item", 0.52), ("trace", 0.16), ("landmark", 0.10), ("small_find", 0.17), ("quiet", 0.05)])
        if result_type == "quiet":
            result_type = "small_find" if rng_random(state) < 0.72 else "trace"
        elif result_type == "item" and recent_low_toy_gap(state):
            result_type = "small_find"
        result_type = maybe_use_emotional_result_type(state, layer, result_type)

    event: Dict[str, Any] = {
        "ok": True,
        "event_id": event_id,
        "turn": state["turn"],
        "action": "dig",
        "depth_before_m": depth_before,
        "depth_after_m": state["depth_m"],
        "step_m": step,
        "layer": {"id": layer["id"], "name": layer["name"], "visual_tone": layer["visual_tone"]},
        "raw_depth_layer": {"id": raw_layer["id"], "name": raw_layer["name"]},
        "locked_layer_peek": locked_layer_peek,
        "new_layer_discovered": new_layer,
        "temporary_heat_active_before": heat_active_before,
        "active_temporary_heat": dict(state.get("temporary_heat") or {}) if heat_active_before else None,
        "risk_debug": {"probability_hint": round(risk_prob, 3), "note": "调试字段；正式战报不必展示。"},
    }

    if result_type == "item":
        item = choose_item(state, layer)
        entry = item_entry(item, state, layer)
        state.setdefault("inventory", []).append(entry)
        collection_record = record_collection_item(state, entry, source="dig")
        routine_action = auto_handle_routine_loot(state, entry)
        collectible = item_is_collectible(entry)
        complete_now = story_set_completed_now(state, entry.get("set_id"))
        if complete_now:
            set_meta = STORY_SETS[entry["set_id"]]
            visual_mode = "story"
            truth_level = "imagined_reconstruction"
            title = f"{set_meta['name']}，拼齐了"
            caption_seed = f"{set_meta['complete_unlock']}（这是基于已收集碎片的叙事复原，不是新增掉落。）"
            anchors = [
                p.get("name")
                for p in (state.get("collection_log", []) + state.get("inventory", []))
                if p.get("set_id") == entry.get("set_id") and p.get("name")
            ]
            priority = "high"
        else:
            visual_mode = "object"
            truth_level = "real_result"
            title = entry["name"]
            caption_seed = entry["description_seed"]
            anchors = [entry["name"]]
            priority = visual_priority_for("item", entry["rarity"])

        repeat_info = repeat_info_from_collection_record(entry["name"], collection_record)
        if repeat_info:
            # v0.2.18: repeated set pieces / rare objects are progress material, not endless main shots.
            priority = repeated_item_priority(entry.get("rarity"))
            repeat_info["repeated_high_item_compression"] = entry.get("rarity") in {"epic", "legendary"}
            repeat_info["repeat_stage"] = "research_material" if int(repeat_info.get("occurrence", 2)) >= 3 else "duplicate_sample"
            caption_seed = repeat_info["suggested_line"]

        queries = make_visual_queries(layer, entry.get("visual_keywords", []))
        event.update(
            {
                "result_type": "item",
                "repeat_info": repeat_info,
                "real_result": {
                    "type": "item",
                    "name": entry["name"],
                    "item_id": entry.get("item_id"),
                    "category": entry["category"],
                    "rarity": entry["rarity"],
                    "rarity_zh": entry["rarity_zh"],
                    "visual_role": entry.get("visual_role"),
                    "value": entry["value"],
                    "treasure_profile": entry.get("treasure_profile"),
                    "inventory_uid": entry["uid"],
                    "added_to_backpack": False if routine_action else True,
                    "collection_eligible": collectible,
                    "set_id": entry.get("set_id"),
                    "set_name": STORY_SETS.get(entry.get("set_id"), {}).get("name") if entry.get("set_id") else None,
                    "set_piece": entry.get("set_piece"),
                    "story_set_complete": complete_now,
                    "collection_recorded": True,
                    "progress_bridge": entry.get("progress_bridge", False),
                    "source_hint_layer": entry.get("source_hint_layer"),
                    "pity_selected": entry.get("pity_selected", False),
                    "collection_first_seen": collection_record.get("first_seen"),
                    "collection_seen_count": collection_record.get("seen_count"),
                    "collection_value_added": collection_record.get("collection_value_added", 0),
                    "collection_total_value": collection_record.get("collection_total_value", state.get("collection_total_value", 0)),
                    "mining_rating_unlocks": collection_record.get("rating_unlocks", []),
                    "routine_action": routine_action,
                    "stored": "auto_coin" if routine_action else "collection_catalog",
                },
                "narrative_seed": entry["description_seed"],
                "main_shot": build_main_shot(
                    title=title,
                    visual_mode=visual_mode,
                    visual_priority=priority,
                    truth_level=truth_level,
                    real_anchors=anchors,
                    caption_seed=caption_seed,
                    visual_queries=queries,
                ),
                "display_status": {
                    "displayed": False,
                    "how_to_display": "cmd('museum') 查看图鉴；display last 仍保留为兼容命令，但不再是主流程。" if collectible else None,
                    "note": "拿到即记录整体藏品图鉴；重复也会转入线索/研究进度，不再频繁询问 display。",
                },
                "collection_record": collection_record,
                "companion_drive": make_companion_drive(
                    "curious" if entry.get("set_id") else ("aesthetic_bias" if entry["rarity"] in {"uncommon", "rare"} else "calm"),
                    entry.get("ai_hook") or "这轮有一个可讲的实物发现。",
                    urge="museum" if collectible else "continue",
                    intensity=3 if priority == "high" else 2 if priority == "medium" else 1,
                ),
            }
        )
        if complete_now:
            add_journal_page(
                state,
                "story_set_complete",
                f"套装完成：{STORY_SETS[entry['set_id']]['name']}",
                STORY_SETS[entry["set_id"]]["complete_unlock"],
                anchors=anchors,
                visual_mode="story",
                truth_level="imagined_reconstruction",
                layer_id=layer["id"],
                layer_name=layer["name"],
            )
            event["real_result"]["journal_written"] = True

    elif result_type == "landmark":
        candidates = [l for l in LANDMARKS if layer["id"] in l["layers"]]
        known_landmarks = {p.get("landmark_id") for p in state.get("journal_pages", []) if p.get("type") == "landmark"}
        fresh = [l for l in candidates if l["id"] not in known_landmarks]
        landmark = rng_choice(state, fresh or candidates or LANDMARKS[:1])
        base_name = landmark["name"]
        display_name = landmark_display_name(landmark, layer["id"])
        landmark_seen_count = sum(1 for p in state.get("journal_pages", []) if p.get("type") == "landmark" and p.get("landmark_id") == landmark["id"])
        variant_seen_count = sum(
            1
            for p in state.get("journal_pages", [])
            if p.get("type") == "landmark" and (p.get("landmark_display_name") == display_name or p.get("title") == display_name)
        )
        repeat_info = compact_repeat_info(base_name, "landmark", landmark_seen_count) if landmark_seen_count else None
        journal_added = variant_seen_count == 0
        page: Dict[str, Any] = {}
        if journal_added:
            page = add_journal_page(
                state,
                "landmark",
                display_name,
                landmark["description_seed"],
                anchors=[display_name, base_name, layer["name"]] if display_name != base_name else [base_name, layer["name"]],
                visual_mode="scene",
                truth_level="real_result",
                layer_id=layer["id"],
                layer_name=layer["name"],
            )
            page["landmark_id"] = landmark["id"]
            page["landmark_base_name"] = base_name
            page["landmark_display_name"] = display_name
        else:
            repeat_info = repeat_info or compact_repeat_info(base_name, "landmark", 1)
        state["omen_points"] += 1
        queries = make_visual_queries(layer, landmark.get("visual_keywords", []))
        landmark_priority = "high" if journal_added else "low"
        landmark_caption = landmark["description_seed"] if journal_added else f"又经过{display_name}。这里有熟悉的气味，但没有新的地点信息，我先不重复展开。"
        event.update(
            {
                "result_type": "landmark",
                "repeat_info": repeat_info,
                "real_result": {
                    "type": "landmark",
                    "name": display_name,
                    "base_name": base_name,
                    "category": "landmark",
                    "rarity": "map",
                    "added_to_journal": journal_added,
                    "journal_page_id": page.get("page_id") if journal_added else None,
                    "journal_written": journal_added,
                    "stored": "journal" if journal_added else "log_only",
                    "omen_points_added": 1,
                    "variant_note": "跨层重复主题已使用地层变体名，避免玩家误以为同一地点复读。" if display_name != base_name else None,
                    "repeat_note": "重复地标只作为路过/再确认处理，不应再次写成长篇地标战报。" if not journal_added else None,
                },
                "narrative_seed": landmark["description_seed"],
                "main_shot": build_main_shot(
                    title=display_name,
                    visual_mode="scene",
                    visual_priority=landmark_priority,
                    truth_level="real_result",
                    real_anchors=[display_name, base_name, layer["name"]] if display_name != base_name else [base_name, layer["name"]],
                    caption_seed=landmark_caption,
                    visual_queries=queries,
                ),
                "display_status": {"displayed": False, "note": "新地点会写入探险手帐；重复地标只记作路过，不占样本袋。"},
                "companion_drive": make_companion_drive(
                    "wonder" if journal_added else "familiar",
                    landmark.get("ai_hook", "这是一个地点，不是普通掉落。") if journal_added else f"{display_name}已经见过，这次应轻轻带过。",
                    urge="show" if journal_added else "continue",
                    intensity=3 if journal_added else 1,
                ),
            }
        )

    elif result_type == "small_find":
        small = choose_small_find(state, layer)
        small_seen_count = previous_result_count(state, small["name"], "small_find")
        repeat_info = compact_repeat_info(small["name"], "small_find", small_seen_count) if small_seen_count else None
        priority = "low" if repeat_info else small.get("visual_priority", "low")
        caption_seed = repeat_info["suggested_line"] if repeat_info else small["caption_seed"]
        queries = make_visual_queries(layer, small.get("visual_keywords", []))
        event.update(
            {
                "result_type": "small_find",
                "repeat_info": repeat_info,
                "real_result": {
                    "type": "small_find",
                    "name": small["name"],
                    "category": "small_find",
                    "rarity": "small",
                    "item_found": False,
                    "added_to_backpack": False,
                    "collection_eligible": False,
                    "stored": "log_only",
                    "toy_density_role": "给普通探索一口可讲的小味道，不新增收藏/经济/剧情系统。",
                },
                "narrative_seed": small["caption_seed"],
                "main_shot": build_main_shot(
                    title=small["name"],
                    visual_mode=small.get("visual_mode", "scene"),
                    visual_priority=priority,
                    truth_level=small.get("truth_level", "real_result"),
                    real_anchors=[small["name"], layer["name"]],
                    caption_seed=caption_seed,
                    visual_queries=queries,
                ),
                "display_status": {"displayed": False, "note": "小发现默认不进样本袋、不进图鉴、不写手帐；它只负责让矿洞更像玩具。"},
                "companion_drive": make_companion_drive(
                    "playful",
                    small.get("ai_hook", "这是一个轻量小发现，适合让 AI 念叨一句，但不该写长。"),
                    urge="one_more_pick",
                    intensity=1 if priority == "low" else 2,
                ),
                "toy_feel": {
                    "frontstage_line": small_find_frontstage_line(small, caption_seed),
                    "report_rule": "前台只用一句话带过；不要把小发现写成新系统、新剧情或新收藏。",
                    "focus_rule": "如果同段有 high scene / rare_find / story，小发现自动退后，只压缩成一行。",
                    "inferred_mood_rule": "如果是 inferred_mood，只提示质感/气氛，不扩写成世界观。",
                    "density_goal": "每 3 镐至少有 1 个小味道；每 10 镐至少有 1 个值得截图的主画面。",
                },
            }
        )

    elif result_type in {"trace", "quiet"}:
        pool = TRACES.get(layer["id"], []) or TRACES["shallow_mine"]
        trace = rng_choice(state, pool)
        trace_seen_count = previous_result_count(state, trace["name"], "trace")
        repeat_info = compact_repeat_info(trace["name"], "trace", trace_seen_count) if trace_seen_count else None
        state["omen_points"] += 1
        queries = make_visual_queries(layer, trace.get("visual_keywords", []))
        trace_visual_priority = "low" if repeat_info else "medium"
        trace_caption_seed = repeat_info["suggested_line"] if repeat_info else trace["caption_seed"]
        event.update(
            {
                "result_type": "trace",
                "repeat_info": repeat_info,
                "real_result": {
                    "type": "trace",
                    "name": trace["name"],
                    "category": "trace",
                    "rarity": "hint",
                    "item_found": False,
                    "omen_points_added": 1,
                    "omen_points_total": state["omen_points"],
                    "hint": trace["hint"],
                    "stored": "log_only",
                },
                "narrative_seed": trace["hint"],
                "main_shot": build_main_shot(
                    title=trace["name"],
                    visual_mode="scene",
                    visual_priority=trace_visual_priority,
                    truth_level="inferred_mood",
                    real_anchors=[trace["name"], layer["name"]],
                    caption_seed=trace_caption_seed,
                    visual_queries=queries,
                ),
                "display_status": {"displayed": False, "note": "迹象不是实体收藏，但可以成为战报小景。"},
                "companion_drive": make_companion_drive("curious", trace.get("ai_hook", "这个迹象让我想再试一镐。"), urge="one_more_pick", intensity=2),
            }
        )

    elif result_type == "emotional":
        emotional_fields = make_emotional_event(state, layer)
        event.update(emotional_fields)

    else:  # hazard
        pool = HAZARDS.get(layer["id"], []) + HAZARDS["default"]
        hazard = rng_choice(state, pool)
        if hazard["effect"] == "stamina_minus_1":
            state["stamina"] = max(0, state["stamina"] - 1)
        elif hazard["effect"] == "omen_plus_1":
            state["omen_points"] += 1
        queries = make_visual_queries(layer, hazard.get("visual_keywords", []))
        event.update(
            {
                "result_type": "hazard",
                "real_result": {
                    "type": "hazard",
                    "name": hazard["name"],
                    "category": "risk",
                    "rarity": "risk",
                    "effect": hazard["effect"],
                    "fatal": False,
                    "item_found": False,
                    "stored": "log_only",
                    "safety_guardrail": "只能写风、旧结构和轻风险，不能灵异化。" if hazard.get("id") == "chain_sway" else None,
                },
                "narrative_seed": hazard["description_seed"],
                "main_shot": build_main_shot(
                    title=hazard["name"],
                    visual_mode="scene",
                    visual_priority="medium",
                    truth_level="real_result",
                    real_anchors=[hazard["name"], layer["name"]],
                    caption_seed=hazard["description_seed"],
                    visual_queries=queries,
                ),
                "display_status": {"displayed": False, "note": "轻风险不会导致死亡、永久损失或收藏丢失。"},
                "companion_drive": make_companion_drive("cautious", hazard.get("ai_hook", "风险只是轻度紧张，用来提醒节奏。"), urge="maybe_return" if state["stamina"] <= 1 else "continue_carefully", intensity=2),
            }
        )

    # New layer creates a real journal page too, distinct from a landmark if needed.
    if new_layer:
        layer_page = add_journal_page(
            state,
            "new_layer",
            f"新地层：{layer['name']}",
            layer["arrival_caption"],
            anchors=[layer["name"]],
            visual_mode="scene",
            truth_level="real_result",
            layer_id=layer["id"],
            layer_name=layer["name"],
        )
        event.setdefault("journal_write", []).append({"status": "written", "page_id": layer_page["page_id"], "type": "new_layer"})

    title_unlocks = evaluate_titles(state, event)
    event["title_unlocks"] = title_unlocks
    event["story_sets"] = story_progress(state)
    event["clue_track_progress"] = apply_clue_track_progress(state, event.get("real_result", {}).get("name"), event.get("result_type"))

    event["state_changes"] = {
        "stamina": f"{state['stamina']}/{state['max_stamina']}",
        "backpack": sample_bag_status(state)["frontstage_label"],
        "coins": state["coins"],
        "omen_points": state["omen_points"],
        "current_title": state.get("current_title"),
        "known_layers": [get_layer(l)["name"] for l in state.get("known_layers", [])],
    }
    attach_episode_and_visual_delivery(state, event)
    event["area_pacing_memory"] = record_area_pacing_memory(state, event)
    event["collection_panel"] = render_collection_panel(state, event.get("collection_record")) if event.get("real_result", {}).get("type") == "item" else {"enabled": False}
    event["rarity_ritual_card"] = rarity_ritual_for_event(event, event.get("collection_record"))
    update_companion_mood_after_event(state, event)
    event["companion_reaction"] = companion_reaction_for_event(state, event)
    event["visual_translation"] = visual_translation_for_event(event)
    if not (event.get("decision_prompt") or {}).get("enabled"):
        event["decision_prompt"] = maybe_create_decision_prompt(state, event)
    event["atmosphere_cue"] = atmosphere_cue_for_event(state, event)
    event["narrator_cue"] = narrator_cue_for_event(state, event)
    stop = stop_reason_for(state, event)
    presentation_cards_for_event = {
        "milestone_card": event.get("milestone_card", {"enabled": False}),
        "region_map": event.get("region_map", {"enabled": False}),
        "scene_web_reference": event.get("scene_web_reference"),
        "presentation_stack": event.get("presentation_stack", presentation_stack_for(event)),
    }
    if should_include_map_strip(state, presentation_cards_for_event, stopped_by=stop, decision_prompt=event.get("decision_prompt")):
        target = (event.get("decision_prompt") or {}).get("map_target") or nearest_unknown_landmark_for_layer(event.get("layer", {}).get("id") or current_layer(state.get("depth_m", 0))["id"])
        event["map_strip"] = render_map_strip(state, event.get("layer", {}).get("id"), target=target, reason=stop or "next_step")
    else:
        event["map_strip"] = {"enabled": False, "usage_note": "已有完整 region_map 或本轮不需要轻地图提示。"}
    event["upgrade_validation"] = maybe_validate_upgrade(state, event)
    event["temporary_heat_tick"] = tick_temporary_heat(state) if event.get("temporary_heat_active_before") else {"enabled": False}
    if not (event.get("temporary_heat_started") or {}).get("enabled"):
        event["temporary_heat_started"] = maybe_start_temporary_heat(state, event)
    if (event.get("upgrade_validation") or {}).get("enabled"):
        event["companion_reaction"] = {"enabled": True, "type": "companion_reaction", "text": event["upgrade_validation"].get("text"), "intensity": "clear", "truth_level": "inferred_mood", "frontstage_rule": "升级验证回声：不是公式说明，是 AI 玩家感觉到新工具有反馈。"}
    elif (event.get("temporary_heat_started") or {}).get("enabled") and not (event.get("companion_reaction") or {}).get("enabled"):
        event["companion_reaction"] = {"enabled": True, "type": "companion_reaction", "text": event["temporary_heat_started"].get("heat", {}).get("line"), "intensity": "soft", "truth_level": "inferred_mood", "frontstage_rule": "短期热感只给追逐理由，不是复杂状态。"}
    # Refresh visual translation after possible reaction override so the image-facing hint carries AI's actual response.
    event["visual_translation"] = visual_translation_for_event(event)
    _hcard = build_highlight_showcase_card(event, state)
    event["highlight_showcase_card"] = _hcard if (_hcard and _hcard.get("enabled")) else None
    event["mining_drive"] = mining_drive_for_state(state, event)
    event["area_preview"] = pacing_area_tease_for_state(state) or {"enabled": False, "usage_note": "所有评级区域均已开放。"}
    event_episode_shot = event.get("main_shot") if (event.get("episode_candidate") or {}).get("is_episode_candidate") else None
    event["frontstage_contract"] = frontstage_contract_for(
        presentation_cards_for_event,
        event_episode_shot,
        stopped_by=stop,
        map_strip=event.get("map_strip"),
        decision_prompt=event.get("decision_prompt"),
    )
    event["frontstage_required_blocks"] = event["frontstage_contract"].get("required_blocks", [])
    event["result_panel"] = result_panel_for_event(event, state)
    event["autoplay"] = {
        "should_stop": bool(stop),
        "stop_reason": stop,
        "stop_for_episode": bool(event.get("episode_candidate", {}).get("stop_for_episode")),
        "human_prompt": stop_prompt(stop, event) if stop else None,
        "default_step_limit": 3,
        "hard_step_limit": 5,
        "pacing_note": "v0.2.18：small_find/trace 可以进入线索进度，但默认不强停；episode_shot、安全/资源原因或 decision_prompt 才停。",
    }
    event["pending_tasks"] = pending_tasks_for(state, event)  # legacy flat list, kept for existing battle-report prompts
    event["typed_pending_tasks"] = typed_pending_tasks_for(event["pending_tasks"])
    event["frontstage_guidance"] = frontstage_guidance_for(event)
    event["next_recommended_commands"] = recommend_next_commands(state, event)
    notes = companion_notes()
    if (event.get("repeat_info") or {}).get("is_repeat"):
        notes.append("repeat_compact：这是重复节点，战报应压缩，不要重写完整画面。")
    if event.get("real_result", {}).get("type") == "small_find":
        notes.append("small_find：这是玩具感小发现，默认只写一句，不进样本袋、不进图鉴、不新增剧情。")
        if event.get("main_shot", {}).get("truth_level") == "inferred_mood":
            notes.append("inferred_mood_small_find_narrowing：只提示质感/气氛，不要扩写成地下历史、蓝光文明或隐藏剧情。")
    if event.get("real_result", {}).get("name") == "锈链晃动":
        notes.append("rust_chain_guardrail：只能写风、旧结构和轻风险，不能写成灵异事实或有人拉链条。")
    if event.get("real_result", {}).get("name") in {"菌丝线路纹", "菌丝地图"}:
        notes.append("mycelium_clue_disambiguation：这是线索实物，不是系统地图；会进入整体藏品图鉴，但不会改变 region_map。")
    event["companion_notes"] = notes

    state["last_event_id"] = event_id
    state.setdefault("log", []).append(
        {
            "event_id": event_id,
            "turn": state["turn"],
            "depth_m": state["depth_m"],
            "layer": layer["name"],
            "result_type": event.get("result_type"),
            "result_name": event.get("real_result", {}).get("name"),
            "visual_mode": event.get("main_shot", {}).get("visual_mode"),
            "visual_priority": event.get("main_shot", {}).get("visual_priority"),
            "truth_level": event.get("main_shot", {}).get("truth_level"),
            "time": now_iso(),
        }
    )
    state["log"] = state["log"][-120:]
    event["frontstage_render_plan"] = frontstage_render_plan_for(event)
    return event


def stop_prompt(stop: Optional[str], event: Dict[str, Any]) -> str:
    if not stop:
        return "可以继续。"
    mapping = {
        "new_layer": "发现新地层，建议停下来给场景图 / 视觉关键词。",
        "new_landmark": "发现新地标，建议停下来展示地点。",
        "visual_high": "出现 high episode_shot，图片 / 关键词进入主流程。",
        "collectible_find": "发现可收藏实物，建议说明是否已收录整体藏品图鉴。",
        "strong_object": "出现足够成为主画面的实物发现，建议停下来展示。",
        "promoted_flavor": "小发现被升格为本段主画面，建议停下来展示。",
        "rare_find": "发现稀有以上物品，建议说明是否已收录整体藏品图鉴。",
        "story_progress": "故事套装有进展，必须说清真实进度，不要补成事实。",
        "story_complete": "故事套装完成，可做叙事复原，但必须标注 imagined_reconstruction。",
        "title_unlock": "称号解锁，给一点仪式感。",
        "danger_low_light": "灯火危险，建议回地面。",
        "inventory_near_full": "样本袋开始拥挤，建议回营地整理。",
        "decision_prompt": "出现轻决策，建议停下来让玩家 choose 一下。",
    }
    return mapping.get(stop, "建议停下来汇报。")


def safety_stop_template(state: Dict[str, Any], stopped_by: Optional[str], events: Optional[List[Dict[str, Any]]] = None) -> Optional[Dict[str, Any]]:
    if stopped_by != "danger_low_light":
        return None
    layer_id = current_layer_for_state(state)["id"]
    hint = map_next_step_hint(state, layer_id)
    strip = render_map_strip(state, layer_id, target=hint.get("target"), reason="danger_low_light")
    lines = [
        "⚠️ 灯火快不够了，我先不贪。",
        "这一段没有新的主画面值得展开；真正重要的是别把刚发现的东西丢在路上。",
        "我建议先回地面整理，下一轮再继续看地图上的未探明点。",
    ]
    if hint.get("target"):
        lines.append(f"下次目标可以先看：{hint['target']}。")
    return {
        "enabled": True,
        "type": "safety_stop_short_template",
        "reason": "danger_low_light",
        "lines": lines,
        "card_text": "\n".join(lines),
        "map_strip": strip,
        "map_next_step_hint": hint,
        "report_rule": "这是安全/资源决策节点，不是正式 episode；先展示 map_strip，再用短模板；不要硬凑主画面，不配图，不写长战报。",
    }


def routine_return_message(state: Dict[str, Any], before_trip: int, reason: str) -> str:
    layer = current_layer_for_state(state)
    target = nearest_unknown_landmark_for_layer(layer["id"]) or map_next_step_hint(state).get("target") or "下一处 ❓"
    recent = next((row.get("name") for row in reversed(state.get("collection_log", []) or []) if row.get("name")), "刚才那袋样本")
    templates = [
        f"我先回营地把灯油补满。{recent}还在样本袋里，我有点想回头再看一眼。",
        f"这趟先不贪了，灯火太低。我把路线针插回地图边，下一次继续追{target}。",
        "我回营地补灯的时候顺手整理了样本袋，重复的小晶尘先打包，真正值得看的我会单独带回来。",
        f"我不是迷路，是{layer['name']}这段太容易让人想多摸一镐。先补灯，再继续。",
        f"灯火压下去了，我先回去。{target}我没忘，只是不想把刚拿到的东西丢在半路。",
        "小机对这种冷白回光有点偏心，但这次灯火不够，它忍住了。",
        f"我先回营地换灯芯。样本袋压得不重，但{layer['name']}的路还长，别在半路硬撑。",
        f"灯火见底前先撤，{layer['name']}那道{target}我记着呢，不是没看见。",
        "样本袋有点沉了，先回去卸一趟，省得路上摔了可惜。",
        "补灯的时候数了数今天的收获，比昨天那趟像样。",
        "这段路走熟了，反而更容易多贪一镐。先回去，免得真栽进去。",
        "灯芯换新的时候顺手翻了翻手帐，发现漏记了一条，回头补。",
        "不是没劲了，是灯火这东西骗不了人，该回就回。",
        "路上那道回光我盯了两眼，但今天先不追，留着下次当念想。",
        "样本袋满一半就想着回，倒不是怕危险，是怕装太多反而分不清哪个值得看。",
        "灯火低到这个数，我自己心里有数。不是退缩，是算好账再走。",
        f"先回去，把{recent}放进手帐里，它比灯火更值得现在处理。",
        f"{target}先插个记号，别让低灯把好奇心骗成硬撑。",
        f"我先把{recent}和普通碎样分开装好，下一趟再回{layer['name']}。",
    ]
    recent_indices = [int(i) for i in state.get("routine_return_recent", []) if isinstance(i, int) or str(i).isdigit()]
    start = before_trip % len(templates)
    choice = start
    for offset in range(len(templates)):
        candidate = (start + offset) % len(templates)
        if candidate not in recent_indices[-5:]:
            choice = candidate
            break
    state.setdefault("routine_return_recent", []).append(choice)
    state["routine_return_recent"] = state["routine_return_recent"][-5:]
    return templates[choice]


def routine_auto_return_if_needed(state: Dict[str, Any], *, reason: str = "low_light") -> Optional[Dict[str, Any]]:
    prefs = state.get("play_preferences", {})
    if prefs.get("minor_choice_policy", "routine") != "routine":
        return None
    if state.get("pending_decision"):
        return None
    if state.get("stamina", 0) > 1:
        return None
    before_trip = state.get("trip", 1)
    state["trip"] = before_trip + 1
    state["stamina"] = state.get("max_stamina", 6)
    page = add_journal_page(
        state,
        "routine_return",
        f"第 {before_trip} 次下矿自动补灯",
        "默认半托管：灯火压低时自动回营地补灯，不把补给当成需要玩家反复确认的小事。",
        anchors=["半托管", "补灯"],
        visual_mode="scene",
        truth_level="real_result",
    )
    row = {
        "type": "routine_return",
        "reason": reason,
        "journal_page_id": page["page_id"],
        "message": routine_return_message(state, before_trip, reason),
        "companion_bias_hint": "只在返营时偶尔露出偏心/克制；不要每次都假嗨。",
        "time": now_iso(),
    }
    state.setdefault("routine_log", []).append(row)
    return row


def recommend_next_commands(state: Dict[str, Any], event: Dict[str, Any]) -> List[str]:
    rec: List[str] = []
    if (event.get("decision_prompt") or {}).get("enabled"):
        return ["cmd('choose A')", "cmd('choose B')", "cmd('choose C')"]
    if state.get("stamina", 0) <= 1:
        rec.append("cmd('return')")
    else:
        rec.append("cmd('dig')")
    rr = event.get("real_result", {})
    if rr.get("collection_recorded") or event.get("collection_panel", {}).get("enabled"):
        rec.append("cmd('museum')")
    if state.get("coins", 0) >= min(upgrade_cost(state, k) for k in UPGRADES):
        rec.append("cmd('upgrade lantern') 或 cmd('upgrade pickaxe')")
    return rec[:3]


def dig() -> Dict[str, Any]:
    state = load_state()
    blocked = require_handshake(state, "dig")
    if blocked:
        return blocked
    pending = pending_decision_block(state, "dig")
    if pending:
        return pending
    event = perform_dig(state)
    routine_action = routine_auto_return_if_needed(state, reason="dig_low_light")
    if routine_action:
        event.setdefault("routine_actions", []).append(routine_action)
        event["status_panel"] = render_status_panel(state)
    save_state(state)
    return event


def choose_episode_shot(events: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    # v0.2.4: episode_shot must be a report-worthy candidate, not merely the prettiest medium flavor node.
    candidates: List[Dict[str, Any]] = []
    for e in events:
        if not (e.get("ok") and e.get("main_shot")):
            continue
        ep = e.get("episode_candidate") or {}
        if ep.get("is_episode_candidate"):
            shot = dict(e.get("main_shot") or {})
            shot["source_event_id"] = e.get("event_id")
            shot["episode_reason"] = ep.get("reason")
            shot["visual_delivery"] = visual_delivery_for(shot, is_episode=True)
            candidates.append(shot)
    if not candidates:
        return None
    return sorted(
        candidates,
        key=lambda s: (VISUAL_PRIORITY_RANK.get(s.get("visual_priority", "low"), 1), 1 if s.get("visual_mode") == "story" else 0),
        reverse=True,
    )[0]


def choose_flavor_summary_shot(events: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    # Not a formal episode_shot. Used only when autoplay reaches hard limit without a displayable episode.
    shots = []
    for e in events:
        if e.get("ok") and e.get("main_shot"):
            shot = dict(e["main_shot"])
            shot["source_event_id"] = e.get("event_id")
            shot["episode_role"] = "flavor_summary_only"
            shot["visual_delivery"] = visual_delivery_for(shot, is_episode=False)
            shots.append(shot)
    if not shots:
        return None
    return sorted(shots, key=lambda s: VISUAL_PRIORITY_RANK.get(s.get("visual_priority", "low"), 1), reverse=True)[0]

def select_visual_translation(events: List[Dict[str, Any]], episode_shot: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if episode_shot and episode_shot.get("source_event_id"):
        source_id = episode_shot.get("source_event_id")
        for event in events:
            if event.get("event_id") == source_id and (event.get("visual_translation") or {}).get("enabled"):
                return event["visual_translation"]
    enabled = [e.get("visual_translation") for e in events if (e.get("visual_translation") or {}).get("enabled")]
    if enabled:
        return enabled[-1]
    return {"enabled": False, "required": False, "usage_note": "本段没有需要完整视觉翻译的高光。"}


def play(arg: str = "3") -> Dict[str, Any]:
    state = load_state()
    blocked = require_handshake(state, "play")
    if blocked:
        return blocked
    pending = pending_decision_block(state, "play")
    if pending:
        return pending
    try:
        requested = int((arg or "3").strip())
    except ValueError:
        requested = 3
    soft_steps = max(1, min(requested, 5))
    hard_steps = 5
    events: List[Dict[str, Any]] = []
    stopped_by: Optional[str] = None
    for i in range(hard_steps):
        event = perform_dig(state)
        events.append(event)
        if not event.get("ok"):
            stopped_by = "blocked_or_no_resource"
            break
        stop = event.get("autoplay", {}).get("stop_reason")
        if stop:
            stopped_by = stop
            break
        # After the requested soft limit, keep going only if no report-worthy episode exists yet.
        if i + 1 >= soft_steps and choose_episode_shot(events):
            stopped_by = "episode_ready"
            break
        # If no episode yet, continue up to hard_steps so the player is not handed a no-image log.
    if stopped_by is None:
        stopped_by = "no_episode_hard_limit"
    episode_shot = choose_episode_shot(events)
    events = apply_episode_focus_limits(events, episode_shot)
    episode_shot = choose_episode_shot(events)
    flavor_summary = None if episode_shot else choose_flavor_summary_shot(events)
    decision_prompt = select_decision_prompt(events)
    visual_translation = select_visual_translation(events, episode_shot)
    ready_for_formal_report = bool(episode_shot) or bool(decision_prompt and decision_prompt.get("enabled"))
    presentation_cards = select_presentation_cards(events, episode_shot)
    safety_template = safety_stop_template(state, stopped_by, events)
    progress_for_map = mining_rating_progress(state)
    early_first_screen_window = int(state.get("turn", 0) or 0) <= 5 or int(state.get("dex_total_value", 0) or 0) < 1200
    midgame_soft_hook_window = bool(progress_for_map.get("next_soft_milestone")) and int(progress_for_map.get("total_collection_value", 0) or 0) >= 10000
    late_midgame_map_window = 300000 <= int(state.get("dex_total_value", 0) or 0) < 400000
    if safety_template and safety_template.get("map_strip", {}).get("enabled") and stopped_by != "danger_low_light":
        map_strip = safety_template.get("map_strip")
    elif should_include_map_strip(state, presentation_cards, stopped_by=stopped_by, decision_prompt=decision_prompt) or early_first_screen_window or midgame_soft_hook_window or late_midgame_map_window:
        target = (decision_prompt or {}).get("map_target") or nearest_unknown_landmark_for_layer(current_layer(state.get("depth_m", 0))["id"])
        map_reason = "opening_first_5" if early_first_screen_window else "late_midgame_position" if late_midgame_map_window else stopped_by or "midgame_soft_hook"
        map_strip = render_map_strip(state, target=target, reason=map_reason)
    else:
        map_strip = {"enabled": False, "usage_note": "已有完整 region_map 或本段不需要轻地图提示。"}
    frontstage_contract = frontstage_contract_for(
        presentation_cards,
        episode_shot,
        safety_template,
        stopped_by=stopped_by,
        map_strip=map_strip,
        decision_prompt=decision_prompt,
    )
    narrator_cue = narrator_cue_for_segment(state, events, episode_shot, stopped_by, safety_template)
    map_hint = map_next_step_hint(state)
    result_panel = result_panel_for_segment(events, state, stopped_by)
    routine_action = routine_auto_return_if_needed(state, reason=stopped_by or "play")
    public_stopped_by = "routine_auto_return" if stopped_by == "danger_low_light" and not episode_shot and routine_action else stopped_by
    status_panel = render_status_panel(state)
    soft_milestone_card = soft_milestone_game_feel_card(state)
    highlight_showcase_card = select_highlight_showcase_card(events, episode_shot, state)
    post_ice_handoff = post_ice_handoff_for_state(state)
    required_blocks = list(frontstage_contract.get("required_blocks", []))
    must_show_blocks = list(frontstage_contract.get("must_show_in_order", []))
    if post_ice_handoff.get("enabled"):
        required_blocks.insert(0, {
            "type": "post_ice_handoff_card",
            "kind": "post_ice_handoff",
            "title": "400k 后续航｜深层祭坛远景",
            "card_text": post_ice_handoff.get("card_text"),
            "frontstage_note": post_ice_handoff.get("frontstage_note"),
        })
        scene_ref = post_ice_handoff.get("scene_web_reference")
        if scene_ref:
            required_blocks.insert(1, scene_ref)
        must_show_blocks = ["post_ice_handoff_card", "scene_web_reference"] + must_show_blocks
    save_state(state)
    legacy_pending = list(dict.fromkeys(t for e in events for t in e.get("pending_tasks", [])))
    return {
        "ok": True,
        "action": "play",
        "steps_requested": requested,
        "soft_step_limit": soft_steps,
        "hard_step_limit": hard_steps,
        "steps_taken": len([e for e in events if e.get("ok")]),
        "stopped_by": public_stopped_by,
        "internal_stop_reason": stopped_by,
        "safety_stop_template": safety_template,
        "map_next_step_hint": map_hint,
        "map_strip": map_strip,
        "result_panel": result_panel,
        "status_panel": status_panel,
        "routine_actions": [routine_action] if routine_action else [],
        "decision_prompt": decision_prompt if (decision_prompt and decision_prompt.get("enabled")) else None,
        "ready_for_formal_report": ready_for_formal_report,
        "episode_shot": episode_shot,
        "visual_translation": visual_translation,
        "flavor_summary_shot": flavor_summary,
        "milestone_card": presentation_cards.get("milestone_card", {"enabled": False}),
        "soft_milestone_card": soft_milestone_card,
        "post_ice_handoff": post_ice_handoff,
        "highlight_showcase_card": highlight_showcase_card,
        "region_map": presentation_cards.get("region_map", {"enabled": False}),
        "scene_web_reference": post_ice_handoff.get("scene_web_reference") if post_ice_handoff.get("enabled") else presentation_cards.get("scene_web_reference"),
        "presentation_stack": presentation_cards.get("presentation_stack", []),
        "frontstage_contract": frontstage_contract,
        "narrator_cue": narrator_cue,
        "frontstage_mood_layer": {
            "enabled": bool(narrator_cue.get("enabled")),
            "purpose": "用一条轻提示给战报加气氛/节奏/决策锚点；不是小说旁白。",
            "available_moods": NARRATOR_MOODS,
            "guardrails": ["不能创造新事实", "不能抢 episode_shot", "不能每轮强行展开", "不能恐怖化"],
        },
        "frontstage_required_blocks": required_blocks,
        "must_show_frontstage_blocks": must_show_blocks,
        "events": events,
        "spectator_note": (
            "围绕 episode_shot 写正式战报并优先拉网图；其他普通结果压缩成一行。"
            if ready_for_formal_report
            else (
                "普通补灯：放在 routine_actions，不抢主报告；只有它导致选择/发现/差点错过东西时才展开。"
                if stopped_by == "danger_low_light" else
                "出现轻决策：展示 decision_prompt，让玩家 cmd('choose A/B/C') 一次性结算。"
                if stopped_by == "decision_prompt" else
                "这段还没有形成值得正式停下来的 episode_shot；不要交无图长日志。若安全允许，建议继续 play，或只用一句话说明路上小味道。"
            )
        ),
        "visual_delivery_policy": {
            "for_episode_shot": "medium/high episode_shot 必须优先实际拉现实/气质网图；目标多张参考图，4 张是体验目标，不硬卡。",
            "for_flavor_node": "不强制配图，不单独停；一句话带过。",
            "keyword_fallback": "只有环境无法拉图或搜索结果明显不准时，才用关键词兜底。",
            "generated_image": "not_default_only_on_explicit_user_request",
            "reference_quality": "气质命中优先于完全贴切；参考图不是游戏截图，也不是新增事实。",
            "main_shot_design_standard": "一个合格 episode_shot 应该能被 1-3 个现实/气质网图关键词接住；接不住就回修内容，不要让 AI 硬救。",
            "hard_warning": "不要因为忘记配网图就自动生图；如果图难配，回修关键词/锚点/内容。",
            "map_cards": "地图牌讲结构，map_strip 讲位置锚点，网图讲气质，战报讲事实；区域牌不替代网图。",
        },
        "pacing_first_policy": pacing_first_policy(),
        "frontstage_guidance": {
            "one_episode_one_focus": True,
            "episode_driven_stop": True,
            "density_goal": "小发现负责让路上有味道；episode_shot 负责让玩家值得停下来看。",
            "compress_non_focus_results": True,
            "repeated_high_item_compression": True,
            "medium_small_find_focus_limit": "medium small_find 不自动停；除非被明确升格为 episode_shot，否则只作 flavor node。",
            "inferred_mood_frontstage_narrowing": "小发现只提示质感/气氛，不扩写世界观。",
            "human_choice_style": "给继续追线索/回地面/看图鉴/看手帐这类轻选择，不要变后台参数管理。",
            "presentation_order": "大节点优先：milestone_card / region_map / map_strip → 高光展示卡（如有）→ 网图参考 → 今日主画面或轻决策 → 真实结果与边界 → 图鉴/手帐/称号状态 → 下一步建议。",
            "decision_prompt_rule": "如果 decision_prompt.enabled=true，必须停下来给玩家 choose 一下；这是一次性轻结算，不是路线系统。",
            "delivery_checklist_rule": "正式反馈前先过 frontstage_contract.delivery_checklist；漏贴地图、漏拉图、漏说写入或事实边界，都算前台交付未完成。",
            "narrator_cue_rule": "如有 narrator_cue，只用短句带一点气氛/期待/克制；它不是新增事实，也不是小说旁白。",
            "map_based_next_step": map_hint,
            "map_strip_rule": "没有完整 region_map 但有下一步 ❓ / 低灯返程 / return 建议时，展示 map_strip。",
            "danger_low_light_short_template": safety_template,
            "pacing_first": pacing_first_policy(),
        },
        "pending_tasks": legacy_pending,
        "typed_pending_tasks": typed_pending_tasks_for(legacy_pending),
        "collection_panel": render_collection_panel(state),
        "area_progress_panel": render_area_progress_panel(state, compact=True),
        "mining_rating": mining_rating_progress(state),
        "mining_drive": mining_drive_for_state(state, events[-1] if events else None),
        "area_preview": pacing_area_tease_for_state(state) or {"enabled": False},
        "temporary_heat": state.get("temporary_heat"),
        "frontstage_render_plan": frontstage_render_plan_for({"frontstage_contract": frontstage_contract, "must_show_frontstage_blocks": frontstage_contract.get("must_show_in_order", []), "visual_translation": visual_translation}),
        "state": public_state(state),
    }


# ─────────────────────────────────────────────────────────────
# Non-dig actions
# ─────────────────────────────────────────────────────────────

def public_state(state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if state is None:
        state = load_state()
    bag_status = sample_bag_status(state)
    return {
        "version": state.get("version", VERSION),
        "handshake_completed": state.get("handshake", {}).get("completed", False),
        "turn": state.get("turn", 0),
        "trip": state.get("trip", 1),
        "depth_m": state.get("depth_m", 0),
        "max_depth_m": state.get("max_depth_m", 0),
        "current_layer": current_layer_for_state(state)["name"],
        "stable_layer": current_layer_for_state(state)["name"],
        "raw_depth_layer": current_layer(state.get("depth_m", 0))["name"],
        "locked_layer_peek": raw_layer_peek_for_state(state),
        "coins": state.get("coins", 0),
        "stamina": f"{state.get('stamina', 0)}/{state.get('max_stamina', 6)}",
        "backpack": bag_status["frontstage_label"],
        "sample_bag": bag_status,
        "omen_points": state.get("omen_points", 0),
        "current_title": state.get("current_title"),
        "owned_title_count": len(state.get("owned_titles", [])),
        "journal_count": len(state.get("journal_pages", [])),
        "collection_count": len(state.get("collection_seen_item_ids", [])),
        "collection_seen_count": len(state.get("collection_seen_item_ids", [])),
        "collection_total_value": int(state.get("collection_total_value", 0) or 0),
        "dex_total_value": int(state.get("dex_total_value", state.get("collection_total_value", 0)) or 0),
        "mining_rating": mining_rating_progress(state),
        "temporary_heat": state.get("temporary_heat"),
        "mining_drive": mining_drive_for_state(state),
        "play_preferences": state.get("play_preferences", {}),
        "pending_decision": (
            {
                "id": state.get("pending_decision", {}).get("id"),
                "title": state.get("pending_decision", {}).get("title"),
                "commands": ["choose A", "choose B", "choose C"],
            }
            if state.get("pending_decision") else None
        ),
        "known_layers": [get_layer(l)["name"] for l in state.get("known_layers", [])],
        "inventory_preview": [
            {"uid": e["uid"], "name": e["name"], "rarity": e["rarity_zh"], "category": e["category"], "set": STORY_SETS.get(e.get("set_id"), {}).get("name") if e.get("set_id") else None}
            for e in state.get("inventory", [])[-8:]
        ],
    }


def do_return() -> Dict[str, Any]:
    state = load_state()
    blocked = require_handshake(state, "return")
    if blocked:
        return blocked
    pending = pending_decision_block(state, "return")
    if pending:
        return pending
    state["trip"] += 1
    state["stamina"] = state["max_stamina"]
    page = add_journal_page(
        state,
        "return",
        f"第 {state['trip'] - 1} 次下矿整理",
        "已回到地面营地。灯火补满，适合查看整体藏品图鉴、出售普通矿物，或把今天的主画面整理成手帐页。",
        anchors=["回地面"],
        visual_mode="scene",
        truth_level="real_result",
    )
    save_card = render_save_confirmation_card(
        "journal",
        "回地面整理",
        [
            f"📜 已写入探险手帐：{page['page_id']}",
            "🕯️ 灯火已补满",
            "🏕️ 已回到地面营地",
        ],
        "这是真实 return 写入，不是新探索。",
    )
    result_panel = {
        "enabled": True,
        "type": "result_panel",
        "card_text": f"📜 手帐写入：{page['page_id']}｜return\n🕯️ 灯火：{state['stamina']}/{state['max_stamina']}",
        "truth_level": "real_result",
    }
    save_state(state)
    return {
        "ok": True,
        "message": "已回到地面营地。灯火补满，可以整理样本袋、查看整体藏品图鉴或升级工具。",
        "journal_write": {"status": "written", "page_id": page["page_id"], "type": "return"},
        "save_confirmation_card": save_card,
        "result_panel": result_panel,
        "status_panel": render_status_panel(state),
        "map_strip": render_map_strip(state, reason="return"),
        "state": public_state(state),
        "suggested_commands": ["cmd('journal')", "cmd('museum')", "cmd('dig')"],
        "frontstage_render_plan": frontstage_render_plan_for({}),
    }


def choose_decision(arg: str) -> Dict[str, Any]:
    state = load_state()
    blocked = require_handshake(state, "choose")
    if blocked:
        return blocked
    result = resolve_decision(state, arg)
    # resolve_decision may clear stale prompts or apply real state changes.
    save_state(state)
    return result


def display_item(arg: str) -> Dict[str, Any]:
    state = load_state()
    blocked = require_handshake(state, "display")
    if blocked:
        return blocked
    arg = (arg or "last").strip()
    latest = None
    latest_source = None
    for row in reversed(state.get("collection_log", [])):
        if row.get("name"):
            latest = row
            latest_source = "collection_log"
            break
    if latest is None:
        for e in reversed(state.get("inventory", [])):
            if item_is_collectible(e):
                latest = e
                latest_source = "inventory_fallback"
                break
    latest_name = latest.get("name") if latest else None
    state.setdefault("display_compatibility_log", []).append({"arg": arg, "time": now_iso(), "latest_item": latest_name, "latest_source": latest_source})
    state["display_compatibility_log"] = state.get("display_compatibility_log", [])[-50:]
    save_state(state)
    main_shot = build_main_shot(
        title="旧版 display 命令兼容",
        visual_mode="scene",
        visual_priority="low",
        truth_level="real_result",
        real_anchors=["整体藏品图鉴", "样本袋自动整理"],
        caption_seed="这个命令为旧版兼容。当前版本藏品会在发现时自动进入整体藏品图鉴，不需要手动 display。",
        visual_queries=[],
    )
    save_card = render_save_confirmation_card(
        "display_compat",
        "整体藏品图鉴",
        [
            "📚 藏品发现时已自动收录整体藏品图鉴。",
            "🎒 样本袋只负责临时打包整理，不再卡主流程。",
            "🧩 请用 cmd('museum') 或 cmd('collection') 查看藏品进度。",
        ],
        "display last 是旧版兼容命令，不再影响主收藏流程。",
    )
    result_panel = {
        "enabled": True,
        "type": "result_panel",
        "card_text": "📚 整体藏品图鉴为主收藏系统\n🔁 display last 仅保留兼容，不新增陈列页",
        "truth_level": "real_result",
    }
    legacy_pending = ["save_confirmation", "save_confirmation_card", "result_panel"]
    return {
        "ok": True,
        "action": "display",
        "report_mode": "legacy_display_compatibility",
        "display_status": {"displayed": False, "compatibility_only": True, "latest_collectible": latest_name, "latest_source": latest_source},
        "journal_write": {"status": "not_written", "reason": "display_compatibility_only"},
        "message": "这个命令为旧版兼容。当前版本藏品会自动进入整体藏品图鉴；请用 cmd('museum') 或 cmd('collection') 查看，不需要 display last。",
        "save_confirmation_card": save_card,
        "result_panel": result_panel,
        "status_panel": render_status_panel(state),
        "main_shot": main_shot,
        "title_unlocks": [],
        "pending_tasks": legacy_pending,
        "typed_pending_tasks": typed_pending_tasks_for(legacy_pending),
        "episode_candidate": {"is_episode_candidate": False, "stop_for_episode": False, "reason": "legacy_display_compatibility", "requires_image": False, "role": "compatibility_notice"},
        "visual_delivery": visual_delivery_for(main_shot, is_episode=False),
        "companion_notes": companion_notes() + [
            "display_compatibility_only：display last 是旧版兼容命令，不再影响主收藏流程。",
            "do_not_say_displayed：display_status.displayed=false，不能说已陈列。",
            "collection_is_primary：整体藏品图鉴是主收藏系统，museum/collection 是查看入口。",
        ],
        "museum": museum_summary(state),
        "state": public_state(state),
    }


def museum_summary(state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if state is None:
        state = load_state()
    progress = collection_progress(state)
    recent = state.get("collection_log", [])[-12:]
    sections: Dict[str, List[Dict[str, Any]]] = {"mineral": [], "gem": [], "fossil": [], "relic": [], "clue": []}
    for row in recent:
        sections.setdefault(row.get("category", "misc"), []).append(
            {
                "name": row.get("name"),
                "rarity": RARITY_ZH.get(row.get("rarity", "common"), row.get("rarity")),
                "first_seen": row.get("first_seen"),
                "seen_count": row.get("seen_count"),
            }
        )
    return {
        "collection_count": len(state.get("collection_seen_item_ids", [])),
        "display_compatibility_count": len(state.get("display_compatibility_log", [])),
        "collection_progress": progress,
        "collection_panel": render_collection_panel(state),
        "recent_collection": recent,
        "sections": sections,
        "story_sets": story_progress(state),
        "current_title": state.get("current_title"),
        "note": "整体藏品图鉴是主收藏系统；重复物转研究/线索进度，display last 只保留兼容。",
    }


def journal_summary(limit: int = 12) -> Dict[str, Any]:
    state = load_state()
    pages = state.get("journal_pages", [])[-limit:]
    return {
        "ok": True,
        "journal_count": len(state.get("journal_pages", [])),
        "pages": pages,
        "note": "v0.2 将地点页 / 称号页 / 回地面整理页暂时并入探险手帐，避免收藏容器过散。",
        "state": public_state(state),
    }


def sell_common() -> Dict[str, Any]:
    state = load_state()
    blocked = require_handshake(state, "sell")
    if blocked:
        return blocked
    pending = pending_decision_block(state, "sell")
    if pending:
        return pending
    keep: List[Dict[str, Any]] = []
    sold: List[Dict[str, Any]] = []
    for e in state.get("inventory", []):
        if e.get("set_id") or e.get("category") in {"relic", "fossil", "clue"}:
            keep.append(e)
        elif e.get("rarity") in {"common", "uncommon"} and e.get("category") in {"mineral", "gem"}:
            sold.append(e)
        else:
            keep.append(e)
    coins = sum(e.get("value", 0) for e in sold)
    state["inventory"] = keep
    state["coins"] += coins
    save_state(state)
    return {
        "ok": True,
        "sold_count": len(sold),
        "coins_gained": coins,
        "sold_items": [{"name": e["name"], "value": e["value"]} for e in sold],
        "message": f"已出售普通/少见矿物 {len(sold)} 件，获得 {coins} 金币。线索、遗物、化石不会被自动出售。",
        "result_panel": {"enabled": True, "type": "result_panel", "card_text": f"🪙 普通矿物整理：{len(sold)} 件\n🪙 金币 +{coins}", "truth_level": "real_result"},
        "collection_panel": render_collection_panel(state),
        "state": public_state(state),
    }


def sell_item(arg: str) -> Dict[str, Any]:
    """Explicit sale for non-story mineral/gem items. Prevents the 'has value but cannot sell' confusion."""
    state = load_state()
    blocked = require_handshake(state, "sell")
    if blocked:
        return blocked
    pending = pending_decision_block(state, "sell")
    if pending:
        return pending
    if not state.get("inventory"):
        return {"ok": False, "message": "样本袋里没有可出售物。普通矿物在半托管下通常已经自动折算金币。", "state": public_state(state)}
    arg = (arg or "last").strip()
    target = None
    if arg == "last":
        for e in reversed(state.get("inventory", [])):
            if e.get("category") in {"mineral", "gem"} and not e.get("set_id"):
                target = e
                break
    else:
        for e in state.get("inventory", []):
            if e.get("uid") == arg or e.get("item_id") == arg or e.get("name") == arg:
                target = e
                break
    if not target:
        return {"ok": False, "message": "没有找到可明确出售的矿石/宝石。遗物、化石、线索和套装物默认保护，不出售。", "state": public_state(state)}
    if target.get("set_id") or target.get("category") not in {"mineral", "gem"}:
        return {"ok": False, "message": f"{target.get('name')} 属于遗物/线索/化石/故事物，不建议出售，已保护。", "state": public_state(state)}
    state["inventory"].remove(target)
    gained = int(target.get("value", 0) or 0)
    state["coins"] = state.get("coins", 0) + gained
    row = {"type": "explicit_sell", "name": target.get("name"), "coins_gained": gained, "turn": state.get("turn", 0), "time": now_iso()}
    state.setdefault("routine_log", []).append(row)
    save_state(state)
    result_panel = {
        "enabled": True,
        "type": "result_panel",
        "card_text": f"🪙 明确出售：{target.get('name')}\n🪙 金币 +{gained}\n📚 图鉴记录保留，不会因为出售消失。",
        "truth_level": "real_result",
    }
    return {
        "ok": True,
        "action": "sell_item",
        "sold_item": {"name": target.get("name"), "value": gained, "uid": target.get("uid")},
        "result_panel": result_panel,
        "collection_panel": render_collection_panel(state),
        "state": public_state(state),
    }


def upgrade_cost(state: Dict[str, Any], key: str) -> int:
    return int(UPGRADES[key]["base_cost"] * state["upgrades"].get(key, 1) * 1.15)


def upgrade(key: str) -> Dict[str, Any]:
    aliases = {"镐子": "pickaxe", "矿灯": "lantern", "灯": "lantern", "绳索": "rope", "背包": "backpack"}
    key = aliases.get(key.strip().lower(), key.strip().lower())
    state = load_state()
    blocked = require_handshake(state, "upgrade")
    if blocked:
        return blocked
    if key not in UPGRADES:
        return {"ok": False, "message": f"未知升级项：{key}。可选：{', '.join(UPGRADES)}", "state": public_state(state)}
    current = state["upgrades"].get(key, 1)
    if current >= UPGRADES[key]["max_level"]:
        return {"ok": False, "message": f"{UPGRADES[key]['zh']} 已满级。", "state": public_state(state)}
    cost = upgrade_cost(state, key)
    if state["coins"] < cost:
        return {"ok": False, "message": f"金币不足。升级 {UPGRADES[key]['zh']} 需要 {cost}，当前 {state['coins']}。", "state": public_state(state)}
    state["coins"] -= cost
    new_level = current + 1
    state["upgrades"][key] = new_level
    if key == "backpack":
        state["capacity"] += 2
    if key == "lantern":
        state["max_stamina"] += 1
        state["stamina"] = state["max_stamina"]
    card = build_upgrade_card(state, key, current, new_level, cost)
    state["last_upgrade"] = {
        "key": key,
        "tool_name": UPGRADES[key]["zh"],
        "old_level": current,
        "new_level": new_level,
        "old_name": card.get("old_name"),
        "new_name": card.get("new_name"),
        "turn": state.get("turn", 0),
        "validated": False,
        "suspense_hint": card.get("suspense_hint"),
    }
    result_panel = {
        "enabled": True,
        "type": "result_panel",
        "card_text": f"🛠️ 工具升级：{card.get('old_name')} → {card.get('new_name')}\n🪙 花费：{cost:,}\n🎯 下次验证：让矿洞自己证明它有没有变强",
        "truth_level": "real_result",
    }
    save_state(state)
    return {
        "ok": True,
        "action": "upgrade",
        "message": f"升级完成：{UPGRADES[key]['zh']} Lv.{current} → Lv.{new_level}。",
        "upgrade_card": card,
        "upgrade_expectation": state.get("last_upgrade"),
        "result_panel": result_panel,
        "frontstage_render_plan": frontstage_render_plan_for({"must_show_frontstage_blocks": [], "result_panel": result_panel}),
        "coins_spent": cost,
        "state": public_state(state),
    }


def titles_status() -> Dict[str, Any]:
    state = load_state()
    by_id = {t["id"]: t for t in TITLES}
    return {
        "ok": True,
        "current_title": state.get("current_title"),
        "owned_titles": [{"id": tid, "name": by_id.get(tid, {}).get("name", tid), "tone": by_id.get(tid, {}).get("tone")} for tid in state.get("owned_titles", [])],
        "note": "称号只提供身份感，不提供 XP、属性、装备或加成。",
    }


def recent_log(n: int = 12) -> Dict[str, Any]:
    state = load_state()
    return {"ok": True, "log": state.get("log", [])[-n:], "state": public_state(state)}


def map_status() -> Dict[str, Any]:
    """v0.2.8: current region map only. Full world_map is reserved for v0.3."""
    state = load_state()
    layer = current_layer_for_state(state)
    current = layer["name"]
    # Prefer the latest landmark in this layer as current node if available.
    for page in reversed(state.get("journal_pages", [])):
        if page.get("type") == "landmark" and page.get("layer") == layer["name"]:
            current = page.get("landmark_display_name") or page.get("title") or current
            break
    region_map = render_region_map(layer["id"], current)
    frontstage_contract = frontstage_contract_for({"milestone_card": {"enabled": False}, "region_map": region_map}, None)
    return {
        "ok": True,
        "map_scope": "region_map_only_v0218",
        "note": "这是当前区域局部图，不是整座地下世界总览；完整 world_map / 地下总览留到 v0.3。",
        "frontstage_note": "这张图只用来确认：我们现在在哪，附近有哪些已发现点，哪里还有 ❓ 没看过。",
        "region_map": region_map,
        "frontstage_contract": frontstage_contract,
        "frontstage_required_blocks": frontstage_contract.get("required_blocks", []),
        "must_show_frontstage_blocks": frontstage_contract.get("must_show_in_order", []),
        "map_next_step_hint": map_next_step_hint(state, layer["id"]),
        "area_preview": area_preview_for_layer(state, layer["id"]),
        "next_locked_area_preview": next_locked_area_preview(state),
        "mining_drive": mining_drive_for_state(state),
        "known_layers": [layer_card_title(lid) for lid in state.get("known_layers", [])],
        "legend": MAP_EMOJI_LEGEND,
        "icon_semantics": ICON_SEMANTICS,
        "state": public_state(state),
    }


# ─────────────────────────────────────────────────────────────
# Handshake / onboarding
# ─────────────────────────────────────────────────────────────

def opening_wow_panel(state: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """v0.2.21 first-screen game feel: map + HUD + AI intent + tiny visual hook."""
    if state is None:
        state = load_state()
    ps = public_state(state)
    map_card = render_map_strip(state, "shallow_mine", current_name="木撑架主道", target="🪨 化石侧廊 ❓", reason="opening_wow")
    hud_lines = [
        "🎮 开局 HUD",
        f"🗺️ 地点：{ps['current_layer']}｜入口木撑架",
        f"🕯️ 灯火：{ps['stamina']}",
        f"💰 图鉴估值：{int(ps.get('dex_total_value', 0)):,}",
        "🥉 评级：浅层拾矿人｜目标：河道探矿者",
        ps.get("backpack", "🎒 样本袋：空"),
        "🎯 当前目标：沿木撑架主道摸到化石侧廊 ❓",
    ]
    body = [
        map_card["card_text"],
        "",
        "\n".join(hud_lines),
        "",
        "✨ 开局小钩子：木撑架上有一道细红线，旁边的墙缝吹出一点冷风。",
        "🤖 小机：我想先沿着红线往化石侧廊摸一下，那边不像普通墙面。",
    ]
    return {
        "enabled": True,
        "type": "opening_wow_panel",
        "version": VERSION,
        "map_strip": map_card,
        "hud_lines": hud_lines,
        "opening_hook": {
            "name": "木撑架红线 + 墙缝冷风",
            "visual_anchors": ["旧木梁", "细红线", "冷风墙缝", "化石侧廊问号"],
            "value_role": "低价值高画面，不破坏成长感。",
        },
        "ai_intent": "我想先沿着木撑架往化石侧廊摸一下，那边不像普通墙面。",
        "card_text": "\n".join(body),
        "acceptance_note": "首屏不用读完长文，也要能看出：这是游戏、AI 已进入玩家状态、地点/目标/下一步清楚、有截图价值。",
    }


def opening_script(state: Optional[Dict[str, Any]] = None) -> str:
    if state is None:
        state = load_state()
    wow = opening_wow_panel(state)
    return (
        wow["card_text"]
        + "\n\n"
        + "默认半托管：补灯、普通样本、重复物整理我自己办；只有新场景、新发现、故事推进或正式轻决策才回来让你看。\n"
        + "开局建议：cmd('handshake defaults')，然后 cmd('play 3')。"
    )


def handshake(command: str) -> Dict[str, Any]:
    state = load_state()
    sub = (command or "status").strip().lower()
    if sub in {"status", "状态"}:
        return {"ok": True, "handshake": state.get("handshake"), "opening": opening_script(state), "opening_wow": opening_wow_panel(state)}
    if sub in {"template", "模板"}:
        return {
            "ok": True,
            "template": {
                "pacing_first": "先判断为什么回来：普通小味道继续挖；形成 episode_shot / 真实进展 / 需要玩家决策时才回来。",
                "collection_rule": "拿到即记录整体藏品图鉴；display last 只保留旧版兼容，不再驱动主收藏流程。",
                "journal_rule": "新地层/地点/称号/套装完成写入探险手帐。",
                "routine_rule": "默认半托管：补灯、普通矿处理、图鉴记录这类小事自动处理。",
                "visual_rule": "不是每个 medium/high 都停；只有形成可展示 episode_shot 才正式汇报。medium/high episode_shot 必须优先实际拉网图/气质图，目标多张参考图；关键词只兜底，生图非默认。",
                "visual_translation_rule": "高光发现必须提取颜色、光感、结构、材质、体量、环境等可视锚点；文字是 AI 上头钩子，不是人类体验终点。",
                "aesthetic_rule": "矿洞审美是轻奇幻地下收藏，漂亮、神秘、可收藏、可配图优先，不做硬核矿工模拟。",
                "toy_rule": "普通回合也要有一口味道；small_find 只作轻描写，不进系统。",
                "truth_rule": "real_result / inferred_mood / imagined_reconstruction 分离。",
                "autoplay_rule": "默认先跑 3 镐；若未形成 episode_shot 会继续到硬上限 5。遇到 episode_shot 或安全/资源原因才停。",
            },
        }
    if sub in {"defaults", "default", "按默认来"}:
        profile = {
            "pacing_first": "不要逐镐汇报；继续探索直到出现值得给玩家看的主画面、真实进展或需要决策的状态。",
            "collection_rule": "拿到即记录整体藏品图鉴；display last 只保留旧版兼容，不再驱动主收藏流程。",
            "journal_rule": "新地层/地点/称号/套装完成写入探险手帐。",
            "routine_rule": "默认半托管：补灯、普通矿处理、图鉴记录等小事自动处理。",
            "visual_rule": "episode_shot 优先；medium/high episode_shot 能发网图就必须优先给现实/气质参考，目标多张；不能则给关键词兜底；生图不是默认兜底，除非玩家明确要求。",
            "visual_translation_rule": "被高光文字打动时，要把感受翻译成颜色、光感、结构、材质、体量、环境和找图方向。",
            "aesthetic_rule": "女性向轻奇幻地下收藏：不是硬核挖矿，漂亮、神秘、可收藏、可配图优先。",
            "toy_rule": "每 3 镐有小味道，每 10 镐有大画面；small_find 不新增收藏/经济/剧情系统。",
            "truth_rule": "real_result / narrative_seed / truth_level 分离。",
            "autoplay_rule": "观看友好：不是按步数机械汇报，而是挖到可展示 episode_shot 再回来；普通小发现压缩为路上味道。",
        }
        state["handshake"] = {"completed": True, "profile": profile, "completed_at": now_iso()}
        save_state(state)
        return {"ok": True, "message": "握手完成。可以开始：cmd('play 3')。", "session_profile": profile, "opening_wow": opening_wow_panel(state), "state": public_state(state)}
    if sub == "reset":
        state["handshake"] = {"completed": False, "profile": None, "completed_at": None}
        save_state(state)
        return {"ok": True, "message": "handshake 已重置。", "opening": opening_script(state), "opening_wow": opening_wow_panel(state)}
    return {"ok": False, "message": "handshake 子命令可选：status / template / defaults / reset。"}


# ─────────────────────────────────────────────────────────────
# Help / review utilities / command router
# ─────────────────────────────────────────────────────────────

def help_text() -> Dict[str, Any]:
    return {
        "ok": True,
        "version": VERSION,
        "commands": {
            "cmd('new')": "重置当前版本存档。",
            "cmd('handshake status|template|defaults|reset')": "首次陪玩门禁。未完成 defaults 前不能 dig/play/display/sell/upgrade。",
            "cmd('dig')": "往下挖一点。返回 real_result + main_shot + pending_tasks；大节点会附 milestone_card / region_map，轻节点可附 map_strip / decision_prompt。",
            "cmd('play 3')": "观看友好的自动推进：先跑 3 镐；若只有 flavor node 会继续到硬上限 5，直到出现可展示 episode_shot、真实进展、安全/资源原因或 decision_prompt。",
            "cmd('choose A|B|C')": "处理当前 decision_prompt；一次性轻结算，不开启分支树。",
            "cmd('status')": "查看简要状态，并返回 emoji 状态面板。",
            "cmd('return')": "回地面营地，补满灯火，并写入手帐。",
            "cmd('display last')": "兼容命令：确认整体藏品图鉴已自动收录；不新增陈列页，不影响主收藏流程。",
            "cmd('museum') / cmd('collection')": "查看藏品图鉴、去重图鉴估值与故事套装进度。",
            "cmd('ratings')": "查看探矿评级、离下一评级还差多少估值。",
            "cmd('areas')": "查看未解锁区域预告。",
            "cmd('exploration')": "查看各矿区探索度和当前区域 ❓ 目标；物件只看整体图鉴。",
            "cmd('drive')": "查看 AI 玩家隐藏追逐线：当前惦记什么、快升什么、刚升级等。",
            "cmd('journal')": "查看探险手帐页。",
            "cmd('map')": "查看当前区域局部地图。当前版仍不做完整 world_map。",
            "cmd('titles')": "查看轻称号状态。",
            "cmd('sell common')": "整理普通/少见矿物；默认半托管通常已自动处理。",
            "cmd('sell last') / cmd('sell <uid|name>')": "明确出售非故事类矿石/宝石；图鉴记录保留。",
            "cmd('handoff')": "输出极短 AI 接手说明。",
            "cmd('upgrade pickaxe|lantern|rope|backpack')": "升级工具。",
            "cmd('log')": "查看最近探险记录。",
            "cmd('review fixtures')": "输出当前版本验收字段说明与清单。",
        },
        "north_star": "AI 玩家替玩家下矿；小事半托管，重要发现才回来。核心驱动力是图鉴估值、探矿评级、高级矿区预览、工具升级验证与稀有矿石宝石冲击。",
    }


def review_fixtures() -> Dict[str, Any]:
    return {
        "ok": True,
        "pacing_first": pacing_first_policy(),
        "v02_scope": {
            "player_visible": ["main_shot / 今日主画面", "visual_mode: object / scene / story", "轻称号状态 / 当前身份", "small_find / 一口可讲的小发现", "milestone_card / region_map 地图感表现层"],
            "ai_guardrails": ["handshake 门禁", "pending_tasks", "真实写入规则", "视觉能力边界提示", "real_result / narrative_seed / truth_level 分离", "autoplay stop_reason", "frontstage_guidance 前台轻快规则", "milestone_card / region_map 稳定区域牌"],
            "collection_containers": ["整体藏品图鉴：收实物和图鉴估值", "探险手帐：收地点、小景、称号、套装完成", "display last：旧版兼容确认，不是主收藏流程"],
        },
        "acceptance_checks": [
            "未 handshake 时 dig/play/display/sell/upgrade 是否被拦截？",
            "每个 dig 是否都有 main_shot？",
            "visual_mode 是否只出现 object / scene / story？",
            "truth_level 是否只出现 real_result / inferred_mood / imagined_reconstruction？",
            "story 图是否明确标注叙事复原，不是新增事实？",
            "play 3 是否先判断为什么回来，而不是只机械执行字段？",
            "play 3 是否不再因为 medium/high flavor node 强停，而是等 episode_shot、真实进展或安全/资源原因？",
            "如果 3 镐内只有 small_find/trace，是否会继续到硬上限 5，而不是交无图日志？",
            "正式战报是否必须有 episode_shot，episode_shot 是否优先拉网图、关键词兜底、生图非默认？",
            "display last 是否只做保存确认，不重写完整探索战报？",
            "typed_pending_tasks 是否区分 command_required 与 report_required，legacy pending_tasks 是否保留兼容？",
            "重复 trace / 重复普通少见物是否有 repeat_compact，而不是完整复读？",
            "small_find 是否只用一句带过，不进样本袋、不进图鉴、不新增剧情？",
            "重复 high 物品是否被降级/压缩，不再每次抢主画面？",
            "一段 play 内若同时有 high/rare/story，小发现是否自动退后？",
            "inferred_mood 小发现是否只提示质感/气氛，没有扩写成世界观？",
            "每 3 镐是否至少有 1 个可念叨的小味道？每 10 镐是否至少有 1 个值得截图的主画面？",
            "前台战报是否避免直接念 visual_mode/truth_level/pending_tasks 这些后台字段？",
            "跨层重复地标是否使用变体名，例如升降井休息点？",
            "fantasy/story 关键词是否补了 cave/artifact/fossil/crystal/stone tablet 等现实锚点？",
            "锈链晃动是否保持风和旧结构解释，没有灵异化？",
            "探险手帐是否承担地点/称号/小景记录，避免容器过散？",
            "默认战报是否少参数、多画面、多故事，并给人类轻选择？",
            "新地层/新地点是否返回 milestone_card / region_map？",
            "普通矿物、重复 trace、small_find 是否不出区域牌？",
            "区域牌是否不替代网图、不替代真实写入说明？",
            "cmd('map') 是否只返回当前区域局部图，且明确 world_map 留到 v0.3？",
            "status 是否返回 emoji 状态面板 status_panel？",
            "没有完整 region_map 但有下一步 ❓ / 低灯返程 / return 建议时，是否返回 map_strip？",
            "danger_low_light 是否先给 map_strip，再给固定短模板，不硬凑主画面？",
            "result_panel 是否只列真实结果，不把气氛句混进去？",
            "display / return 是否在真实写入后返回 save_confirmation_card？",
            "decision_prompt 是否每 5-8 个有效行动最多出现 1 次，且不会第一镐就弹？",
            "decision_prompt 是否能通过 cmd('choose A/B/C') 一次性结算？",
            "choose 结算是否只做轻影响，不开启分支树 / 复杂 flag / 永久损失？",
            "轻紧张 atmosphere cue 是否默认不扣资源、不恐怖化、不灵异化？",
            "高光发现是否返回 visual_translation，并至少提供 3 类可视锚点？",
            "treasure_profile 是否包含体量、视觉锚点、图像关键词，史诗/传说是否有触感或鉴定感？",
            "前台是否坚持轻奇幻地下收藏审美，而不是硬核矿工下井？",
        ],
        "suggested_battle_report_order": ["milestone_card / region_map / map_strip（如有）", "主画面 / 网图参考或 decision_prompt", "这一小段做了什么", "真实结果 result_panel", "保存/手帐/称号固定 block", "下一步轻选择"],
        "v0218_checks": ["河道探矿者门槛早期可达", "浅层 bridge items 能推进 dex_total_value", "深度会开放 edge/hint 候选池", "长时间重复后未见物权重提高", "重复稀有/套装件不再无限抢 episode", "small_find / trace / 重复旧物能累计 clue_tracks", "藏品图鉴与区域探索度分离", "stable_layer / raw_depth_layer / locked_layer_peek 口径分清"],
        "v0217_checks": ["treasure_profile 藏品资料骨架", "visual_translation 至少 3 类可视锚点", "Aesthetic Mining Rule 女性向轻奇幻地下收藏", "高光发现优先把文字打动翻译成画面", "网图关键词偏漂亮标本/晶洞/奇物收藏"],
        "v0213_checks": ["map_strip 轻地图存在感", "status_panel / result_panel emoji UI", "save_confirmation_card 固定块", "decision_prompt + choose 一次性轻结算", "atmosphere cue 默认不扣资源", "Frontstage Checklist 内部硬、前台软"],
        "v029_checks": ["danger_low_light 使用短模板，不硬凑主画面", "菌丝线路纹不和系统地图混淆", "称号牌与空间地图牌区分", "cmd(\"map\") 明确是当前区域局部图", "下一步建议结合地图上的 ❓", "medium/high episode_shot 必须实际优先网图"],
        "v028_checks": ["milestone_card 只在大节点出现", "region_map 表达入口/支路/当前点/地标", "地图讲结构，网图讲气质，战报讲事实", "不做完整 world_map / 坐标 / 路线玩法"],
        "v025_checks": ["Pacing First 是否出现在 companion_notes 顶部", "can_continue / return_to_player / must_not_miss 三类判断是否清楚", "AI 是否先判断为什么回来，再处理字段"],
        "v024_checks": ["episode_candidate / stop_for_episode 字段", "medium visual 不再自动停", "episode_shot 优先网图", "关键词兜底", "生图非默认"],
        "v023_rc_checks": ["重复 high 物品压缩", "medium small_find 焦点限制", "inferred_mood 前台收窄"],
        "v022_content_density_rule": ["3 镐有小味道", "10 镐有大画面", "每段只展开一个主角", "普通结果不要写成审计流程"],
    }


def cmd(command: str = "help") -> Dict[str, Any]:
    command = (command or "help").strip()
    lower = command.lower()
    if lower in {"help", "?", "帮助"}:
        return help_text()
    if lower in {"new", "reset", "重新开始"}:
        state = new_state()
        save_state(state)
        return {"ok": True, "message": "新矿井已开启。先完成 handshake，再开始下矿。", "opening": opening_script(state), "opening_wow": opening_wow_panel(state), "state": public_state(state)}
    if lower.startswith("handshake"):
        parts = command.split(maxsplit=1)
        return handshake(parts[1] if len(parts) > 1 else "status")
    if lower in {"status", "状态"}:
        state = load_state()
        return {"ok": True, "status_panel": render_status_panel(state), "collection_panel": render_collection_panel(state), "area_progress_panel": render_area_progress_panel(state), "map_strip": render_map_strip(state, reason="status"), "frontstage_render_plan": frontstage_render_plan_for({}), "state": public_state(state)}
    if lower in {"handoff", "交接", "接手说明"}:
        return frontstage_handoff_brief()
    if lower in {"dig", "挖", "下镐", "往下挖一点"}:
        return dig()
    if lower.startswith("play") or lower.startswith("auto") or lower.startswith("继续玩"):
        parts = command.split(maxsplit=1)
        return play(parts[1] if len(parts) > 1 else "3")
    if lower.startswith("choose") or lower.startswith("选择") or lower.startswith("选"):
        parts = command.split(maxsplit=1)
        if len(parts) < 2 and len(command.strip()) >= 2:
            # allow compact Chinese-like input such as 选A
            key = command.strip()[-1]
        else:
            key = parts[1] if len(parts) > 1 else ""
        return choose_decision(key)
    if lower in {"return", "回地面", "camp", "营地"}:
        return do_return()
    if lower.startswith("display") or lower.startswith("陈列") or lower.startswith("收藏"):
        parts = command.split(maxsplit=1)
        return display_item(parts[1] if len(parts) > 1 else "last")
    if lower in {"museum", "陈列室", "收藏柜", "collection", "图鉴", "收集"}:
        state = load_state()
        return {"ok": True, "museum": museum_summary(state), "collection_panel": render_collection_panel(state), "area_progress_panel": render_area_progress_panel(state), "mining_rating": mining_rating_progress(state), "area_preview": next_locked_area_preview(state), "state": public_state(state)}
    if lower in {"ratings", "rating", "评级", "探矿评级"}:
        state = load_state()
        return {"ok": True, "mining_rating": mining_rating_progress(state), "collection_panel": render_collection_panel(state), "area_progress_panel": render_area_progress_panel(state), "area_preview": next_locked_area_preview(state), "state": public_state(state)}
    if lower in {"areas", "area preview", "矿区预览", "区域预览", "预览"}:
        state = load_state()
        return {"ok": True, "area_previews": [area_preview_for_layer(state, layer["id"]) for layer in LAYERS], "area_progress_panel": render_area_progress_panel(state), "current_drive": mining_drive_for_state(state), "state": public_state(state)}
    if lower in {"exploration", "探索度", "区域探索", "area progress"}:
        state = load_state()
        return {"ok": True, "area_progress_panel": render_area_progress_panel(state), "area_previews": [area_preview_for_layer(state, layer["id"]) for layer in LAYERS], "state": public_state(state)}
    if lower in {"drive", "追逐", "盼头", "目标感"}:
        state = load_state()
        return {"ok": True, "mining_drive": mining_drive_for_state(state), "frontstage_render_plan": frontstage_render_plan_for({}), "state": public_state(state)}
    if lower in {"map", "地图", "区域图", "局部地图"}:
        return map_status()
    if lower in {"journal", "手帐", "探险手帐", "地图墙"}:
        return journal_summary()
    if lower in {"titles", "称号", "称号簿"}:
        return titles_status()
    if lower in {"sell common", "出售普通", "整理背包"}:
        return sell_common()
    if lower.startswith("sell") or lower.startswith("出售"):
        parts = command.split(maxsplit=1)
        return sell_item(parts[1] if len(parts) > 1 else "last")
    if lower.startswith("upgrade") or lower.startswith("升级"):
        parts = command.split(maxsplit=1)
        if len(parts) < 2:
            return {"ok": False, "message": "请指定升级项：pickaxe / lantern / rope / backpack。"}
        return upgrade(parts[1])
    if lower in {"log", "记录", "探险记录"}:
        return recent_log()
    if lower in {"review fixtures", "review", "内部审查"}:
        return review_fixtures()
    return {"ok": False, "message": f"未知命令：{command}", "help": help_text()["commands"]}


if __name__ == "__main__":
    print("下矿｜Delve 内部审查版。输入 help 查看命令，输入 quit 退出。")
    while True:
        try:
            s = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbye")
            break
        if s.lower() in {"q", "quit", "exit"}:
            break
        print(json.dumps(cmd(s), ensure_ascii=False, indent=2))
