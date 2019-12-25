# plotly standard imports
import plotly.graph_objs as go
import chart_studio.plotly as py

# Cufflinks wrapper on plotly
import cufflinks

# Data science imports
import pandas as pd
import numpy as np

# Options for pandas
pd.options.display.max_columns = 30

df = pd.read_csv('data/blue_jays.csv', index_col=0)

df.head()
print(df)

from plotly.offline import iplot
import plotly.figure_factory as ff

figure = ff.create_scatterplotmatrix(df[['KnownSex', 'Head', 'Mass', 'Skull']],
                                     index='KnownSex', height=800, width=800)
iplot(figure)

corrs = df.corr()

figure = ff.create_annotated_heatmap(z=corrs.round(2).values,
                                     x = list(corrs.columns),
                                     y = list(corrs.index),
                                     showscale=True)
#iplot(figure)

figure = ff.create_scatterplotmatrix(df[['KnownSex', 'Head', 'Mass', 'Skull']], diag='histogram',
                                     index='KnownSex', height=800, width=800)
#iplot(figure)

iplot(ff.create_violin(df, data_header='Mass',
                       group_header='KnownSex'))
figure = ff.create_dendrogram(df[['Mass', 'Skull']])
iplot(figure)
