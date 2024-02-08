# Zinc = 309
# Thiamin = 404

import pandas as pd

df = pd.read_csv('CSVs/FNDDSNutVal.csv')
mainfood = pd.read_csv('CSVs/MainFoodDesc.csv')

keep = [309,404]

filtered_df = df[df['Nutrient Index'].isin(keep)]
filtered_df = filtered_df.drop(columns=['From','To'])

mainfood['Food Index'] = pd.to_numeric(mainfood['Food Index'], errors='coerce')

result_df = pd.merge(filtered_df, mainfood[['Food Index', 'Food']], how='left', left_on='Food Index', right_on='Food Index')

result_df.to_csv('CSVs/Particular Nutrients/ZincThiamin.csv')