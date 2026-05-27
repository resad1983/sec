---
title: "一个人公司 OPC 必备的 36 个营销 Skill"
source: "https://mp.weixin.qq.com/s/9IJE3aAms1OZP8F--9tjZA"
date: 2026-05-04
status: raw
---

陈宇明 *2026年4月14日 11:44*

这个 marketingskills 开源项目在Github上已经有20k的Star了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/RWodr0jgXg6WSjZ3xanaXfl07qDLNQibDVVlKRqUyejzY04Qtia2M4pkgWkUpFvcLK42VHt4P197U6M34FXvKj26dNOlQzm2bb1b7tCbsPDTk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

https://github.com/coreyhaines31/marketingskills

Corey Haines 创办了 Swipe Files，一个结合个人观点与实战经验的营销资讯集合，这份邮件的订阅人数已达 1.9万人。在邮件里拆解 B2B SaaS 的增长逻辑，分享转化优化的技巧，也探讨创业与生活的平衡。

基于在邮件中积累的信任与影响力，Corey 创办了 Conversion Factory，一家专注于 B2B SaaS 的产品营销机构。2023 年 7 月创立，仅用 两个月 就实现 3.6 万美元 的月经常性收入（MRR）。

他们已经服务了 50+ 初创公司，做出了很不错的成绩：

- SavvyCal：从零到 4.7 万美元 MRR，增长 23 倍。
- Senja：新首页带来 17% 的转化率提升，4 个月内 MRR 从 4 万 涨至 6 万。
- Less Annoying CRM：首页优化带来 20% 的试用转化率提升。

这些成果不是靠烧钱广告，而是靠精准的定位、有说服力的文案、高转化的设计与扎实的策略。

他把这些营销策略开源了，做成了 24 个Skill。

以下是营销技能结构图：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

主要解决的问题包含营销的方方面面，我带着大家从上往下来分析。

第一步：先把产品定位、目标用户、卖点、差异化讲清楚。

第二步：分头干活：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

1. **SEO** **& Content（SEO 与内容）** 搞排名、搞内容结构、AI 写 SEO、页面架构、结构化数据等。
2. **CRO** **（** **转化率优化** **）** 优化页面、注册流程、弹窗、付费墙，让更多人下单 / 试用。
3. **Content & Copy（内容与文案）** 写文案、改文案、冷邮件、邮件序列、社交媒体文案。
4. **Paid & Measurement（付费投放与数据）** 投广告、做素材、AB 测试、看数据。
5. **Growth & Retention（增长与留存）** 做推荐、免费工具、防流失。
6. **Sales &** **GTM** **（销售与上市）** 营收运营、销售赋能、产品发布、定价、竞品分析。
7. **Strategy（策略）** 营销思路、心理学、用户研究。

第三步（重点）：

**这些技能不是孤立的，要互相联动。**

- 文案 ↔ 页面转化优化 ↔ AB 测试
- 营收运营 ↔ 销售支持 ↔ 冷邮件
- SEO 审计 ↔ 结构化数据 ↔ AI SEO
- 用户研究 → 指导文案、CRO、竞品对比

## 如何安装？

一共有6种方式，选一种你适合的方式即可。

方式一：使用 npx skills 直接安装技能：

```
# Install all skillsnpx skills add coreyhaines31/marketingskills# Install specific skillsnpx skills add coreyhaines31/marketingskills --skill page-cro copywriting# List available skillsnpx skills add coreyhaines31/marketingskills --list
```

它会自动安装到您的 `.agents/skills/` 目录（并创建到 `.claude/skills/` 符号链接，以兼容 Claude Code）。

方式二：Claude Code 插件

通过 Claude Code 的内置插件系统安装：

```
# Add the marketplace/plugin marketplace add coreyhaines31/marketingskills# Install all marketing skills/plugin install marketing-skills
```

方式三：克隆和复制

克隆整个代码库并复制 skills 文件夹：

