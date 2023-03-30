import pandas as pd

print("NUMBER 1")
print(pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").head())

print("NUMBER 2")
print(pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv").head())

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

print("NUMBER 3")
print(df_selic.info())