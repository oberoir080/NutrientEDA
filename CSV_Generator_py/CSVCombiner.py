import pandas as pd

main_food = pd.read_csv("CSVs/MainFoodDesc.csv")
nut = pd.read_csv("CSVs/NutDesc.csv")
FNDDS_nut = pd.read_csv("CSVs/FNDDSNutVal.csv")

filtered_df = FNDDS_nut.loc[FNDDS_nut.iloc[:,0] == 63101000]


merged_df = pd.merge(filtered_df, nut, left_on='Nutrient Index', right_on='Nutrient Index', how='left')

merged_df = merged_df.drop(columns=['From','To', 'Amount_y','Nutrient Code'])

print(merged_df)