```
git clone https://github.com/coreyhaines31/marketingskills.gitcp -r marketingskills/skills/* .agents/skills/
```

方式四：Git 子模块

添加为子模块以便于更新：

```
git submodule add https://github.com/coreyhaines31/marketingskills.git .agents/marketingskills
```

然后参考 `.agents/marketingskills/skills/` 中的技能。

方式五：分支和定制

1. Fork 此仓库
2. 根据具体需求定制技能
3. 将你的分支克隆到你的项目中

方式六：SkillKit（多智能体）

使用 SkillKit 在多个 AI 代理（Claude Code、Cursor、Copilot 等）中安装技能：

```
# Install all skillsnpx skillkit install coreyhaines31/marketingskills# Install specific skillsnpx skillkit install coreyhaines31/marketingskills --skill page-cro copywriting# List available skillsnpx skillkit install coreyhaines31/marketingskills --list
```

## 如何使用？

安装完成后，只需用 Agent 直接进行营销工作即可：

```
"帮助我优化这个登陆页面的转换"→ Uses page-cro skill"为我的SaaS编写主页文案"→ Uses copywriting skill"为注册用户设置GA4跟踪"→ Uses analytics-tracking skill"创建一个5封邮件的产品介绍"→ Uses email-sequence skill
```

也可以通过技能名称调用：

```
/page-cro/email-sequence/seo-audit
```

技能列表：

