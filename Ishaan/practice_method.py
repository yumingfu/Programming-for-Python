import re
import pandas as pd

company_list=pd.read_csv("companylist.csv",usecols=[0,3])
#

# mask = np.column_stack([df[col].str.contains(r"\^", na=False) for col in df])
# df.loc[mask.any(axis=1)]

a=pd.DataFrame(data=company_list)
user_input=input("Enter the value of the symbol :").strip().upper()
a1=a[a['Symbol']==user_input]
#print(a1)
#if a1['Symbol'].str.contains(user_input).any():
#    tickr = a1.iloc[:]['Symbol']
#    print(tickr)
a2= a[a['Symbol'].str.contains(user_input)]
print(a2)

#return tickr
# else:
#     print("blahblah")


# if a1['Symbol'].str.contains(user_input).any():
#     print(a.iloc[0:10])
#
# else:
#     print("Cannot find the symbol")
#




# elif:
#     user_input2=("Do you want to view the ticker list (Y/N) ? ")
#     if user_input2=="Y":
#         print(company_list)
#     else:
#         print("something something")
#print(company_list.head())
