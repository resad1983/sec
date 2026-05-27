# CONTEXT.md
> 由 Claude Code 自動掃描產出｜2026-04-09

---

## 實際目錄結構

```
sec/                          ← 主 vault
├── 00_Inbox/    (169 files)  ← 原文存檔，按日期子目錄
├── 01_Liter/    (179 files)  ← 蒸餾筆記，平鋪命名
├── 05_Self/     (8 files)    ← 個人原則與思維框架
├── 90_Taxonomy/ (30 files)  ← 標籤定義文件
├── Clippings/   (83 files)  ← Web Clipper 暫存（待處理 backlog）
└── .obsidian/   (5 files)   ← Obsidian 設定
```

---

## 00_Inbox 實際結構

- **格式：日期子目錄**（已完成遷移，root 無平鋪檔案）
- 最舊：2025-09-17，最新：2026-04-08
- 共 23 個日期資料夾
- 部分資料夾含 `_index.md`（每日閱讀索引，純文字，不含 wikilink）

```
00_Inbox/
├── 2026-04-08/  (38 files)  ← 含 _index.md
├── 2026-03-30/  (29 files)
├── 2026-03-29/  (31 files)
└── ... (共 23 個日期)
```

---

## 01_Liter 實際格式（抽樣 5 篇 frontmatter）

**實際使用的欄位（依出現頻率排序）：**

| 欄位 | 格式 | 說明 |
|------|------|------|
| `title` | 字串 | 繁體中文標題 |
| `source` | URL 字串 | 原始網址 |
| `date` | YYYY-MM-DD | 文章日期 |
| `tags` | `[tag1, tag2, ...]` | 分類標籤 |
| `type` | 字串 | 文章類型（如：商業案例、產業報導） |
| `author` | 字串（部分有） | 作者名 |
| `raw_ref` | `"[[YYYY-MM-DD/標題]]"` | 連回 00_Inbox 原文（新格式有，舊格式無） |
| `status` | `draft` | 處理狀態（新格式有，舊格式無） |

**注意：舊筆記（2025-09 ～ 2026-02）缺少 `raw_ref` 和 `status` 欄位，tags 格式不統一（部分用中文標籤、部分用英文）**

---

## 現有腳本清單

```
C:\Users\resad.huang\Documents\COWORK\scripts\
├── rss_scorer.py          ← RSS 抓取 + 關鍵字評分（每天 00:15 跑）
│                            輸出到 C:/tmp/rss_candidates.json
└── clippings_processor.py ← Clippings 處理器（備用，目前用排程任務替代）
```

---

## 現有 SKILL 清單（自訂）

```
~/.claude/skills/
└── save-to-ob/SKILL.md    ← 手動貼 URL → 存入 sec vault

~/.claude/scheduled-tasks/
├── daily-rss-to-obsidian/SKILL.md    ← 每天 00:30，RSS → 00_Inbox + 01_Liter
└── daily-clippings-to-obsidian/SKILL.md ← 每天 01:05，Clippings → 00_Inbox + 01_Liter（每次最多 15 篇）
```

---

## Cowork 排程現況

| 任務 | 時間 | 觸發方式 | 狀態 |
|------|------|---------|------|
| `rss_scorer.py` | 每天 00:15 | Windows Task Scheduler | 運行中 |
| `daily-rss-to-obsidian` | 每天 00:30 | Claude Code 本機排程 | 運行中 |
| `daily-clippings-to-obsidian` | 每天 01:05 | Claude Code 本機排程 | 新建，待首次執行 |

**輸入流程：**
```
RSS feeds          → rss_scorer.py → rss_candidates.json → daily-rss-to-obsidian → sec vault
Obsidian Clipper   → Clippings/                          → daily-clippings-to-obsidian → sec vault
手動貼 URL         →                                     → /save-to-ob → sec vault
```

---

## 01_Liter 蒸餾格式（目前設計）

```markdown
---
title: 文章標題
source: URL
date: YYYY-MM-DD
score: N          ← RSS 才有，Clippings/手動無
tags: [標籤1, 標籤2]
type: 文章類型
raw_ref: "[[YYYY-MM-DD/標題]]"
status: draft
---

## 核心洞察
> 50字內，偷偷視角

## 重點摘要
3-5 條列

## 值得深思的問題
2-3 個問題

## 關聯筆記
掃描 01_Liter/ 自動配對，或 #待連結
```

---

## 待確認問題（Claude Code 自動發現）

1. **Clippings backlog 83 篇**：`daily-clippings-to-obsidian` 每次只處理 15 篇，需手動 Run Now 約 6 次才能清完。

2. **01_Liter 新舊格式不一致**：2026-03 以前的舊筆記缺少 `raw_ref`、`status` 欄位，tags 使用自訂標籤（非標準 34 個標籤庫）。是否需要補齊？

3. **90_Taxonomy 與標籤庫的關係**：`90_Taxonomy/` 有 30 個標籤定義文件，但 SKILL.md 裡的標籤庫有 30 個標籤。兩者是同步的嗎？實際使用中 tags 有出現不在標籤庫的詞（如 `UX研究`、`D2C`、`DBSCAN`）。

4. **`save-to-ob` 中 00_Inbox 的原文轉換**：SKILL.md 要求把簡體中文全部轉繁體，這對內文是否必要？（原文保留簡體可能更準確）

5. **`05_Self` 有 7 個個人原則文件**（decision-principles、system-design-principles 等），目前與筆記系統無連結。是否要讓蒸餾時參照這些原則？