| Skill 名称 | 技能名称 | 描述（Description） |
| --- | --- | --- |
| ab-test-setup | AB 测试设置 | 当用户想要规划、设计或实施 A/B 测试或实验，或者构建增长实验项目时使用。 |
| ad-creative | 广告创意 | 当用户想要生成、迭代或扩展广告创意（标题、描述、主要文本或完整广告）时使用。 |
| ai-seo | AI 搜索引擎优化 | 当用户想要优化内容以适应人工智能搜索引擎、获得大语言模型（LLMs）引用或出现在 AI 生成的答案中时使用。 |
| analytics-tracking | 分析跟踪 | 当用户想要设置、改进或审核分析跟踪和衡量指标时使用；也适用于用户提及相关分析跟踪需求的情况。 |
| aso-audit | ASO 审核 | 当用户想要审核或优化 App Store 或 Google Play 商品信息时使用；也适用于用户提及 “ASO” 相关需求的情况。 |
| churn-prevention | 防止客户流失 | 当用户想要降低客户流失率、构建取消流程、设置优惠活动、追回失败的付款等时使用。 |
| cold-email | 冷邮件 | 用于撰写能获得回复的 B2B 陌生开发邮件和后续跟进邮件；适用于用户想要撰写陌生开发邮件的场景。 |
| community-marketing | 社区营销 | 用于构建并利用在线社区来推动产品增长和品牌忠诚度；适用于用户想要创建 / 运营在线社区的场景。 |
| competitor-alternatives | 竞品替代方案分析 | 当用户想要创建竞品对比页面或备选页面以优化 SEO 和销售转化时使用。 |
| content-strategy | 内容策略 | 当用户想要制定内容策略、确定创作方向或规划内容覆盖主题时使用。 |
| copy-editing | 文字编辑 | 当用户想要编辑、审阅、改进现有营销文案，或更新过时内容时使用；也适用于相关文案优化需求场景。 |
| copywriting | 文案撰写 | 当用户想要为首页、着陆页等任意页面编写、重写或改进营销文案时使用。 |
| customer-research | 客户调研 | 当用户想要开展、分析或整合客户调研工作时使用；也适用于用户提及 “客户调研” 相关需求的场景。 |
| email-sequence | 电子邮件序列 | 当用户想要创建或优化电子邮件序列、滴灌式营销活动、自动化邮件流程或生命周期邮件时使用。 |
| form-cro | 表单转化率优化 | 当用户想要优化除注册 / 登录表单外的其他表单（如潜客收集表单、联系表单等）转化率时使用。 |
| free-tool-strategy | 免费工具策略 | 当用户想要规划、评估或搭建用于获客、提升 SEO 价值等营销目的的免费工具时使用。 |
| launch-strategy | 发布策略 | 当用户想要规划产品发布、功能上线或制定发布相关策略时使用；也适用于相关发布规划需求场景。 |
| lead-magnets | 引流工具 | 当用户想要创建、规划或优化用于收集邮箱 / 获取潜客的引流工具时使用；也适用于相关潜客获取需求场景。 |
| marketing-ideas | 营销创意 | 当用户需要为 SaaS 或软件产品寻找营销创意、灵感或策略时使用。 |
| marketing-psychology | 营销心理学 | 当用户希望将心理学原理、心智模型或行为科学应用于市场营销工作时使用。 |
| onboarding-cro | 新用户引导转化率优化 | 当用户希望优化注册后的引导流程、用户激活、首次使用体验或价值实现时长时使用。 |
| page-cro | 页面转化率优化 | 当用户想要优化、改进或提升首页、着陆页等任意营销页面转化率时使用。 |
| paid-ads | 付费广告 | 当用户需要获取 Google Ads、Meta（Facebook/Instagram）、LinkedIn、Twitter/X 等平台付费广告投放相关帮助时使用。 |
| paywall-upgrade-cro | 付费墙升级转化率优化 | 当用户想要创建或优化应用内付费墙、升级页面、追加销售弹窗或功能入口转化率时使用。 |
| popup-cro | 弹窗转化率优化 | 当用户想要创建或优化弹窗、模态框、叠加层、侧滑窗口或横幅广告以提升转化率时使用。 |
| pricing-strategy | 定价策略 | 当用户需要获取定价决策、产品包装或盈利策略方面的帮助时使用；也适用于用户提及相关定价需求的场景。 |
| product-marketing-context | 产品营销背景文档 | 当用户想要创建或更新产品营销背景文档时使用；也适用于用户提及相关文档制作的场景。 |
| programmatic-seo | 程序化 SEO | 当用户想要借助模板和数据大规模创建 SEO 驱动型页面时使用；也适用于用户提及相关 SEO 规模化需求的场景。 |
| referral-program | 推荐计划 | 当用户想要创建、优化或分析推荐计划、联盟计划或口碑营销策略时使用。 |
| revops | 营收运营 | 当用户需要获取营收运营、销售线索生命周期管理或营销到销售交接流程相关帮助时使用。 |
| sales-enablement | 销售赋能 | 当用户想要创建销售资料、演示文稿、单页宣传册、异议处理文档或演示脚本时使用；也适用于相关销售物料制作场景。 |
| schema-markup | 结构化数据标记 | 当用户想要在网站上添加、修复或优化架构标记和结构化数据时使用；也适用于用户提及相关网站数据标记的场景。 |
| seo-audit | SEO 审核 | 当用户想要审核、检查或诊断网站 SEO 问题时使用；也适用于用户提及 “SEO 审核” 相关需求的场景。 |
| signup-flow-cro | 注册流程转化率优化 | 当用户想要优化注册、账号创建或试用激活流程转化率时使用。 |
| site-architecture | 网站架构 | 当用户想要规划、梳理或重构网站的页面层级、导航、URL 结构或内部链接体系时使用。 |
| social-content | 社交内容 | 当用户需要获取 LinkedIn、Twitter/X、Instagram 等平台社交内容的创建、排期或优化相关帮助时使用。 |

相关推荐：

[一个人公司 OPC 必备的 10 个Skill](https://mp.weixin.qq.com/s?__biz=Mzg2MTYzNzM5OA==&mid=2247521315&idx=1&sn=88627c2fc11d8371b476e8ea75663b73&scene=21#wechat_redirect)

继续滑动看下一个

码个蛋

向上滑动看下一个