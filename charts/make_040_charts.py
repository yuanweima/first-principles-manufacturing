"""040「封顶的被拉平，敞开的被拉开」篇图表(手绘主题)。
Chart 1 = 事件时间线(数据:日期全部有出处,见图注与 Research/2026-09-26-040-ai-math-frontier-sources.md)
Chart 2 = 客服研究三档增益(数据:Brynjolfsson, Li & Raymond, QJE 2025,摘要级数字)
Chart 3 = T07 论点图:终点是否事先定义 × 裁判一次多少钱(定性,裸轴,作者判断;档案 Charts/T07)
运行:/usr/bin/python3 Assets/charts/make_040_charts.py(本机该解释器带 matplotlib)"""
import sys, os
from datetime import datetime as dt, timedelta
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpm_style
from fpm_style import BLUE, ORANGE, INK, INK2, MUTED, SURFACE, strip
fpm_style.apply()
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Ellipse, FancyArrowPatch

OUT = os.path.dirname(os.path.abspath(__file__))
def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)

# ── 1 时间线:八月中到九月中,四条泳道 ──
fig, ax = plt.subplots(figsize=(8.8, 4.9), dpi=200)
lanes = {"Mathematicians": 0, "Anthropic": 1, "Buckmaster & Alpöge": 2, "OpenAI": 3}
def d(m, day, h=0): return dt(2026, m, day, h)
def dot(lane, when, label, color, dy=10, ha="center", side=False):
    y = lanes[lane]
    ax.plot(when, y, "o", ms=8, color=color, zorder=4)
    if side:   # 标签放点右侧,避开 09-05–09-08 的拥挤区
        ax.annotate(label, (when, y), textcoords="offset points", xytext=(8, 0), ha="left",
                    va="center", fontsize=8.5, color=INK)
        return
    ax.annotate(label, (when, y), textcoords="offset points", xytext=(0, dy), ha=ha,
                va="bottom" if dy > 0 else "top", fontsize=8.5, color=INK)

# OpenAI:09-01 起跑 → ~88 h(09-05)→ Lean +17 h(09-06)→ 09-08 中午公布
start = d(9, 1, 8)                       # 起跑具体钟点未公开;取 09-01 白天,只为画段
t88 = start + timedelta(hours=88)
t105 = t88 + timedelta(hours=17)
ax.plot([start, t88], [3, 3], lw=7, color=BLUE, solid_capstyle="round", zorder=3)
ax.plot([t88, t105], [3, 3], lw=7, color=MUTED, solid_capstyle="round", zorder=3)
ax.annotate("~10,000 agents, ~88 h", (start + (t88 - start) / 2, 3), textcoords="offset points",
            xytext=(0, 9), ha="center", va="bottom", fontsize=8.5, color=INK)
ax.annotate("Lean check +17 h", (t88 + (t105 - t88) / 2, 3), textcoords="offset points", xytext=(0, -10),
            ha="center", va="top", fontsize=8, color=INK2)
dot("OpenAI", d(9, 8, 12), "announces\nSep 8, noon", BLUE, side=True)

dot("Buckmaster & Alpöge", d(8, 15), "forced-Euler result\n(forcing route)", ORANGE, dy=9)
dot("Buckmaster & Alpöge", d(8, 22), "Lean-verified", ORANGE, dy=-10)
dot("Buckmaster & Alpöge", d(9, 8, 0), "public statement\n~12 h earlier", ORANGE, side=True)

dot("Anthropic", d(8, 10), "ζ zeros on the line:\n41.6% → 67.2%", INK2, dy=9, ha="left")
dot("Anthropic", d(9, 4), "Fermat formalized in Lean:\n11 days (expected: years)", INK2, dy=9)

dot("Mathematicians", d(9, 11), "25 Fields Medalists:\n\"solving problems is only\na tool and proxy\"", INK2, dy=9, ha="right")

ax.set_yticks(list(lanes.values())); ax.set_yticklabels(list(lanes.keys()), fontsize=9.5)
ax.set_ylim(-0.6, 3.9)
ax.set_xlim(d(8, 7), d(9, 17))
ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=[1, 8, 15, 22]))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %-d"))
ax.tick_params(axis="y", length=0)
for y in lanes.values():
    ax.axhline(y, color=MUTED, lw=0.6, alpha=0.5, zorder=1)
strip(ax, keep=("bottom",))
ax.set_title("Five weeks in 2026: machines did the search, people chose where to aim", loc="left", fontsize=13, pad=12)
ax.text(0, -0.2, "Sources: Anthropic research posts (Aug 10, Sep 4); OpenAI announcement (Sep 8, updated Sep 10);\n"
        "Buckmaster–Alpöge dates via Wikipedia 'Navier–Stokes priority controversy'; declaration text on Terence Tao's blog (Sep 11). Run start hour not public.",
        transform=ax.transAxes, fontsize=7.5, color=INK2, va="top")
save(fig, "2026-09-26-ai-math-timeline.png")

