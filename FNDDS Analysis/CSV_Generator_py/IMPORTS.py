import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math


# Function for converting milligrams, micrograms to grams
def convert_to_grams(row):
    if row['Unit'] == 'mg':
        return row['Amount'] / 1000
    elif row['Unit'] == 'mcg':
        return row['Amount'] / 1000000
    elif row['Unit'] == 'g':
        return row['Amount']
    else:
        return 0



def qn_one(Pxn,pn):
    return (Pxn)/pn

def eq1(data_list, nutrient_code, xn):
    POP = 4968
    c = 0    #num of Pxn
    nut_c =0  #denom of formula
    for i in data_list:
        if i[1] == nutrient_code:
            nut_c+=1
            if i[4] >= xn :
                c+=1
    if(c>POP/2):
        c = POP-c
    return c, nut_c


"""-----------EQUATION2----------"""

# Function for calculating logarithmic standard deviation
def standard_deviation(data,nutrient):
    log_avg = 0
    log_avg_sq = 0
    c=0
    for j in data:
        if(j[1]==int(nutrient)):
            if((j[4]) == 0):
                continue
            
            log_avg += np.log(float(j[4]))
            log_avg_sq += np.log(float(j[4]))**2
            c+=1
            
    return ((log_avg_sq/c) - ((log_avg/c)**2))**0.5

def linear_sd(data,nutrient):
    l=[]
    for j in data:
        if(j[1]==int(nutrient)):
            l.append(j[4])
    return np.std(l)

# Function for calculating mn
def mn_calculator(linear_average_conc,sn):
    # if(linear_average_conc==0):
    #     return 0
    mn = np.log(linear_average_conc) - (sn**2)/2
    return mn

# Function for calculating Mew N
def linear_average_concentration(data,nutrient):
    num=0
    den=0
    for i in data:
        if(i[1]==int(nutrient)):
            num+=i[4]
            den+=1
    if(den==0):
        return 0
    return num/den

# Function for calculating qn
def qn_calculator(xn, data, nutrient):
    sn = standard_deviation(data,nutrient)
    mewn = linear_average_concentration(data,nutrient)
    mn = mn_calculator(mewn,sn)
    bracket = -1*((((np.log(xn)-mn))**2)/(2*sn**2))
    numerator = np.exp(bracket)
    denominator = (xn * sn) * (np.sqrt(2*np.pi)) 
    if(denominator==0):
        return 0
    return numerator/denominator

"""-----------EQUATION2----------"""

# Function for pivoting the dataset
def pivot_dataset(df):
    df.drop(columns=["Nutrient Index", "Unit", "Decimal Places"])
    df = df[df["Nutrient Index"].isin([309, 404])]

    df = df.pivot_table(index=['Food Index', 'Food'], columns='Nutrient Index', values='Amount', aggfunc='sum').reset_index()
    df.columns = ['Food Index', 'Food', 'Zinc', 'Thiamin']
    
    return df

# Function for calculating the skewness
def skewness(data, nutrient):
    log_values = []
    n = 0
    for item in data:
        if item[1] == int(nutrient):
            value = item[4]
            if value != 0:
                log_values.append(np.log(value))
                n += 1
    if n < 3:
        return None  # Skewness is undefined for less than 3 data points

    mean = np.mean(log_values)
    std_dev = np.std(log_values, ddof=1)  # Use ddof=1 for sample standard deviation
    skewness = (n / ((n - 1) * (n - 2))) * np.sum(((log_values - mean) / std_dev) ** 3)
    return skewness

# Function for plotting singular graph
def graph_plot_one(nutrient, x_axis,qn, fig_name):
    if nutrient == '309':
        graph = 'Zinc'
    elif nutrient == '404':
        graph = 'Thiamin'
    else:
        graph = nutrient
        
    plt.plot(x_axis, qn, marker='o')
    plt.xscale('log')  # Set x-axis to logarithmic scale
    plt.title(f'{fig_name} {graph}')
    plt.xlabel('x_axis')
    plt.ylabel('qn')
    plt.show()


