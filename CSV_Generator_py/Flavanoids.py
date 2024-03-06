import pandas as pd

def column_sep(txtfile):
    with open(txtfile, 'r') as file:
        lines = file.readlines()
    parsed_data = []

    for line in lines:
        entries = line.strip().split('^')
        entries = [entry for entry in entries if entry]
        parsed_data.append(entries)

    return pd.DataFrame(parsed_data)

# Read FlavDesc.txt and process the data
flav_desc_df = column_sep('Data/FNDDS_Flavonoids_2007_2010/FlavDesc.txt')
flav_desc_df.columns = ["Nutrient Index", "Nutrient", "Nutrient Category", "Nutrient Code", "Unit", "Decimal Places"]
flav_desc_df["Nutrient"] = flav_desc_df["Nutrient"].str.replace('~', '')
flav_desc_df["Nutrient Code"] = flav_desc_df["Nutrient Code"].str.replace('~', '')
flav_desc_df["Nutrient Category"] = flav_desc_df["Nutrient Category"].str.replace('~', '')
flav_desc_df["Unit"] = flav_desc_df["Unit"].str.replace('~', '')

# Read FlavVal.txt and process the data
flav_val_df = column_sep('Data/FNDDS_Flavonoids_2007_2010/FlavVal.txt')
flav_val_df.columns = ["Food Index", "Nutrient Index", "From", "To", "Amount"]

# Merge FlavVal with FlavDesc based on "Nutrient Index"
combined_df = pd.merge(flav_val_df, flav_desc_df, on="Nutrient Index", how="left")

combined_df.to_csv("CSVs/Flavonoids.csv", index=False)
