#%%
# INF601 - Advanced Programming in Python
# Austin Gray
# Mini Project 2

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('artists.csv', index_col='Artist')

artist = 'Kip Moore'

artist_data   = dict(df.loc[artist])
data_details  = list(artist_data.keys())
artist_values = list(artist_data.values())

for i in range(0, len(artist_values)):
    if pd.isna(artist_values[i]) == True:
        data_details.remove(data_details[i])
        artist_values.remove(artist_values[i])

# %%
