# Web3 行业安全资损 101

《Web3 行业安全资损 101》的源稿、学习站和离线包。在线版：https://claude.ai/artifact/1a5Nx6xTVLuJdCB8Esf2xj

## 目录

```
├── index.html             手册外壳、渲染器、样式（源稿）
├── data/                  章节、事件库、来源（源稿）
├── labs/                  交互复盘页（源稿）
├── slides/                Slides 源稿：每章 narration.json（讲稿）+ compositions/（每个场景一个动画文件）、player.tpl.html
├── slides.html            Slides 播放器（构建产物，tools/make_slides.py 生成）
├── learning-site/         学习站：learn.js、visual.js 学习层 + loss/ 站点（构建产物）
├── web3-loss-101-site/    离线包：源稿 + 本地 Mermaid（构建产物）
└── tools/pack-offline.sh  生成离线包
```

源稿 `data/` 的内容：

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

只改根目录的源稿，改完重新生成两个产物：

```bash
python3 tools/make_slides.py     # → slides.html、data/slides.js（改了 slides/ 先跑这一步）
sh learning-site/loss/build.sh   # → learning-site/loss/index.html、preview.html、data/、labs/、slides.html
sh tools/pack-offline.sh         # → web3-loss-101-site/
```

离线包里的 Slides 用 `vendor/` 下的 GSAP 3.12.5。

## Slides

总论、手法归纳、防御与附录（O/G/D 共 18 章）各做一组 3b1b 风格动画 slides，用来快速过知识点；做法参照 web3-101 课程视频的 PPT 场景，但没有配音：每页对应讲稿里的一句话，显示在画面下方，翻页时播放这一句的动画。时长按字数估算（`tools/make_slides.py` 的 `read_time`）。

- 一章一个目录 `slides/<章 id>/`：`narration.json` 写场景和逐句讲稿；`compositions/<场景 id>.html` 是场景，模板与助手函数（`at / IN / OUT / DRAW / ARROW / COUNT`）同课程视频，时间一律写成 `at(句号, 句内比例)`。
- 屏幕上的事实只取本仓库源稿；手册标「待核实」的不上 slides。
- 手册章节页顶部和页眉有入口，播放器里「读原文」跳回手册。已完成全部 18 章（553 页）。各章 `STORYBOARD.md` 列出知识点覆盖和未上 slides 的理由；制作简报见 `slides/AGENT.md`，自检用 `python3 tools/snap_slides.py <章 id> <输出目录>` 拍每页截图。

源稿本身不用构建，直接用浏览器打开 `index.html`（图表需要联网加载 Mermaid）。离线包里的 Mermaid 是 11.12.0，放在 `vendor/` 下，第一次生成时从 cdnjs 下载。

## 规则

- **以仓库为准。** 发布到在线版之前，先读在线版，把别的会话发布的改动合并回仓库，再发布。
- **每个事件都有自己的来源**（`data/evsrc.js`），优先一手来源。二手汇编只作参考，不作为来源引用。
