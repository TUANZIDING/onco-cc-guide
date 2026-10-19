<p align="center">
  <img src="文档/主图/封面v1.0.svg" width="100%" alt="六组彩色节点由细线互相连接，象征一页一对象、彼此链接的肿瘤学知识图谱">
</p>

<h1 align="center">OnCo肿瘤知识图谱导航 · OnCo Field Guide</h1>

<p align="center">
  <strong>把一张庞大的肿瘤学地图，整理成中文可走的路。</strong><br>
  A Chinese-first map of the open oncology knowledge graph at onco.cc.
</p>

<p align="center">
  面向临床医生、科研人员和医学教育者的 <a href="https://onco.cc/">onco.cc</a> 中文导航：六大栏目、155个子页面、数据接口与引用规范。<br>
  A bilingual guide to onco.cc for clinicians, researchers and educators: sections, pages, API access and attribution.
</p>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="文档/英文说明v1.0.md">English</a>
</p>

<p align="center">
  <a href="https://github.com/TUANZIDING/onco-cc-guide/actions"><img src="https://github.com/TUANZIDING/onco-cc-guide/actions/workflows/%E9%A1%B9%E7%9B%AE%E6%A3%80%E6%9F%A5v1.0.yml/badge.svg" alt="项目检查"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/guide-MIT-637568" alt="本仓库文档MIT许可"></a>
  <a href="https://creativecommons.org/licenses/by-nc/4.0/"><img src="https://img.shields.io/badge/OnCo%20data-CC%20BY--NC%204.0-96704f" alt="OnCo数据CC BY-NC 4.0"></a>
</p>

<p align="center">
  <code>六大栏目中文地图</code> · <code>六条阅读路径</code> · <code>静态JSON接口</code> · <code>引用与许可边界</code>
</p>

<p align="center">
  <a href="#use-cases">使用场景</a> ｜ <a href="#showcase">网站一览</a> ｜ <a href="#quick-start">快速开始</a> ｜ <a href="#capabilities">能力状态</a> ｜ <a href="#contribute">参与共创</a>
</p>

<p align="center"><sub>主图为本仓库原创SVG概念图，不是onco.cc的截图。本仓库是独立的中文导航，与OnCo官方没有隶属关系。</sub></p>

---

<a id="use-cases"></a>

## 从你的问题进入 · Use cases

