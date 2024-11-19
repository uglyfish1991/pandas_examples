import pandas as pd
#*  -------------  Useful Pandas Methods ----------------

#? Reading the csv file in to Pandas and making a dataframe:

df = pd.read_csv("sup_spotify_songs.csv")

#? - value_counts() counts how many times a unique value appears in a series.
#? For example, if I had "apples, apples, oranges, cherries, apples, cherries" value counts would return:
#? apples      3
#? oranges     1
#? cherries    2
print(df["playlist_genre"].value_counts())

#? A side effect of seeing the value counts in a set with this result is learning the mode!
#? If we are looking for the mode, though, there are better ways of discovering it!

#*  -------------  Statistics Methods ----------------

#? .mode() always returns a series. There can be more than one mode. 
#? Pandas always returns a collection in preperation for this. 
print(df["playlist_genre"].mode())

#? If we JUST want a single result, and not the box the mode comes in we can use index position:
print(df["playlist_genre"].mode()[0])

# print(df["duration_ms"].median())
# print(df["duration_ms"].mean())

# max_ms = df["duration_ms"].max()
# min_ms = df["duration_ms"].min()
# print(max_ms - min_ms)

# print(df["duration_ms"].sum())

# print(df.sort_values(by=["duration_ms"]))

# print(df.groupby('playlist_genre')["duration_ms"].max())

print(df.query("track_artist=='Ricky Martin'"))

mean_val = df["duration_ms"].mean()

print(df.query("duration_ms > @mean_val"))
