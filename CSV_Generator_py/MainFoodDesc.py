import pandas as pd

def column_sep(txtfile):
    with open(txtfile , 'r') as file:
        lines = file.readlines()
    parsed_data = []
    
    for line in lines:
        entries = line.strip().split('^')
        entries = [entry for entry in entries if entry]
        parsed_data.append(entries)
        
    df = pd.DataFrame(parsed_data, columns=["Food Index","From","To","Food"])
    df["Food"] = df["Food"].str.replace('~', '')
    df.to_csv("CSVs\MainFoodDesc.csv", index=False)
    
column_sep('Data\FNDDS_2009_2010\MainFoodDesc.txt')

