#%%
import numpy as np
import pandas as pd
import holoviews as hv
import datashader as ds
import time
import holoviews.operation.datashader as hd

hv.extension('bokeh')

N = 100_000_000

x = np.random.normal(0, 1, N)
y = np.random.normal(0, 1, N)


df = pd.DataFrame({'x': x, 'y': y})

points = hv.Points(df, kdims=['x', 'y'])


shaded = hd.datashade(points, dynamic=True, aggregator=ds.count(), color_key='lightblue')

#%%

shaded = shaded.opts(
    height=200,
    width=300,
    title="Zoom & Pan to Dynamically Trigger Datashader"
)


shaded  # This will display the plot in Jupyter or VS Code interactive window

# %%
