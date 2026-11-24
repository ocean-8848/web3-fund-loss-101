# G06 前端、DNS 与软件供应链 · 分镜

源稿：`data/groups.js` 中 `id:"g06"`；事件行 `rowsOf(g)` = `data/events.js` 中 tech `T7` 的 14 行（node 现算：合计 158.59 → `$1.59 亿`；≥ $10M 2 起；金额未披露 4 起；另 3 起不足 $0.1M；有独立章 1 起 BadgerDAO）。

## 知识点清单（源稿逐条）

| # | 知识点 | 出处 | 场景 |
|---|---|---|---|
| K1 | 攻击者篡改用户加载的代码（前端、统计脚本、npm 包、浏览器扩展、域名解析） | intro | chain L0–L1 |
| K2 | 上游：npm 维护者 / 注册商与 DNS / CDN 与 Cloudflare API / 扩展商店发布密钥，被钓鱼或凭据泄露 | mermaid | chain L1–L2 |
| K3 | 上游任一环被改，所有下游用户同时受影响；影响面大，单笔可能小 | readpts 1 | chain L2、fix L1 |
| K4 | 被改的前端替换收款地址 / 请求无限授权 → 用户签名 → 资产转出 | mermaid | chain L3–L4 |
| K5 | 用户用的是“官方”渠道；攻击者控制代码分发而不是钱包 | why | chain L4、术语卡 |
| K6 | BadgerDAO 2021：最早的大额案例，Cloudflare API 密钥被盗，前端注入请求无限授权的脚本，约 1.2 亿美元 | readpts 2 | badger L0–L4 |
| K7 | Gate.io / StatCounter 2018：统计 JS 被投毒，只在 Gate.io 提现页替换 BTC 收款地址 | examples | cases L0–L1 |
| K8 | Ledger Connect Kit 2023：前员工 npm 账号被钓鱼，恶意版本影响大量 dApp 约 5 小时 | examples | cases L2–L3 |
| K9 | npm chalk/debug 2025：维护者被钓鱼，18 个包植入地址替换代码；直接资损很小，影响面极大 | examples | cases L4–L5 |
| K10 | Trust Wallet 扩展 2025：Shai-Hulud 蠕虫 → GitHub 密钥 → Chrome 商店 API key → 发布恶意版本，5 层；$8.5M | readpts 3、事件行 | trust L0–L2 |
| K11 | BigONE 2025（$27M）：第三方攻击影响生产环境，账户与风控逻辑被操纵；私钥安全 | examples、事件行 | trust L3–L4 |
| K12 | DNS 被改 → 指向钓鱼前端（Curve 等） | 事件行 | dns L0 |
| K13 | Squarespace DNS 2024：域名迁移后无 MFA，多个 DeFi 前端 DNS 被劫持 | 事件行 | dns L1 |
| K14 | CoW Swap 2026：社工 + 伪造身份文件骗取注册商 / 注册局；合约未受影响，访问用户损失约 $1.2M | 事件行 | dns L2–L3 |
| K15 | 事件表：14 起、$1.59 亿、4 起未披露 | 事件行 | fix L0–L1 |
| K16 | P1 依赖锁定版本 + 发布延迟窗口（72 小时后才进入构建） | controls | fix L2 |
| K17 | P0 前端资源 SRI + 构建产物签名（篡改一个 JS，浏览器必须拒绝加载） | controls | fix L3 |
| K18 | P0 注册商锁 + 硬件 MFA，每季度检查 | controls | fix L4 |
| K19 | P1 钱包对无限授权显著警告（approve(max) 必须显示警告） | controls | fix L5 |

## 场景

1. **chain 上游被改，下游全中**（5 句）“用户加载的前端代码”扇出到 12 个用户；上方四个上游盒子汇入；上游变红，红色沿扇出线传到每个用户；前端旁出现“替换收款地址 / 请求无限授权”；硬币从每个用户流向“资产转出”。
2. **badger BadgerDAO：注入无限授权**（5 句）“官方前端”浏览器窗口；Cloudflare API 密钥被拖到攻击者；攻击者注入 `<script>`，页面弹出 `approve(max)` 签名请求；用户点“批准”；箭头流向“损失约 1.2 亿美元”。
3. **cases 脚本与 npm 投毒**（6 句）统计 JS 通过总线连到三页，只有提现页的地址从“用户的地址”换成“攻击者地址”；npm 账号 → 恶意版本 → 12 个 dApp 变红 + 约 5 小时时间条；维护者 → 18 个包变红 → 小硬币“直接资损很小”对比一大片红点“影响面极大”。
4. **trust 扩展与生产环境**（5 句）Trust Wallet 的阶梯式攻击链；BigONE 的生产环境里账户逻辑、风控逻辑变红，旁边私钥盒子标“私钥是安全的”。
5. **dns 域名与 DNS**（4 句）用户 → 域名 → DNS 记录 → 官方前端，箭头改指钓鱼站；Squarespace：注册商“迁移后没有 MFA”、多个域名叠起来；CoW Swap：伪造身份文件送进注册商；最后合约“没有受影响”、钓鱼站下方“访问用户损失约 $1.2M”。
6. **fix 防御落点**（6 句）事件条形图 + 4 个“?”；然后“npm 依赖 → 构建 → CDN / 域名 → 浏览器 → 钱包签名”管道，每个环节下挂一个绿色控制。

## 未上 slides 的点

- Aerodrome、Curve 的 DNS 事件、KuCoin / CoinList 官方 X 账号被控、Liquid（GoDaddy 员工遭社工）、Coincheck（お名前.com）只在条形图或完全没有出现。社交账号类与“代码分发”主线不同，放进来会冲淡本章，所以留给事件表。
- BadgerDAO 的授权对象、资金去向源稿没有写，画面只画到“批准 → 损失”，不画授权给谁。
- Trust Wallet 的“5 层”照源稿写作“手册记为 5 层”，画面画出源稿列出的 4 个环节，不自行编号补第 5 层。
- 动手验证 L2（盲签实验）与本章的关系是“界面与数据不一致”，讲稿里没有单独一页。
