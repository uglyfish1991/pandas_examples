import pandas as pd 

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
rankings = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": rankings
})

df.loc[4] = ["PHP", 11]
# df.loc[3.5] = ["KESL", 20]

# df = df.sort_index()
# df = df.reset_index(drop=True)
print(df)