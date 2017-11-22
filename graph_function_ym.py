import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filedirectory = "GOOG.csv"
data = np.genfromtxt(filedirectory,delimiter=',')

# def graph(x,filename):
#     """ this function will plot the graph using mapplotlib package"""
#     plt.plot(x[:, 1])
#     #plt.xlim((-1, 5))
#     #plt.ylim((-1, 5))
#     plt.axis("equal")
#     plt.savefig(filename)
#     plt.show(filename)
#     plt.close()
#
# graph(data,"test.png")

def menu():
    """ input is input()
        return p = Userinput( the real input )
    """
    #print(""" press 1 for      """)
    print("please enter: ")
    q = Stock(Userinput(input()).ticker)
    #print(q.price)
    q.graph()
class Userinput:
    """ take user input and classfiy/categorize it
    match and display"""
    def __init__(self,input):
        self.ticker_name = "this is the refined ticker name"+ str(input)
        self.ticker = str(input) + ".csv"

# p = Userinput(input())
# p.ticker_name --> what we are looking for
# p = Ticker()
class Stock:
    """if a stock p euqals to Stock, then p can have p.graph, p.mean, p.blabla
    all called in the same time"""
    def __init__(self,csvfile = "GOOG.csv"):
        x = pd.read_csv(csvfile)
        #self.head = pd.head(x)
        self.price = x.Open
        # self.__open_price = pd.  #make a list
        # self.lowsprice
        # self.n = pd.readdatacount row()

    def graph(self):
        """this will plot graph for every element that is the class stock"""
        plt.plot(self.price[:])
        #plt.xlim((-1, 5))
        #plt.ylim((-1, 5))
        plt.axis("equal")
        plt.show()
        #plt.close()
        #graph(data,"test.png")
menu()
