import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("sup_results.csv")

profile = ProfileReport(df, title = "International Results")

profile.to_file('ydata_results_report.html')