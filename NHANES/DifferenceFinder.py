import pandas as pd

df = pd.read_csv("firstDay.csv")
df2 = pd.read_csv("secondDay.csv")
main_df = pd.read_csv("MainFoodDesc.csv")
figure1_c = pd.read_excel("Paper Dataset/SourceData_Figure1.xlsx", sheet_name=2)

figure1_c = figure1_c.rename(columns={'food': 'Food'})

print(figure1_c)
df_filtered = df[df["DRABF"] != 1]
df2_filtered = df2[df2["DRABF"] != 1]

lst = df_filtered["DR1IFDCD"].tolist()
lst2 = df2_filtered["DR2IFDCD"].tolist()

lst.extend(lst2)

# Remove non-numeric values and convert the "Food Index" column to int
main_df["Food Index"] = pd.to_numeric(main_df["Food Index"], errors='coerce')  # coerce converts non-numeric values to NaN
main_df = main_df.dropna(subset=["Food Index"])
main_df["Food Index"] = main_df["Food Index"].astype(int)

result_df = main_df[main_df["Food Index"].isin(lst)]
print(result_df)
# Merge result_df and figure1_c on "Food Index"
merged_df = pd.merge(result_df, figure1_c, how='outer', on="Food", indicator=True)

# Filter rows where the indicator column is not "both"
different_rows = merged_df[merged_df["_merge"] != "both"]
different_rows.to_csv("Difference_Set.csv")

