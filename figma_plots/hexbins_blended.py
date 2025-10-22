#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.colors as mcolors
N = 1_000_000
grid_size = 200
classes = ['A', 'B', 'C']

xmin, xmax = -1, 1
ymin, ymax = -1, 1
extent = (xmin, xmax, ymin, ymax)
maxalpha = 0.8

means = {
    'A': (0, 0),
    'B': (1.5, 1.5),
    'C': (-1.5, -1.5)
}

colors = {
    'A': "red",
    'B': "green", 
    'C': "blue" 
}

# Custom fade colormaps: hexstring color fading to alpha 0 except value==1 is alpha 1
def make_fade_colormap(hexstr, N=256):
    """
    Create a colormap that fades from the given hex color to transparent,
    but only the top value (v=1) is fully opaque (alpha=1), rest fade to 0.
    hexstr: hex color string, e.g. '#ff937e'
    N: number of steps in the colormap
    """
    rgb = mcolors.to_rgb(hexstr)
    colors = np.zeros((N, 4))
    colors[:, 0] = rgb[0]
    colors[:, 1] = rgb[1]
    colors[:, 2] = rgb[2]
    colors[:, 3] = np.linspace(0.0, 1.0, N)
    colors[1, 3] = 0.5
    return ListedColormap(colors, name=f"fade_{hexstr}")

custom_cmaps = {
    'A': make_fade_colormap(colors['A']),
    'B': make_fade_colormap(colors['B']),
    'C': make_fade_colormap(colors['C'])
}

#%%

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


# %%
