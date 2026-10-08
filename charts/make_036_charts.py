"""036《同一次产能转移，两本账》数据图 ×2。
主图: 年度货物贸易顺差(柱, 海关总署) vs 工业产能利用率(线, 统计局) —— 出口吸纳到顶、产线照样空转。
副图: 光伏组件价格 2022–2026 —— 价格战的一根线。
数据出处逐点注释在下方; ⚠️ 标记的点成文前须二次点核。
"""
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

# ── 1 主图: record exports, emptier factories ─────────────────────────
# 顺差 (USD bn, 海关总署年度; 全部经 2026-08-25 检索核实):
#   2021 676 (GACC via marketbeat/merics) / 2022 838 (CPA) / 2023 823 (CPA/statista)
#   2024 992 (GACC) / 2025 1190 (GACC 2026-01-14 发布, 新浪/腾讯)
SURPLUS = {2021: 676, 2022: 838, 2023: 823, 2024: 992, 2025: 1190}

# 产能利用率 (%, 统计局季度). ✓=检索核实; 其余出自 NBS 历史发布(训练知识, ⚠️成文前抽查):
#   2020Q1 67.3✓(历史最低) 2021Q2 78.4✓(历史最高) 2024Q1 73.6✓ 2024Q3 75.1✓ 2024Q4 76.2✓
#   2025Q1 74.1✓ 2025Q2 74.0✓ 2025Q3 74.6✓ 2025Q4 74.9✓ 2026Q1 73.6✓ 2026Q2 73.0✓(六年新低)
# 2026-08-27 抽查(stats.gov.cn 原发布逐条对上): 2019Q4 77.5✓ 2022Q4 75.7✓ 2023Q3 75.6✓
#   2023Q4 75.9✓ 2024Q2 74.9✓ —— 抽查 5 点全过, ⚠️ 解除。
UTIL = [  # (year.quarter-as-decimal, %)
    (2019.00, 75.9), (2019.25, 76.4), (2019.50, 76.4), (2019.75, 77.5),   # ⚠️
    (2020.00, 67.3), (2020.25, 74.4), (2020.50, 76.7), (2020.75, 78.0),   # Q1✓ 其余⚠️
    (2021.00, 77.2), (2021.25, 78.4), (2021.50, 77.1), (2021.75, 77.4),   # Q2✓ 其余⚠️
    (2022.00, 75.8), (2022.25, 75.1), (2022.50, 75.6), (2022.75, 75.7),   # ⚠️
    (2023.00, 74.3), (2023.25, 74.5), (2023.50, 75.6), (2023.75, 75.9),   # ⚠️
    (2024.00, 73.6), (2024.25, 74.9), (2024.50, 75.1), (2024.75, 76.2),   # Q1✓Q3✓Q4✓ Q2⚠️
    (2025.00, 74.1), (2025.25, 74.0), (2025.50, 74.6), (2025.75, 74.9),   # 全✓
    (2026.00, 73.6), (2026.25, 73.0),                                     # 全✓
]

fig, ax = plt.subplots(figsize=(8.2, 5.6), dpi=200)
axr = ax.twinx()

# bars: surplus (right axis) — bar centered on year midpoint
yrs = sorted(SURPLUS)
axr.bar([y + 0.375 for y in yrs], [SURPLUS[y] for y in yrs],
        width=0.62, color=ORANGE, alpha=0.32, edgecolor=ORANGE, lw=1.4, zorder=1)
for y in yrs:
    lab = "$1.19T — all-time record,\nany country, ever" if y == 2025 else f"${SURPLUS[y]}B"
    axr.text(y + 0.375, SURPLUS[y] + 28, lab, ha="center", va="bottom",
             fontsize=8.6 if y != 2025 else 9.0, color=ORANGE,
             fontweight="normal" if y != 2025 else "bold")
axr.set_ylim(0, 2300)
axr.set_yticks([])
for sp in axr.spines.values():
    sp.set_visible(False)

# line: utilization (left axis)
ux = [p[0] + 0.125 for p in UTIL]   # center of quarter
uy = [p[1] for p in UTIL]
ax.plot(ux, uy, color=BLUE, lw=2.2, zorder=3)
ax.set_ylim(64, 80)
ax.set_yticks([67.3, 70, 73, 76.4, 78.4])
ax.set_yticklabels(["67.3", "70", "73", "76.4", "78.4"], fontsize=8.5)

