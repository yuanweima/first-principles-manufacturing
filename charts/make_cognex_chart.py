"""Cognex × RealSense 简评示意图:谁拥有哪一层(无数据示意,手绘主题)。
事实出处见 Drafts/2026-09-23-cognex-realsense-zh.md 文件头 %%C%% ①。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpm_style
from fpm_style import BLUE, ORANGE, INK, INK2, MUTED, SURFACE
fpm_style.apply()
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = os.path.dirname(os.path.abspath(__file__))

fig, ax = plt.subplots(figsize=(7.6, 5.2), dpi=200)
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")

# (y, layer, who, owner note, style)
layers = [
    (7.9, "The line", "GM, Stellantis, Ford, Toyota ...", "the manufacturer", "plain"),
    (5.9, "Robot + controller", "FANUC, UR, ABB, KUKA, Yaskawa, Comau", "robot makers sell it in", "plain"),
    (3.9, "Guidance software", "Inbolt", "the only layer the startup builds", "own"),
    (1.9, "3D camera", "RealSense D435  ($314 list)", "independent since 2025", "moving"),
]
for y, layer, who, note, style in layers:
    edge = {"plain": INK2, "own": BLUE, "moving": ORANGE}[style]
    lw = 2.6 if style != "plain" else 1.5
    ax.add_patch(FancyBboxPatch((0.3, y), 6.0, 1.35, boxstyle="round,pad=0.05,rounding_size=0.15",
                                fc=SURFACE, ec=edge, lw=lw))
    ax.text(0.6, y + 0.88, layer, fontsize=13, color=INK, va="center")
    ax.text(0.6, y + 0.40, who, fontsize=10, color=INK2, va="center")
    ax.text(6.6, y + 0.67, note, fontsize=10, color=edge if style != "plain" else INK2, va="center")

# 9/22 标注
ax.annotate("Sept 22: Cognex agrees to\nbuy RealSense, ~$500M cash\n(close expected Q4 2026)",
            xy=(6.35, 2.3), xytext=(6.6, 0.15), fontsize=10, color=ORANGE, va="bottom",
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.6))

ax.set_title("The startup builds one layer.\nThe layer under it just got a buyer.", loc="left", fontsize=15, pad=6)
fig.text(0.02, -0.01,
         "Sources: Cognex 8-K Ex. 99.1 (Sept 22, 2026); Inbolt, UR, FANUC and RealSense releases; RealSense store price, Sept 23, 2026.\n"
         "Inbolt says its software works with any standard 3D camera; the D435 is the camera in its public Hannover Messe 2026 demo.",
         fontsize=7.5, color=INK2)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "2026-09-23-who-owns-which-layer.png"), bbox_inches="tight", facecolor=SURFACE)
