#%%
import pandas as pd
import matplotlib.pyplot as plt
from dask import dataframe as dd

#%%
hierarchy_raw = '~/Downloads/geonames/hierarchy.txt'
cities_500_raw = '~/Downloads/geonames/cities500.txt'

#%%
hierarchy_df = pd.read_csv(hierarchy_raw, delimiter='\t')

#%%
cities_df = pd.read_csv(cities_500_raw, delimiter='\t')