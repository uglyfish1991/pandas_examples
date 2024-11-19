import pandas as pd 

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
rankings = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": rankings
})

# df.loc[4] = ["PHP", 11]
# df.loc[3.5] = ["KESL", 20]

# df = df.sort_index()
# df = df.reset_index(drop=True)
print(df)

new_data = pd.DataFrame({
    "Languages" : ["PHP"],
    "Ranking": [11]
})

df = pd.concat([df,new_data], ignore_index=True)

df.loc[5] = ["Java", 7]
df.loc[6] = ["TypeScript", 5]
print(df)

df["Ranking 2022"] = [4,1,2,3,10,6,5]
print(df)

# new_data = pd.DataFrame({"Ranking 2022":[4,1,2,3,10,6,5]})
# df = pd.concat([df,new_data], axis=1)

df["Ranking 2020"] = [4,1,2,3,8,5,9]
df["Ranking 2019"] = [4,1,2,3,8,5,10]

print(df)

df.insert(3, "Ranking 2021", [3,1,2,4,11,5,7])
print(df)

df.rename(columns={"Ranking":"Ranking 2023"}, inplace=True)
print(df)

df = df.set_index("Languages")
print(df)