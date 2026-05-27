---
title: "一篇论文引发存储芯片股暴跌，Google 的「DeepSeek 时刻」来了？"
source: "https://mp.weixin.qq.com/s/b6q_nV6hhdmrvrUHr95sKw"
date: 2026-04-08
status: raw
---

原创 发现明日产品的 *2026年3月26日 12:22*

看过 HBO 神剧《硅谷》（Silicon Valley）的朋友，想必都对那个名为 Pied Piper（魔笛手）的虚构公司念念不忘。

在剧中，男主角 Richard Hendricks 发明了一种「中间压缩算法」，能以极高的压缩率无损处理文件，甚至因此改写了整个互联网的规则。

当时我们都以为这只是编剧的脑洞。直到 Google Research 正式发布了名为 TurboQuant 的 AI 压缩算法。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/dCG7OC48IfK0wPEjkOwfYvKSJqKOQgC3w9OCTyibe1B27ysovsSt2ibHyHibKWJQQeQLlkicGGBbRCKxk5hl62vlCdROFa7qLeMxaVmmFbiaK91s/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

这原本是一条枯燥的技术新闻，却在社交网络上引发了病毒式传播，不到 24 小时，就收获了 1280 万次浏览。原因无他，这项技术的设定简直就是 Pied Piper 的翻版：

在不损失模型性能的前提下，将 AI 的「工作记忆」压缩至少 6 倍。

市场的反应也极为真实，美股存储芯片板块盘中遭遇抛售，美光科技、闪迪等头部企业股价齐齐收跌。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

这不禁让人好奇，一项纯软件层面的算法创新，为什么会让卖硬件的先慌了神，而 Google 到底向当前的 AI 牌桌上扔了一张怎样的底牌？

困在「记忆黑洞」里的大模型

抛开网络热梗，TurboQuant 的出现其实不仅是为了好玩，更是为了解决一个让整个 AI 行业头疼已久的真实瓶颈。

众所周知，现在的 AI 模型越来越大，对显存的胃口也像无底洞一样。尤其是在推理阶段（也就是你和 AI 聊天的时候），AI 需要记住上下文信息，这部分数据被称为 KV Cache（键值缓存）。