[OnCo](https://onco.cc/) 是一个公开、带引用、可编辑的肿瘤学知识图谱：癌种、技术、靶点、药物、公司、机构、通路、试验、路线图和研究创意，每个对象一页，先给通俗TL;DR，再给技术层。内容多、栏目深，这里把入口按中文读者的问题重新排好。

| 你想做什么 | 可以怎样开始 |
| --- | --- |
| 查一个癌种的标准治疗、历史和在研管线 | [癌种](https://onco.cc/cancers/) → 例如 [三阴性乳腺癌](https://onco.cc/cancers/tnbc/)；或 [为我查询](https://onco.cc/for-me/) |
| 追踪靶点、药物和试验读出 | [靶点](https://onco.cc/targets/) · [治疗与检测](https://onco.cc/drugs/) · [读出日历](https://onco.cc/calendar/) |
| 了解一类技术从过去到未来的路线 | [路线图](https://onco.cc/roadmaps/)，如 [ADC代际](https://onco.cc/roadmaps/adc-generations/)、[放疗路线](https://onco.cc/roadmaps/radiation-roadmap/) |
| 关注放疗损伤、肌肉与骨的恢复 | [放射治疗前线](https://onco.cc/fronts/radiation/) · [恢复与再生](https://onco.cc/fronts/rejuvenation/) · [恶病质通路](https://onco.cc/pathways/cachexia-biology/) |
| 找研究空白和可做的课题 | [瓶颈](https://onco.cc/bottlenecks/) · [创意](https://onco.cc/ideas/) · [开放问题](https://onco.cc/open-questions/) |
| 用数据做分析或接入AI工具 | [开放API](https://onco.cc/api/) · 本仓库的 [数据接口说明](文档/数据接口v1.0.md) |

<p align="center">
  <img src="文档/主图/栏目结构v1.0.svg" width="100%" alt="OnCo六大栏目结构示意：开始查询、癌种与治疗、新闻与证据、机构与人物、与癌症共处、学习与贡献">
</p>

<sub>结构示意为本仓库原创SVG，数字为栏目地图收录的子页面数（2026-10-19核对）· [完整栏目地图](文档/栏目地图v1.0.md)</sub>

<a id="showcase"></a>

## 网站一览 · Showcase

以下截图来自OnCo官方仓库（2026-09-17截取），图片直接引用其 `docs/screenshots/`，点击进入对应页面。

| 首页 Home | 人体地图 Body map |
| --- | --- |
| [![OnCo首页](https://raw.githubusercontent.com/judegomila/OnCo/main/docs/screenshots/home.png)](https://onco.cc/) | [![按身体部位查找癌种](https://raw.githubusercontent.com/judegomila/OnCo/main/docs/screenshots/body-map.png)](https://onco.cc/body/) |
| [打开首页 →](https://onco.cc/) | [打开人体地图 →](https://onco.cc/body/) |

| 图谱浏览 Graph explorer | 分子图库 Molecule gallery |
| --- | --- |
| [![每个页面都是图谱中的节点](https://raw.githubusercontent.com/judegomila/OnCo/main/docs/screenshots/graph.png)](https://onco.cc/graph/) | [![药物分子三维结构](https://raw.githubusercontent.com/judegomila/OnCo/main/docs/screenshots/molecules.png)](https://onco.cc/molecules/) |
| [打开图谱 →](https://onco.cc/graph/) | [打开分子图库 →](https://onco.cc/molecules/) |

<sub>截图版权归OnCo所有，仅作引用展示；本仓库没有复制或打包这些图片。</sub>

<a id="quick-start"></a>

## 先用起来 · Quick start

**只想浏览：** 直接打开 [onco.cc](https://onco.cc/)，按 [阅读路径](文档/阅读路径v1.0.md) 一站站走，或在 [栏目地图](文档/栏目地图v1.0.md) 里找中文对应的入口。网站提供八种界面语言，可用页眉的 Aa 按钮切换。

**想用数据：** OnCo提供无需密钥的静态JSON接口。本仓库的示例只依赖Python 3标准库：

```sh
git clone https://github.com/TUANZIDING/onco-cc-guide.git
cd onco-cc-guide
python3 示例/检索示例v1.0.py cachexia
```

它会下载 `https://onco.cc/api/v1/search.json`（约9 MB），按关键词列出匹配的对象类型、名称和网页链接，并打印OnCo要求的署名。

[数据接口说明](文档/数据接口v1.0.md) · [English quick start](文档/英文说明v1.0.md#quick-start)

<a id="workflow"></a>

## 怎样读一个对象 · Workflow

**先读TL;DR → 再看技术层与来源 → 沿链接走到相关对象 → 回到原始来源核实**

| 想做的事 | OnCo怎样支持 |
| --- | --- |
| 快速判断一个对象是什么 | 每页开头一两句通俗TL;DR |
| 找到证据出处 | 每条记录至少链接一个一手来源，并标注最近核对日期 |
| 看清彼此关系 | 癌种、药物、靶点、试验、论文互相链接，反向链接自动生成 |
| 按国家理解“已获批” | 页眉选择国家后，“获批”指该国监管机构的结论 |

<a id="capabilities"></a>

## 当前包含什么 · Capability status

| 状态 | 内容 | 实际边界 |
| --- | --- | --- |
| 已整理 | 六大栏目、155个子页面的中英文对照地图 | 栏目会随原站更新；以 onco.cc 当前页面为准 |
| 已核对 | 栏目地图链接、接口路径与示例脚本可访问（2026-10-19） | 只核对可访问性，不核对OnCo内容的医学正确性 |
| 可运行 | `示例/检索示例v1.0.py` 关键词检索 | 需要联网；数据来自OnCo当日构建 |
| 外部入口 | OnCo官方CLI与MCP服务器 | 源码在官方仓库 `packages/`；npm上同名 `onco` 包不是OnCo，需从源码构建 |
| 不包含 | OnCo数据副本、网站源码、医学建议 | 数据请从官方API或Release获取 |

> **使用提醒：** OnCo本身声明内容仍在建设中，可能不完整、过时或有误；不是医学建议。任何临床或科研决策请回到每页链接的原始来源核实。

<details>
<summary><strong>接入AI工具 / MCP and LLM access</strong></summary>

OnCo为语言模型提供了 `https://onco.cc/llms.txt`、逐对象Markdown上下文 `https://onco.cc/api/v1/context/<id>.md`，以及OpenAPI 3.1描述 `https://onco.cc/api/v1/openapi.json`。

MCP服务器与命令行工具需从官方仓库源码构建（`npm run mcp:build`、`npm run cli:build`），步骤见 [数据接口说明](文档/数据接口v1.0.md#mcp)。

</details>

<a id="contribute"></a>

## 一起把它做得更清楚 · Contribute

欢迎补充更准确的中文译名、按临床科室或研究方向整理的阅读路径，以及失效链接报告。OnCo内容本身的错误，请到 [OnCo官方仓库](https://github.com/judegomila/OnCo/issues) 或网站的 [建议修改](https://onco.cc/suggest/) 提交。

| 你想了解什么 | 从这里进入 |
| --- | --- |
| 按问题走的路线 | [阅读路径](文档/阅读路径v1.0.md) |
| 小白也能看懂的图文课 | [团子AI学院 S11：OnCo入门](https://tuanziding.github.io/tuanzi-ai-academy/lessons/onco-guidev1.0.html) |
| 全部栏目与链接 | [栏目地图](文档/栏目地图v1.0.md) |
| API、CLI与MCP | [数据接口说明](文档/数据接口v1.0.md) |
| English overview | [English homepage](文档/英文说明v1.0.md) |
| 来源、许可与署名 | [素材说明](文档/素材说明v1.0.md) |
| 本地检查 | `python3 验证/项目检查v1.0.py` |
| 本仓库的问题或建议 | [GitHub Issues](https://github.com/TUANZIDING/onco-cc-guide/issues) |

---

<p align="center">
  <strong>OnCo肿瘤知识图谱导航 · OnCo Field Guide</strong><br>
  从一个问题出发，沿着链接走到证据。<br>
  <a href="https://github.com/TUANZIDING">TUANZIDING</a> · <a href="LICENSE">MIT</a> · <a href="文档/素材说明v1.0.md">素材来源</a>
</p>

<sub>本仓库的原创文档、SVG与脚本采用MIT许可。OnCo的数据与文字版权归OnCo，按CC BY-NC 4.0供个人与教育非商业使用，须署名“Data from OnCo (onco.cc)”；商业使用须联系OnCo获得授权。OnCo代码为MIT许可。</sub>
