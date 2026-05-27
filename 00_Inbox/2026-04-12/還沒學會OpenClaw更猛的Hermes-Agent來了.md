---
title: 還沒學會OpenClaw更猛的Hermes-Agent來了
source: 人人都是產品經理
url: https://www.woshipm.com/ai/6375548.html
date: 2026-04-12
score: 8
tags: [人工智慧, 數位系統, 產品, 學習與思考]
---

Hermes Agent 是由 Nous Research 開發的開源 AI 智能體運行時，在兩個月內獲得 51.8k stars。與 OpenClaw 的主要區別在於其自進化機制——它能自動保存執行流程為可復用技能，而不需人工干預。

**關鍵特性**

**四層架構：**
- 入口層：支持 CLI、Telegram、飛書等多平台
- Agent 層：兼容 Claude、OpenAI 等多個模型供應商
- 執行層：內置 28 個工具，提供 6 種代碼沙箱
- 持久層：整合會話、長期記憶、技能庫和用戶畫像

**自進化機制**

「執行任務→遇到問題自主修正→完成後自動保存為 Skill→下次復用→持續改進」的閉環，對比 OpenClaw 需要手動安裝和微調的方式有質的差異。

**技術演進線**

從「Prompt Engineering→Context Engineering→Harness Engineering→自進化 Agent」的演進路徑，強調人的參與度逐步降低，從操作者升級為設計者和監督者。

**實際限制**

- 本地進程需持續運行，24 小時在線需部署到服務器
- 大規模 token 消耗仍可能觸發 API 限流
- 生態相比 OpenClaw 仍處早期階段
