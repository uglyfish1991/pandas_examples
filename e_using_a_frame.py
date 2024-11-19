import pandas as pd

df = pd.read_csv("sup_spotify_songs.csv")

print(df["playlist_genre"].value_counts())