# ── 2 客服研究:封顶的活上,AI 是加法 ──
fig, ax = plt.subplots(figsize=(6.4, 3.6), dpi=200)
rows = [("Most experienced /\nhighest-skilled", 0.6, "minimal"), ("All 5,179 agents\n(average)", 14, "+14%"),
        ("Novice /\nlow-skilled", 34, "+34%")]
for i, (lab, v, txt) in enumerate(rows):
    ax.barh(i, v, height=0.52, color=BLUE, zorder=3)   # 单系列单色;橙色在本篇专指"敞开"
    ax.text(v + 1, i, txt, va="center", ha="left", fontsize=11, color=INK)
ax.set_yticks(range(3)); ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
ax.set_xlim(0, 42); ax.set_xticks([0, 10, 20, 30, 40])
ax.set_xlabel("Productivity gain from a gen-AI assistant (issues resolved per hour)", fontsize=9.5)
ax.tick_params(axis="y", length=0)
strip(ax, keep=("bottom",))
ax.set_title("On capped work, AI is addition: the bottom moves most", loc="left", fontsize=13, pad=10)
ax.text(0, -0.3, "Source: Brynjolfsson, Li & Raymond, 'Generative AI at Work', QJE 140(2), 2025. 'Minimal' is the paper's word; bar drawn near zero.",
        transform=ax.transAxes, fontsize=7.5, color=INK2, va="top")
save(fig, "2026-09-26-capped-work-compression.png")

# ── 3 T07 论点图:封顶 vs 敞开 ──
fig, ax = plt.subplots(figsize=(7.4, 5.6), dpi=200)
ax.add_patch(Ellipse((2.0, 2.0), 4.6, 3.6, angle=20, color=BLUE, alpha=0.10, lw=0))
ax.add_patch(Ellipse((7.9, 7.8), 4.6, 3.8, angle=25, color=ORANGE, alpha=0.10, lw=0))
ax.text(0.25, 4.35, "CAPPED — AI adds, gaps compress", fontsize=9.5, color=BLUE, style="italic")
ax.text(5.1, 9.55, "OPEN — AI multiplies, gaps stretch", fontsize=9.5, color=ORANGE, style="italic")

capped = [("3D part pose\n(mm error)", 0.9, 0.8, (0, -22)),
          ("Support ticket", 2.9, 1.1, (0, 9)),
          ("Formalizing Fermat\n(Lean checks)", 0.8, 2.3, (0, 9)),
          ("Navier–Stokes,\nas Clay stated it", 2.4, 3.1, (0, 9)),
          ("School essay\n(rubric)", 3.9, 2.4, (0, -22))]
for lab, x, y, off in capped:
    ax.plot(x, y, "o", ms=9, color=BLUE, zorder=3)
    ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha="center", fontsize=8.5, color=INK)

between = [("Weld: is it sound inside?\n(NDT — slow, costly)", 3.6, 6.9, (0, 9))]
for lab, x, y, off in between:
    ax.plot(x, y, "o", ms=9, color=MUTED, zorder=3)
    ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha="center", fontsize=8.5, color=INK2)

open_ = [("Pick the problem\n& the route", 8.9, 8.8, (0, -26)),
         ("Why is it true?\n(understanding)", 9.0, 6.6, (0, -26)),
         ("Set the tolerance;\ndefine \"clean\"", 7.0, 7.7, (-4, 9))]
for lab, x, y, off in open_:
    ax.plot(x, y, "o", ms=9, color=ORANGE, zorder=3)
    ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha="center", fontsize=8.5, color=INK)

# 去毛刺:今天(空心)→ 造出裁判之后(实心蓝)
x0, y0, x1, y1 = 6.0, 5.6, 4.6, 2.2
ax.plot(x0, y0, "o", ms=9, mfc=SURFACE, mec=INK2, mew=1.6, zorder=3)
ax.annotate("Deburring: \"clean?\"\n(a veteran's glove)", (x0, y0), textcoords="offset points", xytext=(10, 0),
            ha="left", va="center", fontsize=8.5, color=INK2)
ax.plot(x1, y1, "o", ms=9, color=BLUE, zorder=4)
ax.annotate("…with an independent\ncamera re-check", (x1, y1), textcoords="offset points", xytext=(10, -2),
            ha="left", va="center", fontsize=8.5, color=INK)
ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", color=INK, lw=1.8, mutation_scale=15,
                             shrinkA=7, shrinkB=7, connectionstyle="arc3,rad=0.15", zorder=5))
ax.text(5.55, 3.75, "build a judge →\ntask moves to the\ncapped side", ha="left", va="center", fontsize=8.5, color=INK)

ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_xticks([]); ax.set_yticks([])
strip(ax, keep=("bottom", "left"))
ax.set_xlabel("Is \"done\" defined in advance?  →   (fixed spec  →  you must define it)", fontsize=10)
ax.set_ylabel("Cost of one judgment  →   (a proof checker  →  a person who knows)", fontsize=10)
ax.set_title("Capped work gets flattened. Open work gets stretched.", loc="left", fontsize=14, pad=12)
ax.text(0, -0.09, "Positions are qualitative — author's judgment, no units.",
        transform=ax.transAxes, fontsize=8.5, color=INK2)
save(fig, "2026-09-26-capped-vs-open.png")
print("040 charts generated")
