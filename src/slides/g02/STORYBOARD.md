# G02 私钥与签名者失陷 · 分镜

源稿：`data/groups.js` 中 `G[1]`（id g02，techs T1）；事件行 = events.js 中 tech 为 T1 的 31 行（node 现算，含 41f253f 的金额修订：Step Finance $40M、Coincheck $5.3 亿）。

## 知识点清单

| # | 知识点（源稿） | 场景 |
|---|---|---|
| K1 | intro：攻击者拿到私钥、MPC 分片或签名服务调用能力 | sign L0–L1 |
| K2 | intro：签出“合法”交易 | sign L2 |
| K3 | 统计：31 起，24 起 ≥ $10M，合计 $83.4 亿 | scope L0–L1 |
| K4 | 统计（现算）：Binance 2026 $63.4 亿，占 76%；其余 30 起约 $20 亿 | scope L2–L3 |
| K5 | 统计：7 起有独立案件章 | scope L4 |
| K6 | intro + mermaid：入口多为社工（假招聘·假客户·钓鱼）→ 终端失陷 → 会话 / 云凭据 → 签名能力 | entry L0–L3 |
| K7 | intro + mermaid：密钥生成缺陷（弱随机数 · nonce 复用）不需要入侵 | keygen L0–L1 |
| K8 | readpts + 案例：Wintermute Profanity 靓号地址、32 位种子、公钥暴力还原、$1.6 亿 | keygen L2–L3 |
| K9 | intro + 事件行：Ledger 应用 nonce（Zilliqa 旧版应用，公开签名可暴露私钥） | keygen L4 |
| K10 | readpts + mermaid：私钥泄露 ≠ 签名能力被滥用；私钥 → 直接签名，签名服务 → 伪造签名请求，都到链上转出 | misuse L0–L2 |
| K11 | readpts：后者例子 Binance 热钱包事件、Bitget | misuse L3 |
| K12 | readpts 局限：多数事件只公开“私钥受影响” | misuse L4 |
| K13 | 案例 BitoPro 2025 $11.5M：云运维社工、AWS 会话劫持、升级迁移期间模拟正常运维 | intrude L0–L1 |
| K14 | 案例 WOO X 2025 $14M：外部协作项目恶意程序 → 开发者终端 → Kubernetes → 数据库 → 改账户提现，5 层 | intrude L2–L3 |
| K15 | 案例 Mixin 2023 $2 亿：云服务商数据库被入侵，热钱包密钥外泄 | intrude L4 |
| K16 | why：最终都取得签名能力；防线在“谁能触达签名”“签名前谁核对意图” | defend L0、L1、L3 |
| K17 | controls P0：签名设备与办公网隔离；私钥不落盘，HSM / MPC；任一台服务器失陷不能独立签出 | defend L1–L2 |
| K18 | controls P0：签名前独立策略层（类型、地址、金额、速率） | defend L3 |
| K19 | controls P1：靓号地址与自研密钥工具熵审计 | defend L4 |
| K20 | controls P1：运维与开发招聘社工演练，红队投递假 offer | defend L5 |
| K21 | 动手验证 L8：MPC 保护密钥，不判断意图（L8 描述） | defend L6 |

## 场景

1. sign（3 句）攻击者 → “签名能力”框，长出私钥 / MPC 分片 / 签名服务三种形态，再签出带“签名有效”章的交易。
2. scope（5 句）31 点（按损失排序，24 个变黄）→ 合计条 $83.4 亿 → Binance 段占 76% → 其余 30 起 ≈ $20 亿 → 7 个有案件章的点加绿圈。
3. entry（4 句）mermaid 上半支逐格长出，“攻击者”标记沿链路移动到签名能力。
4. keygen（5 句）生成工具 → 私钥 → 公钥，红色回推箭头；工具换成 Profanity、加 32 位种子；最后换成 Ledger · Zilliqa 的小流程。
5. misuse（5 句）签名能力分出两支，≠；上支钥匙被拿走，下支钥匙留在原地但照签；底部挂例子，顶部挂局限。
6. intrude（5 句）三条入侵路径逐格展开，WOO X 末尾挂“5 层”。
7. defend（7 句）办公网 → 签名设备 → 策略层 → 链上；隔离墙、HSM / MPC、策略层依次装上，两个 P1 挂在对应位置；最后 L8 结论。

## 没上 slides 的点

- BitoPro 金额：示例卡写 $11.5M，事件表显示 $12M（同一个 11.5 取整）；按示例卡。BitoPro 事件表层数已修订为 6，slides 未提层数。
- 年份分布：2026 年 8 起 $65.6 亿，几乎全部来自 Binance；已由 Binance 占比表达，未单独画。
- 事件表其余条目（Coincheck $5.3 亿、PlayDapp、Atomic Wallet 等）不逐条上。
- L9（熵与暴力还原）、L1（阻塞点模拟器）：只在旁白里由 L8 收尾，L9 只在熵审计处隐含，未单列一页。
