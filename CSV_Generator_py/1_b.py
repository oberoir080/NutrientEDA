import pandas as pd

raw_apple = '63101000'     #from file MainFoodDesc.csv  #in mg
maraschino_cherry = '63111010'     #from file MainFoodDesc.csv  #in mg
margarine = '81102000'     #from file MainFoodDesc.csv  #in mg
yeast = '75236000'         #from file MainFoodDesc.csv  #in mg
raw_oyester = '26315100'   #from file MainFoodDesc.csv  #in mg


thiamin = '404'         #from file NutDesc.csv
zinc = '309'            #from file NutDesc.csv



def find_avg(data,food,nutrient):
    num = 0
    denom=0
    for i in data:
        j = i[0].split(',')
        
        if(j[0]==food and j[1]==nutrient):
            num += float(j[-1])
            denom += 1

    return str(num/denom)


f = open('CSV_Generator_py\CSVs\FNDDSNutVal.csv', 'r')

# Initialize an empty list to store the data
data = []

# Read each line in the file
for line in f:
    # Split each line by space and append to the data list
    data.append(line.strip().split(' '))

# Close the file
f.close()

# Print the resulting list
data = data[1:]
# print(data)

print("raw_apple: thiamin: "+find_avg(data,raw_apple,thiamin)+"x10^-3")
print("maraschino_cherry: thiamin: "+find_avg(data,maraschino_cherry,thiamin)+"x10^-3")
print("margarine: thiamin: "+find_avg(data,margarine,thiamin)+"x10^-3")
print("raw_oyester: thiamin: "+find_avg(data,raw_oyester,thiamin)+"x10^-3")
print("yeast: thiamin: "+find_avg(data,yeast,thiamin)+"x10^-3")

print()

print("raw_apple: zinc: "+find_avg(data,raw_apple,zinc)+"x10^-3")
print("maraschino_cherry: zinc: "+find_avg(data,maraschino_cherry,zinc)+"x10^-3")
print("margarine: zinc: "+find_avg(data,margarine,zinc)+"x10^-3")
print("raw_oyester: zinc: "+find_avg(data,raw_oyester,zinc)+"x10^-3")
print("yeast: zinc: "+find_avg(data,yeast,zinc)+"x10^-3")




