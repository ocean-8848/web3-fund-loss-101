# Slides 制作代理简报

你负责把手册的一章或几章做成 3b1b 风格的动画 slides。只写你分到的章节目录 `src/slides/<章 id>/`，不改其他文件（播放器、tools/、src/handbook/、dist/、别的章节目录都不要动）。

## 目标

读者翻 slides 几分钟过完一章的知识点。一页 = 讲稿里的一句话（显示在画面下方，没有配音）。播放器翻页时直接显示这一句的句末画面，不播过渡动画；所以每页的句末画面本身要完整、好读，动画时间轴只用来决定元素在哪一句出现、在哪一句消失。

## 先读

1. `README.md` 的「Slides」一节。
2. 参考实现 `src/slides/o00/`：`narration.json`，以及 `compositions/mtgox.html`、`compositions/dao.html`（写法、坐标、助手函数照它们来）。
3. 你的章节源稿：
   - O00–O03：`src/handbook/data/core.js`；
   - G01–G10 是数据驱动的：`src/handbook/data/groups.js` 里 `const G=[...]` 中该章的对象（intro、mermaid、readpts、why、examples、defense 等字段），渲染逻辑见同文件的 `renderG`；该章的事件行来自 `src/handbook/data/events.js`（`rowsOf(g)` 怎么筛选就怎么用）；
   - D01–D05：`src/handbook/data/defense.js`；A01、A02：`src/handbook/data/groups.js` 中对应的 `H.docs.push({id:"a0x"...})` 及其用到的数据。
   - 要统计数字（件数、金额合计、年份分布）就用 node 读数据文件现算，不要估。

## 第 3 部分（D01–D05）的补充要求

- 章节 id（也就是 slides 目录名）是语义名：D01 `defense`、D02 `hardening`、D03 `secops`、D04 `response`、D05 `recovery`。目录写成 `src/slides/<id>/`，`narration.json` 的 `"id"` 和 `tools/snap_slides.py` 的参数都用这个 id。
- 这一部分讲“怎么做”，画面要把做法画出来：防线排在攻击链上、签名请求经过策略层被拒、余额上限截断损失、告警到停签的时间线、事件指挥与各角色的分工、冻结请求在各方之间流转、时间窗口逐个关闭。少用表格截图式的画面。
- 每条做法尽量讲清“做什么 → 怎样验证”；数字（如“告警到全链停签 &lt; 5 分钟”）照正文写。
- 外部框架（NIST、CCSS、SEAL 等）只按正文里的说法引用，不额外补充。
- 旧 D01 防御矩阵、D02 应急止损与追回的场景在 `src/slides/_retired/` 下，可以复用画面写法（矩阵点阵、止损分层、洗钱路径），但讲稿与事实以新正文为准。

## 产出（每章）

```
src/slides/<id>/STORYBOARD.md      知识点清单（从源稿逐条列出）→ 每个场景覆盖哪些点；没上 slides 的点写明理由
src/slides/<id>/narration.json     {"id","title","scenes":[{"id","title","lines":[...]}]}
src/slides/<id>/compositions/<场景 id>.html
```

- 每章 4–7 个场景，合计 18–40 页（句）。A01 事件库、A02 术语表做 3–5 页的导览（分布、怎么查、高频术语），不要逐条搬。
- 每句 ≤ 40 字，一句一个点；口语、短句。讲稿不照念屏幕文字；屏幕文字短。
- 场景 `title` 是给目录用的短标题（≤ 16 字）。最后一个场景通常是本章要点回收或防御落点。
- 时长由脚本按字数算：`read_time = clamp(1.6 + 0.17 × 字数, 4, 10)` 秒；`C.L[i] = [起, 止]` 由构建时注入。

## 事实规则

- 屏幕和讲稿上的事实（金额、日期、项目名、因果）只用源稿原文有的；源稿没写的不补，不用你自己的知识补细节。
- 手册标「待核实」「未公开」「未确认」的，照原样说「未公开」等，不下结论。归因（如朝鲜关联）按源稿措辞，不加强语气。
- 金额写法跟源稿一致（「$2.85 亿」「约 1.3 亿美元」）。

