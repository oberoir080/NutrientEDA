import pandas as pd

main_food = pd.read_csv("CSVs/MainFoodDesc.csv")
nut = pd.read_csv("CSVs/NutDesc.csv")
FNDDS_nut = pd.read_csv("CSVs/FNDDSNutVal.csv")
flav_val = pd.read_csv("CSVs/FlavVal.csv")
flav_desc = pd.read_csv("CSVs/FlavDesc.csv")

filtered_df = FNDDS_nut.loc[FNDDS_nut.iloc[:,0] == 63101000]
filtered_flav_df = flav_val.loc[flav_val.iloc[:,0] == 63101000]

merged_flav_df = pd.merge(filtered_flav_df, flav_desc, left_on='Nutrient Index', right_on='Nutrient Index', how='left')
merged_df = pd.merge(filtered_df, nut, left_on='Nutrient Index', right_on='Nutrient Index', how='left')


merged_flav_df = merged_flav_df.drop(columns=['From','To','Amount_y','Nutrient Category','Nutrient Code'])
merged_df = merged_df.drop(columns=['From','To', 'Amount_y','Nutrient Code'])

final_df = pd.concat([merged_df, merged_flav_df], ignore_index=True)
final_df.to_csv('CSVs/Figure1a_FinalDF.csv')