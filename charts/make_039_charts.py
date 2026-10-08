"""Idea 039「摊销还是推迟」三张论点图。

诚实规则(Charts/README):三张全部是**预测的形状**,不是实测数据。
因此一律裸轴(无刻度值),图注标 "qualitative — author's prediction"。
一旦 P1/P2 被真实实验测出来,应另画数据图,不要往这三张上填数。

用法: python3 make_039_charts.py
"""
import numpy as np
import matplotlib.pyplot as plt
import fpm_style
from fpm_style import BLUE, ORANGE, INK, INK2, MUTED

fpm_style.apply()

OUT = "."
NOTE = "qualitative — author's prediction, not measured data"


def finish(fig, ax_list, fname):
    for ax in ax_list:
        ax.set_xticks([])
        ax.set_yticks([])
    fig.savefig(f"{OUT}/{fname}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("wrote", fname)


# ---------------------------------------------------------------- Fig 1
# 摊销 vs 推迟:各有一条指数轴 —— 全文的核心重构
def fig_two_exponentials():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.6))
    x = np.linspace(0, 1, 200)

    # 左:摊销 —— 代价随「要覆盖的约束族数」指数上升,与状态维数无关
    a1.plot(x, np.exp(3.2 * x) - 1, color=ORANGE, lw=3)
    a1.set_title("AMORTIZE — bake the decision into parameters",
                 fontsize=12.5, color=INK, pad=10)
    a1.set_xlabel("number of task / constraint families to cover", fontsize=11)
    a1.set_ylabel("cost", fontsize=11)
    a1.text(0.50, 9.5, "exponential\nin coverage", color=ORANGE, fontsize=12)
    a1.text(0.04, 3.2, "but the query itself\nstays O(1) — the state\ndimension never bites",
            color=INK2, fontsize=9.5)
    a1.text(0.04, 20.3, "failure mode: SILENT\n(the policy has no idea it left\nthe distribution)",
            color=INK2, fontsize=9.5)

    # 右:推迟 —— 代价随「不确定性的分支」指数上升,对维数只是多项式
    a2.plot(x, 1.5 * x ** 3 * 6, color=BLUE, lw=3)
    a2.plot(x, np.exp(3.2 * x) - 1, color=BLUE, lw=3, ls=":")
    a2.set_title("DEFER — solve it at deployment time",
                 fontsize=12.5, color=INK, pad=10)
    a2.set_xlabel("horizon & dimension  (solid)   ·   uncertainty branching  (dotted)",
                  fontsize=11)
    a2.text(0.62, 2.0, "polynomial\nin dimension", color=BLUE, fontsize=12)
    a2.text(0.16, 13.0, "exponential\nin branching", color=BLUE, fontsize=12)
    a2.text(0.04, 20.3, "failure mode: EXPLICIT\n(infeasible / no convergence —\nit tells you)",
            color=INK2, fontsize=9.5)

    for ax in (a1, a2):
        ax.set_ylim(-1, 24)
        fpm_style.strip(ax, keep=("bottom", "left"))

    fig.suptitle("Each side has its own exponential — which is why the architecture is hybrid",
                 fontsize=15, color=INK, y=1.13)
    fig.text(0.5, -0.06,
             "Argue from only one axis and you get a one-sided answer: count dimensions alone and planning "
             "looks unbeatable;\ncount closed-loop reaction time alone and policy does.  " + NOTE,
             ha="center", fontsize=9, color=MUTED)
    finish(fig, [a1, a2], "2026-09-09-amortize-vs-defer.png")


# ---------------------------------------------------------------- Fig 2
# P1:约束新颖性曲线
def fig_p1():
    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    x = np.linspace(0, 1, 200)

    ax.plot(x, 0.06 + 0.80 / (1 + np.exp(-7 * (x - 0.5))), color=ORANGE, lw=3,
            label="pure policy")
    ax.plot(x, 0.10 + 0.05 * x, color=BLUE, lw=3, label="hybrid (policy + online solve)")

    ax.annotate("", xy=(0.93, 0.155), xytext=(0.93, 0.0),
                arrowprops=dict(arrowstyle="<->", color=INK2, lw=1.4))
    ax.text(0.60, 0.185, "ceiling set by warm-start quality\n× solver completeness",
            color=INK2, fontsize=9.5)

    ax.text(0.05, 0.80, "policy fails silently as the\nconstraint geometry drifts\nout of its training set",
            color=ORANGE, fontsize=10.5)
    ax.text(0.04, 0.30, "the planner takes the constraint as INPUT\n— covering it costs nothing",
            color=BLUE, fontsize=10.5)

    ax.set_xlabel("constraint novelty  →  how far this obstacle / fixture geometry sits from anything in training",
                  fontsize=11)
    ax.set_ylabel("failure rate", fontsize=11)
    ax.set_title("P1 — hold in-distribution success fixed, then walk the constraints away",
                 fontsize=14, color=INK, pad=14)
    ax.set_xlim(0, 1.0)
    ax.set_ylim(0, 1.0)
    ax.legend(loc="upper left", bbox_to_anchor=(0.015, 0.60), frameon=False, fontsize=11)
    fpm_style.strip(ax, keep=("bottom", "left"))
    fig.text(0.5, -0.04, "Testable on systems that exist today.  " + NOTE,
             ha="center", fontsize=9, color=MUTED)
    finish(fig, [ax], "2026-09-09-p1-constraint-novelty.png")


# ---------------------------------------------------------------- Fig 3
# P2:延迟交叉点
def fig_p2():
    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    x = np.linspace(-1.4, 1.4, 300)          # log10(required reaction time / solve time)

    policy = 0.72 + 0 * x
    hybrid = 0.72 + 0.24 / (1 + np.exp(-9.0 * (x - 0.25)))

    ax.plot(x, policy, color=ORANGE, lw=3, label="pure policy")
    ax.plot(x, hybrid, color=BLUE, lw=3, label="hybrid")

    ax.axvline(0, color=INK2, lw=1.6, ls="--")
    ax.text(0.03, 0.60, "crossing point:\nrequired reaction time\n= solve time",
            color=INK2, fontsize=10)

    ax.text(-1.32, 0.90, "no time to solve\n→ hybrid ≈ policy\n(everything must be amortized)",
            color=INK2, fontsize=10)
    ax.text(0.52, 0.79, "time to solve\n→ hybrid ≫ policy",
            color=BLUE, fontsize=10.5)
    ax.annotate("", xy=(-0.62, 0.545), xytext=(0.30, 0.545),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=2))
    ax.text(-0.62, 0.555, "cheaper inference drags the crossing this way",
            color=ORANGE, fontsize=10)

    ax.set_xlabel("required reaction time  /  solve time      (log scale)", fontsize=11)
    ax.set_ylabel("task success", fontsize=11)
    ax.set_title("P2 — the crossing point is measurable, and it moves as inference gets cheaper",
                 fontsize=14, color=INK, pad=14)
    ax.set_ylim(0.5, 1.02)
    ax.legend(loc="lower right", frameon=False, fontsize=11)
    fpm_style.strip(ax, keep=("bottom", "left"))
    fig.text(0.5, -0.04,
             "Falling inference cost drags this line leftward — that is the whole bet on deferred computation.  "
             + NOTE, ha="center", fontsize=9, color=MUTED)
    finish(fig, [ax], "2026-09-09-p2-latency-crossover.png")


if __name__ == "__main__":
    fig_two_exponentials()
    fig_p1()
    fig_p2()