## 画面规则

- 画布 1920×1080，深色背景 `#0f1117`。一次引入一个对象，新对象从旧对象长出或变形；图形承担论证（流程、资金流、阈值、时间线、对比、计数）。不要做成要点列表，不要一排三张雷同卡片（O00 的口径卡片是上限）。
- 颜色语义（全系列一致）：紫 `#B48EF0` 托管方 / CEX / 平台；蓝 `#58C4DD` 合约 / 代码 / 链；黄 `#F0B90B` 资金 / 资产；红 `#FC6255` 攻击者 / 损失 / 错误；绿 `#83C167` 防御 / 正确做法；冰蓝 `#9CDCEB` 冻结；灰 `#8a8f99` 中性 / 次要；正文 `#e8e6df`；面板 `#161a22`。
- 字号：阅读文字 ≥ 28 px，标题 44–64 px。左右留 ≥ 60 px，上下留 ≥ 40 px。
- 术语卡（模板里 `X-term`）在左上 x 70–700、y 56–190；出现期间这块不放别的东西。
- **防遮挡**：任何两段文字包围盒不相交；文字不压线、箭头、方框描边（留 ≥ 12 px）；新文字要放到旧内容的位置，旧内容先完全淡出。文字宽度估算：汉字 ≈ 1 个字号，英文 / 数字 ≈ 0.6 个字号。
- **叠放顺序 = DOM 顺序**：后写的元素盖住先写的。要移动到别的方框里的东西（钥匙、硬币），写在那个方框之后。
- 每句至少一个动作。这一句要讲的东西在 `at(i, 0.85)` 前全部出现（翻页停在句末画面）。

## 技术约定

- 从 `src/slides/o00/compositions/mtgox.html` 复制骨架：`<template>` 包住 style + `#root` div + script；`/*CUES*/{}/*END*/` 原样保留；`window.__timelines["<场景 id>"] = tl;` 的 key 必须等于场景 id 和文件名。
- 不写 `@font-face`，字体由播放器给（中文默认字体；`.mono` 用于英文代码、地址，`.mono` 里不放中文）。
- 所有 id 加本场景两三个字母的前缀，整章唯一。不用 `[id^=...]` 选择器。
- 不用 CSS `transform`（SVG 的 `transform` 属性可以）；位移用 gsap 的 `x / y` 作用在 `<g>` 上；缩放用 `svgOrigin: "x y"`；同一元素不要既位移又缩放（外层 g 位移，内层 g 缩放）。
- 带 `marker-end` 的路径：`class="dr h" pathLength="1"` + `ARROW()`；普通线：`class="dr" pathLength="1"` + `DRAW()`。
- 已可见元素的后续变化用 `tl.to`，或 `fromTo` 加 `immediateRender: false`。不用 `Math.random()`、不用 `repeat: -1`、不用 `foreignObject`。
- 结尾保留模糊淡出那两行（`#X-all` blur + term 淡出）。

## 自检（必做）

```bash
python3 tools/snap_slides.py <id> <你的 scratch 目录>/<id>          # 全部页
python3 tools/snap_slides.py <id> <你的 scratch 目录>/<id> 5-9      # 只重拍改过的页
```

它会生成 `src/slides/<id>/preview.html`（已 gitignore），用无头 Chrome 拍每页句末画面 `pNN.png`，拼成 `sheet-N.png`（每张 9 页，下方是讲稿）。用 Read 看 sheet，必要时看单页 png：

- 逐页查遮挡、出框、文字压线、该消失没消失、画面与讲稿不符、空白页（空白页多半是脚本报错：检查 id、选择器、timeline key）。
- 修完重拍改过的页再看一次。全部 sheet 至少完整看过一遍。
- 不要运行不带 `--only` 的 `tools/make_slides.py`，不要跑 `tools/build.sh`，不要 git commit，不要 kill 任何进程。

## 交付

每章一行：场景数 / 页数、看过几张 sheet、遗留问题、源稿里拿不准而没上 slides 的事实。不要贴代码。
