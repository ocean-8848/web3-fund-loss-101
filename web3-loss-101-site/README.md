# Web3 行业安全资损 101 · 本地站点

在线版：https://claude.ai/artifact/1a5Nx6xTVLuJdCB8Esf2xj
由 `tools/pack-offline.sh` 从仓库根目录的源稿生成。

## 打开方式

任选一种：

1. 直接双击 `index.html`，用浏览器打开。
2. 在本目录启动本地服务器（推荐。部分浏览器限制 `file://` 下的 iframe）：

```bash
python3 -m http.server 8000
```

然后访问 http://localhost:8000

## 目录

| 路径 | 内容 |
|---|---|
| `index.html` | 手册外壳、渲染器、样式 |
| `data/core.js` | 首页、写作规范、O00–O03 总论 |
| `data/cases-a.js` … `cases-e.js` | 32 个独立案件章 |
| `data/groups.js` | G01–G10 手法归纳，D01–D04 防御与附录 |
| `data/events.js` | 全量事件库（213 条） |
| `data/evsrc.js` | 事件库逐条来源链接与核对状态 |
| `data/labs.js` | L1–L9 实验室 |
| `labs/binance-1029.html` | 币安热钱包事件原版交互复盘（L7、L8 引用） |
| `vendor/mermaid.min.js` | Mermaid 11.12.0，本地化以便离线渲染图表 |

## 离线说明

- 图表、交互、搜索全部离线可用。
- 字体来自 Google Fonts。离线时自动回退到系统字体，版式不变。
- 章节与来源中的外部链接需要联网。
