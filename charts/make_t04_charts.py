"""T04 自动化率 vs 变体×柔性(跨行业论点图) + IFR 密度定量副图。
依据: Charts/T04-automation-vs-variety.md + Research/2026-08-25-automation-vs-variety-evidence.md"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpm_style
from fpm_style import BLUE, ORANGE, INK, INK2, MUTED, SURFACE, strip
fpm_style.apply()
import matplotlib.pyplot as plt

OUT = os.path.dirname(os.path.abspath(__file__))
def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)

# ── 1 论点主图: automation vs variety x compliance (qualitative) ──
fig, ax = plt.subplots(figsize=(7.6, 6.0), dpi=200)

# the frontier: unmoved for 60 years
import numpy as np
fx = np.linspace(0.5, 9.8, 100)
fy = 10.4 - 1.0 * fx
ax.plot(fx, fy, ls=(0, (5, 4)), color=MUTED, lw=1.6, zorder=1)
ax.text(3.3, 4.62, "the frontier —\nbarely moved in 60 years",
        fontsize=9, color=INK2, ha="left", style="italic")

pts_hi = [  # machines' corner
    ("Wafer fab (AMHS)",   0.75, 9.15, (0, 9), "center"),
    ("Beverage canning",   2.4, 9.5, (8, 4), "left"),
    ("SMT placement",      3.3, 8.9, (8, 5), "left"),
    ("Injection molding",  1.35, 8.35, (0, -16), "center"),
    ("Auto stamping",      2.5, 8.45, (10, -4), "left"),
    ("Auto body-in-white", 3.6, 7.6, (9, 4), "left"),
    ("Auto paint",         4.4, 6.6, (9, 4), "left"),
    ("Ship panel line",    5.2, 5.4, (9, 4), "left"),
]
pts_lo = [  # hands' corner
    ("Ship outfitting",        6.35, 3.5, (0, 9), "center"),
    ("Aircraft fuselage",      8.35, 2.75, (-6, 7), "right"),
    ("Auto final assembly",    7.0, 2.1, (-8, 5), "right"),
    ("Phone final assembly",   7.7, 1.75, (-12, -14), "center"),
    ("Poultry deboning",       8.75, 1.35, (8, 4), "left"),
    ("Wire-harness install",   9.15, 0.9, (-8, -6), "right"),
    ("Garment sewing",         9.8, 0.45, (0, -15), "center"),
]
for lab, x, y, off, ha in pts_hi:
    ax.plot(x, y, "o", ms=8, color=BLUE, zorder=3)
    ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha=ha, fontsize=8.8, color=INK)
for lab, x, y, off, ha in pts_lo:
    ax.plot(x, y, "o", ms=8, color=INK2, zorder=3)
    ax.annotate(lab, (x, y), textcoords="offset points", xytext=off, ha=ha, fontsize=8.8, color=INK)

# zone labels
ax.text(0.4, 10.35, "robots ate this corner — decades ago", fontsize=10, color=INK2, style="italic")
ax.text(9.9, -0.75, "hands kept this corner", fontsize=10, color=INK2, style="italic", ha="right")

# factual anchors (orange)
ax.annotate("<5% robotic (ABB);\n“90% manual” (VW)", (6.85, 1.95), (5.0, 0.75),
            fontsize=8.6, color=ORANGE, ha="center",
            arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.1))
ax.annotate("Boeing 777: riveting robots\nretreated to drilling, 2019", (8.5, 3.0), (9.9, 4.75),
            fontsize=8.6, color=ORANGE, ha="right",
            arrowprops=dict(arrowstyle="-", color=ORANGE, lw=1.1))

# the thesis: agents enter the coordination layer on BOTH sides
ax.annotate("", xy=(2.6, 7.2), xytext=(1.15, 4.75),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.0))
ax.annotate("", xy=(6.1, 2.6), xytext=(1.7, 4.28),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.0))
ax.text(0.35, 4.45, "AI agents enter the\ncoordination layer —\non both sides", fontsize=9.6, color=ORANGE, va="center")
ax.text(0.35, 3.28, "machines' side: scheduling,\nparameters, yield loops\nhands' side: guidance,\nverification, traceability", fontsize=8.2, color=INK2, va="top")

ax.set_xlim(0, 10.4); ax.set_ylim(-1.1, 10.9); ax.set_xticks([]); ax.set_yticks([])
strip(ax, keep=("bottom", "left"))
ax.set_xlabel("Product variety × compliant parts  →   (one geometry forever  →  every piece different & floppy)", fontsize=9.5)
ax.set_ylabel("Degree of automation  →", fontsize=10)
ax.set_title("Automation follows task parameters, not how advanced the industry is", loc="left", fontsize=14, pad=12)
ax.text(0, -0.075, "Positions are qualitative — author's judgment, no units. Anchors cite public data (see article). Frame after Hayes & Wheelwright, HBR 1979.",
        transform=ax.transAxes, fontsize=8, color=INK2)
save(fig, "2026-08-25-automation-vs-variety.png")

# ── 2 定量副图: IFR robot density ──
fig, ax = plt.subplots(figsize=(7.3, 4.4), dpi=200)
rows = [("Korea — automotive", 2867, BLUE),
        ("Germany — automotive", 1500, BLUE),
        ("United States — automotive", 1457, BLUE),
        ("Japan — automotive", 1422, BLUE),
        ("China — automotive", 772, BLUE),
        ("All manufacturing,\nglobal average", 162, MUTED)]
labs = [r[0] for r in rows]; vals = [r[1] for r in rows]; cols = [r[2] for r in rows]
bars = ax.barh(labs, vals, height=0.55, color=cols)
for b, v in zip(bars, vals):
    ax.text(v + 40, b.get_y() + b.get_height()/2, f"{v:,}", va="center", fontsize=12, color=INK)
ax.set_xlim(0, 3350); ax.invert_yaxis()
strip(ax, keep=()); ax.set_xticks([]); ax.tick_params(left=False, labelsize=10)
ax.set_title("Robots per 10,000 employees: the car industry runs\n~9–10× the manufacturing average", loc="left", fontsize=14.5, pad=12)
ax.text(0, -0.155, "Automotive: IFR, 2021 stock. Global manufacturing average: IFR, 2023 (162). Same-country check — Poland: automotive 247 vs 62 elsewhere.",
        transform=ax.transAxes, fontsize=8, color=INK2)
save(fig, "2026-08-25-ifr-density.png")
print("2 charts generated")
