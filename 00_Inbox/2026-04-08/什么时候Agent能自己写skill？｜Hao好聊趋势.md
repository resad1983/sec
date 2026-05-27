---
title: 什么时候Agent能自己写skill？｜Hao好聊趋势
source: https://mp.weixin.qq.com/s/9V0xYqveQigc3yJq-2-XQA
date: 2026-04-08
status: raw
---

---
title: "什么时候Agent能自己写skill？｜Hao好聊趋势"
source: "https://mp.weixin.qq.com/s/9V0xYqveQigc3yJq-2-XQA"
author:
  - "[[博阳]]"
published:
created: 2026-04-08
description: "其实，「让 skill 自己长出来」这个问题其实已经被追问了 26 年。"
tags:
  - "clippings"
---
原创 博阳 *2026年3月30日 22:03*

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/QmK3dYQtkw2lgiaukPXSC35EnQaJYibWq0ZE2BDXmJRuuGKWvYlhkPicLFYuicOhUTXAcyFiaekRMcotwSte0UCvEOvSOR8UJxw1G80G8QE479tg/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

腾讯前沿科技论文解读专栏，在代码与商业的交汇处，寻找AI的确定性。

**文｜博阳**

**编辑｜徐青阳**

龙虾为什么好用？其中一个答案就是它的skill太好用了。

2025 年 12 月 18 日，Anthropic 把 Agent Skills 发布为开放标准。一套标准化的文件夹规范，让 agent 像装 App 一样加载专业技能。每个 skill 文件夹里有一份 SKILL.md，写清楚这个技能是什么、怎么用，还可以放可执行脚本，让 agent 除了「知道怎么做」，还能真正动手。

标准一出，行业跟进速度快得异常。Microsoft 在 VS Code 和 GitHub 里直接集成。OpenAI 在 ChatGPT 和 Codex CLI 里采用了几乎一模一样的架构，只是没官宣。Cursor、Goose、Amp 等编码工具也跟了。Box 用 skill 教 Claude 把文件转成符合公司规范的 PPT 和 Excel，Notion 用 skill 让 Claude 直接在笔记里执行任务而不是光聊天。

这个标准为什么重要？模型公司们用MCP、CLI、记忆层等harness改造给 agent 装了手脚，但脑子里没有专业知识。

Agent Skills 补的就是这一层。不是「你整体上能调用什么工具怎么做事」，而是「一件具体的事，你该怎么把事做对」。

Skill就是工作流程中Know how的结晶。它的另一个好处是可以快速复制。一家公司写了一套合规检查 skill，直接分发给所有同事的 Agent 就行。

蓝图确实漂亮，然后现实撞了上来。

Anthropic 自带了一个叫 skill-creator 的工具，说是能帮用户自动生成 skill。上线第一周，开发者 Samhita Alla 专门观察了 100 多个用户的使用情况，结论是「大多数实现看起来更像玩具而不是工具。」

skill 该触发时不触发、塞进去的指令太多导致 agent 晕掉、安全漏洞、文件格式出错。反复出现。

自动生成的 skill 粗糙、不可靠，真正好用的 skill 全靠人手工打磨。

当然，skill这个产品之所以能流行，正是因为现阶段的Agent对于人类工作的流程、规范和know how还不够了解。

但我们还是希望 agent 能自己发现解决问题的方法。

其实，「让 skill 自己长出来」这个问题其实已经被追问了 26 年。

**01**

**从权重到代码，skill 追了二十六年**

1999 年，Rich Sutton 和他的学生 Doina Precup、Satinder Singh 提出了一个叫 options framework 的理论框架。核心想法是，agent 应该能自己发现和组合可复用的行为模块，而不是每次都从零开始、一步一步试。这是强化学习领域第一次正式提出类似skill的概念。

但那个年代的 skill 困在神经网络的权重矩阵里，不可解释、不可迁移、不可编辑。你训练出一个开门的 skill，想把它用到另一个环境里，几乎不可能。

这个困局持续了 24 年，直到 2023 年 Jim Fan 等人的 Voyager 在 Minecraft 里把 skill 从权重里拉到了代码里。在那里，GPT-4 驱动的 agent 在游戏中自主探索，每学会一个新能力就把它写成一段 JavaScript 函数，存进一个 skill library。下次遇到类似情况，先在 library 里检索，找到了就直接调用，找不到再造新的。

结果Voyager 获得的独特物品数量是前代最强方法的 3.3 倍，解锁科技树的速度快了 15.3 倍。skill 用代码写，意味着它天然可解释、可编辑、可组合、可迁移。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Voyager 架构图：自动课程、迭代提示机制与 Skill Library（Wang et al., 2023）

