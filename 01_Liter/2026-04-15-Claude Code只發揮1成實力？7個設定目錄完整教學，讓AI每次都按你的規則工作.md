---
title: "Claude Code只發揮1成實力？7個設定目錄完整教學，讓AI每次都按你的規則工作"
source: "https://www.bnext.com.tw/article/90642/claude-code-folder-config-guide"
date: 2026-04-15
tags: [人工智慧, 學習與思考, 數位系統, 產品]
keywords: [Claude Code, .claude資料夾, agents, CLAUDE.md, hooks, settings.json]
type: 技術分析
raw_ref: "[[2026-04-15/Claude Code只發揮1成實力？7個設定目錄完整教學，讓AI每次都按你的規則工作]]"
project: [~]
wiki_evolved: true
wiki_evolved_at: 2026-04-15
principle: []
links: '{"direct":[],"deep":[],"serendipity":[]}'
status: draft
---
## 核心洞察

> .claude/ 資料夾讓使用者把個人工作規則「基因化」給Claude——這是AI從通用工具到專屬助手的關鍵設定，也是AI個人化的底層基礎設施。

## 重點摘要

**7個設定目錄功能：**

| 目錄 | 功能 | 類比 |
|------|------|------|
| agents | 自訂AI助理團隊，各有角色設定 | 組織架構 |
| CLAUDE.md | 全域規則說明書（每次啟動必讀）| 上工前必讀文件 |
| commands | 自訂/指令集，封裝複雜操作 | 巨集指令 |
| hooks | 特定事件的自動化觸發器 | 工作流自動化 |
| memories | 長期記憶存放區 | 個人知識庫 |
| mcp.json | MCP伺服器連線設定 | 外部工具橋接 |
| settings.json | 核心行為設定檔 | 系統偏好 |

**核心邏輯**：
- 內建子代理（Explore、Plan、general-purpose）→ 通用任務
- 自訂子代理（.claude/agents/）→ 專職同事，根據工作流打造

**為什麼重要**：從「每次重新解釋規則」到「規則永久生效」——這是AI工具「個人化」的本質提升。

## 值得深思的問題

1. **個人工具視角**：偷偷的.claude/設定目前有哪些可以優化？哪些agents可以建立（顧問分析agent、地方創生研究agent）？
2. **顧問服務視角**：如何幫助客戶建立他們自己的.claude/設定，讓AI助理真正貼合他們的業務邏輯？
3. **系統設計視角**：「規則基因化」這個概念能否應用到其他AI工具的設定？（不只是Claude Code）


## 關聯筆記

- [[2026-03-31-MCP到Skill的範式轉移AI認知架構的進化|MCP到Skill的範式轉移AI認知架構的進化]] — 同樣探討AI工具的架構設計，.claude/設定是其中的個人化層面
- [[2026-03-31-OpenAI給Claude Code發插件，兩大AI巨頭化敵為友|OpenAI給Claude-Code發插件兩大AI巨頭化敵為友]] — Claude Code的生態系擴展，與本文的設定教學互為補充

---
> [!TIP]
> AI的真正價值不在取代人，而在放大人的獨特判斷力。