# annotations
ax.annotate("78.4% — post-COVID peak\n(2021 Q2)", xy=(2021.375, 78.4), xytext=(2019.3, 79.6),
            fontsize=8.8, color=INK2, arrowprops=dict(arrowstyle="-", color=INK2, lw=1.0))
ax.annotate("67.3%\nCOVID shutdowns", xy=(2020.125, 67.3), xytext=(2020.5, 65.4),
            fontsize=8.8, color=INK2, arrowprops=dict(arrowstyle="-", color=INK2, lw=1.0))
ax.annotate("73.0% — six-year low\n(2026 Q2)", xy=(2026.375, 73.0), xytext=(2025.1, 68.9),
            fontsize=9.2, color=BLUE, fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.4))
ax.text(2019.1, 71.0, "capacity utilization\n(line, left)", fontsize=9.4, color=BLUE)
ax.text(2021.05, 71.6, "goods trade surplus\n(bars)", fontsize=9.4, color=ORANGE,
        transform=ax.transData)

ax.set_xlim(2018.9, 2026.9)
ax.set_xticks([y + 0.5 for y in range(2019, 2027)])
ax.set_xticklabels([str(y) for y in range(2019, 2027)], fontsize=9)
strip(ax, keep=("bottom", "left"))
ax.set_ylabel("industrial capacity utilization (%)", fontsize=9.5)
ax.set_title("Record exports, emptier factories", loc="left", fontsize=15, pad=12)
ax.text(0, -0.115,
        "Utilization: NBS quarterly, national industrial enterprises. Surplus: GACC annual, goods trade, USD.\n"
        "The world already buys more from China than from any country in history — and one production line in four still sits idle.",
        transform=ax.transAxes, fontsize=8, color=INK2, va="top")
save(fig, "2026-08-25-record-exports-emptier-factories.png")

# ── 2 副图: the price war in one line (solar modules) ─────────────────
# 逐点出处 (元/W, 2026-08-25 检索核实):
#   2022-02 1.83 / 2022-07 2.02(峰) / 2022-12 1.90  — 知乎 2022 组件招标年度盘点
#   2023-02 1.80                                     — mysteel 2023 组件价格页
#   2024-01 0.93                                     — 报告大厅/低碳网 (2024-01-24 主流均价)
#   2024-12 0.60                                     — 报告大厅 "2024 年末跌破 0.6"; CPIA 同月最低成本 0.692 → 市场价低于行业成本线
#   2025-03 0.75                                     — 低碳网 (抢装潮反弹至 0.7–0.8 区间)
#   2026-07 0.69                                     — 腾讯新闻 (TOPCon 击穿 0.7; N 型集采 0.685)
PV = [(2022 + 1/12, 1.83), (2022 + 6/12, 2.02), (2022 + 11/12, 1.90),
      (2023 + 1/12, 1.80), (2024 + 0/12, 0.93), (2024 + 11/12, 0.60),
      (2025 + 2/12, 0.75), (2026 + 6/12, 0.69)]

fig, ax = plt.subplots(figsize=(7.6, 4.8), dpi=200)
px = [p[0] for p in PV]; py = [p[1] for p in PV]
ax.plot(px, py, color=BLUE, lw=2.4, zorder=3, marker="o", ms=6)

# CPIA minimum-cost reference (Dec 2024, 0.692 yuan/W incl. minimum necessary fees)
ax.axhline(0.692, color=ORANGE, lw=1.4, ls=(0, (5, 4)), zorder=2)
ax.text(2022.05, 0.73, "industry minimum cost, CPIA (Dec 2024): 0.69", fontsize=8.6, color=ORANGE)

ax.annotate("2.02 — peak\n(Jul 2022)", xy=(2022.5, 2.02), xytext=(2022.85, 2.02),
            fontsize=9, color=INK2, va="center",
            arrowprops=dict(arrowstyle="-", color=INK2, lw=1.0))
ax.annotate("0.60 — below the\ncost line (Dec 2024)", xy=(2024.917, 0.60), xytext=(2023.6, 0.28),
            fontsize=9, color=INK2, arrowprops=dict(arrowstyle="-", color=INK2, lw=1.0))
