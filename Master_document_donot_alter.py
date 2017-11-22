import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from matplotlib.finance import candlestick_ohlc
import numpy as np
import pandas as pd
import datetime

filedirectory = "GOOG.csv"
data = np.genfromtxt(filedirectory, delimiter=',')


def menu():
    """Input is input() return p = Getcsv( the real input )."""

    # print(""" press 1 for      """)
    print("please enter: ")
    #q = Stock(Csvfile(input()).get_data)
    # print(q.price)
    #q.graph()
    print(Csvfile(input()).get_data())

# def search():
#     try list(input()) in list():
#         # FIXME
#     Exception
#
# class Userinput:
#     """Take user input and classfiy/categorize it, match and display.
#        self.correct_ticker_name ()
#        self.possible_ticker(should be a list)
#        self.possible_company_name(should be a list)"""

class Csvfile:
    """Get csv file from """
    def __init__(self,Ticker = "GOOG", timestart = "2017-09-01", timeend = "2017-11-01"):
        self.ticker_name = Ticker.upper().strip()
        self.startdt = (datetime.datetime.strptime(timestart,'%Y-%m-%d'))
        self.startmonth = (self.startdt.strftime("%b"))
        self.enddt = (datetime.datetime.strptime(timeend,'%Y-%m-%d'))
        self.endmonth = (self.enddt.strftime("%b"))
    def get_data(self):
        url1='http://finance.google.com/finance/historical?q='
        url2='&startdate'
        url3='=&num=30&ei=NGoQWtDQFMGKUIuSsYgF&output=csv'
        self.url = url1 + self.ticker_name + url2 + self.startmonth + '+' + str(self.startdt.day) + '%2C+' + str(self.startdt.year) + '&enddate=' + self.endmonth + '+' + str(self.enddt.day) + '%2C+' + str(self.enddt.year) + url3
        return self.url
# p = Getcsv(input())
# p.ticker_name --> what we are looking for
# p = Ticker()

class Stock:
    """if a stock p euqals to Stock, then p can have p.graph, p.mean, p.blabla
    all called in the same time"""

    def __init__(self, csvfile="GOOG.csv"):
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

        # plt.close()
        # graph(data,"test.png")


menu()
