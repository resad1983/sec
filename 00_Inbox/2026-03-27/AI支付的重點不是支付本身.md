---
title: AI支付的重点 不是支付本身
source: https://www.jinse2.com/blockchain/3730989.html
date: 2026-03-27
author: 刘红林律师
tags: [AI支付, AI Agent, Stripe, Google, Coinbase, 電商, 平台策略]
type: 深度分析
status: raw
score: 9/10
---

## 核心論點

「AI 支付的重點，不是支付本身」——大家最後只會用一個樸素的標準判斷：我跟 AI 說了一句，它到底能不能真的替我把事辦了。

## 中國 vs 海外：兩種故事

**中國**：AI 支付是成熟互聯網體系上的自然延伸。平台（阿里/字節）已把商家、支付、配送、地圖組織好，AI 只是把能力重新編排，讓用戶從「自己操作」→「開口就行」。用戶感受：「這功能挺方便」。

**海外**：AI 支付是一場迟來的補課。服務入口、商家、支付工具掌握在不同公司，AI 替用戶完成交易時立刻遇到「別人認不認你這個 AI 代理」。Amazon vs Perplexity 訴訟（2026/3/9）：你授權給 AI ≠ 網站授權給 AI。

## 三條實現路徑（中國）
1. AI 看屏幕替你操作（問題：頁面一變就出錯，如豆包手機被微信圍剿）
2. 平台把服務能力直接給 AI 調用（最順，阿里千問/字節豆包）
3. 跨平台跨公司（hard mode，目前無人挑戰）

## 海外三大解法

**Google AP2**（2025/9）：解決「憑什麼信任 AI 下單」→ Cart Mandate（用戶確認）+ Payment Mandate（告知支付網絡）+ 與 PayPal 整合

**Stripe ACP + Machine Payments**：
- ACP（Agentic Commerce Protocol，2025/9 with OpenAI）：「AI 可讀的 checkout 標準」，商家開放 API 給 AI 直接調用
- Machine Payments（2026/3）：軟體為軟體付錢，API/算力/數據，低至 0.01 USDC

**Coinbase Agentic Wallets**（2026/2）：讓 AI 成為「獨立的經濟行為體」，有自己的錢包，能自主收支，不需每次等人確認

## 三者定位
- Google：補信任機制
- Stripe：接進現有商業網絡
- Coinbase：押注「軟體直接為軟體付錢」的未來