# 亏损口径 2026-08-27 核定(一财 2026-07-25): 21 家已披露预告合计预亏 130–168 亿;
# 隆基/通威/TCL中环三家合计超百亿。原"8 of 9 leaders"无出处, 已替换。
ax.annotate("0.69 (Jul 2026): 21 listed PV firms\nforecast ¥13–17B in H1 losses —\nand capacity still isn't exiting", xy=(2026.5, 0.64),
            xytext=(2025.35, 0.22), fontsize=9.2, color=BLUE, fontweight="bold", ha="left",
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.4))
ax.annotate("brief rebound: installation rush\nahead of a subsidy-policy deadline", xy=(2025.167, 0.78),
            xytext=(2023.9, 1.35), fontsize=8.4, color=INK2,
            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.9))

ax.text(2023.15, 2.12, "“Economics textbooks say: price below cost,\n  firms exit, market clears.”", fontsize=9.2,
        color=INK2, style="italic")

ax.set_xlim(2021.95, 2026.95); ax.set_ylim(0, 2.35)
ax.set_xticks([2022.5, 2023.5, 2024.5, 2025.5, 2026.5])
ax.set_xticklabels(["2022", "2023", "2024", "2025", "2026"], fontsize=9)
ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
ax.set_yticklabels(["0", "0.5", "1.0", "1.5", "2.0 ¥/W"], fontsize=8.5)
strip(ax, keep=("bottom", "left"))
ax.set_title("The price war, in one line: solar modules", loc="left", fontsize=15, pad=12)
ax.text(0, -0.13,
        "Mainstream module price, yuan per watt. Points: 2022 bid-price yearbook; Mysteel; CPIA cost floors; 2026 trade press. −66% in four years.",
        transform=ax.transAxes, fontsize=8, color=INK2, va="top")
save(fig, "2026-08-25-pv-price-war.png")

# ── 3 PPI 温度计: 41 个月零下 + 2026 转正 ────────────────────────────
# 逐点出处 (同比 %, 全部 2026-08-27 检索核实, 统计局原发布/解读或多源财经报道):
#   2021-10 +13.5(本轮峰值) / 2022-10 -1.3(转负首月, 澎湃引统计局) / 2023-06 -5.4(本轮低点)
#   2024-12 -2.3(统计局) / 2025-06 -3.6 / 2025-07 -3.6(统计局解读) / 2025-12 -1.9(统计局)
#   2026-03 +0.5(连负 41 个月后首次转正, 统计局/ChemNet) / 2026-06 +4.1(由 7 月解读回推) / 2026-07 +3.5(统计局)
PPI = [(2021 + 9/12, 13.5), (2022 + 9/12, -1.3), (2023 + 5/12, -5.4),
       (2024 + 11/12, -2.3), (2025 + 5/12, -3.6), (2025 + 6/12, -3.6),
       (2025 + 11/12, -1.9), (2026 + 2/12, 0.5), (2026 + 5/12, 4.1), (2026 + 6/12, 3.5)]

fig, ax = plt.subplots(figsize=(8.2, 5.2), dpi=200)
ax.axhline(0, color=INK2, lw=1.2)
ax.axvspan(2022 + 9/12, 2026 + 2/12, color=ORANGE, alpha=0.10, zorder=0)
ax.plot([p[0] for p in PPI], [p[1] for p in PPI], color=BLUE, lw=2.4, marker="o", ms=5.5, zorder=3)

ax.annotate("+13.5% — post-COVID commodity peak\n(Oct 2021)", xy=(2021.75, 13.5), xytext=(2022.4, 13.2),
            fontsize=8.8, color=INK2, va="center",
            arrowprops=dict(arrowstyle="-", color=INK2, lw=1.0))
ax.annotate("−5.4% (Jun 2023)", xy=(2023 + 5/12, -5.4), xytext=(2023.0, -8.2),
            fontsize=8.8, color=INK2, arrowprops=dict(arrowstyle="-", color=INK2, lw=1.0))
ax.text(2024.55, -10.6, "41 months below zero\n(Oct 2022 – Feb 2026)", fontsize=9.6,
        color=ORANGE, ha="center", fontweight="bold")
ax.annotate("Mar 2026: first positive print\nin 41 months", xy=(2026 + 2/12, 0.5), xytext=(2024.75, 4.6),
            fontsize=9.0, color=INK2, arrowprops=dict(arrowstyle="-", color=INK2, lw=1.0))
