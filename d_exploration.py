
#* --------------------- Data Exploration in Pandas ----------------------------------

#? Data exploration is the intitial step for you, as the analyst, to learn about the data you are working with.
#? It's not necessarily going to answer questions for the problem statement, but it will help you be more informed about your data.

#* --------------------- Reading the Data In ----------------------------------
import pandas as pd

df = pd.read_csv("sup_results.csv")

#* --------------------- Exploration Methods ----------------------------------

#? df.info() prints information about your frame. It gives information like the number of columns and rows, how many cells have missing values, the column names, and the data type of the columns.
#? It gives no analytical information, but is useful to introduce you to the frame.
df.info()

#? df.describe() produces descriptive statistics for any numerical column. These figures include:
#? The five-figure summary (min, 25%, median, 75%. max)
#? The mean (adding up all the values in the column and dividing by the number of values - gives a value which can represent the data, an average) 
#? The standard deviation (the average distance a value is from the mean. It shows how much the data varies)
#? The count (how many values are in the column)

print(df.describe())
#? These descriptive statistics can tell us lots about our data wuthout us having to trawl through row by row. 
#? We discovered that 75% of our data is made up of the numbers 0,1,and 2. 
#? The last 25% of our data is made up of the numbers 3-31! 

#? We need to see how much of an impact that last 25% of our data is having on our stats. A large dataset is not as impacted by outliers, they don't hold as much weight.
#? I can use the value_count() method to see how the values make up the data. Because I've been referencing percentiles throughout, I can normalise the data to give the realtive frequencies, and * by 100 turns this into the percentage.
print(df["home_score"].value_counts(normalize=True)*100)

