---
title: Prompt Master免費安裝教學，不用一直問AI也能寫出精準提示詞
source: https://www.bnext.com.tw/article/90592/prompt-master
date: 2026-04-15
status: raw
---

你是否有過這種經驗：把相同的提示詞（Prompt）分別貼入 Claude、Gemini 或 ChatGPT 等 AI 工具中，得出來的結果卻大相徑庭？因此，你得重複修改提示詞，直到獲得可用的答案。在這一來一往的互動過程中，往往白白浪費了寶貴的時間與模型額度（token）。為此，如何「寫好提示詞」成了提升問答效率的關鍵。

《未來商務》介紹一款免費的開源工具「 Prompt Master 」，它可以直接整合進 Claude，幫你自動生成任何 AI 工具的精準提示詞。2 分鐘即可完成安裝，完整說明請繼續往下閱讀。

## Prompt Master 是什麼？

Prompt Master 是一套專為 Claude 設計的技能外掛（Claude Skill），即一組可重複使用的指令集。由開發者 Nidhinjs 在 GitHub 上以 MIT（麻省理工學院）授權釋出，完全免費。它的核心功能是：自動偵測你目標使用的 AI 工具，並將你的原始需求改寫成最符合該工具邏輯的格式。

它支援超過 20 種 AI 工具，涵蓋推理模型（Claude、ChatGPT、Gemini、o1/o3）、圖像生成（Midjourney、DALL-E、Stable Diffusion）、程式碼工具（Cursor、GitHub Copilot）、自主 AI 代理（Devin、Claude Code）、影片生成（Runway）、工作流程自動化（Zapier、Make）及其他。

## Prompt Master 安裝方式，2 分鐘完成

### 方法一：直接在 Claude 上傳 Prompt Master 技能包（最推薦）

1. 前往 github 下載 Prompt Master 技能外掛
2. 點選右上角綠色「Code」按鈕，選擇「Download ZIP」下載整個專案
3. 接著，打開網頁/桌面版 Claude
4. 點選左側欄 → 自訂（Customize）→ 技能（Skills）→ 上傳技能（Upload a Skill）
5. 把剛剛下載的資料夾（不需解壓縮）進行上傳
6. 完成後，你在 Claude 的對話框就能直接呼叫 Prompt Master

### 方法二：透過終端機安裝（適合開發者）

```
mkdir -p ~/.claude/skills
git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master
```

## 如何使用 Prompt Master？

安裝後直接在 Claude 對話框用自然語言呼叫。例如：「Write me a prompt for Cursor to refactor my auth module」、「Generate a Midjourney prompt for a cyberpunk city at night」、貼上舊提示詞請它修正，或直接在呼叫「/prompt-master」後說明需求。

## Prompt Master 背後的運作原理是什麼？

Prompt Master 並非隨機改寫文字，其核心邏輯建立在對主流提示詞工程（Prompt Engineering）框架的深度整合。當你輸入指令時，它會啟動後台的「框架比對引擎」，從 12 種提示詞框架自動比對最適合當前工具的一款：

內建 12 種架構自動選用：

- RTF（角色、任務、格式）：快速一次性任務
- CO-STAR（情境、目標、風格、語調、受眾、回應）：專業文件、報告、商務寫作
- RISEN（角色、說明、步驟、最終目標、範圍縮小）：複雜的多步驟項目
- CRISPE（能力與角色、洞見、陳述、個性、實驗）：創意作品、品牌聲音、迭代內容
- Chain of Thought（思維鏈）：數學、邏輯、調試、多步驟分析
- Few-Shot（少量範例）：一致的結構化輸出、模式複製
- File-Scope Template：Cursor、Windsurf、Copilot（IDE 型程式碼 AI）
- ReAct + Stop Conditions：Claude Code、Devin、AutoGPT — 任何自主代理
- Visual Descriptor（視覺描述）：Midjourney、DALL-E、Stable Diffusion、Sora
- 參考影像編輯：編輯現有影像
- ComfyUI：基於節點的影像工作流程
- Prompt Decompiler（提示詞解構工具）：破解簡化、調整、簡化或分割現有提示

這些框架均已驗證，並明確排除了已知產生幻覺或不可預測輸出的方法（思維樹、思維圖、普遍自我一致性、提示鏈）。

除此之外，Prompt Master 會內建一個記憶區塊（Memory Block），自動儲存使用者的風格偏好、驗證方式、命名規範等關鍵決策，讓 AI 不會在同一專案中給出前後矛盾的建議，以確保輸出的品質一致性。

## Prompt Master 適合哪些人使用？

這款工具適合需要在不同 AI 工具遊走及切換的使用者，如常用 AI 工具的內容創作者、開發者（搭配 Cursor、GitHub Copilot、Claude Code 效果最佳）、設計師（提升 Midjourney、DALL-E 出圖品質）、對 AI Workflow 有興趣的使用者（搭配 Zapier、Make 生成精確代理指令）。
