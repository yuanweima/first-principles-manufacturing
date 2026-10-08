"""037 Engineering the Map 篇图表(手绘主题版)。
Chart 6 = T01 地图 + 拖动箭头:轴不是天定的——仿真/空跑把失败变可逆(向左拖),在线复检把验证变便宜(向下拖)。
底图打点与 make_033_charts.py Chart 5 完全一致(T01 档案);只新增箭头与去毛刺工位的"拖后位置"。
定性放置,无刻度,作者判断(Charts/README 诚实规则)。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpm_style
from fpm_style import BLUE, ORANGE, INK, INK2, MUTED, SURFACE, strip
fpm_style.apply()
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

OUT = os.path.dirname(os.path.abspath(__file__))
def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)

# ── 6 论点地图 v2:轴是可动的 ──
fig, ax = plt.subplots(figsize=(7.3, 5.4), dpi=200)
demos = [("Cup from cabinet", 1.3, 1.9), ("Fold laundry", 2.0, 1.1), ("Make coffee", 2.6, 2.1)]
indus = [("Palletizing", 3.0, 2.7), ("Machine tending", 4.4, 4.1), ("Welding", 6.4, 6.0),
         ("Precision assembly", 8.5, 8.3)]
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

# 去毛刺:原位(空心)→ 两步拖动后的位置(实心橙)
x0, y0 = 7.4, 6.9          # 原位,与 T01 一致
x1, y1 = 5.4, 6.9          # 第一步:失败可逆(向左)
x2, y2 = 5.4, 3.3          # 第二步:验证便宜(向下)
ax.plot(x0, y0, "o", ms=9, mfc=SURFACE, mec=BLUE, mew=1.6, zorder=3)
ax.annotate("Deburring ±0.3 mm\n(as taught today)", (x0, y0), textcoords="offset points", xytext=(10, -4), ha="left", va="center", fontsize=9, color=INK2)
ax.plot(x1, y1, "o", ms=7, mfc=SURFACE, mec=ORANGE, mew=1.4, zorder=3)
ax.plot(x2, y2, "o", ms=10, color=ORANGE, zorder=4)
ax.annotate("Deburring, engineered", (x2, y2), textcoords="offset points", xytext=(0, -16), ha="center", fontsize=9.5, color=ORANGE)

arrow_kw = dict(arrowstyle="-|>", color=ORANGE, lw=2.0, mutation_scale=16, shrinkA=6, shrinkB=6, zorder=5)
ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), **arrow_kw))
ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), **arrow_kw))
ax.text((x0 + x1) / 2, y0 + 0.3, "① make failure reversible\nsimulation · dry run · single-step", ha="center", va="bottom", fontsize=9, color=ORANGE)
ax.text(x1 + 0.25, (y1 + y2) / 2, "② make verification cheap\nin-line re-inspection · replay", ha="left", va="center", fontsize=9, color=ORANGE)

ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_xticks([]); ax.set_yticks([])
strip(ax, keep=("bottom", "left"))
ax.set_xlabel("Cost of failure  →   (redo it  →  crashed spindle, stopped line)", fontsize=10)
ax.set_ylabel("Cost of verification  →   (a glance  →  physical trial)", fontsize=10)
ax.set_title("The axes are not fixed: drag the task, don't wait for the robot", loc="left", fontsize=14, pad=12)
ax.text(0, -0.09, "Positions are qualitative — author's judgment, no units. Base map from 'Is Manufacturing at Dusk or Dawn?' (T01); arrows added.",
        transform=ax.transAxes, fontsize=8.5, color=INK2)
save(fig, "2026-09-22-engineering-the-map.png")
print("chart 6 generated")
