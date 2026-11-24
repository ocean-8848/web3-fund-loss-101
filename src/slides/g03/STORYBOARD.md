# G03 盲签、界面篡改与供应商通道 · 分镜

源稿：`data/groups.js` 中 `G[2]`（id g03，techs T2 + T12）；事件行 = events.js 中 tech 为 T2 或 T12 的 11 行（node 现算）。

## 知识点清单

| # | 知识点（源稿） | 场景 |
|---|---|---|
| K1 | intro：签名者看到的内容与实际签名的数据不一致（盲签） | mismatch L0 |
| K2 | intro：篡改发生在签名者与链之间：网页前端、托管商界面、供应商交易构造 API、通信通道 | mismatch L1–L2 |
| K3 | why：签名者使用真实私钥，签名完全有效 | mismatch L3 |
| K4 | why：攻击者不需要接触受害方的系统 | mismatch L4 |
| K5 | 统计：11 起（T2 3 起、T12 8 起），合计 $25 亿，7 起 ≥ $10M | tally L0–L1 |
| K6 | 事件行：Bybit $14.6 亿最大；Bitget $3.88 亿、DMM $3.05 亿、WazirX $2.35 亿 | tally L2–L3 |
| K7 | mermaid：意图（转账到温钱包）→ 界面 / 供应商通道（被篡改）→ 待签数据（升级 · delegatecall · 改权限）→ 硬件钱包（只显示哈希）→ 有效签名 → 链上执行 | route L0–L4 |
| K8 | readpts：Bybit、WazirX、Radiant 2024、DMM、SwissBorg / Kiln 走同一条路 | route L5 |
| K9 | readpts：硬件钱包只有“清晰签名”时才是独立核验点；只显示哈希时只证明“我签了”，不证明“我签对了” | clear L0–L2 |
| K10 | mermaid：独立核验（第二台设备解码 calldata）本可发现 | clear L3 |
| K11 | 案例 Radiant 2024 $50M：3 名签名者设备恶意软件、Safe 界面正常后台替换、Mandiant 归因 UNC4736 | vendors L0–L1 |
| K12 | 案例 SwissBorg / Kiln 2025 $41.5M：GitHub 令牌 → CI → 基础设施凭据 → 交易构造 API 返回的 unstake 夹带提款权限转移 | vendors L2–L4 |
| K13 | readpts 局限：Kiln 的恶意交易来自 API，不是网页前端 | vendors L5 |
| K14 | 案例 Fortress Trust 2023 $13.5M：第三方云工具供应商受影响，托管客户资产被转走 | vendors L6 |
| K15 | controls P0：独立设备解码 calldata，核对 safeTxHash | guard L0 |
| K16 | controls P0：Safe Guard 禁止 delegatecall 与实现地址变更；测试网升级交易必须回滚 | guard L1–L2 |
| K17 | controls P1：交易请求端到端签名；通道改一个字节签名端必须拒绝 | guard L3–L4 |
| K18 | controls P1：供应商安全评估覆盖开发终端、云会话、发布流程；合同写明审计权 | guard L5 |
| K19 | 动手验证 L2：选真实场景与核验方式，看能否在签名前发现篡改（L2 描述） | guard L6 |

## 场景

1. mismatch（5 句）签名者屏幕“转账到温钱包” ≠ 链上“升级 / 改权限”；中间长出虚线区和四种环节；补上真实私钥、签名有效章；最后攻击者只连到中间环节，到受害方系统的虚线被划掉。
2. tally（4 句）11 条横向条形图（实心 = 盲签，空心 = 供应商通道），合计计数到 $25 亿，再标出 Bybit 和三起亿级事件。
3. route（6 句）mermaid 主链做成 S 形两行逐格长出，最后在两行之间列出五个案例名。
4. clear（4 句）左“清晰签名”屏幕显示解码字段，右“只显示哈希”屏幕；✓我签了 / ?我签对了；下方第二台设备向上核验。
5. vendors（7 句）Radiant：三台设备 + Safe 界面正常、后台替换；Kiln：令牌 → CI → 凭据 → API → unstake + 提款权限转移，API 标红，网页前端虚线框“未被改”；Fortress：供应商 → 托管商 → 被转走。
6. guard（7 句）交易请求 → 界面 / 通道 → 签名者 → Safe 多签，依次挂上独立设备、Safe Guard（测试网回滚）、端到端签名弧（改 1 字节被拒）、供应商评估；最后 L2 实验面板。

## 没上 slides 的点

- Bitget 2026（T12）机制细节（安全设备 0day → Web shell → 生产钱包任务服务器）：属于 Bitget 案件章，只在 tally 里出现金额。
- DMM（供应商 Ginco 假招聘 → 会话劫持 → 篡改交易请求）、WazirX（4/6 多签界面与交易不一致）的细节：属于各自案件章；route 只列名字。
- Fortress Trust 事件表另有“Retool 被钓鱼”“Ripple 承担赔付”等细节；按示例卡只说“第三方云工具供应商受影响”。
- 读图要点里“图中‘界面 / 供应商通道’合并表示”的说明：用 vendors L5（Kiln 篡改点在 API）表达，未单列。
- 动手验证 L1（阻塞点模拟器）省略。
