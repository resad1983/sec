---
title: "Token 為王的資安新時代 AI 算力大開，防禦者如何用「鈔能力」取勝？"
source: "https://cyberq.tw/2026/04/17/when-cybersecurity-defense-becomes-tokens-war/"
date: 2026-04-17
status: raw
---

在 AI 代理程式（AI Agents）深入軟體開發日常的 2026 年，我們對於 AI 的關注焦點除了它能寫出多少程式碼，也包括它能找出多少漏洞。

科技策略專家 Drew Breunig 日前發表了一篇名為《 [Cybersecurity Looks Like Proof of Work Now](https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html) 》（網路安全現在看起來就像工作量證明）的文章，說明了新一代 AI 資安模型的驚人能力，更指出網路安全的底層邏輯已經被徹底改寫。

## Anthropic Mythos 與沒有極限的漏洞提款機

由於 Anthropic 近期研發、卻因在電腦安全任務上能力過強而暫不對大眾公開的新模型 [Mythos](https://red.anthropic.com/2026/mythos-preview/) ，是市場的焦點，目前僅提供給關鍵軟體開發商測試與加固系統安全上。

Breunig 在文章中引用了 [英國人工智慧安全研究所（AISI）針對 Mythos 的第三方分析報告](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) 。AISI 設計了一項名為「The Last Ones」的 32 步驟企業網路攻擊模擬（人類專家需耗時約 20 小時）。

測試相關資料是這樣的，AISI 為模型每次嘗試編列了 1 億個 Token 的預算（折合約 $12,500 美元）。

在對 Mythos、Opus 4.6 以及 GPT-5.4 進行的 10 次測試中，Mythos 是唯一成功完成任務的模型，成功率為 3/10（總測試耗費 $12.5 萬美元）。

最駭人的發現是，在尋找漏洞這件事上，AI 沒有表現出邊際效益遞減。 只要你繼續提供 Token 預算，模型就能繼續找出新的漏洞。

## 資安淪為算力的工作量證明

基於上述資料，Drew Breunig 提出的想法是，未來的資安防禦，將退化為一條簡單暴力的經濟學方程式。他認為，「要加固（Harden）一個系統，你必須花費比攻擊者更多的 Token 去發現並修補漏洞。你不必比別人聰明，你因為付了更多錢而獲勝。」

這種機制就像加密貨幣的工作量證明（Proof of Work, PoW），只要你買足夠的 Token 算力，你就有機會搶先挖出漏洞。

在這種算力即安全的新常態下，Breunig 點出開源軟體（OSS）反而會變得比以往更有價值。因為 Linus 定律（給定足夠的眼球，所有的 Bug 都將浮現）在 2026 年已經擴展為給定足夠的 Token。企業可以集資共享算力預算來稽核開源專案，而閉源軟體則必須孤軍奮戰，獨自承擔龐大的 AI 掃描開銷。

## 開發者與防禦者該怎麼辦呢？

CyberQ 以資安從業的角度來看，這個看似由算力決定一切的未來，其實可以有更深層次的探討，

**1、防禦者其實享有不對稱優勢**

雖然帳面上看起來是比誰有鈔能力，口袋誰的夠深，但實際上 CyberQ 認為，防禦方擁有絕對的效率優勢，在美國與一些先進市場，藍隊的優秀人才，薪資是可以比紅隊要高不少的。攻擊方假設利用工具、 API 或二進制檔案進行全盤掃描，而擁有原始碼的防禦方，可以直接將 AI 的注意力集中在剛修改過程式碼的 PR（Pull Request）上。在同樣燃燒 Token 的情況下，防禦者的效率遠高於攻擊者，因此長遠來看，這類資安模型反而會讓世界更安全。

**2、資安沒有所謂的 AI 垃圾 (Slop)**

在 AI 充斥的時代，許多人抱怨網路上充滿 AI 生成的垃圾內容（Slop）。但是在資安領域，漏洞研究最棒的地方在於，漏洞要麼存在，要麼不存在。世界上沒有所謂的 Slop 漏洞。只要 AI 能精確跑出權限升級或提權的步驟，它就是一個具備實質價值的產出。

**3、原始碼外洩的災難性升級**

不過在實務上，過去員工電腦被駭或原始碼外流可能只是虛驚一場，因為攻擊者不一定有精力去翻找你龐大的程式庫，但現在，駭客只需把外流的程式碼丟給廉價的模型進行自動化掃描，幾個小時內就能將程式碼中的微小瑕疵轉變為致命的權限升級攻擊，因此企業資料外流的風險與相關管控 DLP 的措施會比以往更重要。

**4、軟體經濟學的重塑**

面對高昂的 Token 審計成本，軟體該如何發展？CyberQ 認為，未來的開源軟體可能會轉變為「開放規格（Open Spec）」。人類可能不需要再編寫或維護具體的大量原始碼，而是維護高階規格，實際的程式碼由模型在部署時即時生成。屆時，所有的資安與治理壓力，都將轉移到 AI 模型層面來解決。

## 迎接加固作為獨立階段的時代

CyberQ 認為，我們在 AI 蓬勃發展的當下，已經看到了軟體開發流程的可能變革。未來的 Agentic（代理化）開發將被明確拆分為前期開發與後期加固，人類的介入與決策是前期的瓶頸，而金錢與 Token 預算則是後期的唯一限制。

當花錢買 Token成為捍衛系統安全的必要成本時，每一家科技公司都必須重新盤算，你的防禦預算，跑得贏隱藏在暗處的 AI 駭客嗎？怎樣掌握藍隊應該有的優勢，開發出適合自己防禦的流程和避免資料外流，將是未來的持續強化重點。

<iframe title="解析 Claude Opus 4.7 AI 代理與寫程式的巔峰，卻因隱形漲價與檢索退化引發社群關注？ — CyberQ 賽博客" src="https://cyberq.tw/2026/04/17/analyzing-claude-opus-47-the-pinnacle/embed/#?secret=33fum0rAez#?secret=d3V6Q9aA0P" width="500" height="335" frameborder="0"></iframe><iframe title="駭客攻破 a16z 投資的 AI 網軍農場！發迷因嘲諷 a16z — CyberQ 賽博客" src="https://cyberq.tw/2026/04/14/hackers-breach-a16z-invested-quotai/embed/#?secret=7LYHcmpeVX#?secret=216zqOOykH" width="500" height="335" frameborder="0"></iframe><iframe title="歐洲網路安全局（ENISA）4 月份最新漏洞警告：未經授權 RCE 與零日攻擊企業邊界防護 — CyberQ 賽博客" src="https://cyberq.tw/2026/04/12/eu-cyber-security-agency-euvd/embed/#?secret=7TyYOE9ven#?secret=5DLoxziykW" width="500" height="335" frameborder="0"></iframe><iframe title="WireGuard Windows 用戶端新版革新了底層架構與微軟憑證風波始末 — CyberQ 賽博客" src="https://cyberq.tw/2026/04/11/the-new-version-of-the-wireguard/embed/#?secret=tfOKQU0s7d#?secret=CjiMyawtuJ" width="500" height="335" frameborder="0"></iframe><iframe title="知名硬體監控工具 CPUID 網站遭駭：HWMonitor 與 CPU-Z 下載連結遭替換為惡意軟體 — CyberQ 賽博客" src="https://cyberq.tw/2026/04/10/the-website-of-the-well-known-hardware/embed/#?secret=rutYpHJf5s#?secret=yUH7tKFDU3" width="500" height="363" frameborder="0"></iframe><iframe title="揮別盲目的背景連線：macOS 知名網路監控工具 Little Snitch 正式登陸 Linux — CyberQ 賽博客" src="https://cyberq.tw/2026/04/09/little-snitch-for-linux/embed/#?secret=gy4xlpJEQt#?secret=J3EQYWRtt1" width="500" height="309" frameborder="0"></iframe><iframe title="為什麼 ChatGPT 突然不能打字？逆向工程揭密 Cloudflare 的隱藏防護機制 — CyberQ 賽博客" src="https://cyberq.tw/2026/03/31/chatgpt-cloudflare-react-security-check/embed/#?secret=kKE1nqKPUe#?secret=YyJbUb2qEa" width="500" height="335" frameborder="0"></iframe>