Voyager 真正的贡献不在数字。它证明了，当 skill 的表示形式从内部参数变成可读代码，整个游戏规则都变了。参数形态的 skill 是黑箱，看不到、改不了、没法分享给别的 agent。代码形态全都可以。这才是 26 年里真正的拐点。

Agent 不是变聪明了才学会 skill，而是 skill 变得可读了，才能被积累、检验、传播。

不过 Voyager 其实有个根本局限，它只活在 Minecraft 里。游戏规则封闭、状态可观测、验证即时。真实世界不是这样。一个处理财务数据的 agent 没法即时验证 skill 有没有在特殊情况下出错。

从 Minecraft 走进真实世界，验证、质量保证、跨环境迁移，一整套问题等着解决。

2025 年下半年到 2026 年初，Anthropic 定义了标准，产业有了需求，学术界有了着力点，事情开始密集变化。不是一篇论文，是一整批。从 skill 的自主发现、封装组合到持续改进，几乎每个环节都有了系统性方案。

skill 有了流通的基础设施之后，「skill 怎么来」从学术兴趣变成了产业瓶颈。

这波研究按 skill 的生命周期展开，包括三个部分，skill怎么被发现、怎么封装组合、怎么持续被改进。

**02**

**三条路都走通了，探索、失败、学习**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

最根本的问题先来。agent 能不能在没人手把手教的情况下，自己发现有用的 skill？

2025 年 6 月，KAIST 的 Yongjin Yang 等人发了 EXIF（Exploratory and Iterative Feedback），提出了一个很有意思的双 agent 架构。两个 agent，一个叫 Alice，一个叫 Bob，分工明确。Alice 是探索者，被放进一个环境里自由探索，尝试各种操作，记录下什么行得通、什么行不通。然后 Alice 回头看自己的探索轨迹，从中提炼出这算一个 skill 的定义。

接着这些 skill 被交给 Bob，Bob 拿着这些 skill 去执行具体任务。Bob 的表现被反馈回来，哪些 skill 好用，哪些不好用，Bob 在哪些地方卡住了，这些信息反过来引导 Alice 下一轮探索的方向。

这个循环持续迭代。Alice 探索 → 定义 skill → Bob 执行 → 评估短板 → 引导下一轮探索。重点在于整个过程不需要人类提供任何任务描述或 skill 定义，Alice 和 Bob 自己完成了从什么都不会到积累出一套可用 skill的全过程。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

EXIF 架构图：Alice 探索环境生成 Skill，Bob 执行任务并反馈

EXIF 最有意思的发现来自拆解测试。研究者试了让同一个模型同时扮演 Alice 和 Bob，直觉上，自己教自己应该效果很差。但结果是，单模型自进化居然也有效。skill discovery 不一定需要两个模型互补，一个模型的「探索」和「利用」能自己博弈出有效的 skill。

如果说 EXIF 是靠「探索」来发现 skill，Sentient 的 Salaheddin Alzubi 等人在 2026 年 3 月发表的 EvoSkill 则走了一条完全不同的路，靠「失败」。

EvoSkill 不让 agent 去自由探索环境。它让 agent 直接执行任务，然后分析失败原因。执行过程中的每一步操作都被记录下来。当任务失败时，一个 Proposer agent 审查这些执行记录，诊断出失败的具体原因，比如数据提取出了错、时间粒度搞混了、缺少多源验证，然后针对性地提出新 skill 或修改现有 skill。

提出的 skill 不是直接采纳，而是要过一道淘汰赛。新 skill 必须在验证集上证明自己比现有的 skill 组合更好，或者在不损害其他维度表现的前提下在某个维度上有进步，才能被保留。这套筛选机制借鉴了多目标优化里的帕累托前沿（Pareto frontier）思路。只保留那些「在任何维度上都不被别人全面压制」的 skill，其他的淘汰。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

EvoSkill 进化循环：从失败中提出新 Skill，经帕累托筛选后保留

因为发布在Anthropic已经把Skill安全产品化了之后，EvoSkill 的优化纯粹发生在 skill 层。不需要微调模型，不需要额外的训练数据，只需要让 agent 在任务上不断失败、不断分析、不断改进 skill。

经过迭代后的skill在 OfficeQA（办公场景的问答任务）上提升 7.3%，在 SealQA（搜索增强问答）上提升 12.1%。但更值得关注的是跨任务的通用性。从 SealQA 进化出来的 skill，不做任何额外适配，直接拿到 BrowseComp（一个结构迥异的网页搜索测试集）上用，提升了 5.3%。

进化出来的 skill 在自己的任务上管用，搬到别的任务上也管用。

