
import re
import pandas as pd

dict ={}
stock = pd.read_csv("companylist.csv", sep= ",",header = 0)
for i in range(len(stock.Symbol)):
     dict[stock.Name[i]] = stock.Symbol[i]

#print(dict)
p = list(dict.keys())
#print(p)
for i in range(len(p)):
#searchres = re.search(r'[A][a]*',p[i])
    a = []
    if re.search('(?<=abc)ap',p[i]):
        return a.append(p[i])
    #searchres = re.search('(?<=abc)ap',p[i])
a.group(0)
