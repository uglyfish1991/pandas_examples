import pandas as pd

df = pd.read_csv("sup_results.csv")

print(df.query('home_team=="England"').groupby('tournament')['home_team'].count())

print(df.describe())

print(df["home_score"].value_counts(normalize=True)*100)

mask = df["home_score"]<4

masked_df = df[mask]

print(masked_df["home_score"].mean())
