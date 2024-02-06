import pandas as pd

def column_sep(txtfile):
    with open(txtfile , 'r') as file:
        lines = file.readlines()
    parsed_data = []
    
    for line in lines:
        entries = line.strip().split('^')
        entries = [entry for entry in entries if entry]
        parsed_data.append(entries)
        
    df = pd.DataFrame(parsed_data, columns=["Nutrient Index","Nutrient","Nutrient Code","Unit", "Amount"])
    df["Nutrient"] = df["Nutrient"].str.replace('~', '')
    df["Nutrient Code"] = df["Nutrient Code"].str.replace('~', '')
    df["Unit"] = df["Unit"].str.replace('~', '')
    df.to_csv("CSVs/NutDesc.csv", index=False)
    
column_sep('Data/FNDDS_2009_2010/NutDesc.txt')
