import pandas as pd
from pandas.io.json import json_normalize

with open('jsonfile_dev.json', encoding='utf-8') as inputfile:
    df_dev = pd.read_json(inputfile)
with open('jsonfile_prd.json', encoding='utf-8') as inputfile:
    df_prd = pd.read_json(inputfile)

n_df_dev = json_normalize(df_dev['Parameters'])
n_df_dev = n_df_dev.add_prefix('dev_')
n_df_prd = json_normalize(df_prd['Parameters'])
n_df_prd = n_df_prd.add_prefix('prd_')
# n_df_dev = n_df_dev[['Name', 'Type', 'Value']]
# n_df_dev.to_csv("csvfile.csv", encoding='utf-8', index=False)

merged_df = pd.merge(n_df_dev, n_df_prd, left_on='dev_Name', right_on='prd_Name')
merged_df = merged_df[['dev_Name', 'dev_Type', 'dev_Value', 'prd_Value']]
merged_df.rename(columns = {'dev_Name':'Name', 'dev_Type':'Type'}, inplace = True)
merged_df.to_csv("csvfile.csv", encoding='utf-8', index=False)
