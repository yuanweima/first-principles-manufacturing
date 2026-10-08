# 三判据:环节能否进 agent 循环

**论点**:一个环节能否进入 agent 循环,看三条:①能否被另一个程序调用;②能否中途移交状态;③有没有独立于自身的校验。不满足者将被挤出——不是因为机器差,而是它会变成全链等待的唯一位置,相对成本爆炸。
**首发**:[[../Published/2026-08-21-physical-ai-agent-loop-zh|033 Is Manufacturing at Dusk or Dawn?]] (2026-08-25)

## 证据账本

| 日期 | 事实 | 来源 | 支持/挑战 |
|---|---|---|---|
| 2026-08-27 | Anthropic 发布 MHS,把判据① 标准化;官方限制条款原话 "doesn't yet work with hardware that lacks a programming interface" | [原发布] anthropic.com/news/model-hardware-standard-research-preview | 支持 |
| 2026-08-27 | MHS 对判据② 只有设备状态雏形(Janelia 共享内存状态字典),无任务状态交接标准位;判据③ 闭环实验中 agent 自判弃板重跑 | [原发布]+[推演] MHS 简评三判据打分 1+0.5+0.5 | 支持(缺口即预测) |
| 2026-Q2/Q3 | Siemens TIA Portal agent 写并验证 PLC 代码;Rockwell AI-native 工程流商用;Beckhoff TwinCAT 发 MCP client(可气隙) | [多源] 033 证据链 | 支持 |
| 2026-08-28 | Siemens 在泰国推出 Eigen Engineering Agent(区域商用落地) | [单源] Siemens Newsroom via 雷达 | 支持 |
| 2026-08-27 | UR、Doosan 首批建 MHS 支持;Doosan 测"自动质检+多机器人协调" | [多源] 雷达/媒体名单 | 支持 |

## 反例区

(空——需主动找:有没有"不可被调用"却长期没被挤出的环节案例?)

## 派生预测

见 [[predictions]] P1、P6–P8。
