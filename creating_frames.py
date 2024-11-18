
#* --------------------- Pandas Structures ----------------------------------

#? importing the pandas library with an allias so we don't have to keep writing pandas
import pandas as pd 

#* --------------------- The Series ----------------------------------

#? A series is a one dimentional structure. It is like a list, but with access to more data-specific methods 
languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
rankings = pd.Series([3,1,2,4])

#? It prints out differently, showing the index positions and the data type of the column
print("The languages series:")
print(languages)
print("\n")
print("The ranking series:")
print(rankings)
print("\n ---------------------------------------------------- \n")

#* --------------------- The DataFrame ----------------------------------

#? A dataframe is a table like structure. 
#? This dataframe is made up of three rows and two columns. 
#? Anne, Bill, and Charlie fill one column. 30, 27, and 55 fill the other. 

#? The columns keyword argument lets us name out columns something more useful 
#? By default, they's just be named 0 ++, based on index positions

df = pd.DataFrame([("Anne", 30),("Bill", 27),("Charlie", 55)], columns=["Name", "Age"])
print("The People DataFrame:")
print(df)
print("\n ---------------------------------------------------- \n")
#? We can make a dataframe from existing structures using a dictionary, where the keys are the column names and the values are the contents of the serieses we are referencing. 

#? This is a straightforward way of making a dataframe, and is very popular.
df = pd.DataFrame({
    "Languages": languages,
    "Ranking": rankings
})

print("The Language Ranking DataFrame")
print(df)

#? pd.concat() joins two or more structures together. It is easy to add new rows and columns to existing data this way. 

df = pd.concat([languages, rankings])
df.columns = ["Languages", "Ranking"]
print("The language DataFrame made with .concat()")
print(df)

print("\n ---------------------------------------------------- \n")

#* --------------------- Reading External Files ----------------------------------

#? We can read in common data formats to Pandas to work with: 

#? CSV is a common file type - it stands for comma seperated values
#? I know 14, 16, 19 are different values because of the comma
#? They are an easy-to-work with, small, efficient data format but they are not easy to read!
#? We can read them into pandas to work with them easily

df = pd.read_csv("speeds.csv")
print(df)

#? We can also work with Excel files. These are a little slower, but still work very well!
df = pd.read_excel("speeds.xlsx")
print(df)