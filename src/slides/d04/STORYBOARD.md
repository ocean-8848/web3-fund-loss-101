# D04 术语表 · 分镜

源稿：`data/groups.js` 中 `const GL=[...]`（46 条）与 `H.docs.push({id:"d04"...})`（lede：按出现顺序排列，全书每个术语只用这一个词）。
导览形式：不逐条念定义，而是把 46 个词挂到“人 → 钥匙 → 合约 → 跨链与价格 → 资金去向”五站 + 防御闸门上；每站挑高频词讲，定义只取 GL 原文。

## 分组（46 个全部归位，map 场景用点数表示）

| 站 | 术语 |
|---|---|
| 人与入口（8） | 社会工程、会话令牌、MFA / 2FA、SIM 换卡、供应链攻击、Contagious Interview、Web shell、0day |
| 钥匙与签名（10） | 私钥、助记词、EOA、盲签、清晰签名、MPC、多签、阈值、热/温/冷钱包、Profanity |
| 合约与代码（9） | calldata、函数选择器、delegatecall、masterCopy / 实现合约、代理合约、重入、EIP-7702、nonce、sysvar |
| 跨链与价格（10） | 跨链桥、验证者、DVN、VAA、Keeper、预言机、TWAP、闪电贷、重组、51% 攻击 |
| 资金去向与归因（5） | Tornado Cash、THORChain、Lazarus、TraderTraitor、ATT&CK |
| 防御闸门（4） | SRI、Safe Guard、时间锁、熔断 |

## 场景

- map 一条链装下术语表（3 句）：46 个点 → 归入五站与防御条 → 站名与举例。
- sign 钥匙与签名（5 句）：助记词→私钥→EOA→转走；设备只显示哈希（盲签）→ 解析显示（清晰签名）；5 个签名者 3/5 阈值 + 共用依赖；MPC 三分片共同签名，任意交易照样签出。术语卡：私钥、盲签、清晰签名、多签/阈值、MPC。
- code 合约与代码（5 句）：calldata 条 + 前 4 字节选择器；两个签名碰到同一选择器、2^32；代理合约→实现合约被替换；delegatecall 把目标代码放进钱包存储，masterCopy 槽被改写；EIP-7702 委托 + nonce 匹配。
- xchain 跨链与价格（5 句）：链 A 锁定→桥→链 B 铸造；5 个验证者 3/5 → 1-of-1 DVN 单点；一笔交易内借入/归还 + 预言机喂价；即时价格尖峰 vs TWAP；主链被更长分支替换、已确认交易被撤销、51%。
- people 人与资金去向（6 句）：话术气泡→员工→系统没被攻破；令牌绕过密码/MFA、短信转到攻击者 SIM；攻击者→依赖→目标；假招聘→面试作业→开发者电脑；赃款分两路 Tornado Cash / THORChain；Lazarus 与 TraderTraitor 两个名字的层级。
- gate 防御闸门（5 句）：五站链 → SRI、Safe Guard、时间锁、熔断四道绿闸依次落位 → “新词”落到某一站。

## 未上 slides 的点

- 逐条讲解的术语：MFA / 2FA、Web shell、0day、EOA 单独定义、热/温/冷钱包、Profanity、masterCopy 单独定义、重入、nonce 单独定义、sysvar、VAA、Keeper、ATT&CK。它们出现在 map 的点数里，未展开：要么是另一个已讲术语的一部分（EOA、nonce、masterCopy 在 sign / code 画面中出现），要么属于单一案例（Profanity、Keeper、VAA、sysvar），导览篇幅内价值较低。
- 重入：O00 的 The DAO 场景已经讲过，此处不重复。
- “多签：需要 M 个签名者中的 N 个签名”原文 M/N 用法与常见写法相反，slides 只说“凑够阈值”，不写 M-of-N。
- 闸门在链上的位置（SRI 在入口、熔断在资金去向前等）是本 slides 的归类，不是源稿原文。
