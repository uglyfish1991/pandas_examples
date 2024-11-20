
#* --------------------- Accessing Parts of A Frame ----------------------------------

import pandas as pd

#* --------------------- Remaking the Frame ----------------------------------

#? The following code is simply remaking the frame from the last session quickly!

df = pd.read_excel("sup_dev_rankings.xlsx")
df = df.set_index("Languages")
print(df)

#* --------------------- Amending Structures ----------------------------------

#? We can access a specific column of a frame using square brackets, much like refrencing a dictionary key. 
print(df["Ranking 2019"])
#? We get the series back, showing us the index positions, the data types, and the single column.

#? We can also view a number of columns by handing over a list. Notice there are two sets of square brackets!
print(df[["Ranking 2022", "Ranking 2021"]])

#? We can reference a single row by using .loc[] and the index label. We renamed our index above to make this easier, so we don't have to remember the location numbers!
print(df.loc["HTML"])

#? Pandas does keep a back up of the index numbers though, under the .iloc property - short for integer location. 
print(df.iloc[3])

#? We can access a specific cell by using the .at[] property. We can also use this pattern with .loc[]. but "print the information at this reference" might feel more natural!
print(df.at["HTML", "Ranking 2023"])

#? We can use slice notation to access a chunk of a frame. 
#? Slice notation is a usful feature in Python, allowing us to take chunks of a collection based on a start, stop, step, pattern.

#? Bracket slice notation [start:stop:step] lets you extract parts of a list, string, or other sequence:
#? - start: Index to begin slicing (inclusive, defaults to 0).
#? - stop: Index to stop slicing (exclusive, slicing ends before this index).
#? - step: How many steps to skip (defaults to 1, use -1 for reverse).
#? Examples:
#?   my_list[1:4]  -> Items from index 1 to 3.
#?   my_list[:3]   -> First 3 items (start defaults to 0).
#?   my_list[2:]   -> Items from index 2 to the end.
#?   my_list[::2]  -> Every other item (step 2).
#?   my_list[::-1] -> All items in reverse order.


#? We can use a similar technique with .loc[]
#? .loc enxpects information as df.loc[rowstart:rowstop:rowstep, columnstart:columnstop:columnstep]

#? This gives us the rows from Python - HTMl, and every other column. 
#? Note - .loc[] is inclusive! We say we want to stop on hTML, and we do actually stop on HTML!

print(df.loc["Python":"HTML":1, "Ranking 2023":"Ranking 2019":2])

