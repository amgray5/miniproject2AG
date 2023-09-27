#%%
# INF601 - Advanced Programming in Python
# Austin Gray
# Mini Project 2

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

df = pd.read_csv('artists.csv', index_col='Artist')

def printGraph(artist):
    artist_data   = dict(df.loc[artist])
    data_details  = list(artist_data.keys())
    artist_values = list(artist_data.values())
    artist_values_rounded = []

    #Find missing values and remove them from lists
    for i in range(0, len(artist_values)):
        if pd.isna(artist_values[i]) == True:
            data_details.remove(data_details[i])
            artist_values.remove(artist_values[i])
        else:
            #Turn float64 to a readable float for plt
            value_rounded = ''
            for x in str(artist_values[i]):
                if x ==',':
                    continue
                else:
                    value_rounded += x

            artist_values_rounded.append(round(float(value_rounded), 2))

    #Plot Creation
    graph = plt.subplot()

    #Remove Plot Boarder
    for s in ['top', 'bottom', 'left', 'right']:
        graph.spines[s].set_visible(False)

    #Import data and set color for plot
    graph.barh(data_details, artist_values_rounded, color='#1DB954')

    #Set gray background grid
    graph.grid(color='gray', linestyle='-.', linewidth=0.5, alpha=0.2)

    for i in graph.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize = 10, fontweight='bold', color ='gray')

    #Set graph labels and title
    graph.set_ylabel(f'Types of Streams for {artist}')
    graph.set_xlabel('Amount of Streams')
    graph.set_title(f'Spotify Stream Stats for {artist}')

    #Saves images
    save_location = f"charts/{artist.replace(' ', '')}.png"
    plt.savefig(save_location)

    #Show graph
    plt.show()

def getArtist():
    while True:
        artist = input(f'Please give an artist name: ')

        try:
            print('Checking Artist')
            dict(df.loc[artist])
            print('Valid Artist')
            break
        except:
            print('That artist is not in the Spotify statistics. Please enter another')

    return artist


#Start of Program
#Try to create charts folder
try:
    Path('charts').mkdir()
except FileExistsError:
    pass

printGraph(getArtist())

# %%
