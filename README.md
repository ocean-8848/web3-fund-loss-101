# Web3 行业安全资损 101

《Web3 行业安全资损 101》的源稿、动画 Slides、学习站和离线包。在线版：https://claude.ai/artifact/1a5Nx6xTVLuJdCB8Esf2xj

**本地直接看：双击 [`dist/offline/index.html`](dist/offline/index.html)**（不用联网；页眉「▶ Slides」进动画播放器）。

## 目录

```
├── src/                     源稿：只改这里
│   ├── handbook/            手册
│   │   ├── index.html       外壳、渲染器、样式（HTML 片段，发布时由平台包成完整文档）
│   │   ├── data/            章节、事件库、来源
│   │   └── labs/            交互复盘页
│   ├── slides/              动画 Slides
│   │   ├── <章 id>/         narration.json 讲稿 · compositions/ 每个场景一个文件 · STORYBOARD.md 知识点覆盖
│   │   ├── player.tpl.html  播放器模板
│   │   └── AGENT.md         制作简报（新做或改一章时先读）
│   └── learning/            学习层：learn.js、visual.js，以及接入本手册的 config.js
├── dist/                    构建产物：不手改，用 tools/build.sh 重建
│   ├── site/                在线版：发布到 artifact 的就是这个目录（Mermaid / GSAP 走 cdnjs）
│   ├── learning/            学习站：手册 + 学习层（preview.html 是带 doctype 的预览版）
│   └── offline/             离线包：完整 HTML 文档，Mermaid / GSAP 在 vendor/
└── tools/
    ├── build.sh             一条命令重建 dist/ 全部产物
    ├── make_slides.py       生成 Slides 播放器（build.sh 会调用；--only <章> 生成单章预览）
    ├── snap_slides.py       无头 Chrome 拍某章每页截图并拼 contact sheet，用于自检
    └── offline-README.md    离线包里的 README
```

手册数据 `src/handbook/data/`：

| 文件 | 内容 |
|---|---|
| `core.js` | 首页、写作规范、O00–O03 总论 |
| `cases-a.js` … `cases-e.js` | 32 个独立案件章 |
| `groups.js` | G01–G10 手法归纳，D01–D04 防御与附录 |
| `events.js` | 全量事件库（213 条） |
| `evsrc.js` | 事件库逐条来源链接与核对状态 |
| `labs.js` | L1–L11 实验室 |

`labs/binance-1029.html` 是币安热钱包事件的交互复盘，L7、L8 引用。

## 构建

改完 `src/` 后：

```bash
sh tools/build.sh
```

依次生成 `dist/site`（源稿 + `slides.html` + `data/slides.js`）、`dist/learning`、`dist/offline`。离线包的 Mermaid 11.12.0 和 GSAP 3.12.5 第一次构建时从 cdnjs 下载到 `dist/offline/vendor/`，之后复用。

## 发布在线版

在线版是多文件 artifact：页面是 `dist/site/index.html`，附带 `dist/site/` 下的 `data/`、`labs/`、`slides.html`。

1. 先读在线版，把别的会话发布的改动合并回 `src/`。
2. `sh tools/build.sh`。
3. 发布 `dist/site/`。

## Slides

总论、手法归纳、防御与附录（O/G/D 共 18 章，553 页）各有一组 3b1b 风格动画 slides，用来快速过知识点。做法参照 web3-101 课程视频的 PPT 场景，但没有配音：每页对应讲稿里的一句话，显示在画面下方。翻页直接显示整页画面（场景时间轴停在这一句的句末），不等动画；「自动」按每句的阅读时间翻页，时长按字数估算（`tools/make_slides.py` 的 `read_time`）。

- 一章一个目录 `src/slides/<章 id>/`；场景模板与助手函数（`at / IN / OUT / DRAW / ARROW / COUNT`）同课程视频，时间一律写成 `at(句号, 句内比例)`。规则见 `src/slides/AGENT.md`。
- 屏幕上的事实只取本仓库源稿；手册标「待核实」的不上 slides。各章 `STORYBOARD.md` 列出知识点覆盖和未上 slides 的理由。
- 自检：`python3 tools/snap_slides.py <章 id> <输出目录>`。
- 手册章节页顶部和页眉有入口，播放器里「读原文」跳回手册。

## 规则

- **以仓库为准。** 发布到在线版之前，先读在线版，把别的会话发布的改动合并回仓库，再发布。
- **只改 `src/`。** `dist/` 是构建产物，手改会在下次构建时被覆盖。
- **每个事件都有自己的来源**（`src/handbook/data/evsrc.js`），优先一手来源。二手汇编只作参考，不作为来源引用。
