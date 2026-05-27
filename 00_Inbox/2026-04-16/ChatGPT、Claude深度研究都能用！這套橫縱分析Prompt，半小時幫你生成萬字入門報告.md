---
title: "ChatGPT、Claude深度研究都能用！這套橫縱分析Prompt，半小時幫你生成萬字入門報告"
source: "https://www.bnext.com.tw/article/90656/horizontal-vertical-analysis-ai-research"
date: 2026-04-16
status: raw
---

X 帳號「數字生命卡茲克」（@khazix0918）近日分享了一段他使用兩年的深度研究 Prompt，聲稱能在 30 分鐘內讓 AI 產出一份上萬字的研究報告，幫助使用者快速建立任何陌生領域的認知框架。

## 為什麼「兩條軸線」比直接提問有效？

橫縱分析法的底層邏輯，來自語言學家索緒爾（Ferdinand de Saussure）的經典研究框架：歷時分析（Diachronic）追蹤一個事物如何隨時間演變，共時分析（Synchronic）觀察它在某個時間切面上與其他事物的關係。

核心邏輯很簡單：單看歷史，你知道它怎麼走到今天，但不知道它現在站在哪裡；單看競爭對手，你知道它跟誰比，但不知道為什麼會變成這樣。

掌握最新AI、半導體、數位趨勢！訂閱《數位時代》日報及社群活動訊息

兩條軸線交叉，才能看到全貌。

## 30分鐘搞懂任何陌生領域！怎麼用？4步驟操作

在動手之前，先用一張圖釐清兩條軸線的關係：

### 第 1 步：選一個支援「深度研究」的 AI 工具

橫縱分析法的效果與工具能力直接相關。建議優先使用支援深度研究（Deep Research）功能的工具，這類工具會主動聯網搜尋、交叉驗證，單次任務通常耗時 10 分鐘以上，品質遠優於普通對話模式。

