# 下矿｜Delve v0.2.21.6.1 Regression Report

Date: 2026-07-07

## Test Run

Implementation:

- `delve.py`
- `VERSION = 0.2.21.6.1-rc-polish`
- `SAVE_FILE = mine_v0221_6_1_save.json`

Commands:

- `python3 -m py_compile delve.py`
- `python3 mining_companion/qa_v02_21_6_1_rc_polish.py`

Telemetry:

- `/private/tmp/mining_v022161_rc_polish.json`

## P0

Pass.

Leak scan found no:

- `display_count`
- `整体图鉴收集`
- `行囊已满`
- `背包已满`
- `没有带回样本`
- `代表矿`

Pre-handshake `dig` remained blocked.

## Main Pacing Guard

The RC polish patch did not break the main pacing spine.

| Threshold | Hit Count | Median Segment | Min-Max | Causes |
|---:|---:|---:|---:|---|
| 100,000 | 12/12 | 138 | 123-157 | `single_item` 6, `virtual_bridge_research` 6 |
| 200,000 | 12/12 | 181 | 171-201 | `virtual_bridge_research` 12 |
| 300,000 | 12/12 | 205 | 186-225 | `single_item` 9, `collection_item_value_update` 3 |
| 400,000 | 12/12 | 406 | 213-785 | `single_item` 2, `clue_track_research` 10 |

## RC Polish Checks

| Check | Result |
|---|---:|
| Displayed occurrence regressions for same item_id | 0 |
| Routine auto-return consecutive duplicate messages | 0 |
| Routine auto-return repeats within recent 5 messages | 0 |
| Repeat sample wording violations | 0 |
| Clue-track 4th+ repetition wording violations | 0 |
| Clue-track result_panel outlet violations | 0 |
| Seeds missing 82k-400k transition-title feedback | 0 |
| Decision prompt three-window isomorphism | 0 |
| Seeds missing post-400k handoff | 0 |

Per-seed polish summary:

| Seed | Final Segment | Final Value | Rating | Routine Returns | Recent Routine Repeats | Occurrence Regressions | Clue Repeat Violations | Transition Titles | Handoff |
|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | 456 | 404,598 | ruin_surveyor | 312 | 0 | 0 | 0 | 5 | 1 |
| 2 | 817 | 403,630 | ruin_surveyor | 570 | 0 | 0 | 0 | 5 | 1 |
| 3 | 741 | 403,591 | ruin_surveyor | 532 | 0 | 0 | 0 | 5 | 1 |
| 4 | 333 | 414,250 | ruin_surveyor | 232 | 0 | 0 | 0 | 5 | 1 |
| 5 | 905 | 404,021 | ruin_surveyor | 640 | 0 | 0 | 0 | 4 | 1 |
| 6 | 517 | 406,033 | ruin_surveyor | 358 | 0 | 0 | 0 | 5 | 1 |
| 7 | 738 | 403,831 | ruin_surveyor | 529 | 0 | 0 | 0 | 5 | 1 |
| 8 | 385 | 413,960 | ruin_surveyor | 269 | 0 | 0 | 0 | 5 | 1 |
| 9 | 535 | 403,741 | ruin_surveyor | 365 | 0 | 0 | 0 | 5 | 1 |
| 10 | 407 | 403,694 | ruin_surveyor | 272 | 0 | 0 | 0 | 5 | 1 |
| 11 | 512 | 403,426 | ruin_surveyor | 350 | 0 | 0 | 0 | 5 | 1 |
| 12 | 905 | 403,688 | ruin_surveyor | 648 | 0 | 0 | 0 | 5 | 1 |

A4 result-panel outlet check: every completed `clue_track_research` now renders its graded `line` in the player-visible result panel. The old hardcoded result-panel copy did not reappear.

## Judgment

v0.2.21.6.1 passes RC polish.

This version is ready for Release Candidate / README preparation. Remaining future work is not RC-blocking: true post-400k content can be a later feature patch.
