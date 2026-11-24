# G04 多签与验证者阈值 · 分镜

源稿：`data/groups.js` 中 `id:"g04"`；事件行 `rowsOf(g)` = `data/events.js` 中 tech `T3` 的 8 行（node 现算：合计 1418.75 → `$14.2 亿`，≥ $10M 7 起，有独立章 4 起）。

## 知识点清单（源稿逐条）

| # | 知识点 | 出处 | 场景 |
|---|---|---|---|
| K1 | 桥和多签用“多个签名者里至少几个同意”分散风险 | intro | gate L0 |
| K2 | 失效原因几乎都是签名者不独立：同一组织 / 云账号 / 运维机 | intro | gate L2–L3 |
| K3 | 或者阈值本身太低 | intro | gate L4 |
| K4 | 图：表面 9 个签名者，实际组织 A 持 S1–S4 + 代签 S5，攻破 1 个组织即 5/9 | mermaid、事件行 Ronin | ronin L0–L3 |
| K5 | Ronin $6.25 亿，Lazarus（执法） | 事件行 | ronin L4 |
| K6 | 阈值应按“攻击者需要攻破几个独立组织”计算 | readpts 1 | ronin L5–L6 |
| K7 | 每一起事件都能用“最少需要攻破几个组织”解释；攻击者凑够了阈值 | why | ronin L6、gate |
| K8 | Harmony 2/5 热钱包，拿到 2 把私钥，$1 亿，FBI 归因 Lazarus | readpts 2、examples | cases L0–L1 |
| K9 | Orbit 7/10，但签名者私钥同时失陷，$81.5M，研究机构怀疑朝鲜 | readpts 2、examples | cases L2–L3 |
| K10 | Drift 2026：6 个月线下社工，2/5 签名者预签 durable nonce 交易，timelock 为 0，$2.8 亿 | examples | cases L4–L5 |
| K11 | KelpDAO 2026：1-of-1 DVN，RPC 被投毒 = 全部验证者被投毒；伪造 burn 消息释放 116,500 rsETH，$2.9 亿；LayerZero 称 TraderTraitor | readpts 3、examples、事件行 | kelp L0–L4 |
| K12 | 事件表：8 起、合计 $14.2 亿、7 起 ≥ $10M；含 AFX、THORChain、Shibarium | 事件行 | fix L0–L1 |
| K13 | P0 按独立实体设计阈值：最少攻破组织数 ≥ 3 | controls | fix L2 |
| K14 | P0 临时授权带到期时间；每月比对签名权限与审批单 | controls | fix L3 |
| K15 | P1 验证者使用不同云、不同 RPC、不同运维团队 | controls | kelp L5 |
| K16 | P1 阈值变更与管理员操作走时间锁，timelock > 0、可取消 | controls | fix L4 |
| K17 | 动手验证 L3 实验 | labs | fix L5 |

## 场景

1. **gate 阈值的承诺**（5 句）9 个签名者 + 资金；凑够 5 格放款 → 签名者汇聚到同一依赖框，攻破一处全部变红 → 阈值标记滑到 2，“阈值太低”。
2. **ronin Ronin：9 个签名 1 个组织**（7 句）同一排签名者按组织框起来，S5 用虚线“代签”连回组织 A；假招聘箭头攻破组织 A，计数 5/9；资金流失 $6.25 亿；术语卡“最少攻破组织数”，按人头 5 vs 按组织 1。
3. **cases 阈值失守的三种样子**（6 句）同一种“签名点 + 阈值括号”图依次换成 Harmony（2/5，两把钥匙）、Orbit（7/10，七个点同时变红）、Drift（两份预签文件 + timelock 条缩到 0）。
4. **kelp KelpDAO：1-of-1 DVN**（6 句）消息 → DVN → 目标链释放；RPC 被投毒，DVN 变红，“1/1 被投毒 = 全部”；伪造 burn 消息穿过，计数到 116,500 rsETH；最后 DVN 换成三个各用不同 RPC 的验证者。
5. **fix 防御落点**（6 句）8 起事件条形图 + $10M 线；三条防御带：按组织分组的阈值（最少攻破 3）、临时授权到期、时间锁时间线；最后模拟 L3 实验勾选两个组织“还差 1 个”。

## 未上 slides 的点

- Ronin 的阈值、组织 A/B–E 的分组按源稿 mermaid；没有补充 Sky Mavis 等源稿 G04 未写的名字。
- Orbit 的年份：examples 写“2024”，事件表日期为 2023-12-31，口径不一致，slides 不写年份。
- AFX Bridge（约 2/3 门槛）、THORChain（TSS 分片）、Shibarium（闪电贷买验证者多数）只在条形图里出现名字和金额，不展开机制，避免本章过长。
- fix 场景里“阈值 7/9、每组织 3 个”是示意配置，不是某个真实事件。