目前適用的工具包括： [ChatGPT](https://chatgpt.com/) Deep Research、 [Claude](https://claude.ai/) 深度研究模式等。

### 第 2 步：複製 Prompt，改一行就能用

完整 Prompt 開源在 [GitHub 倉庫](https://github.com/KKKKhazix/khazix-skills) ，使用時只需修改開頭的「研究對象」等號右邊。以下是核心結構的精簡版，可直接複製貼入工具的深度研究模式：

```
> 橫縱分析法

## 變數定義
研究對象 = [在此填入你要研究的主題]

你是一位資深的技術與商業研究分析師。請使用「橫縱分析法」對「研究對象」
進行一份完整的深度研究報告。

### 一、縱向分析（Diachronic / Longitudinal）
沿時間軸，完整還原研究對象從誕生到現在的發展全貌：
1. 起源追溯：誕生背景、技術/理念基礎、核心推動者
2. 誕生節點：首次發布/成立時間、最初形態
3. 演進歷程：按時間梳理所有關鍵節點
4. 決策邏輯：還原每個節點背後的原因
5. 用故事方式串連，不要寫成流水帳年表

### 二、橫向分析（Synchronic / Cross-sectional）
以當前時間點為切面，與同賽道的競品進行全面對比：
- 核心差異：技術路線、產品形態、商業模式、目標用戶
- 用戶視角：真實口碑、使用體驗、優缺點
- 生態位分析：在賽道中的位置，填補什麼空白
- 趨勢判斷：競爭格局走向、機會與風險

### 三、橫縱交匯
把縱向脈絡與橫向格局結合，給出對研究對象當前位置
和未來走向的判斷。

寫作風格：可讀性優先，用故事驅動而非條列羅列。
觀點必須建立在事實之上，用具體細節取代空洞形容。
```

研究對象可以是產品（Cursor、Claude Code）、公司（Anthropic、OpenAI）、技術概念（MCP 協定、RAG），甚至是人物。

Prompt 會根據對象類型自動調整分析側重點。想要更完整的指令細節（包含篇幅要求、競品場景分類等），可直接到 [GitHub 倉庫](https://github.com/KKKKhazix/khazix-skills) 取用原版。

### 第 3 步：發送，等 AI 跑完

把 Prompt 貼入深度研究模式，直接發送。AI 可能會先確認研究對象的範圍，補充說明即可。

《數位時代》以「harness engineering」為對象實測，使用 Claude 深度研究模式， **14 分 33 秒** 後產出 **約 7,500 字** 的報告（Claude 將範圍聚焦在 AI／ML 訓練工具生態，而非 agent 層面的 harness 概念）。

報告中一個具分析縱深的判斷：

> 每一次 AI 能力的突破，都會在 6 到 12 個月內催生出一波工程化工具的爆發，而這些工具又降低了下一輪突破的門檻。

前後共耗時 14 分半鐘、7,500 字，換來的不是一份能當作切入陌生領域的研究地圖。完整報告見： [Claude 實測產出（harness engineering）](https://claude.ai/artifacts/latest/019d9042-2d11-7620-9b4d-3de6fee3ea29) 。

![縱橫分析報告](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/3i32-1776243580.png?w=1200&output=webp)

若對特定的陌生領域有興趣，可以試看看本文提供的縱橫分析法 prompt。

圖／ Claude

### 第 4 步：以報告為地圖，針對疑點深挖

拿到報告後，先快速通讀建立框架，再針對有疑問或特別感興趣的段落搜尋更多資料驗證。

> **關鍵心態** ：報告是研究的起點，不是結論。橫縱分析法產出的框架加上自己深挖，比從零開始的效率高太多。

## 進階玩法：裝成 Skill 讓 Agent 自動跑

如果你使用 Claude Code、Cowork 或 Codex 等 Agent 工具，原作者還提供了 Skill 版本（hv-analysis），安裝後對 Agent 說「幫我研究一下 XXX」就會自動執行。

Skill 版本額外支援自動網路搜尋、串接 arXiv API 查論文，並產出排版好的 PDF 報告。同樣可在 [GitHub 倉庫](https://github.com/KKKKhazix/khazix-skills) 取得。

## 這套方法有什麼限制？

**要注意的是，AI 產出的報告仍可能有事實錯誤。** 儘管模型幻覺率已大幅降低，報告中的數據與事實仍需自行驗證，不能直接當定論使用。

報告品質也高度依賴工具能力。深度研究工具（每次 10 分鐘以上）效果明顯優於僅有基本網路搜尋的工具（不到一分鐘），後者在資訊完整度和準確度上都會打折扣。

最根本的限制是：橫縱分析法幫你快速搭起認知框架，但取代不了真正深入的第一手研究。它是地圖，不是目的地。

現在，工具讓你取得資訊的成本趨近於零，但你要問什麼問題、從什麼角度看、怎麼把散落的資訊組織成判斷，這些方向得自己定。

> 延伸閱讀：  
> [用Claude Code管理100篇研究筆記！OpenAI共同創辦人公開LLM知識庫系統，貼一段指令就能建起來](https://www.bnext.com.tw/article/90530/llm-knowledge-base-obsidian-claude-code)  
> [不用Obsidian也能建AI知識庫！Karpathy同款「說明書」設定，4.1萬人超人氣方法完整拆解](https://www.bnext.com.tw/article/90650/andrej-karpathy-ai-how)

資料來源： [@khazix0918 X 貼文](https://x.com/khazix0918/status/2043555868902637845) 、 [khazix-skills GitHub 倉庫](https://github.com/KKKKhazix/khazix-skills)

本文初稿為AI編撰，整理．編輯/ 李先泰

[![](https://cdn.bnextmedia.com.tw/img/16x9.png "風格經濟學程 2026 搶先選修｜設計驅動的品牌策略學院")](https://eventgo.bnextmedia.com.tw/event/detail/e34173u694e29aef3348?utm_source=web_bn&utm_medium=aa_event_er&utm_campaign=stage_1&utm_term=model_5 "風格經濟學程 2026 搶先選修｜設計驅動的品牌策略學院")

[風格經濟學程 2026 搶先選修｜設計驅動的品牌策略學院](https://eventgo.bnextmedia.com.tw/event/detail/e34173u694e29aef3348?utm_source=web_bn&utm_medium=aa_event_er&utm_campaign=stage_1&utm_term=model_5 "風格經濟學程 2026 搶先選修｜設計驅動的品牌策略學院")

[

活動詳情

](https://eventgo.bnextmedia.com.tw/event/detail/e34173u694e29aef3348?utm_source=web_bn&utm_medium=aa_event_er&utm_campaign=stage_1&utm_term=model_5 "風格經濟學程 2026 搶先選修｜設計驅動的品牌策略學院")

關鍵字： [＃AI工具](https://www.bnext.com.tw/tags/AI%E5%B7%A5%E5%85%B7) [＃提示詞（prompt）](https://www.bnext.com.tw/tags/%E6%8F%90%E7%A4%BA%E8%A9%9E%EF%BC%88prompt%EF%BC%89)

往下滑看下一篇文章

<iframe src="chrome-extension://ookjlbkiijinhpmnjffcofjonbfbgaoc/iframes/ads-stack.html?id=06Aa38pErDyjUDjPTWo2A&amp;ea=0x0CcB0D05912414625e43B229273441Eb43F8f8Ab&amp;cn=ethereumMainnet&amp;ads-meta=6&amp;ads-meta=7&amp;o=https%3A%2F%2Fwww.bnext.com.tw%2Farticle%2F90656%2Fhorizontal-vertical-analysis-ai-research&amp;categories=other&amp;categories=crypto" allow="accelerometer; gyroscope"></iframe><iframe src="chrome-extension://ookjlbkiijinhpmnjffcofjonbfbgaoc/iframes/ads-stack.html?id=dply745fKUcBBKjpne-Nw&amp;ea=0x0CcB0D05912414625e43B229273441Eb43F8f8Ab&amp;cn=ethereumMainnet&amp;ads-meta=6&amp;ads-meta=7&amp;o=https%3A%2F%2Fwww.bnext.com.tw%2Farticle%2F90656%2Fhorizontal-vertical-analysis-ai-research&amp;categories=other&amp;categories=crypto" allow="accelerometer; gyroscope"></iframe><video controls=""></video>

閱讀全文

<iframe src="chrome-extension://ookjlbkiijinhpmnjffcofjonbfbgaoc/iframes/ads-stack.html?id=FH8UfXv5odcxy70OQXU1K&amp;ea=0x0CcB0D05912414625e43B229273441Eb43F8f8Ab&amp;cn=ethereumMainnet&amp;ads-meta=3&amp;ads-meta=6&amp;o=https%3A%2F%2Fwww.bnext.com.tw%2Farticle%2F90656%2Fhorizontal-vertical-analysis-ai-research&amp;categories=other&amp;categories=crypto" allow="accelerometer; gyroscope"></iframe>

即時熱門文章

[1 Perplexity轉型AI代理，短短一個月營收成長50%！為什麼AI搜尋錢難賺？](https://www.bnext.com.tw/article/90569/perplexity-ai-agent) [2 每次換AI就得狂改prompt？Prompt Master免費安裝教學：2分鐘讓提示詞跨平台通用](https://www.bnext.com.tw/article/90592/prompt-master) [3 AI時代下，台灣軟體的生存機會在哪？簡立峰：別搶食衣住行小市場，去解決台積電等級的問題](https://www.bnext.com.tw/article/90612/ai-talent-brain-drain-bn370) [4 Claude Code只發揮1成實力？7個設定目錄完整教學，讓AI每次都按你的規則工作](https://www.bnext.com.tw/article/90642/claude-code-folder-config-guide) [5 不會Claude Code也能上手！用Projects打造AI工作流，5步驟養成長期記憶助理](https://www.bnext.com.tw/article/90621/claude-projects-skills-mcp-guide) [6 從會員數據到 AI 行銷：Vpon 打造零售業 AI-Ready 數據中台，提升決策效率](https://www.bnext.com.tw/article/90448/Vpon033026)

<iframe src="chrome-extension://ookjlbkiijinhpmnjffcofjonbfbgaoc/iframes/ads-stack.html?id=CKv6hBMFHnkzJ0szj2F-H&amp;ea=0x0CcB0D05912414625e43B229273441Eb43F8f8Ab&amp;cn=ethereumMainnet&amp;ads-meta=6&amp;ads-meta=7&amp;o=https%3A%2F%2Fwww.bnext.com.tw%2Farticle%2F90656%2Fhorizontal-vertical-analysis-ai-research&amp;categories=other&amp;categories=crypto" allow="accelerometer; gyroscope"></iframe><iframe src="chrome-extension://ookjlbkiijinhpmnjffcofjonbfbgaoc/iframes/ads-stack.html?id=a-YqdxpsODAYDbhmlAXsM&amp;ea=0x0CcB0D05912414625e43B229273441Eb43F8f8Ab&amp;cn=ethereumMainnet&amp;ads-meta=3&amp;ads-meta=6&amp;o=https%3A%2F%2Fwww.bnext.com.tw%2Farticle%2F90656%2Fhorizontal-vertical-analysis-ai-research&amp;categories=other&amp;categories=crypto" allow="accelerometer; gyroscope"></iframe>