SkillCraft 还有第三条路，需求驱动。agent 不靠探索也不靠失败，而是在执行任务时发现「我缺一个处理这类情况的 skill」，直接造。这就像程序员写代码写到一半，发现要用一个不存在的函数，于是停下来先写函数再回来继续。

这条路来自 UC Berkeley 和 EPFL 的联合团队。2025 年 12 月，Xu Huang、Junwu Chen 等人发表了 CASCADE（Cumulative Agentic Skill Creation through Autonomous Development and Evolution）。

CASCADE 的出发点不一样。科学研究用到的工具，比如材料模拟软件、化学计算包、机器学习力场等都极度专业。而且其用法文档分散，版本混乱，连人类科学家都经常要花几天才能跑通一个新软件。这使得让 agent 去「自由探索」或者「从失败中学」都不够，因为它首先得弄明白这些工具到底怎么用。

CASCADE 的解法是给 agent 装上两个 meta-skill（学技能的技能）。第一个是持续学习，遇到不会用的工具，agent 会自己去搜索文档、从网页提取代码示例、阅读源码，搞懂用法。第二个是自我反省，执行报错后，agent 不是简单地重试，而是回头检查运行时状态，用知识图谱回溯依赖关系，甚至直接去读底层包的源代码来定位问题根因。

这两个 meta-skill 不是硬编码的流程，而是通过精心设计的 prompt 和工具调用接口涌现出来的行为模式。

agent 在解决一个任务的过程中掌握的工具用法和调试经验，会被固化到记忆系统里，从短期的 session memory，到跨会话的 consolidated memory，最终沉淀为可复用的 skill set。下次遇到类似的工具或问题，直接调用已有经验。

在 SciSkillBench（116 个材料科学和化学研究任务）上，GPT-5 裸跑成功率 35.4%，加上 CASCADE 的进化机制后被曝光达到 93.3%。更值得注意的是，CASCADE 成功复现了已发表论文中的计算实验，还能驱动真实实验室的自动化合成流程。

这得操控一个它从未见过、没有文档、不在训练数据中的内部软件包。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

CASCADE 架构图：LLM + Skill Acquisition 范式与 DeepSolver 多 Agent 架构

上面提到的三条路径其实对应了人类学习技能的三种方式，好奇心驱动（我去试试看）、失败驱动（上次栽了所以学会了）、需求驱动（干活时发现缺这个）。

人类三种都用，但大多数人在大多数时候靠的是后两种。目前的 agent 也一样，探索这条路在真实环境里效率最低。

但人之所以学东西快，是因为三种模式可以自由切换，该探索时探索，该复盘时复盘，该查资料时查资料。目前没有任何一个系统同时具备三种。EXIF 不会主动查文档，EvoSkill 不会好奇地去探索未知领域，CASCADE 不会系统性地从失败中提炼经验。当前的 agent 在学习策略上还是偏科的。

至此，「skill 从哪来」这个问题有了答案，但答案还不完整。

**03**

**简单 skill 没问题，组合一崩就全崩**

一个skill 被发现之后，还得变成可靠的、可复用的模块。这一步没做好，前面的发现等于白搭。

上面这些方法发现的 skill，无一例外都是原子级的，单步操作、单个 API 调用、单一场景的处理逻辑。agent 造一个从网页提取表格数据的 skill，没问题。造一个调用某个 API 查询天气的 skill，也没问题。哪怕是使用工程模式明确的复杂工具去处理一个问题，都没问题。但真实世界的任务几乎不会只需要一个 skill。

给 5 个猫品种各调 5 个 API 收集详细信息，然后交叉对比生成报告。这需要把「查品种资料」「提取健康数据」「格式化输出」等多个 skill 嵌套组合起来，循环 5 次，再做一层汇总。这件事，目前的 agent 做起来会崩。

2026 年 2 月，中科院和哈尔滨工业大学发表了 SkillCraft，专门测量 agent skill 组合能力。126 个任务，21 个 API 家族，按两个维度缩放难度，实体数量（N）和每个实体的 API 调用复杂度（M）。N×M 构成一个二维矩阵，从 Easy（N=1, M=2）到 Hard（N=5, M=5），难度梯度很陡。

SkillCraft 设计了一个三阶段 Skill Mode 协议。第一阶段探索，给 agent 简单版任务自己摸索。第二阶段组合，把经验封装成可复用 skill。第三阶段复用，面对大规模同类任务，必须复用之前的 skill。

有 skill 加持到底能做到什么程度？这个差距就是 skill 组合能力的直接度量。

Claude Sonnet 4 在 Easy 上 baseline 已经 95%，开 Skill Mode 还是 95%。成功率没变，但 token 从 1.96M 降到 0.44M，省了 77%。强模型不需要 skill 帮它「做对」，但 skill 能帮它「做快」。

