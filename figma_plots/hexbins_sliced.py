#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
N = 1_000_000
grid_size = 25
classes = ['A', 'B', 'C']

xmin, xmax = -3, 3
ymin, ymax = -3, 3
extent = (xmin, xmax, ymin, ymax)

means = {
    'A': (0, 0),
    'B': (1.5, 1.5),
    'C': (-1.5, -1.5)
}

class_cmaps = {
    'A': 'Reds',
    'B': 'Greens',
    'C': 'Blues'
}

# Custom fade colormaps: red, green, blue fading to alpha 0
def make_fade_colormap(color, N=256):
    """
    Create a colormap that fades from the given color to transparent using numpy linspace for alpha.
    color: 'red', 'green', or 'blue'
    N: number of steps in the colormap
    """
    color_dict = {
        'red':   (1, 0, 0),
        'green': (0, 1, 0),
        'blue':  (0, 0, 1)
    }
    rgb = color_dict[color]
    alpha = np.linspace(0, 1, N)
    colors = np.zeros((N, 4))
    colors[:, 0] = rgb[0]
    colors[:, 1] = rgb[1]
    colors[:, 2] = rgb[2]
    colors[:, 3] = alpha
    return ListedColormap(colors, name=f"fade_{color}")

custom_cmaps = {
    'A': make_fade_colormap('red'),
    'B': make_fade_colormap('green'),
    'C': make_fade_colormap('blue')
}

fig = plt.figure(figsize=(8, 6), facecolor='none')
ax = fig.gca()
ax.set_facecolor('none')

# Custom colormap with alpha=0 for values under threshold
threshold = 10  # adjust as needed

for cls in classes:
    x = np.random.normal(means[cls][0], 1, N)
    y = np.random.normal(means[cls][1], 1, N)
    ax.hexbin(
        x, y, gridsize=grid_size,
        cmap=custom_cmaps[cls],
        edgecolors='none',
        extent=extent,
        vmin=threshold  # values < threshold will be transparent
    )
    # ax.scatter([], [], color=custom_cmaps[cls](0.9), label=cls)

# plt.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Independent Hexbin Overlay by Class')
plt.show()