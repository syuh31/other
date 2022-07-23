import pandas as pd
from pandas.io.json import json_normalize

with open('jsonfile.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

n_df = json_normalize(df['Parameters'])
n_df = n_df[['Name', 'Type', 'Value']]
n_df.to_csv("csvfile.csv", encoding='utf-8', index=False)

