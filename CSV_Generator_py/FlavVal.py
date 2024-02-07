import pandas as pd

def column_sep(txtfile):
    with open(txtfile , 'r') as file:
        lines = file.readlines()
    parsed_data = []
    
    for line in lines:
        entries = line.strip().split('^')
        entries = [entry for entry in entries if entry]
        parsed_data.append(entries)
        
    df = pd.DataFrame(parsed_data, columns=["Food Index","Nutrient Index","From","To", "Amount"])
    df.to_csv("CSVs/FlavVal.csv", index=False)
    
column_sep('Data/FNDDS_Flavonoids_2007_2010/FlavVal.txt')