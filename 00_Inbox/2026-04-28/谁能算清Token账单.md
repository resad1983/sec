---
title: "谁能算清Token账单"
source: "值得关注的"
date: 2026-04-28
status: raw
---

---
title: "谁能算清“Token账单”？"
source: "https://mp.weixin.qq.com/s/Cl2kGNiM4Q5nbes1utOH-g"
author:
  - "[[值得关注的]]"
published:
created: 2026-04-16
description: "黄仁勋讲了Token的故事，但也难算清Token背后的账"
tags:
  - "clippings"
---
值得关注的 *2026年4月16日 08:15*

编者按：本文为《Token经济学》系列之一。算力货币Token正在重塑AI时代的价值坐标，但它的单价透明，价值却是黑盒，AI行业仍在寻找一个真正能为结果标价的锚。

文｜晓静

编辑｜徐青阳

在刚刚过去的3月，黄仁勋站在GTC 2026的舞台上，描绘了一个由Token驱动的新工业时代：AI factory持续产出Token，agentic AI则把推理需求推向新的峰值。听上去，Token像是AI时代最标准、最统一、最可量化的经济单位。

打开大模型的官方定价页，我们也能看到一种近乎工业标准的整齐划一：每百万Token明码标价，输入、输出、缓存、批量处理各有刻度。这种格式上的高度趋同，常让人产生一种错觉：AI行业已进入了规则成熟、产品标准化的竞争阶段，Token就是这个时代最重要的度量衡。

但事实恰恰相反。

2026年4月，OpenAI旗舰模型GPT-5.4的输入价格是每百万Token 2.5美元，输出15美元，相对Anthropic旗舰模型Claude Opus 4.6是5美元和25美元。仅看标价，Anthropic贵了一倍。但对任何一位企业技术负责人来说，单纯比对这两个数字毫无意义，两家公司在上下文窗口策略、工具调用计费逻辑以及缓存折扣深度上的差异，足以抹平甚至倒置标价上的倍数关系。

Token的价格确实是透明的，但Token价格背后的“价值”是个黑盒。获得同等的价值，究竟要支付多少价格，现在还很难定义清楚。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图片由AI生成

## 01

## 同样的Token，不一样的智力

Token的定价本身并不神秘。

一位长期使用API（应用程序编程接口）的开发者表示，“Token的价格不是黑盒，厂商也做不了假。输入输出Token数量都是可以估算的，即使tokenizer不公开，也差不多能算出来。”

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图：GPT5.4和Opus4.6的价格对比

经济学上，这类似于一种典型的“同质化计量单位”，就像千瓦时之于电力、GB之于存储，Token提供了一个标准化的消耗度量，让买卖双方可以在同一个尺度上交易。

但问题在于：Token不只是传统的计量单位，它计量的是智能，承诺了一种价值。用户购买Token，是为了获得模型的“智能”，真正能够成为生产力。比如写出能跑的代码、完成一次客服对话、做出一份数据分析。而这种“每个Token能换来多少能力”的兑换率，才是真正的黑盒。

还有开发者反馈，“有时候，比如新模型发布之前，模型厂商会降智、降思考强度。这个是黑盒，但用户能感知到。”

2026年4月初，AMD AI战略总监Stella Laurenzo在GitHub上发布了一份基于6852个Claude Code会话的分析。数据显示，从2026年2月下旬开始，Claude Opus 4.6的推理深度大幅下降——“reads-per-edit”（每次代码编辑前的文件阅读次数）从6.6骤降至2.0，降幅约67%。换句话说，模型不再仔细阅读代码就开始动手修改了。

Laurenzo的结论是：“当思考变得肤浅，模型倾向于采取成本最低的行动。不经阅读直接修改、未完成就停止、对错误推卸责任、选择最简单而非最正确的解法。”

