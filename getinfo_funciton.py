import pandas as pd
import numpy as np
import csv
#from sklearn.svm import SVR
import matplotlib.plot as plt


dates=[]
prices=[]

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFilereader=csv.reader(csvfile)
        next(csvFilereader)
        for row in csvFilereader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
        return

def predict_prices(dates,prices,x):
    data=np.reshape(dates,(len(dates),1))
    

def getinfo(x):
    companies = (companylist[(companylist == x).any(1)].stack())

    if len(companies) == 0: # HANDLING ERROR
        print ("Company Not Found :   *Please enter exact name or symbol* \n")
        getdetails("1")

    elif len(companies)>8:
        design()
        print(companies[0:],"\n")
        design()
        confirm = input("confirm the Company Symbol by entering : ").upper() #Upper to handle case sensitive execpts
        design()
        x = (np.where(companylist.Symbol == confirm))
        p = int(x[0])
        print (companylist.iloc[p][0:7])

    else:
        design()
        print((companies[0:7]),"\n") #For memory quote in companies[8]
        design()
