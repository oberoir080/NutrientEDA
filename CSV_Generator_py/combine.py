import pandas as pd

with open("Data/FNDDS_2009_2010/FNDDSNutVal.txt", "r") as file:
    lines1 = file.readlines()

columns1 = ["Food Index", "Nutrient Index", "From", "To", "Amount"]

# Split each line and create a list of lists for Food Index
data1 = [line.strip().split('^')[:5] for line in lines1]
food_df = pd.DataFrame(data1, columns=columns1)

with open("Data/FNDDS_2009_2010/NutDesc.txt", "r") as file:
    lines2 = file.readlines()

columns2 = ["Nutrient Index", "Nutrient", "Nutrient Code", "Unit", "Decimal Places"]

data2 = [line.strip().split('^')[:5] for line in lines2]
nutrient_df = pd.DataFrame(data2, columns=columns2)

nutrient_df["Nutrient"] = nutrient_df["Nutrient"].str.replace('~', '')
nutrient_df["Nutrient Code"] = nutrient_df["Nutrient Code"].str.replace('~', '')
nutrient_df["Unit"] = nutrient_df["Unit"].str.replace('~', '')

combined_df = pd.merge(food_df, nutrient_df, on="Nutrient Index", how="inner")

with open("Data/FNDDS_2009_2010/MainFoodDesc.txt", "r") as file:
    lines3 = file.readlines()

columns3 = ["Food Index","From", "To", "Food"]

data3 = [line.strip().split('^')[:4] for line in lines3]
main_food_desc = pd.DataFrame(data3,columns = columns3)
main_food_desc.drop(columns=["From","To"], inplace=True)

final_df = pd.merge(combined_df, main_food_desc, on="Food Index", how="inner")
final_df.to_csv("CSVs/FNDDS.csv", index=False)