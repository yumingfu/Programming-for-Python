import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filedirectory = "GOOG.csv"
data = np.genfromtxt(filedirectory,delimiter=',')

def graph(x,filename):
    """ this function will plot the graph using mapplotlib package"""
    plt.plot(x[:, 1])
    #plt.xlim((-1, 5))
    #plt.ylim((-1, 5))
    plt.axis("equal")
    plt.savefig(filename)
    plt.show(filename)
    plt.close()

graph(data,"test.png")


















class Stock:
    """if a stock p euqals to Stock, then p can have p.graph, p.mean, p.blabla
    all called in the same time"""
    def __init__(self,csvfile = "GOOG.csv"):
        x = np.genfromtxt(csvfile)
        self.head = pd.head(x)
        self.__open_price = pd.  #make a list
        self.lowsprice
        self.n = pd.readdatacount row()

    def graph(self,csvfile):
        """this will plot graph for every element that is the class stock"""
        plt.plot(x[:, 1])
        #plt.xlim((-1, 5))
        #plt.ylim((-1, 5))
        plt.axis("equal")
        plt.savefig(filename)
        plt.show(filename)
        #plt.close()
        #graph(data,"test.png")
    def mean(self):
        return sum(self.open_price)/self.n
    def count(self):
        return

p = Stock("goog.csv")
p._price

p.head


q = Stock(google)
q.graph()

def stock_mean(x,csvname):
    assert x=
    x = Stock(csvname)
    x.__graph()
    x.price
def our_stock_2(x,csvname):
    assert x =

def our_stock_3(x,csvname):


def graph by user(x.price, x.time):


def index():
    try:
        sdf
    except:
        sdf