![The KV Cache: Memory Usage in Transformers](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

The KV Cache: Memory Usage in Transformers

每处理一个词，模型都要把它转成一个高维向量存进 GPU 显存。对话越长，这份「数字备忘录」膨胀越快，很快就把 GPU 显存塞满。这就是为什么你的 AI 助手聊久了会「变笨」或者直接报错，脑容量不够了。

更棘手的是，传统的压缩方法一直面临一个两难困境：压缩数据时，需要额外存储「量化常数」来告诉模型怎么解压。这些元数据听起来很小，加起来却能把压缩带来的收益全部抵消掉。

Google 的 TurboQuant 的诞生正是基于此。

研究人员设计了一套两阶段的数学解法。第一阶段叫 PolarQuant，把数据向量从传统的直角坐标系转换成极坐标系，拆分成「半径」（表示大小）和「角度」（表示方向）。

这个几何变换的妙处在于：转换后角度的分布变得高度可预测，模型不再需要为每个数据块单独存储昂贵的归一化常数，直接映射到固定的圆形网格上就行了，开销为零。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

第二阶段叫 QJL（Quantized Johnson-Lindenstrauss 变换），充当数学层面的纠错器。它把压缩后残留的误差投影到低维空间，再把每个误差值压缩成一个符号位（+1 或 -1）。

这个设计保证了 AI 在计算「注意力分数」时，压缩版本的结果与高精度原版在统计意义上完全一致。所谓注意力分数，就是模型判断上下文里哪些词最重要的关键步骤。

如果说以前 AI 记笔记是「逐字逐句抄写」，那么 TurboQuant 就像发明了一套「极简速记符号」：该记的一个不漏，占的空间却少了六倍。

这套方法还有一个对企业来说格外友好的特性：无需重新训练模型。你现有的开源模型，或者自己微调过的模型，直接套上 TurboQuant 就能跑，不用额外的数据集，也不用重新跑一遍训练流程。

光说不练假把式，在「大海捞针」基准测试里，让 AI 从 10 万个词里找出一句藏好的话，TurboQuant 在 Llama-3.1-8B 和 Mistral-7B 上跑出了满分召回率，同时把 KV Cache 的显存占用压缩了至少 6 倍。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在 LongBench 综合评测套件（涵盖问答、代码生成、长文摘要）上，TurboQuant 全面追平甚至超过了此前的最强基线方法 KIVI。

最硬核的数字来自英伟达 H100 GPU 的实测：4 位精度的 TurboQuant 在计算注意力逻辑上的速度，比未压缩的 32 位方案快了整整 8 倍。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Google 的「DeepSeek 时刻」？

论文发布后的 24 小时内，社区已经开始动手验证。

Apple Silicon MLX 框架的知名开发者 @Prince\_Canuma 把算法移植到了 Apple Silicon 的 MLX 框架，测试 Qwen3.5-35B 模型，上下文长度从 8500 到 64000 token 全覆盖，每个量化等级都跑出了 100% 的精确匹配。

他还发现，2.5 位的 TurboQuant 能把 KV Cache 压缩近 5 倍，准确率零损失。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对于 TurboQuant 的发布，Cloudflare CEO Matthew Prince 甚至将其称为 Google 的「DeepSeek 时刻」。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

把时间拨回一年前，DeepSeek 以极低的成本训练出了性能惊人的模型，彻底打破了硅谷大厂对高成本才能训练出高性能 AI 的迷信。那次冲击也让整个行业意识到：光有大模型不够，还得跑得起、跑得快。

TurboQuant 也是这种背景下的产物。如果这项技术能从实验室走向大规模应用，它将带来肉眼可见的商业价值。

同样一张 H100，推理成本理论上可以直接打折超过 50%；端侧部署的门槛也会大幅降低，以前需要 32 位精度才能跑的大模型，放在 Mac Mini 或者本地服务器上也能运行，还不会有质量损耗。

![TIs the Mac Mini M4 Cluster the Ultimate Machine for Running Large AI  Models? | by Faizan Saghir | Medium](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

TIs the Mac Mini M4 Cluster the Ultimate Machine for Running Large AI Models? | by Faizan Saghir | Medium

市场的反应，已经很说明问题了。TurboQuant 发布当天，美股存储芯片板块盘中遭遇明显抛售。闪迪、美光科技等头部企业股价显著收跌，存储芯片与硬件供应链相关指数单日跌幅超过 2%。

究其原因，如果 AI 巨头能用一套纯软件算法把显存需求砍掉六分之五，那些押注 AI 会持续疯狂消耗高带宽显存的多头，就得重新盘算自己的仓位了。

而这种防御性反应背后，也表明，过去两年支撑存储股估值的核心逻辑之一，是 AI 对显存的需求只会越来越大。TurboQuant 第一次在技术层面正式动摇了这个假设。

当然，虽然听起来很美好，还是要泼一盆冷水。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一方面，历史上每次效率提升，往往反而带动了总需求增长，经济学里叫「杰文斯悖论」。AI 跑得更便宜，可能意味着更多人更频繁地用它，最终消耗的算力反而更多。所以这场「显存危机」到底会不会因此化解，还真不好说。

另一方面，TurboQuant 目前仍处于实验室阶段，根据最新消息，Google 计划在下个月的 ICLR 2026 大会上正式展示这项技术，届时还将同步亮相另一场顶会 AISTATS 2026。

但从论文到大规模生产部署，中间隔着工程适配、不同架构的兼容性测试、真实场景的性能验证，每一关都不轻松。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

论文地址：https://arxiv.org/abs/2504.19874

有网友直接开炮，这篇论文的底层研究其实早在去年四月就已公开，根本谈不上横空出世，眼下的舆论热潮，多少有点追着旧闻起哄的意思。

在他看来，如果存储股因为一篇算法论文而大跌，恰恰暴露了市场里有多少人根本没搞清楚这件事的边界，并把这波反应比作「丰田出了新混动引擎，石油就该崩盘」。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

更重要的是，TurboQuant 解决的只是推理（Inference）阶段的显存瓶颈，训练阶段的显存消耗依然是另一座大山。想从头训练一个主流量级的大模型，需要的算力资源依然是天文数字。

在《硅谷》里，Pied Piper 的压缩算法最终改变了整个互联网。而在现实中，TurboQuant 的野心没那么大，目标只是让 AI 在有限的物理空间里记得更多、算得更快、跑得更便宜。

现实终究不是好莱坞剧本，不必彻底改变互联网，能和 AI 聊得更长、不再半途报错，已经是很多人想要的了。

附上 TurboQuant 官方技术博客：

https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/

  
![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

我们正在招募伙伴

**📮 简历投递邮箱** hr@ifanr.com

**✉️ 邮件标题** 「姓名+岗位名称」（请随简历附上项目/作品或相关链接）

[更多岗位信息请点击这里🔗](https://mp.weixin.qq.com/s?__biz=MjgzMTAwODI0MA==&mid=2652396877&idx=2&sn=dfef25453a6bf0dca147b0adca3deaf7&scene=21#wechat_redirect)

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

继续滑动看下一个

APPSO

向上滑动看下一个