弱模型就翻车了。Kimi-K2-Thinking 在 Hard 上 baseline 38%，开 Skill Mode 反而掉到 33%。它造的 skill 有三分之一跑不通，一个 bug 在 5 个实体上反复执行，错误放大 5 倍。skill 没帮上忙，反成了累赘。

skill 质量和编码能力高度相关（r=0.65）。比如 Claude 造的 skill 执行成功率 98%，给谁用都接近 100%。弱模型造的 skill 给自己用会出问题，给别人用更糟。

但真正致命的是嵌套。SkillCraft 对比了 flat（skill 平铺互不依赖）和 hierarchical（skill 嵌套调用）两种组织方式。直觉上嵌套应该更强，因为允许更高层抽象。

实测恰好相反。GPT-5.2 在 flat Skill Mode 下成功率 90%，hierarchical 直接掉到 79%。注意，单个 skill 执行成功率是 95%。零件都好使，装到一起就崩了。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

SkillCraft 层级组合案例：成功 vs 失败的 Skill 嵌套对比（Chen et al., 2026）

**论文还总结了嵌套崩溃的三个机制。第一，错误累积，成功率随嵌套层数指数衰减，每层 95%，三层只剩 85.7%，五层剩 77.4%。第二，隐藏缺陷，底层 skill 创建时测试通过，是因为当时的输入没触发特殊情况，被高层调用碰到新输入才暴露。第三，排查成本，嵌套失败要逐层追溯依赖链，调试成本经常超过直接打平重做。**

比如上面踢的猫的案例。底层 skill「查品种档案」没做空值检查，大多数品种的「性格」字段有值所以没出错。中层 skill 对这个字段做文本拆分，遇到没有性格数据的品种就崩了。每一层单独测都没问题，但组合起来，一个底层的特殊情况像滚雪球一样把整条执行链炸掉。

因此单个 skill 不是瓶颈，组合才是。

SkillCraft 画出了这条线。发现原子级 skill 不是瓶颈，组合才是。而组合问题有两层：弱模型的瓶颈是 skill 质量差（随模型能力提升会自然缓解），强模型的瓶颈是嵌套组合时边界条件的指数级放大（这个不是靠模型变强就能解决的，需要架构层面的创新）。

那学术界怎么攻这个问题？

**04**

**从粗糙原型到可组合模块，封装和组合有了方法论**

回到 SkillCraft 指出的第一个痛点：组合崩溃的根源不是组合本身，而是原子 skill 不够稳定、接口不够确定。

2025 年 4 月，Ohio State University 发表的 SkillWeaver，攻的就是这个问题。SkillWeaver 的过程分三步。

第一步和第二步，是结合了探索和试错的skill发现流程。

第三步是关键，把这些经验蒸馏成标准化的 API。不是文字描述（先点这个按钮再填那个表单），而是一段封装好的、有明确输入输出接口的可执行代码。

蒸馏这一步的设计思路值得多说几句。一般的 skill 存储方式是自然语言描述加上示例，「当遇到 X 情况时，做 Y 操作」。这种方式的问题在于，自然语言是模糊的，不同的 agent 对同一段描述可能理解不同，执行路径也不同。SkillWeaver 把 skill 蒸馏成代码级的 API，接口明确、行为确定，不管谁调用结果都一样。这就是为什么它的 skill 可以跨 agent 迁移。

数据上，SkillWeaver的skill 在 WebArena（标准化的 web agent 测试集）上提升 31.8%，在真实网站上提升 39.8%。

但最有说服力的数字是跨 agent 迁移实验。用一个强 agent（GPT-4 级别）造出来的 API，直接给一个弱 agent（GPT-3.5 级别）用，弱 agent 在 WebArena 上的表现提升了 54.3%。skill 造出来之后，不是只有造它的那个 agent 能用，能力可以下传。一个高手总结出来的操作手册，新手拿着也能用。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

AgentFactory 走了同一条路，但更极端。2026 年 3 月，北京大学的 Zhang Zhang 等人把封装粒度从「一段 API 代码」推到了「一个完整的 Python subagent」。

AgentFactory 的做法和前面所有方法有一个根本性的不同。之前的方法，EXIF、EvoSkill、CASCADE，造出来的 skill 都是文本描述或代码片段。AgentFactory 造出来的不是 skill 片段，而是一个完整的 Python subagent。

当 agent 成功解决了一个任务，AgentFactory 不是把成功经验存成一段反思文字（像此前的 Reflexion 系统那样，让 agent 用自然语言写下「下次该怎么做」），而是把整个解决方案封装成一个可独立执行的 Python 程序，有明确的输入输出接口，有异常处理，有日志记录。

