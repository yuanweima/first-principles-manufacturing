"""FPM 图表手绘主题（2026-08-21 Yuanwei 拍板:全部图表用手绘主题,与 whiteboard hero 图统一笔触）。
数据永远由 matplotlib 计算;本模块只管风格。用法: import fpm_style; fpm_style.apply()"""
import matplotlib.pyplot as plt
import matplotlib as mpl

BLUE, ORANGE = "#2a78d6", "#eb6834"     # 已过 dataviz validator (CVD dE 24.7)
INK, INK2, MUTED = "#1a1a1a", "#52514e", "#a8a7a0"
SURFACE = "#fdfcf7"                      # 微暖白板色,贴 hero 图

def apply():
    plt.xkcd(scale=0.6, length=80, randomness=1.2)
    mpl.rcParams.update({
        "font.family": ["Chalkboard", "DejaVu Sans"],   # 缺字形(× →)逐字回退
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
        "text.color": INK, "axes.edgecolor": INK2, "axes.labelcolor": INK2,
        "xtick.color": INK2, "ytick.color": INK2,
        "path.sketch": (0.6, 80, 1.2), "svg.fonttype": "none"})

def strip(ax, keep=("bottom",)):
    for name, sp in ax.spines.items():
        sp.set_visible(name in keep)
