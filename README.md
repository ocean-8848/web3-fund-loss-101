# Web3 行业安全资损 101

《Web3 行业安全资损 101》的源稿、学习站和离线包。在线版：https://claude.ai/artifact/1a5Nx6xTVLuJdCB8Esf2xj

## 目录

```
├── index.html             手册外壳、渲染器、样式（源稿）
├── data/                  章节、事件库、来源（源稿）
├── labs/                  交互复盘页（源稿）
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
sh learning-site/loss/build.sh   # → learning-site/loss/index.html、preview.html、data/、labs/
sh tools/pack-offline.sh         # → web3-loss-101-site/
```

源稿本身不用构建，直接用浏览器打开 `index.html`（图表需要联网加载 Mermaid）。离线包里的 Mermaid 是 11.12.0，放在 `vendor/` 下，第一次生成时从 cdnjs 下载。

## 规则

- **以仓库为准。** 发布到在线版之前，先读在线版，把别的会话发布的改动合并回仓库，再发布。
- **每个事件都有自己的来源**（`data/evsrc.js`），优先一手来源。二手汇编只作参考，不作为来源引用。