AgentFactory 的 subagent 库会越长越大。早期，agent 遇到新任务需要从头解决，成本高。但随着库的积累，越来越多的新任务可以通过调用或组合已有的 subagent 来完成，后期的平均解决成本持续下降。

这是一个正反馈循环，用得越多，积累越多，成本越低。

SkillWeaver 和 AgentFactory 解决的是同一个问题，让原子 skill 从模糊的文字描述变成确定性的可执行代码，消除每次调用结果不一样的不稳定性。

零件可靠了，就该处理组合了。

目前看，组合能力这件事情，属于模型的一种基本能力，处理的方法，只有通过训练。

University of Wisconsin-Madison 和 Amazon Science 的 Jiongxiao Wang 等人在 2025 年 12 月发表的 SAGE（Skill Augmented GRPO for self-Evolution），把 skill 直接嵌入强化学习的训练循环。它解决的是另一个层面的问题，agent 怎么被激励去主动积累和复用 skill。

SAGE 的核心设计有两个。第一个是「边干边攒」（Sequential Rollout）。agent 在执行一个长任务时，每完成一个阶段就检查自己的操作序列，看有没有值得抽取为 skill 的重复模式。抽取出来的 skill 被加入 library，后续阶段如果遇到类似情况就直接调用，不再从头执行。任务链越长，积累的 skill 越多，后面的阶段就越高效。

第二个是「奖励造技能」（Skill-integrated Reward），在强化学习的奖励函数里显式加入两个信号，造新 skill 有奖励，复用已有 skill 也有奖励。这等于是在训练目标层面告诉 agent，学会积累和复用能力这件事本身就是值得做的，跟任务完成率一样重要。

效果在 AppWorld（一个模拟真实 app 环境的标准测试集）上验证了。目标完成率提升 8.9%，这个数字本身不算惊艳，但两个效率指标更耐看，交互步骤减少 26%，token 消耗减少 59%。skill 积累带来的效果在效率上更明显。做同样的任务花的力气少了很多。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

SAGE 架构图：Skill Library Agent 与 Sequential Rollout + Skill-integrated Reward

2026 年 2 月，University of North Carolina at Chapel Hill 的 Peng Xia 等人发表了 SkillRL，把 skill 的锤炼推到了一个新的层次，即递归进化。

SkillRL 建了一个叫 SkillBank 的分层 skill library。和之前的 skill library 不同，SkillBank 里的 skill 不是平铺的，而是分层级的，低层 skill 可以被组合成高层 skill，高层 skill 又可以被进一步组合。

这个层级结构不是人类设计的，而是在 RL 训练过程中自动涌现的。agent 在解决越来越难的任务时，自然地把之前学会的小 skill 拼成更复杂的大 skill。

SkillRL 的另一个关键设计是自适应检索。agent 不是在每个任务开始前就决定调用哪些 skill，而是在执行过程中根据实时状态动态决定。这更接近人类使用技能的方式。你不会在做一道菜之前先列出所有要用到的技巧，而是切到一半发现肉太硬了，才想起来"对了，我会一个叫腌渍的技巧"。

在 ALFWorld、WebShop 和 7 个搜索增强任务上，SkillRL 超过最强 baseline 14%。复用率数据也印证了这一点。随着训练推进，agent 调用已有 skill 的频率稳步上升，新造 skill 的频率逐渐下降，说明 SkillBank 确实在积累可复用的能力，而不是每次都白手起家。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

SkillRL 框架：从轨迹蒸馏到分层 SkillBank，再到递归进化

SAGE 在训练层面解决积累激励，让 agent 知道攒 skill和完成任务一样重要。SkillRL 把组合推到了递归层级，底层 skill 自动涌现成高层 skill，层级结构不是人设计的，是 RL 训练出来的。

从粗糙原型到可靠模块，再到分层组合，skill 工程化这条路的骨架搭起来了。

**05**

**造出来只是开始，Skill 怎么越用越好**

发现、封装、组合的问题都有人在解了。但还有一个问题被悬着，skill 造出来之后怎么办？一个今天好用的 skill，一个月后可能因为环境变了、API 改了、需求变了而完全失效。

更常见的情况是，skill 不是突然失效，而是慢慢变差。最初跑出 90% 成功率的 skill，因为环境变化，用了两周后掉到 70%，但没人注意到，因为没有持续监控的机制。

其实前面讲 skill 发现时提到的 EvoSkill，已经包含了进化的种子。它不只是发现新 skill，更是一个「执行→失败→诊断→改进」的持续循环，每一轮失败都在定向修复已有的 skill。

