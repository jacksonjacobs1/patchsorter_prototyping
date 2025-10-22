#%%
import numpy as np
import pandas as pd
import holoviews as hv
import datashader as ds
import time
import holoviews.operation.datashader as hd

hv.extension('bokeh')

N = 100_000_0

x = np.random.normal(0, 1, N)
y = np.random.normal(0, 1, N)

# Assign random classes to points
classes = np.random.choice(['A', 'B', 'C'], size=N)

df = pd.DataFrame({'x': x, 'y': y, 'class': classes})

points = hv.Points(df, kdims=['x', 'y'], vdims=['class'])

# Define a color key for the classes
color_key = {'A': 'red', 'B': 'green', 'C': 'blue'}

shaded = hd.datashade(points, dynamic=True, aggregator=ds.count_cat('class'), color_key=color_key)

#%%

shaded = shaded.opts(
    height=200,
    width=300,
    title="Zoom & Pan to Dynamically Trigger Datashader"
)

shaded  # This will display the plot in Jupyter or VS Code interactive window

# %%