4月14日，媒体在公开报道中还原了事情的另一面。Claude Code的创建者Boris Cherny回应称，2月9日起Opus 4.6默认启用了“adaptive thinking”（自适应思考），3月3日进一步将默认effort level从高调整为中等（85%），Anthropic认为这是“对多数用户在智能、延迟和成本之间的最佳平衡”。用户可以手动输入/effort high来恢复完整推理。

问题在于：这些改变没有在任何显著位置通知用户。大量开发者是在代码质量明显下降之后，才开始怀疑“模型是不是变笨了”。但这很难被证明，一句“测试环境不一致”就能够完美回应质疑，“大模型的概率性让一些事情很难实锤。”

这就是Token经济学中最重要、也最难定价的变量：同样消耗100万个Token，你获得的推理质量可能完全不同。在高峰期和低峰期不同，在默认配置和手动调高effort之后不同，在订阅用户接近配额上限时和配额充裕时也可能不同。Token的数量和价格是透明的，但Token里装了多少“智力”，用户无从得知，也无法事先约定。

经济学上有一个概念叫“质量调整”（hedonic adjustment），当一件商品的质量发生变化时，即使名义价格不变，真实价格也已经变了。

Token正面临这样的困境：标价没变，数量没变，但“含金量”可能悄悄缩水。这比价格上涨更隐蔽，也更难以追责。

## 02

## 牵动价格的“缓存命中率”

除了“智力含量”波动这个黑盒，还有一层更隐蔽的成本结构在价格表之下。

2026年2月，Claude Code的一次更新导致第三方平台的缓存命中率大幅下降。随即有人质疑Anthropic是否故意破坏第三方模型的缓存。

一位工程师用AI工具下载了Claude Code v2.1.0到v2.1.41共11个版本的源码，逐一分析。结论是：代码中不存在针对第三方模型的蓄意破坏逻辑。但从v2.1.23开始，Claude Code引入了Claude专属的分块缓存机制，“跨session全局共享、1小时有效期”这些优化改变了system prompt的结构，第三方模型的API无法识别这些标记，只能依赖最基础的前缀匹配，而前缀恰恰因为版本号、构建时间、A/B测试变量的持续变化而高度不稳定。

用通俗的语言总结，Anthropic没有主动“投毒”，但它在优化自家模型效率的过程中，作为副作用，破坏了第三方模型原本依赖的缓存条件。

这件事虽然不是蓄意而为，但是暴露了一件事，缓存命中率会决定你为Token付多少钱。一位开发者对Claude Code一周使用数据的追踪显示，正常情况下91%的Token来自缓存命中，缓存命中价格只有标准输入价格的十分之一。如果缓存全部失效，Input成本会暴涨到原来的5.7倍。

Claude Code的创建者Boris Cherny自己也承认：“使用1M上下文窗口时，cache miss的代价非常高。如果你离开电脑超过一小时再继续旧session，通常完全命中不了缓存。”

还有更值得注意的细节。社区中流传着一项分析称，Claude Code在检测到用户进入“Extra Usage”（超额付费）模式后，会静默地将缓存时长从1小时降级为5分钟。也就是说，你只要停下来超过5分钟就会触发完整的上下文重建，费用直接从超额余额里扣。

根据媒体报道，4月有Pro用户反映自己在5小时内只能在ClaudeCode发两条提示词。一位用户直接说：“在这些缓存bug修复之前，任何关于5分钟还是1小时TTL的讨论都是空谈，因为数字完全是错的。”

缓存命中率的示例可以看出，即使获得同样的结果（价值），付出的价格也会产生巨大的波动。

## 03

## 300倍降价背后的预算泥潭

根据行业数据，Token单价在三年内大约跌了300倍，但企业的AI支出反而更难控制了。原因很简单：单价的降幅，赶不上用量的暴涨。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图：三年间，LLM Token单价下跌约300倍——但单价的崩塌并没有让企业的AI支出变得更可预测。（来源：TokenCost）

