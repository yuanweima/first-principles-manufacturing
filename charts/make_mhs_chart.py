"""MHS 简评配图: 三层控制环频率阶梯 — MHS 活在哪一层, 够不到哪一层。
示意+规格混合: 频率带为公开规格(伺服 1-4kHz / UR RTDE 500Hz / MCP 往返数百 ms),
定位为定性判断。快端(接触任务)agent 够不到, 最慢端(批间漂移)恰是 agent 地盘。
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpm_style
from fpm_style import BLUE, ORANGE, INK, INK2, MUTED, SURFACE, strip
fpm_style.apply()
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))

fig, ax = plt.subplots(figsize=(8.8, 4.9), dpi=200)
ax.set_xscale("log")
ax.set_xlim(2e4, 2e-7)   # fast on the left, slow on the right
ax.set_ylim(0, 1)
ax.set_yticks([])

# bands
ax.axvspan(1e3, 4e3, color=BLUE, alpha=0.16, zorder=0)
ax.axvspan(125, 500, color=BLUE, alpha=0.16, zorder=0)
ax.axvspan(0.02, 2, color=ORANGE, alpha=0.20, zorder=0)

ax.text(2000, 0.80, "servo loop\n1–4 kHz\nin the drives", ha="center", va="center",
        fontsize=9.2, color=BLUE, fontweight="bold")
ax.text(250, 0.44, "motion control\n125–500 Hz\nvendor controller", ha="center", va="center",
        fontsize=9.2, color=BLUE, fontweight="bold")
ax.text(250, 0.29, "(UR RTDE: 500 Hz)", ha="center", va="center", fontsize=8.0, color=INK2)
ax.text(0.2, 0.80, "task layer\na few Hz and below", ha="center", va="center",
        fontsize=9.2, color=INK, fontweight="bold")
ax.text(0.2, 0.665, "MHS read/write\nlives here", ha="center", va="center",
        fontsize=10.0, color=ORANGE, fontweight="bold")
ax.text(0.2, 0.545, "agent behind MCP:\nhundreds of ms per round trip", ha="center", va="center",
        fontsize=8.0, color=INK2)

# divider: MHS stops here
ax.axvline(16, color=INK, lw=1.6, ls=(0, (6, 4)))
ax.annotate("MHS stops here — force response\ncloses 3 orders of magnitude to the left",
            xy=(16, 0.96), xytext=(0.02, 0.955), fontsize=9.0, color=INK, va="center",
            arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2))
ax.text(700, 0.135, "deburring · grinding · welding\nclose their loops here —\nthe agent can't follow", ha="center",
        va="center", fontsize=8.6, color=INK2, style="italic")

# drift: the slow end
ax.plot([1e-5], [0.42], marker="o", ms=8, color=ORANGE, zorder=3)
ax.annotate("batch-to-batch drift (hours–days):\nthe slow loop nobody records —\nthe agent's opening",
            xy=(1e-5, 0.42), xytext=(3e-3, 0.16), fontsize=9.0, color=ORANGE, fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.3))

ax.set_xticks([1e3, 100, 10, 1, 0.1, 1e-3, 1e-5])
ax.set_xticklabels(["1 kHz", "100", "10", "1 Hz", "0.1", "10⁻³", "10⁻⁵ Hz"], fontsize=8.6)
strip(ax, keep=("bottom",))
ax.set_xlabel("control-loop frequency (log scale)", fontsize=9.5)
ax.set_title("Where MHS lives — and where it can't reach", loc="left", fontsize=15, pad=12)
ax.text(0, -0.19,
        "Band rates are public specs (drives, UR RTDE); MCP round-trip per the MHS announcement. Placement is the author's judgment.\n"
        "The agent can't reach the fastest loops. The slowest loop — drift — is exactly where it belongs.",
        transform=ax.transAxes, fontsize=8, color=INK2, va="top")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "2026-08-27-mhs-control-loops.png"), bbox_inches="tight", facecolor=SURFACE)
print("done")
