
from matplotlib import ticker

def despine(ax, sides=None):
    sides = sides or ['top', 'bottom', 'left', 'right']
    for side in sides:
        ax.spines[side].set_visible(False)

percentages = ticker.PercentFormatter(xmax=1, decimals=0)