Agent类应用让AI自主执行复杂长链路任务，单次消耗可能是传统对话的几十倍。亚太区电商技术公司Branch8的6人团队，启用Claude Code的第一个月花了2400美元，经过8周密集优化，包括设定每日Token配额、限制思考模式预算、非关键任务从Opus切到Sonnet，才勉强降到680美元。Token支出管理本身已经变成了一项需要专门技能的工作。

在Nutanix 2026年的.NEXT大会上，一位CIO分享了更极端的案例：一名开发者产生了10万美元的意外Token账单，他不得不向毫无准备的CFO解释，用他自己的话说，那是一场”极其狼狈的会议“。另一位参会者说已经有公司在给员工发每日Token额度，“就像配给制”。

Mavvrik与Benchmarkit对372家企业的调查印证了这种普遍性：84%的企业报告AI成本对毛利率的侵蚀超出预期，仅15%能将预算误差控制在10%以内。

经济学上，这是“单位度量失灵”的典型表现。当一个计量单位既不能准确反映成本，比如缓存、降智等隐性变量，也不能准确反映价值，同一Token在不同场景下产出天差地别，它就失去了度量衡的基本功能，无法帮助市场形成共识、降低交易摩擦。

换个角度看，Token消耗量的暴涨对模型公司来说仍然是核心叙事。

但Token增长同时也是一个成本故事。OpenAI 2025年的推理成本达84亿美元，2026年预计升至141亿美元，全年现金消耗约170亿美元。它已签下超过5000亿美元的云基础设施合同。Anthropic累计融资超640亿美元。两家公司目前都未盈利。

OpenAI 2026年4月以8520亿美元估值融了1220亿美元，Anthropic 2月以3800亿美元估值融了300亿美元。投资者希望未来能看到，每个Token消耗的算力成本会持续下降，从而让“卖Token”最终变成一门赚钱的生意。

但早期亚马逊卖的是标准化的商品和云服务，单位经济模型相对稳定。AI公司卖的是Token，一个看似标准化、实际高度异质的东西，而且异质的部分（智力含量、缓存效率、任务适配度）恰恰是影响成本和价值的核心变量。“规模效应”能不能如期出现，比电商和云计算时代更不确定。

## 04

## 行业在寻找定价的“锚”

回到核心问题：谁能算清Token的价值？

短期内，没有人能。Token的价格是透明的，但它兑换的智力质量是波动的，它背后的真实成本是被缓存、框架设计和算力效率层层折叠的，它产出的业务价值更是因场景而异。

一个计量单位同时承受这么多维度的不确定性，本身就说明它还不能成为AI时代的度量衡。

Token也没有成为一种可以被标准定价的商品。它是AI行业尚未找到价值锚之前，所有人不得不使用的临时记账单位。

目前行业对Token的定价，本质上还是在对“算力的使用权”定价，买的是让模型替你“想”一次的机会。至于它想得多深、想得多好、最终有没有解决你的问题，不在这个价格的承诺范围内。

这种定价方式的合理性，目前没有任何一方能独立评判。厂商无法替用户衡量产出的业务价值，用户无法穿透模型的推理过程判断每个Token是否“物有所值”，投资者看到的是消耗量增长曲线，但没看到每一个Token的价值转化率。

最终能算清Token价值的，也许是需要发现客户愿意为之付费的“结果单位”，能够定义智能的真正生产力，并在内部把Token成本和算力成本的换算关系管理到可预测。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

推荐阅读

[我，怕断电断网，更怕断Token](https://mp.weixin.qq.com/s?__biz=Mjc1NjM3MjY2MA==&mid=2691566685&idx=1&sn=c8209766ba19ec5b42a4a9559402b47d&scene=21#wechat_redirect)

[AI代码的“屎山危机”才刚刚开始](https://mp.weixin.qq.com/s?__biz=Mjc1NjM3MjY2MA==&mid=2691566538&idx=1&sn=dac9297157536671c0a11b8c6c9eb4a4&scene=21#wechat_redirect)

继续滑动看下一个

腾讯科技

向上滑动看下一个
