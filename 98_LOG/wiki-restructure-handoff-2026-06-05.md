# Wiki 結構重整交接紀錄

日期：2026-06-05

## 新對話接續關鍵字

`繼續 wiki 結構重整`

建議新對話開場可以直接貼：

> 繼續 wiki 結構重整。請先讀 `98_LOG/wiki-restructure-handoff-2026-06-05.md`、`wiki_cleanup_report.md`，再接著處理 `市場與需求.md` 的子題導覽問題。

## 本次已完成

### 1. Skill 重構

`D:\gemini\skill\知識蒸餾_處理器` 已整理成一個總入口與三個子 skill：

- `SKILL.md`：`knowledge-pipeline`
- `skills/distill/SKILL.md`：`knowledge-distiller`
- `skills/wiki-compiler/SKILL.md`：`knowledge-wiki-compiler`
- `skills/project-sync/SKILL.md`：`knowledge-project-sync`

分工原則：

- `knowledge-distiller` 只處理 `Clippings` -> `00_Inbox` + `01_Liter`。
- `knowledge-wiki-compiler` 只處理 `wiki_evolved: false`，更新 wiki。
- `knowledge-project-sync` 只處理 `project_synced: false`，更新 `04_Projects`。

### 2. Wiki skill 規則更新

`knowledge-wiki-compiler` 已改成三層 wiki 結構：

- `02_wiki`：標準標籤主頁，只保留 30 個標準標籤，每頁最多 30 條近期案例。
- `022_wiki_topics`：topic / 子題頁區。
- `021_wiki`：季度歸檔區。

重要規則：

- 非標準 tag 不可寫入 `02_wiki`。
- `02_wiki` 若出現非標準 Markdown 檔，wiki compiler 應停止大量寫入。
- 歷史案例歸到 `021_wiki/{Tag}_{YYYYQn}.md`。
- 無法判斷日期時使用處理當日季度，不可產生 `0000Q0`。

### 3. Skill 再檢查與修正

已修正：

- `knowledge-distiller` 原本寫「34 個標籤」，已改成「30 個標籤」。
- `knowledge-distiller` 已補上不直接更新 `022_wiki_topics`。
- `knowledge-project-sync` 已補上不更新 `022_wiki_topics`。
- `knowledge-wiki-compiler` 的 稽核 文字已改成：topic / 子題頁一律應位於 `022_wiki_topics`。

驗證：

- skill 檔沒有 NUL 字元。
- skill 檔沒有字面 `` `r`n`` 殘留。
- `34` 已不再出現在 skill 規則裡。

## Wiki 檔案實際整理結果

### 1. `02_wiki`

目前狀態：

- 30 個 `.md`。
- 沒有非 Markdown 檔。
- 沒有非標準 topic 頁混在裡面。
- 每頁案例數最多 30。
- 沒有重複 link target。
- 歸檔連結都能找到對應 `021_wiki` 檔案。

### 2. `022_wiki_topics`

目前狀態：

- 24 個 `.md`。
- 沒有重複 link target。
- 大多 topic 頁案例數在 50 以下。
- `品牌_公關與消費洞察.md` 有 51 條，略超過 50，但目前 skill 尚未明定 topic 頁上限，所以不是硬錯。

### 3. `021_wiki`

目前狀態：

- 93 個 `.md`。
- 檔名都符合 `{名稱}_{YYYYQn}.md`。
- 沒有空歸檔。
- 沒有重複 link target。
- 沒有 `0000Q0`。

## 本次產出的輔助檔

- `wiki_cleanup_plan.md`
- `wiki_cleanup_report.md`
- `scratch/wiki_cleanup.py`
- `scratch/wiki_tools/`
- `scratch/wiki_cleanup_backup_20260605_124318/`
- `scratch/wiki_cleanup_backup_20260605_124421/`
- `scratch/wiki_cleanup_merged_0000Q0/`

## 待處理事項

### P1：整理 `02_wiki/市場與需求.md` 的子題導覽

目前 `02_wiki/市場與需求.md` 有兩條 topic 導覽連結放在 `## 實踐洞察與案例` 區塊內：

- `[[市場與需求_近期觀察]]`
- `[[市場與需求_前期趨勢]]`

這兩條不是案例，應移到新的 `## 子題導覽` 區塊，避免日後 稽核 或腳本把它們誤算成案例。

建議修法：

```markdown
## 子題導覽
- [[市場與需求_近期觀察]]：情緒消費、品牌案例、零售變革、新消費趨勢（2026-04 ~ 06）
- [[市場與需求_前期趨勢]]：宏觀消費結構、在地文旅、AI 影響下的市場變化（2026-02 ~ 04）
```

並從 `## 實踐洞察與案例` 移除原本兩條。

### P2：決定 topic 頁是否也需要上限

目前 `022_wiki_topics/品牌_公關與消費洞察.md` 有 51 條案例。

可以討論是否要讓 topic 頁也有上限，例如：

- topic 頁最多 50 條。
- topic 頁超量時也歸到 `021_wiki/{Topic}_{YYYYQn}.md`。

### P3：是否建立 `022_wiki_topics/_index.md`

現在 topic 頁已經搬到 `022_wiki_topics`，但還沒有 index。

可討論是否建立：

- topic 清單
- 所屬標準標籤
- 最近更新時間
- 案例數

## 注意事項

- 目前 git worktree 原本就有大量非本次造成的 `00_Inbox` / `01_Liter` 變更，不要誤判為這次 wiki 清理造成。
- 後續如果要 commit，請先做 scoped diff，只看 `02_wiki`、`021_wiki`、`022_wiki_topics`、`98_LOG`、`scratch/wiki_cleanup.py`、`wiki_cleanup_report.md`。
