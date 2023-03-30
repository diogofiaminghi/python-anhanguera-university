import pandas as pd

df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json")

print(df_selic.loc[['selic_0', 'selic_4', 'selic_200']])