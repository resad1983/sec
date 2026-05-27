---
title: 一文讀懂GPT-5.5：從今天起，OpenAI「不賣」Token了
source: https://mp.weixin.qq.com/s/uesnoZmSRS5sLaoPo80G0g
date: 2026-04-25
status: raw
---

值得关注的 *2026年4月24日 10:36*

![图片](https://mmbiz.qpic.cn/mmbiz_png/QmK3dYQtkw0OSmEWS0PdqQlLaYLIpSz9xe2Sba0hUxsnTqIzy2q1Ac5laHZfUhrC2cfgvUJ81Tib95qE6K4dMD5H0aHziap7N9xUlLOJAoTgI/640?from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

图片由AI生成

文丨李海伦

编辑丨苏扬

当地时间4月23日，OpenAI正式发布新一代旗舰模型GPT-5.5，官方将其定位为“面向真实工作的全新智能层级”，也是迈向全新计算机工作方式的重要一步。

这次发布核心关注的有两点：

一是效率层面的突破：同等延迟下，模型更大了，速度却没慢。GPT-5.5上下文窗口达到100万Token，但它不是GPT-5.4简单能力升级，而是在效率上做到了同等延迟下的更高智能。

二是GPT-5.5 在训练过程中，参与了自身推理基础设施的优化。简而言之，AI第一次学会帮自己调参数。

在测试复杂命令行工作流的Terminal-Bench 2.0中，GPT-5.5得分82.7%，Claude Opus 4.7的69.4%超过13个百分点；在测试AI独立操作真实电脑的OSWorld-Verified中，成功率78.7%，超越人类基线；在测试跨44种职业知识工作的GDPval中，84.9%的任务达到或超过行业专家水平。

不过，GPT-5.5的价格也明显涨了。

API定价为每百万Token输入5美元、输出30美元，是GPT-5.4（每百万Token输入2.50美元、输出15美元）的两倍，但官方强调GPT-5.5完成相同任务所需Token数量大幅减少，综合成本未必显著上升。GPT-5.5 Pro API定价为每百万Token输入30美元、输出180美元。批量处理和弹性定价享受半价优惠，优先处理为标准价格的2.5倍。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

在ChatGPT中，GPT-5.5以“GPT-5.5 Thinking”形式上线，逐步取代此前版本。

一个新增的小设计是：模型开始思考前会先给出一段思路概述，用户可以在执行过程中随时插话，调整方向。

如果用一句话概括GPT-5.5的意义：过去的模型是能力的集合，GPT-5.5更接近一个会规划、会检查、会持续推进的工作系统。

01  
84.9%的任务，达到专业人士水准

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

图：GPT-5.5与各竞品在Terminal-Bench 2.0、GDPval、OSWorld-Verified等核心基准测试中的对比

先看评估模型在真实职业场景中的表现。OpenAI用了一个叫“GDPval”的基准测试，它要求模型完成一整套职业任务。测试覆盖44种职业场景，包括财务建模、法律分析、数据科学报告、运营规划等等。

结果显示：GPT-5.5在84.9%的任务中达到或超过行业专业人士水平。作为对比，GPT-5.4是83.0%，Claude Opus 4.7是80.3%，Gemini 3.1 Pro 只有 67.3%。

这种差距不止体现在总分上。电子表格建模任务中，GPT-5.5内部测试拿到88.5%；投资银行级别的建模任务同样领先前代。早期测试者的反馈也挺一致：GPT-5.5 Pro 的回答在全面性、结构性和实用性上比 GPT-5.4 Pro 有明显提升，商业、法律、教育和数据科学领域尤其明显。

光看数字容易麻木，OpenAI这次干脆掀开自家工位给你看。

OpenAI表示，公司内部超过85%的员工每周都在用Codex，覆盖财务、传播、市场、产品、数据科学等多个部门。传播团队拿它分析了六个月的演讲邀约数据，搭起了一套自动化分级流程；财务团队用它审阅了24,771份K-1税务表格、合计 71,637 页，比去年提前两周完工；市场拓展团队靠自动化周报生成，每人每周省下5到10小时。

这不是实验室demo，已经变成一种工作日常。

02  
最强自主编程模型

OpenAI称，GPT-5.5目前是其最强的自主编程模型。

在Terminal-Bench 2.0上（测试复杂命令行工作流，需要规划、迭代与工具协调），GPT-5.5得分82.7%，对比GPT-5.4的75.1%，提升幅度接近8个百分点，同时Token消耗更少。在SWE-Bench Pro上（评估真实GitHub问题的一次性解决能力），GPT-5.5得分58.6%。在内部Expert-SWE评测上（长周期编程任务，中位人工完成时间约20小时），GPT-5.5同样超越GPT-5.4。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

配图：Terminal-Bench 2.0和Expert-SWE散点图

Codex在GPT-5.5的驱动下，已经能够从一句话的提示词出发，独立完成从代码生成、功能测试到视觉调试的完整开发流程。

OpenAI官方展示的演示案例显示，太空任务应用基于NASA真实轨道数据构建，支持3D交互操控，轨道力学模拟达到真实物理精度；地震追踪器接入实时数据源并完成可视化，说明模型已具备调用外部API、处理动态数据并实时渲染的完整能力。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E) ![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

对于使用反馈方面。Every创始人兼 CEO Dan Shipper 讲了一段经历：他之前遇到过一个上线后的 bug，自己调了好几天没搞定，最后只能请公司最强的工程师出手，重写了一部分系统。GPT-5.5 出来后，他做了个实验——把模型放回 bug 还没修的那个状态，看它能不能自己得出和工程师一样的方案。GPT-5.4 做不到，GPT-5.5 做到了。他评价："这是我用过的第一个真正具备概念清晰度的编程模型"。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一位英伟达工程师的评价更直白："失去GPT-5.5的访问权限，感觉就像截肢"。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Cursor联合创始人兼CEO Michael Truell对此的补充是：GPT-5.5比GPT-5.4更聪明、更坚韧，在复杂长时任务中能坚持更久而不提前停下——而这恰恰是工程工作最需要的。

03  
知识工作：AI第一次真正能“用”电脑

在OSWorld-Verified测试中（测试模型能否独立操作真实计算机环境），GPT-5.5成功率78.7%，高于GPT-5.4的75.0%，也优于Claude Opus 4.7的78.0%。

这不是截图分析，而是真正的屏幕操控：看到界面、点击、输入、在多个工具之间切换，直到任务完成。GPT-5.5让人第一次感受到，AI可以真正与你共同使用同一台电脑。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

财务建模演示视频

在电信客服工作流测试Tau2-bench上，GPT-5.5在无提示词调优情况下准确率达98.0%，GPT-5.4仅为92.8%。

这意味着模型对任务意图的理解足够深入，不需要精心设计提示词就能处理复杂的多步骤对话流程。

在工具搜索能力上，GPT-5.5在BrowseComp测试中得分84.4%，GPT-5.5 Pro更达90.1%，意味着在需要跨多个信息来源综合推理的研究类任务中，模型表现出了相当强的持续检索和信息整合能力。

04  
科学研究：协助发现数学新证明

在这次发布中，GPT-5.5在科研领域的表现，可能是最出人意料的一部分。

过去我们谈AI做科研，更多是“辅助工具”，用来查文献、写代码、整理数据。但这一次，它的角色明显前移，开始参与更核心的环节：复杂推理，甚至是发现本身。

在GeneBench上（遗传学和定量生物学多阶段数据分析评测），GPT-5.5得分25.0%，GPT-5.4为19.0%。这些任务通常对应科学专家数天的工作量，模型需要在几乎没有监督的情况下推理可能存在错误的数据、应对隐藏的混杂因素，并正确实施现代统计方法。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

从图表曲线可以看出，随着输出Token数量的增加，GPT-5.5的得分提升幅度始终领先于GPT-5.4，且在约15,000Token处出现明显拉开——这意味着面对需要深度推理的长任务，GPT-5.5的优势会随任务复杂度的提升而进一步放大。

在BixBench（真实世界生物信息学和数据分析基准测试）上，GPT-5.5以80.5%的得分领先于GPT-5.4的74.0%，在已发布得分的模型中位居前列。

真正引发关注的是一个具体案例：配备自定义工具框架的GPT-5.5内部版本，协助发现了一项关于拉姆齐数的新数学证明，并在形式化证明工具Lean中得到验证。拉姆齐数是组合数学的核心研究对象，该领域的成果十分罕见，技术难度极高。这不是AI提供代码或解释，而是真正贡献了一个数学论证。

实际应用层面同样有说服力。Jackson实验室免疫学教授Derya Unutmaz用GPT-5.5 Pro分析了一个包含62个样本、近28,000个基因的基因表达数据集，生成详细研究报告，提炼出关键发现和研究问题——他表示这项工作通常需要团队耗费数月。

波兹南亚当·密茨凯维奇大学数学系助理教授Bartosz Naskręcki，仅凭一条提示词，用Codex中的GPT-5.5在11分钟内构建出一款代数几何应用，可视化两个二次曲面的交线并将所得曲线转化为魏尔斯特拉斯模型。右侧实时显示的方程系数可直接用于后续数学研究，从提示词到可运行的研究工具，全程由模型独立完成。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

配图：Bartosz Naskręcki教授构建的代数几何应用截图——二次曲面相交可视化与魏尔斯特拉斯方程实时计算界面

Axiom Bio联合创始人Brandon White的评价更为直接：“如果OpenAI保持这一势头，年底前药物发现的基础将会发生改变。”

05  
推理效率：AI第一次帮自己优化了基础设施

这次发布有一个容易被忽视的细节，但它可能是技术层面最值得关注的进展。

GPT-5.5是一个更大、更强的模型，但它在实际服务中的单Token延迟与GPT-5.4持平。要在更强的能力下维持同等延迟，OpenAI将推理系统作为整体重新设计——而Codex和GPT-5.5本身在这一过程中直接参与了优化。

从Artificial Analysis智能指数图可以直观看出这一点：横轴是输出Token总量（对数刻度），纵轴是综合智能得分。GPT-5.5的曲线不仅在得分上全面领先GPT-5.4、Claude Opus 4.7和Gemini 3.1 Pro Preview，更关键的是，它在Token消耗较少的区间就已经达到其他模型需要消耗更多Token才能达到的得分水平——更强的能力，更低的成本，这正是“效率提升”的直观体现。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

配图：Artificial Analysis智能指数折线图

具体来说，团队面临的问题是负载均衡：此前将请求拆分为固定数量的块以均衡GPU工作，但静态分块对所有流量形态并非最优。Codex分析了数周的生产流量数据，编写了自定义启发式算法，将Token生成速度提升超过20%。

GPT-5.5与NVIDIA GB200和GB300 NVL72系统协同设计、协同训练和协同部署。换句话说，这一代模型参与优化了服务自身的推理架构——这不是比喻，是字面意义上的“AI改进了跑自己的系统”。

06  
网络安全：能力提升，管控同步收紧

GPT-5.5在网络安全能力上有明确提升。在CyberGym测试中，GPT-5.5得分81.8%，GPT-5.4为79.0%，Claude Opus 4.7为73.1%。在内部“夺旗”（CTF）挑战任务中，GPT-5.5得分88.1%，GPT-5.4为83.7%。

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

配图：CyberGym柱状图与CTF挑战任务散点图

OpenAI将GPT-5.5的网络安全和生物/化学能力评级定为应急准备框架下的“高”级，尚未达到“关键”级，但相比前代有明确提升。与此同时也坦承，新部署的更严格风险分类器“部分用户最初可能会觉得有些不便”，并将持续调整。

为平衡防御需求与访问限制，OpenAI推出了“网络安全可信访问”计划：符合条件的安全研究人员和关键基础设施防御者可申请更宽松的访问权限，以更少摩擦使用高级网络安全能力。

这背后的逻辑是：能力扩散是不可逆的趋势，比限制扩散更现实的路径，是让防御者比攻击者先用上最强的工具。

**特约编译无忌对本文亦有贡献**

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

推荐阅读

[一文读懂ChatGPT Images 2.0：图像AI的下一个阶段](https://mp.weixin.qq.com/s?__biz=Mjc1NjM3MjY2MA==&mid=2691567234&idx=1&sn=acfbc48078534e745f70fdc262f6fd9c&scene=21#wechat_redirect)

[腾讯混元大模型重建第一步，用Hy3 preview验证自己的AI节奏](https://mp.weixin.qq.com/s?__biz=Mjc1NjM3MjY2MA==&mid=2691567347&idx=1&sn=d182af313c5544c7dcefc57faa66b215&scene=21#wechat_redirect)

继续滑动看下一个

腾讯科技

向上滑动看下一个