但 EvoSkill 的进化是绑定在发现skill的过程里的，skill 造出来之后独立运转时怎么持续变好，需要专门的机制。

学术界在 2025-2026 年密集发表了三篇代表性工作，AutoRefine、ACE、EvolveR。它们的切入点不同，但回答的问题可以收敛成三个。

**第一问，经验从哪来？**

agent 在执行任务时会留下大量轨迹， **但轨迹不等于经验。** 从原始操作记录中提炼出可复用的策略，是进化的起点。

**三个方案走了三条不同的提取路径** 。

AutoRefine（2026 年 1 月）用批量对比提取。它不是每做完一个任务就提一条经验，而是每 10 个任务攒一批，把成功轨迹和失败轨迹放在一起做对比分析（contrastive analysis）。一个专门的 extraction agent 看一批成功记录和一批失败记录，通过反事实推理（counterfactual reasoning）找出「成功时做了什么、失败时差了什么」，然后抽象成可复用的模式。

批量是因为单个任务的成功可能是偶然的，只有跨任务反复出现的策略才值得提取。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

AutoRefine 论文 Figure 1 三阶段框架总览。左侧 Task Execution 展示双形态经验（Skill Pattern + SubAgent Pattern），中间 Pattern Extraction 是对比分析流水线，右侧 Pattern Maintenance 是三维评分+合并/修剪

ACE（2025 年 10 月，Stanford 和 SambaNova）则选择了用实时评估的方法。ACE 的 Generator（干活的 agent 本身）在执行任务时不只是产出结果，还会标注自己用了 playbook 里的哪些条目，并给出「有帮助」或「有误导」的投票。每条经验的 helpful/harmful 计数器在每次使用后被更新。不需要事后分析，信号在使用过程中就自然产生了。

与此同时，Reflector（反思器）检查 Generator 的执行轨迹，提取新策略（bullet），对表现差的旧策略提出修正建议。关键设计是它可以多轮迭代反思（multi-epoch），同一批任务跑多遍，每一遍 playbook 都在变好。

EvolveR（上海人工智能实验室）用的是离线自蒸馏（Offline Self-Distillation）。agent 的策略参数被冻结，它回顾自己之前的执行轨迹，用自己的模型（不依赖外部教师模型）扮演专家角色，从成功轨迹中提取「指导原则」，从失败轨迹中提取「警示原则」。

每条原则由自然语言描述加结构化知识三元组组成。三种方法的对比很清晰。 **AutoRefine 靠事后对比，ACE 靠实时评估，EvolveR 靠自我蒸馏** 。

提取的时机不同（批量 vs 实时 vs 离线），但目标一致，都是从原始轨迹里提炼出可复用的策略。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

ACE 论文 Figure 4 三角色架构。Generator 产出轨迹并投票，Reflector 提炼洞察，Curator 以 Delta 方式增量更新 Playbook

**第二问，经验库怎么管？**

提取只是第一步。经验库会不断膨胀。好的经验需要保留，坏的需要淘汰，冗余的需要合并。如果不做管理，经验库最终会变成一个塞满过时策略的垃圾堆，反而拖累 agent 的表现。

AutoRefine 设计了三维评分追踪每条经验的健康状况。被检索次数（有多少次被翻牌）、被实际采用次数（翻牌后真的用了多少次）、成功次数（用了之后成功了多少次），三项相乘得出综合评分。其中「采纳精度」这一项很妙。

如果一条经验总是被检索但从不被采纳，说明它的描述写得像是相关，但实际上没用，这种虚假相关的经验需要淘汰。维护频率不是固定的，而是指数递增间隔（10、20、40、80 次任务后各做一次清理）。因为早期经验库不稳定需要频繁修剪，后期稳定了就减少干预。embedding 相似度超过 0.85 的同类经验，由一个专门的 merge agent 判断是否值得合并，检查它们是否解决同一个子任务、流程步骤是否兼容、适用场景是否重叠，确认后合并成一条更精炼的版本。

ACE 的管理者叫 Curator（策展器）。它做了三件事。

- 增量合并，新 bullet 不替换旧的，而是以 delta 的方式追加，旧知识不会丢。
- 语义去重，用 embedding 相似度检测冗余 bullet，合并同义项。
- 投票淘汰，被标记为 harmful 次数多的 bullet 被修剪掉。

还有一个关键设计叫 Grow-and-Refine。先让 playbook 自由增长（grow），积累够多之后做一轮整理（refine），去重、修剪、合并。整理可以是「每次追加后立刻做」（proactive），也可以是「等 context window 快满了再做」（lazy）。两种模式的选择取决于任务密度和上下文预算。

