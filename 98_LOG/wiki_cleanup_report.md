# Wiki 清理報告

產生時間：2026-06-05 12:50:00

## 清理目標

依照 `knowledge-wiki-compiler` 的新規則，將 wiki 拆成三層：

- `02_wiki`：只保留 30 個標準標籤主頁，每頁最多 30 條近期案例。
- `022_wiki_topics`：承接原本混在 `02_wiki` 裡的子題頁與非標準頂層頁。
- `021_wiki`：承接標準主頁搬出的歷史案例。

## 備份位置

- 第一次實際清理前備份：`scratch/wiki_cleanup_backup_20260605_124318`
- 第二次刷新主頁前備份：`scratch/wiki_cleanup_backup_20260605_124421`
- 錯誤季度 `0000Q0` 原檔留存：`scratch/wiki_cleanup_merged_0000Q0`

## 已移出 02_wiki 的工具檔

- `02_wiki/_final_report.py` -> `scratch/wiki_tools/_final_report.py`
- `02_wiki/_scan.py` -> `scratch/wiki_tools/_scan.py`
- `02_wiki/_scan_v2.py` -> `scratch/wiki_tools/_scan_v2.py`

## 已移到 022_wiki_topics 的頁面

- `022_wiki_topics/人工智慧_工具與應用.md`
- `022_wiki_topics/人工智慧_社會與經濟.md`
- `022_wiki_topics/人工智慧_開發與組織.md`
- `022_wiki_topics/個人品牌.md`
- `022_wiki_topics/品牌_公關與消費洞察.md`
- `022_wiki_topics/品牌_策略與趨勢.md`
- `022_wiki_topics/商業模式_平台生態與AI.md`
- `022_wiki_topics/商業模式_零售消費與品牌.md`
- `022_wiki_topics/商業模式_體驗文旅與資本.md`
- `022_wiki_topics/市場與需求_前期趨勢.md`
- `022_wiki_topics/市場與需求_近期觀察.md`
- `022_wiki_topics/建築與美學.md`
- `022_wiki_topics/歷史.md`
- `022_wiki_topics/科技影響_AI產業與企業.md`
- `022_wiki_topics/科技影響_硬體社會與地緣.md`
- `022_wiki_topics/空間設計.md`
- `022_wiki_topics/系統設計.md`
- `022_wiki_topics/組織與策略_組織管理與文化.md`
- `022_wiki_topics/組織與策略_策略與增長.md`
- `022_wiki_topics/職涯發展.md`
- `022_wiki_topics/行銷_AI與數位增長.md`
- `022_wiki_topics/行銷_品牌與情緒策略.md`
- `022_wiki_topics/體驗_空間文旅案例.md`
- `022_wiki_topics/體驗_品牌產品案例.md`

## 標準主頁瘦身結果

- `02_wiki` 原本有 54 個 Markdown 頁面，清理後剩 30 個 Markdown 頁面。
- 30 個標準標籤主頁全部保留在 `02_wiki`。
- 24 個非標準頁 / topic 頁已移到 `022_wiki_topics`。
- 3 個工具檔已移到 `scratch/wiki_tools`。
- 標準主頁共搬出 3200 條舊案例。
- 其中 422 條是 `021_wiki` 尚未存在的案例，已新增到對應季度歸檔；其餘案例本來已在歸檔中，這次只從主頁移除。
- 無法從 link target 判斷日期的案例，已依處理日歸到 `2026Q2`，沒有保留 `0000Q0` 歸檔。

## 最終稽核

- `02_wiki` Markdown 檔案數：30
- `02_wiki` 標準標籤主頁：30 / 30
- `02_wiki` 非 Markdown 檔案數：0
- `02_wiki` 非標準頂層頁：0
- `02_wiki` 超過 30 條案例的標準主頁：0
- `021_wiki` / `02_wiki` / `022_wiki_topics` 中沒有 `0000Q0` 連結或檔案。

## 後續建議

- 先跑一陣子新 skill，確認新筆記只會寫入標準主頁，不會再把 topic 頁塞回 `02_wiki`。
- 之後再討論 `022_wiki_topics` 是否需要命名規則與 topic 索引頁。
