---
title: Anthropic新工具：Sonnet遇難題可請教Opus的Advisor策略
source: 人人都是產品經理
url: https://www.woshipm.com/ai/6374802.html
date: 2026-04-10
score: 7
tags: [人工智慧, 數位系統, 科技影響, 資料與演算法]
---

Anthropic推出Advisor Tool，實現「Advisor策略」：讓Sonnet或Haiku在執行任務遇到困難決策點時，自動向更強大的Opus模型請教指導。

## 創新邏輯

顛倒傳統多Agent方式的邏輯——「Sonnet作為執行者運行完整任務，Opus作為顧問在需要時提供指導」。小模型自主工作，只在必要時請求指導，而非大模型指揮小模型。

## 性能數據

- SWE-bench Multilingual：Sonnet + Advisor提升2.7個百分點，成本降低11.9%
- BrowseComp：Haiku + Advisor達到41.2%（是Haiku單獨的兩倍），成本比Sonnet單獨低85%
- 實現「智能接近Opus但成本接近Sonnet」的突破

## 技術優勢

- 無需複雜任務分解或協作框架
- Advisor只生成400-700 token的短計畫，成本極低
- 整個過程在單次API調用中完成，內建上下文共享
