
#* --------------------- Amending Structures ----------------------------------

import pandas as pd 

#* --------------------- Remaking the dataframe from the previous session ----------------------------------

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
rankings = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": rankings
})

#* --------------------- Adding a new row / rows ----------------------------------

#? We can access a location on a dataframe by using .loc[], the location property.
#? If the location we are trying to access doesn't exist, it is created at the end of the dataframe

#* df.loc[4] = ["PHP", 11]

#? We can also concatenate two dataframes together

new_data = pd.DataFrame({
    "Languages" : ["PHP"],
    "Ranking": [11]
})

df = pd.concat([df,new_data], ignore_index=True)

#? .loc[] is used to add one or two rows. pd.concat() should be used for anything more than that as it is faster.

#? Row order is usually not important. You'll likely be sorting data by a specific row anyway! But if you do want to insert a value into a specific row, you can use floating points as index positions.
#* df.loc[3.5] = ["KESL", 20]

#? At this point, KESL will still be added to the end of the frame, but we can sort the frame via the index column to re-order it.
#* df = df.sort_index()

#? If we then wanted to re-order the index so it was back to whole numbers, we can reset. 
#? By default, Pandas will make the old index positions a new column, just in case we need them! We can cancel this action with adding drop=True as an argument
#* df = df.reset_index(drop=True)

#? Let's add Java and TypeScript to our Frame
df.loc[5] = ["Java", 7]
df.loc[6] = ["TypeScript", 5]
print(df)

#* --------------------- Adding a new column/columns ----------------------------------

#? We can add a new column similarly to how we can add a new dictionary key. We can reference the frame, and use [] to add a column.
df["Ranking 2022"] = [4,1,2,3,10,6,5]
print(df)

#? We can also concatenate again, but this time we need to hand over another keyword argument. 
#? axis tells the concat() method how to add the two frames together - should it stack them on top of eachother (axis 0) or next to each other? (axis 1)
# new_data = pd.DataFrame({"Ranking 2022":[4,1,2,3,10,6,5]})
# df = pd.concat([df,new_data], axis=1)

#? Let's add 2020 and 2019's results to our frame
df["Ranking 2020"] = [4,1,2,3,8,5,9]
df["Ranking 2019"] = [4,1,2,3,8,5,10]
print(df)

#? If you look at the frame above, we've missed out 2021!
#? While row order generally doesn't matter, column order can be important. We've set a pattern on our frame of chronological order, and we should maintain that!
#? The insert method allows us to add a column at a specific location. We hand over the index positiobn, column name, and information.
df.insert(3, "Ranking 2021", [3,1,2,4,11,5,7])
print(df)

#* --------------------- Renaming Rows and Columns ----------------------------------

#? We've set a convention in our column names, Ranking YYYY. Our first column does not follow that convention!
#? This makes our frame inconsistent, and unclear. We can rename it

#? You'll notice on some occasions, I've written df = df.method() when making a change to my dataframe. 
#? You may also see inplace=True used sometimes. This allows the change to be made to the current dataframe, but it is considered to be poor practise.
df.rename(columns={"Ranking":"Ranking 2023"}, inplace=True)
print(df)

#? An index of numerical values increimenting by 1 each time is a very effective, efficient way of labelling rows. However, it might not be the most readable!
#? Remember how much easier it was to look up values in a dictionary than a list? 
#? It's probably easier to remember "the HTML row" than trying to remember which index row HTML is at!

#! Only change the index if you know no-one else, or nothing else, is relying on it! You could make things harder to look up!

df = df.set_index("Languages")
print(df)