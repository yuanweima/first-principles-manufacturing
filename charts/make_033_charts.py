"""033 Physical AI 篇图表(手绘主题版)。数据来源见各图 source 行与 Ideas/033;风格见 fpm_style.py。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpm_style
from fpm_style import BLUE, ORANGE, INK, INK2, MUTED, SURFACE, strip
fpm_style.apply()
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

OUT = os.path.dirname(os.path.abspath(__file__))
def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)

# ── 1 资金:六个月 vs 三年 ──
fig, ax = plt.subplots(figsize=(7.3, 3.6), dpi=200)
cats = ["2022–2024\n(three years combined)", "H1 2026\n(six months)"]
vals = [41.9, 47.4]
bars = ax.barh(cats, vals, height=0.42, color=[MUTED, BLUE])
for b, v in zip(bars, vals):
    ax.text(v + 0.8, b.get_y() + b.get_height()/2, f"${v}B", va="center", fontsize=14, color=INK)
ax.set_xlim(0, 56); ax.invert_yaxis()
strip(ax, keep=()); ax.set_xticks([]); ax.tick_params(left=False, labelsize=11)
ax.set_title("Venture funding into physical AI:\nsix months now outweigh three years", loc="left", fontsize=15, pad=14)
ax.text(0, -0.30, "Physical AI = robotics, AVs, aerospace, drones, industrial automation, sensors.  Source: Crunchbase News, Aug 2026",
        transform=ax.transAxes, fontsize=8.5, color=INK2)
save(fig, "2026-08-21-physical-ai-funding.png")

# ── 2 精度:20 倍差 ──
fig, ax = plt.subplots(figsize=(7.3, 4.0), dpi=200)
cats = ["Repeatability\n(return to a taught point)", "Path accuracy, ISO 9283\n(go where commanded)"]
vals = [0.025, 0.53]
bars = ax.barh(cats, vals, height=0.42, color=BLUE)
ax.set_xscale("log"); ax.set_xlim(0.01, 1.6); ax.set_ylim(1.55, -0.85)
for b, v in zip(bars, vals):
    ax.text(v * 1.12, b.get_y() + b.get_height()/2, f"{v} mm", va="center", fontsize=14, color=INK)
ax.axvline(0.3, color=ORANGE, lw=2.2, ls=(0, (4, 3)))
ax.text(0.315, -0.62, "deburring tolerance ±0.3 mm", color=ORANGE, fontsize=11, ha="left")
strip(ax, keep=("bottom",))
ax.set_xticks([0.01, 0.1, 1.0]); ax.set_xticklabels(["0.01 mm", "0.1 mm", "1 mm"], fontsize=10)
ax.tick_params(left=False, labelsize=11)
ax.set_title("Same robot, same datasheet: a 20× gap\n(ABB IRB 1200)", loc="left", fontsize=15, pad=12)
ax.text(0, -0.30, "End-to-end models command absolute poses — the 0.53 mm side. Taught trajectories replay — the 0.025 mm side.  Source: ABB IRB 1200 datasheet",
        transform=ax.transAxes, fontsize=8.5, color=INK2)
save(fig, "2026-08-21-precision-gap.png")

# ── 3 时间线:90 天四步棋 ──
fig, ax = plt.subplots(figsize=(7.6, 3.2), dpi=200)
events = [(3.18, "NVIDIA GTC", "GR00T N1.7 licensed;\n110 'robot brain' developers"),
          (4.20, "Siemens", "Eigen agent in TIA Portal:\nplan, execute, validate"),
          (5.15, "Rockwell", "AI-native engineering flow\ncommercial (Emulate3D loop)"),
          (6.23, "Beckhoff", "TwinCAT CoAgent:\nMCP client, model-agnostic")]
ax.hlines(0, 3.0, 7.0, color=INK2, lw=1.5)
for i, (x, who, what) in enumerate(events):
    up = i % 2 == 0
    ax.plot(x, 0, "o", ms=9, color=BLUE, zorder=3)
    ax.vlines(x, 0, 0.28 if up else -0.28, color=MUTED, lw=1)
    ytxt = 0.34 if up else -0.34
    ax.text(x, ytxt, who, ha="center", va="bottom" if up else "top", fontsize=12, color=INK)
    ax.text(x, ytxt + (0.16 if up else -0.16), what, ha="center", va="bottom" if up else "top", fontsize=8.5, color=INK2)
for m, lab in [(3, "Mar"), (4, "Apr"), (5, "May"), (6, "Jun"), (7, "Jul")]:
    ax.text(m, -0.95, lab + " 2026", ha="center", fontsize=9, color=INK2)
    ax.vlines(m, -0.04, 0.04, color=INK2, lw=1)
ax.set_xlim(2.8, 7.2); ax.set_ylim(-1.1, 1.15); ax.axis("off")
ax.set_title("One quarter, four moves: the controller side learns to be called", loc="left", fontsize=14.5, pad=10)
save(fig, "2026-08-21-agent-90days.png")

# ── 4 LLMflation ──
fig, ax = plt.subplots(figsize=(7.3, 4.2), dpi=200)
yrs, cost = [2021, 2022, 2023, 2024], [60, 6, 0.6, 0.06]
ax.plot(yrs, cost, color=BLUE, lw=2, marker="o", ms=8, zorder=3)
ax.set_yscale("log"); ax.set_ylim(0.02, 200)
ax.annotate("$60 / Mtok\nGPT-3 (davinci)", (2021, 60), textcoords="offset points", xytext=(12, 6), ha="left", fontsize=10.5, color=INK)
ax.annotate("$0.06 / Mtok\nLlama 3.2 3B", (2024, 0.06), textcoords="offset points", xytext=(-16, 36), ha="right", fontsize=10.5, color=INK)
ax.text(2022.5, 3.5, "÷10 every year", rotation=-38, fontsize=11.5, color=BLUE, ha="center")
ax.text(2023.55, 22, "GPT-4-class tier: ÷62\nsince Mar 2023", fontsize=9, color=INK2)
strip(ax); ax.set_xticks(yrs); ax.tick_params(labelsize=10.5)
ax.set_yticks([0.06, 0.6, 6, 60]); ax.set_yticklabels(["$0.06", "$0.60", "$6", "$60"])
ax.set_title("The price of constant-quality intelligence:\n÷1000 in three years", loc="left", fontsize=15, pad=12)
ax.text(0, -0.16, "Cost per million tokens at constant MMLU quality.  Source: a16z, 'Welcome to LLMflation', Nov 2024",
        transform=ax.transAxes, fontsize=8.5, color=INK2)
save(fig, "2026-08-21-llmflation.png")

# ── 5 论点地图:demo vs process ──
fig, ax = plt.subplots(figsize=(7.3, 5.4), dpi=200)
demos = [("Cup from cabinet", 1.3, 1.9), ("Fold laundry", 2.0, 1.1), ("Make coffee", 2.6, 2.1)]
indus = [("Palletizing", 3.0, 2.7), ("Machine tending", 4.4, 4.1), ("Welding", 6.4, 6.0),
         ("Deburring  ±0.3 mm", 7.4, 6.9), ("Precision assembly", 8.5, 8.3)]
ax.add_patch(Ellipse((2.0, 1.8), 3.6, 2.8, angle=15, color=MUTED, alpha=0.18, lw=0))
ax.add_patch(Ellipse((6.6, 6.4), 6.2, 4.4, angle=38, color=BLUE, alpha=0.10, lw=0))
ax.text(0.35, 3.7, "where humanoid demos sample", fontsize=9.5, color=INK2, style="italic")
ax.text(4.7, 8.9, "where manufacturing lives", fontsize=9.5, color=INK2, style="italic")
for lab, x, y in demos:
    ax.plot(x, y, "o", ms=9, color=MUTED, zorder=3)
    dy = 9 if lab == "Cup from cabinet" else -15
    ax.annotate(lab, (x, y), textcoords="offset points", xytext=(0, dy), ha="center", fontsize=9, color=INK2)
for lab, x, y in indus:
    ax.plot(x, y, "o", ms=9, color=BLUE, zorder=3)
    ax.annotate(lab, (x, y), textcoords="offset points", xytext=(0, 9), ha="center", fontsize=9.5, color=INK)
ax.plot(4.1, 1.6, "o", ms=9, color=BLUE, zorder=3)
ax.annotate("Inspection", (4.1, 1.6), textcoords="offset points", xytext=(0, 9), ha="center", fontsize=9.5, color=INK)
ax.text(3.5, 2.68, "← commoditized first", color=ORANGE, fontsize=9.5, ha="left", va="center")
ax.annotate("industrial AI's first beachhead:\ncheap to verify, nothing to crash", (4.1, 1.6), (5.6, 0.7),
            fontsize=9, color=ORANGE, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_xticks([]); ax.set_yticks([])
strip(ax, keep=("bottom", "left"))
ax.set_xlabel("Cost of failure  →   (redo it  →  crashed spindle, stopped line)", fontsize=10)
ax.set_ylabel("Cost of verification  →   (a glance  →  physical trial)", fontsize=10)
ax.set_title("Why humanoids are still looking for a cell", loc="left", fontsize=15, pad=12)
ax.text(0, -0.09, "Positions are qualitative — author's judgment, no units. Axes after the argument in 'The Submillimeter Trap of Embodied AI'.",
        transform=ax.transAxes, fontsize=8.5, color=INK2)
save(fig, "2026-08-21-demo-vs-process-map.png")
print("5 charts regenerated (sketch theme)")
