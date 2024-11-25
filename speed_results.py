import pandas as pd

df = pd.read_excel("speed_results.xlsx")

print(df.describe())