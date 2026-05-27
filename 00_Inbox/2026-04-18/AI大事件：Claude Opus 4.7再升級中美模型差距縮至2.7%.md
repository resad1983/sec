---
title: AI大事件：Claude Opus 4.7再升級，中美模型差距縮至2.7%
source: 人人都是產品經理
url: https://www.woshipm.com/ai/6379704.html
date: 2026-04-18
score: 10
tags: [人工智慧, 科技影響, 學習與思考, 資料與演算法]
---

今天我认真翻了翻AI圈的新消息，发现有几个变化挺有意思的——Anthropic这次直接把Claude Opus拉到了4.7，编码和Agent能力又上了一个台阶；具身智能那边，智元直接搞了2500人的合作伙伴大会，4款新本体现成亮相，这个赛道真的在加速；阿里的世界模型也出来了，视频编辑方向直接冲到了全球第一。数字层面上，中国日均词元调用量突破140万亿，Stanford的报告说中美模型差距只剩2.7%——这些都不是小事。趁周末整理了15条最近24小时我觉得值得关注的内容。

## 1. Anthropic正式发布Claude Opus 4.7

Anthropic正式发布Claude Opus 4.7，这是其最新旗舰模型。新版本在编码、Agent任务、视觉理解和多步骤任务上均有显著提升，官方描述为"更强的性能、更高的一致性"。Anthropic当前估值已达800亿美元。值得注意的一个细节：Opus 4.7上架后，Opus 4.5从商店消失，Opus 4.7直接成为旗舰担当。

点评：Anthropic每次旗舰更新都在刷新编码能力的上限，4.7这次重点打磨了Agent任务一致性——意思是AI在多步骤任务中不会轻易"迷路"或前后不一致。对需要长时间自主工作的场景，这是关键提升。

## 2. Claude Code v2.1.111发布

Claude Code连续发布v2.1.111和v2.1.112两个版本。新增xhigh努力等级（介于high和max之间），并引入了交互式努力滑块（/effort命令），用户可以更灵活地控制AI的思考深度。Auto模式正式向Max订阅用户全面开放，无需再排队等候内测资格。

## 3. Google MaxText新增SFT和RL支持

Google的MaxText框架新增支持在单主机TPU配置上进行监督微调（SFT）和强化学习（RL）训练，使用JAX和Tunix库实现模型精调。这一更新大幅降低了在Google TPU上进行模型后训练的门槛——之前做这类训练需要大规模集群，现在单台TPU机器就能跑。

## 4. NVIDIA开源量子AI模型Ising

NVIDIA发布开源量子AI模型"Ising"，专门用于量子计算机的校准优化。该模型基于统计物理学的Ising模型框架，将量子系统的校准时间从原来的数天大幅压缩至数小时。

## 5. Anthropic MCP协议安全漏洞

安全研究人员披露Anthropic的MCP（Model Context Protocol）协议存在设计缺陷，可能导致远程代码执行漏洞，影响全球超过20万台AI服务器。漏洞细节已提交给Anthropic，官方正在修复中。

## 6. 阿里发布世界模型HappyOyster

阿里巴巴ATH创新事业部团队发布新一代开放世界模型HappyOyster，支持实时交互和多模态创作。HappyHorse-1.0在视频编辑方向的全球排名达到第一。

## 7. 腾讯开源Huanyuan 3D World Model 2.0

腾讯正式开源Huanyuan 3D World Model 2.0，支持一键生成可编辑的3D资产，可导出多种格式并与Unity、Unreal等主流游戏引擎无缝集成。
