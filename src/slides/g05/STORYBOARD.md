# G05 账户接管：钓鱼、2FA 与 API Key · 分镜

源稿：`data/groups.js` 中 `id:"g05"`；事件行 `rowsOf(g)` = `data/events.js` 中 tech `T8` 的 12 行（node 现算：合计 613.13 → `$6.13 亿`；≥ $10M 5 起；金额未披露 5 起；另 2 起不足 $1M；无独立章）。

## 知识点清单（源稿逐条）

| # | 知识点 | 出处 | 场景 |
|---|---|---|---|
| K1 | 攻击者不碰平台钱包，接管用户账户 | intro | entry L0 |
| K2 | 入口一：钓鱼站 / 恶意插件 / 数据泄露 → 密码 + 2FA | intro、mermaid | entry L1 |
| K3 | 入口二：账户恢复缺陷（SMS 恢复） | intro、mermaid | entry L2 |
| K4 | 入口三：第三方工具泄露（3Commas）→ API Key | intro、mermaid | entry L3 |
| K5 | 单个用户损失小，合计可达数千万美元 | intro | entry L4 |
| K6 | 登录或调用 API 后两条路：提现到外部地址 / 交易权限对敲拉盘 | mermaid | api L0–L1 |
| K7 | 只有交易权限的 API Key 也能造成损失：Binance VIA 2018 用受害账户高价买入攻击者挂出的代币 | readpts 1、事件行 | api L2–L4 |
| K8 | 阻止外部提现不等于用户零损失（VIA 外部提现被拦截） | readpts 2、事件行 | api L5 |
| K9 | Binance 2019：钓鱼与恶意代码取得 API Key 和 2FA，多账户协同通过检查，一次性提现 7,000 BTC | examples | cases L0–L1 |
| K10 | Crypto.com 2022：2FA 被绕过，483 个账户未授权提现，$34M，平台全额补偿 | examples、事件行 | cases L2–L3 |
| K11 | Coinbase 2021：SMS 账户恢复缺陷，至少 6,000 名客户资金被转出；金额未披露 | examples、事件行 | cases L4–L5 |
| K12 | 局限：此类事件的总金额通常未披露 | readpts 3 | cases L5、fix L0 |
| K13 | 事件表：12 起、$6.13 亿、5 起未披露 | 事件行 | fix L0 |
| K14 | 入口在用户侧，平台风控决定损失上限 | why | fix L1 |
| K15 | P0 新设备 / 新 IP 提现冷却 + 地址白名单（24 小时内不能提到新地址） | controls | fix L2 |
| K16 | P0 API Key 默认无提现权限、绑定 IP；无 IP 绑定的 Key 不能交易低流动性币 | controls | fix L3–L4 |
| K17 | P1 异常交易模式检测：多账户同时买入同一低流动性币 | controls | fix L5 |

## 场景

1. **entry 入口在用户侧**（5 句）平台框里“平台钱包没被碰”、用户账户被攻击者接管；左侧三个入口依次长出箭头汇到“密码 + 2FA / API Key”；底部一排小用户的小额硬币汇成一条长红条。
2. **api 没有提现权限也能亏**（6 句）受害账户分出“提现 / 交易”两条路；提现路变暗，攻击者挂出 VIA 高价卖单，硬币沿交易路流向攻击者，两边余额条此消彼长；最后提现路上出现冰蓝“拦截”，结论“拦截 ≠ 零损失”。
3. **cases 三起典型案例**（6 句）Binance 2019 的 9 个账户穿过“原有检查”汇成一次提现 7,000 BTC；Crypto.com 的 2FA 盾牌裂开，120 个点变红、计数到 483，再变绿表示全额补偿；Coinbase 的 SMS → 账户恢复 → 一片账户变红，“至少 6,000 名客户 · 总额未披露”。
4. **fix 风控决定损失上限**（6 句）事件条形图（5 起已披露大额 + 5 个“?”）；然后一条从被接管账户到“提现 / 交易”的管道，绿色风控框里逐个立起 4 道闸门，红色代币被第一道挡住。

## 未上 slides 的点

- FTX（破产期转移，$4.77 亿）只在条形图出现名字和金额。事件行写明“起诉书未点名 FTX，媒体指认”，且要与挪用、破产缺口区分，几秒的画面讲不清这层限定，所以不在讲稿里展开。
- IRA Financial Trust / Gemini、Kronos Research / WOO X、Bithumb 数据泄露、LocalBitcoins、Coinmama、Coinbase SIM 劫持个案、3Commas 的事件行细节没有展开；3Commas 只作为第三方工具入口的例子出现。
- 动手验证 L1（阻塞点模拟器）没有单独一页：它面向全部案件，与本章关系弱于 G04 的 L3。