ax.annotate("+3.5% (Jul 2026) — while capacity\nutilization sits at a six-year low", xy=(2026.5, 3.5),
            xytext=(2025.4, 9.2), fontsize=9.2, color=BLUE, fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.4))

ax.set_xlim(2021.5, 2026.95); ax.set_ylim(-12.5, 16.5)
ax.set_xticks([y + 0.5 for y in range(2022, 2027)])
ax.set_xticklabels([str(y) for y in range(2022, 2027)], fontsize=9)
ax.set_yticks([-5.4, 0, 5, 13.5])
ax.set_yticklabels(["−5.4", "0", "+5", "+13.5%"], fontsize=8.5)
strip(ax, keep=("bottom", "left"))
ax.set_title("The price thermometer: 41 months below zero", loc="left", fontsize=15, pad=12)
ax.text(0, -0.125,
        "Producer Price Index, year-over-year, NBS monthly releases. Line connects verified monthly prints only.\n"
        "The 2026 rebound: NBS attributes it to imported input costs and improved supply–demand in some industries — not to full factories.",
        transform=ax.transAxes, fontsize=8, color=INK2, va="top")
save(fig, "2026-08-27-ppi-thermometer.png")

# ── 4 两条推导链条 (示意图, 无数据) ───────────────────────────────────
fig, ax = plt.subplots(figsize=(8.6, 6.6), dpi=200)
ax.axis("off")

def chain(x, color, title, steps, ys):
    ax.text(x, 0.965, title, ha="center", fontsize=12.5, color=color, fontweight="bold",
            transform=ax.transAxes)
    for (s, y) in zip(steps, ys):
        ax.text(x, y, s, ha="center", va="center", fontsize=9.0, color=INK,
                transform=ax.transAxes,
                bbox=dict(boxstyle="round,pad=0.42", fc=SURFACE, ec=color, lw=1.6))
    for y1, y2 in zip(ys, ys[1:]):
        ax.annotate("", xy=(x, y2 + 0.042), xytext=(x, y1 - 0.042),
                    xycoords=ax.transAxes, textcoords=ax.transAxes,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=1.5))

L = ["price falls below cost", "rational firms cut losses, exit", "supply contracts",
     "price recovers", "market clears"]
chain(0.24, BLUE, "The neoclassical chain", L, [0.865, 0.72, 0.575, 0.43, 0.285])
ax.text(0.24, 0.155, "blind spot: jobs politics, the option value\nof outliving rivals, near-zero salvage on exit —\nso losses don't force exit", ha="center", va="center",
        fontsize=8.2, color=INK2, style="italic", transform=ax.transAxes)

R = ["capital accumulates faster than wages", "home demand can't absorb output",
     "surplus exits through exports", "exports hit tariffs and ceilings",
     "price war turns inward", "profits and wages both fall"]
chain(0.735, ORANGE, "The political-economy chain", R, [0.865, 0.75, 0.635, 0.52, 0.405, 0.29])
# loop back: falling wages feed the demand gap
ax.annotate("", xy=(0.955, 0.75), xytext=(0.955, 0.29),
            xycoords=ax.transAxes, textcoords=ax.transAxes,
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.3,
                            connectionstyle="arc3,rad=-0.35"))
ax.text(0.985, 0.52, "the loop closes", rotation=90, ha="center", va="center",
        fontsize=8.2, color=ORANGE, style="italic", transform=ax.transAxes)
ax.text(0.735, 0.155, "blind spot: the hard edge of cash flow —\nprice discipline arrives in the end,\nby market or by mandate", ha="center", va="center",
        fontsize=8.2, color=INK2, style="italic", transform=ax.transAxes)

ax.text(0.5, 0.04, "Same price war, two inference chains — each predicts what the other can't see.",
        ha="center", fontsize=9.6, color=INK, transform=ax.transAxes, fontweight="bold")
ax.set_title("Two chains, one price war", loc="left", fontsize=15, pad=10)
ax.text(0, -0.015, "Schematic — no data. Author's compression of each framework's canonical inference chain.",
        transform=ax.transAxes, fontsize=8, color=INK2, va="top")
save(fig, "2026-08-27-two-chains.png")

print("done: 4 charts")