EvolveR 的管理逻辑更严格。新蒸馏出来的原则不是直接塞进库里。先做同批次去重。同一道题生成的多个原则，如果语义等价，只保留一个代表。再做两阶段匹配，先用 embedding 相似度检索库中最相似的已有原则，再用 LLM 做语义等价判断。

如果是全新的洞察，加入库中；如果是已有原则的新证据，把新轨迹合并到已有条目下，增强它的支撑力度。

每条原则有一个动态评分 s(p) = (成功次数+1) / (使用次数+2)，分数低于阈值的原则被定期修剪。

三个方案在管理上的差异，反映了对「什么是好经验」这个问题的不同理解。

AutoRefine 用多维量化（被翻牌、被采纳、被验证三重筛选），ACE 让 agent 自己投票（用的人最有发言权），EvolveR 用贝叶斯式的动态评分（每条原则的分数随使用结果持续更新）。

但它们有一个共同的直觉， **进化的过程本身就包含管理** ， **淘汰劣质经验、合并冗余经验、持续校准评分，这些不是进化之外的维护工作，而是进化机制的一部分** 。

**第三问，经验怎么起效？**

这是最关键的分歧。经验提取出来了，库也管好了，它到底以什么方式影响 agent 的行为？改 prompt？改 context？还是改模型本身？

AutoRefine 做了一件其他方案都没做的事。 **它提取出来的经验不只是文字规则，还包括活的子 agent** 。

AutoRefine 定义了两种经验形态。第一种叫 Skill Pattern，简单策略，以自然语言指南或可执行代码片段的形式存在，比如「发票文件应该归到 financial而不是 personal」。

第二种叫 Subagent Pattern，复杂的多步骤流程，直接封装成一个独立的子 agent，有自己的推理能力和记忆。

比如「交通规划」这个子任务太复杂了，一条文本规则写不清楚，于是 AutoRefine 把整个解决方案蒸馏成一个专门的子 agent，主 agent 遇到相关子任务时直接把活委托给它。 **别人提取经验都是文本，AutoRefine 提取的经验可以是一个活的 agent** 。

ACE 的经验以 playbook 的形式注入 agent 的 context。Generator 在执行时参考 playbook 中的条目，playbook 在使用中不断被投票筛选和更新。ACE 的进化逻辑和 AutoRefine 方向相反。AutoRefine 是从轨迹中蒸馏新经验，ACE 是在使用中筛选旧经验。

一个靠提取，一个靠投票。

但 **两者有一个共同的天花板，它们都不改模型本身** 。经验库再好，也是外挂的。模型的推理策略没有因此进化。

EvolveR 跨过了这条线。它的三阶段闭环中，前两步（离线自蒸馏 + 在线交互）和其他方法类似蒸馏经验，在推理时检索经验引导行为。但第三步是 AutoRefine 和 ACE 都没做的。EvolveR 用 GRPO（Group Relative Policy Optimization）对 agent 的策略参数做强化学习更新。

奖励函数有两个分量，结果奖励（答对了给分）和格式奖励（推理过程结构完整、有合理的检索行为也给分）。

关键在于，因为 agent 在线阶段的行为是被经验库引导的，RL 更新学到的不是泛化的推理策略，而是「怎么有效利用自己蒸馏出来的经验」这个能力。

**模型本身在进化，而不只是外挂的经验库在进化** 。 **这是一个真正的闭环** 。 **蒸馏经验→用经验引导行为→从行为结果中学习→更好地蒸馏和利用经验** 。在 HotpotQA、NaturalQuestions 等七个问答基准上，EvolveR 显著超过所有 agentic baseline，而且在从未见过的数据集上也能泛化，说明蒸馏出来的策略原则确实有迁移能力。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

EvolveR 论文 Figure 2 经验生命周期完整流程。左侧 Online/Offline 双阶段闭环，右侧 Experience Base 的检索与维护逻辑

三种方案构成了一个光谱。AutoRefine 用经验创造新的能力载体（活的子 agent），ACE 用经验调节已有行为（playbook），EvolveR 用经验改变模型本身（RL 策略更新）。 **越往右走，进化越深，但工程成本也越高** 。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

EvolveR 论文 Figure 1 四种 Agent 学习范式对比。从「无状态执行」到「自蒸馏+进化」，越往右走 Agent 的自主进化程度越高

这三个方案是学术界的回答。产品界也有人在做，而且做法很不一样。

2026 年 3 月，Anthropic 悄悄把 Skill Creator 升级到了 2.0。旧版只帮你写 SKILL.md，新版变成了一个完整的生命周期管理工具，包含四个模式。

