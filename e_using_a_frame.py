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

#? The mean and median of a column can be found using the below methods.
#? Notice how consistent the syntax is - dot notation is very useful!

print(df["duration_ms"].median())
print(df["duration_ms"].mean())

#? There is no specific "range" function in Pandas - instead, we can find the range using .min() and .max()
max_ms = df["duration_ms"].max()
min_ms = df["duration_ms"].min()
print(max_ms - min_ms)

#? We can sum the total of a column using the .sum() method.
print(df["duration_ms"].sum())

#*  -------------  Sorts and Groups Methods ----------------

#? Rows in a dataframe aren't usually in any specific order. We can re-sort our frame based on a column. For example, I can order the frame based on the duration column
#? The dataframe prints out  in a new order, the row with the shortest durartion value will be first, and the other rows go in ascending order. 
print(df.sort_values(by=["duration_ms"]))

#? We can also group data. We saw earlier with value counts that I have 6 genres of playlist on my  dataframe. 
#? Take a look at just the second half of the below code - ["duration_ms"].max() we know from above that this would find the longest song. 

#? If I group my data by the playlist genre, my data gets split into 6 groups - one for each different genre, and finds out the longest song from each of those six categories!
print(df.groupby('playlist_genre')["duration_ms"].max())

#*  -------------  Queries ----------------

#? We can use the .query() method to find specific results from our dataframe. 
#? We hand a string over to the query method. That string is a comparison - here we are referencing the column track artist, but inside the rows of that column we are looking for the string 'Ricky Martin'
print(df.query("track_artist=='Ricky Martin'"))

#? I can reduce my dataframe down to results which are longer than the average length of a song.
mean_val = df["duration_ms"].mean()

#? Running
#! print(df.query("duration_ms > mean_val"))
#? would give me an error. The query is not looking into the surround scope to find our what mean_val is, it is only looking at the dataframe. 

#? To instruct the frame to reference the outer scope (global scope) I can prefix my variable name with an @ symbol!
print(df.query("duration_ms > @mean_val"))