Create 负责创建。通过对话生成 skill 文件，这部分沿用旧版。Eval 负责验证——用子 agent 并行执行，一组带着 skill 跑，一组不带，同样的任务同时跑两份，然后由 Grader（评分器）做断言评分，Comparator（比较器）做盲 A/B 对比，Analyzer（分析器）做统计分析。这样不是人拍脑袋说「感觉变好了」，而是有量化数据。

Improve 负责迭代。基于 Eval 的数据改进 skill。核心机制是 Description Optimization，把评估集分为 60% 训练集和 40% 测试集（防止过拟合），最多跑 5 轮迭代，选出最佳版本。用户还可以在浏览器查看器里逐个审查测试用例的输出，留下定性反馈。

Benchmark 负责度量。定量比较通过率、Token 消耗和执行时间，支持新旧版本快照对比。

四个模式构成了一个闭环。Create→Eval→Improve→Benchmark，然后基于 Benchmark 的结果决定是否再来一轮 Improve。

Skill Creator 2.0 的哲学和学术界的方案有一个本质区别。 **学术界的进化是自动的** ，agent 自己提取经验、自己评估、自己淘汰，人类不介入。

**Skill Creator 2.0 的进化是人机协作的** 。自动化测试提供数据，但最终的判断和反馈由人来做。它不追求完全自主进化，而是让人类开发者能高效地参与进化循环。这可能是更务实的路径。

OpenClaw 的 Self-Improving 模块走了另一条路，打通了从运行时经验到 skill 标准文件的自动转化。

agent 在执行任务时积累的临时经验，通过分层记忆系统逐步固化，先是短期记忆（本次会话内的操作记录），然后是长期记忆（跨会话的模式总结），最终沉淀为 SKILL.md 文件。AutoSkill 组件负责最后一步，把成熟的经验自动写成符合 Anthropic 标准的 skill 文件，包括元数据头（frontmatter）、触发条件、执行步骤，甚至版本号。

每次更新不是覆盖式重写，而是语义级增量修改，只改变需要改的部分，其余保持不变。

Anthropic Skill Creator 2.0 则代表了产品界的务实选择，不追求完全自主进化，而是用 Eval→Improve→Benchmark 的自动化流水线让人类开发者高效地参与进化循环。

skill 生命周期上， **「持续变好」这一环开始闭合了** 。

**06**

**26年的进化，走到了临界点**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

回到开头的矛盾。Anthropic 定义了 skill 怎么流通，这波研究正在解决 skill 怎么来、怎么变好、怎么维护。生命周期上的每一环，发现、封装组合、流通、持续改进，都有了技术原型。

一年前，「agent 能不能自己学新技能」还是一个学术兴趣。今天它是一个工程问题。从学术兴趣变成工程问题，意味着基础的可行性已经不需要被证明了，剩下的是怎么做得更稳、更安全、更可扩展。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Sutton 在 1999 年问了这个问题，Voyager 在 2023 年用 Minecraft 里的 JavaScript 函数给了第一个可信的回答，Anthropic 在 2025 年底让 skill 有了产品级的标准和流通基础设施。

2026 年初这波研究，第一次让「agent 自己造 skill」在真实任务上跑出了可观的数据。

二十六年，从一个理论框架到一个产品级问题。

说到底，这不是一个纯粹关于 AI 的问题。它关乎知识如何积累和传承。人类文明的核心竞争力就是每一代人不需要从零开始，上一代人造了轮子，下一代人直接用，把精力花在造汽车上。

如果 agent 真的学会了这一点，不只是在单次对话中完成任务，而是能把经验沉淀成可复用、可传承、可进化的能力模块，那它就不再只是一个工具。它会成为一种能自我积累知识的基础设施。

我们还没走到那一步。

但方向已经确认了，路上已经有了脚印。

推荐阅读

[一只看不见的手，把机器人推上了春晚](https://mp.weixin.qq.com/s?__biz=Mjc1NjM3MjY2MA==&mid=2691564987&idx=1&sn=f64411c3f532580b7537f44c927a351c&scene=21#wechat_redirect)

[春晚机器人，急着“争”什么？](https://mp.weixin.qq.com/s?__biz=Mjc1NjM3MjY2MA==&mid=2691564964&idx=1&sn=fa965072b8994c835b62ae631560f65e&scene=21#wechat_redirect)

[我们不需要100万台“跳舞机器人”](https://mp.weixin.qq.com/s?__biz=Mjc1NjM3MjY2MA==&mid=2691564155&idx=1&sn=992d25665e3e995cff6d94b679e195c5&scene=21#wechat_redirect)

继续滑动看下一个

腾讯科技

向上滑动看下一个
