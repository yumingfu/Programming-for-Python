"""
** graph_function_ym_copy.py for Programming-for-Python in /Users/Yuming/Programming-for-Python
**
** Made by Yuming Fu
** Login   <Yuming@epitech.net>
**
** Started on  Fri Nov 24 19:59:15 2017 Yuming Fu
** Last update Fri Nov 24 19:59:15 2017 Yuming Fu
"""

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MO, date2num
from matplotlib.finance import candlestick_ohlc
from matplotlib.axes import Axes
import numpy as np
import pandas as pd
import datetime

def menu():
    """Input is input() return p = Getcsv( the real input )."""

    # print(""" press 1 for      """)
    #print("please enter: ")
    #q = Stock(Csvfile("goog",timestart = "2017-05-01", timeend = "2017-10-01").get_data())
    #q.graph()
    #q.candlestick()
    print(Userinput("GOOG", condition = True).a1)

class Userinput:
    """Self.correct_ticker_name ()
       self.possible_ticker(should be a list)
       self.possible_company_name(should be a list)"""
    def __init__(self, symbol, condition = False):
        company_list=pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download",usecols=[0,1,3])
        self.company_list = pd.DataFrame(data=company_list)
        user_input= symbol.strip().upper()
        self.a1 = []
        if user_input in set(company_list['Symbol']) and condition == True:
        #if self.company_list['Symbol'].str.match(str(user_input)) is True:
            self.a1 = self.company_list[self.company_list['Symbol']== str(user_input)]
        else:
            a1= self.company_list[self.company_list['Symbol'].str.contains(user_input[:-1])]
            self.test= "False"
            self.a1 = a1


class Companylist:
        def __init__():
            companylist = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download", usecols = [0,1,3])
            self.companylist = pd.DateFrame(data=company_list)


class Csvfile:
    """Get csv file from """
    def __init__(self, Ticker = "GOOG", timestart = "2017-09-01", timeend = "2017-11-01"):
        assert pd.to_datetime(timeend) - pd.to_datetime(timestart) >= pd.Timedelta('0 days'),\
        "sorry your enddate is earler than you startdate"
        self.ticker_name = Ticker.upper().strip()
        self.startdt = datetime.datetime.strptime(timestart,'%Y-%m-%d')
        self.startmonth = (self.startdt.strftime("%b"))
        self.enddt = datetime.datetime.strptime(timeend,'%Y-%m-%d')
        self.endmonth = (self.enddt.strftime("%b"))
    def get_data(self):
        url1='http://finance.google.com/finance/historical?q='
        url2='&startdate='
        url3='&num=30&ei=NGoQWtDQFMGKUIuSsYgF&output=csv'
        self.url = url1 + self.ticker_name + url2 + self.startmonth + '+' + str(self.startdt.day) + '%2C+' + str(self.startdt.year) + '&enddate=' + str(self.endmonth) + '+' + str(self.enddt.day) + '%2C+' + str(self.enddt.year) + url3
        #self.url = url1 + str(ticker_name) + url2 + month_name1 + '+' + str(startdt.day) + '%2C+' + str(startdt.year) + '&enddate=' + month_name2 + '+' + str(enddt.day) + '%2C+' + str(enddt.year) + url3
        return self.url

# p = Getcsv(input())
# p.ticker_name --> what we are looking for
# p = Ticker()

class Stock:
    """if a stock p euqals to Stock, then p can have p.graph, p.mean, p.blabla
    all called in the same time"""

    def __init__(self, csvfile="GOOG.csv"):
        self.x = pd.read_csv(csvfile)
        #self.head = pd.head(x)
        self.open_price = self.x.Open
        self.close_proce = self.x.Close
        self.Date = pd.to_datetime(self.x['Date'])
        # self.__open_price = pd.  #make a list
        # self.lowsprice
        # self.n = pd.readdatacount row()

    def graph(self):
        """this will plot graph for every element that is the class stock"""

        plt.plot(self.Date,self.close_proce[:],lw = 1.8)
        #plt.xlim((-1, 5))
        #plt.ylim((-1, 5))
        #plt.axis("equal")
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()

        # plt.close()
        # graph(data,"test.png")
    def candlestick(self, stick = 1, otherseries = ['5d','10d','20d','w5d',"Bol_upper","Bol_lower"]):
        """
        :param dat: pandas DataFrame object with datetime64 index, and float columns "Open", "High", "Low", and "Close", likely created via DataReader from "yahoo"
        :param stick: A string or number indicating the period of time covered by a single candlestick. Valid string inputs include "day", "week", "month", and "year", ("day" default), and any numeric input indicates the number of trading days included in a period
        :param otherseries: An iterable that will be coerced into a list, containing the columns of dat that hold other series to be plotted as lines

        This will show a Japanese candlestick plot for stock data stored in dat, also plotting other series if passed.
        """

        # Create a new DataFrame which includes OHLC data for each period specified by stick input
        transdat = self.x.loc[:, ["Date", "Open", "High", "Low", "Close"]]
        transdat['Date'] = pd.to_datetime(transdat['Date'])
        transdat.set_index('Date',inplace=True)
        if (type(stick) == str):
            if stick == "day":
                plotdat = transdat
                stick = 1 # Used for plotting
            elif stick in ["week", "month", "year"]:
                if stick == "week":
                    transdat["week"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[1]) # Identify weeks
                elif stick == "month":
                    transdat["month"] = pd.to_datetime(transdat.index).map(lambda x: x.month) # Identify months
                transdat["year"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[0]) # Identify years
                grouped = transdat.groupby(list(set(["year",stick]))) # Group by year and other appropriate variable
                plotdat = pd.DataFrame({"Open": [], "High": [], "Low": [], "Close": []}) # Create empty data frame containing what will be plotted
                for name, group in grouped:
                    plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0,0],
                                                "High": max(group.High),
                                                "Low": min(group.Low),
                                                "Close": group.iloc[-1,3]},
                                               index = [group.index[0]]))
                if stick == "week": stick = 5
                elif stick == "month": stick = 30
                elif stick == "year": stick = 365

        elif (type(stick) == int and stick >= 1):
            transdat["stick"] = [np.floor(i / stick) for i in range(len(transdat.index))]
            grouped = transdat.groupby("stick")
            plotdat = pd.DataFrame({"Open": [], "High": [], "Low": [], "Close": []}) # Create empty data frame containing what will be plotted
            for name, group in grouped:
                plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0,0],
                                            "High": max(group.High),
                                            "Low": min(group.Low),
                                            "Close": group.iloc[-1,3]},
                                           index = [group.index[0]]))

        else:
            raise ValueError('Valid inputs to argument "stick" include the strings "day", "week", "month", "year", or a positive integer')


        mondays = WeekdayLocator(byweekday=MO)        # major ticks on the mondays
        alldays = DayLocator()              # minor ticks on the days
        dayFormatter = DateFormatter('%d %b')
        weekFormatter = DateFormatter('%b %d')

        # Set plot parameters, including the axis object ax used for plotting
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        if plotdat.index[-1] - plotdat.index[0] < pd.Timedelta('730 days'):
            ax.xaxis.set_major_locator(mondays)
            #ax.xaxis.set_major_locator(alldays)
            #ax.xaxis.set_minor_locator(alldays)
            ax.xaxis.set_major_formatter(weekFormatter)

        else:
            weekFormatter = DateFormatter('%b %d')
            ax.xaxis.set_major_formatter(weekFormatter)

        ax.grid(True)
        # Create the candelstick chart

        candlestick_ohlc(ax, list(zip(list(date2num(plotdat.index.tolist())), plotdat["Open"].tolist(), plotdat["High"].tolist(),
                          plotdat["Low"].tolist(), plotdat["Close"].tolist())),
                          colorup = "green", colordown = "red", width = stick * .6, alpha = 0.5)


        plotdat["5d"] = np.round(plotdat["Close"].rolling(window = 5, center = False).mean(), 2)
        plotdat["10d"] = np.round(plotdat["Close"].rolling(window = 10, center = False).mean(), 2)
        plotdat["20d"] = np.round(plotdat["Close"].rolling(window = 20, center = False).mean(), 2)
        plotdat["50d"] = np.round(plotdat["Close"].rolling(window = 50, center = False).mean(), 2)
        plotdat["200d"] = np.round(plotdat["Close"].rolling(window = 200, center = False).mean(), 2)

        plotdat['Bol_upper'] = pd.rolling_mean(plotdat['Close'], window=5) + 2* pd.rolling_std(plotdat['Close'], 5, min_periods=3)
        plotdat['Bol_lower'] = pd.rolling_mean(plotdat['Close'], window=20) - 2* pd.rolling_std(plotdat['Close'], 20, min_periods=20)
        plotdat['Bol_BW'] = ((plotdat['Bol_upper'] - plotdat['Bol_lower'])/plotdat['20d'])*100
        #plotdat['Bol_BW_200MA'] = pd.rolling_mean(plotdat['Bol_BW'], window=50)#cant get the 200 daa
        #plotdat['Bol_BW_200MA'] = plotdat['Bol_BW_200MA'].fillna(method='backfill')##?? ,may not be good

        plotdat["w5d"] = plotdat["Close"].ewm(span= 5,adjust = False).mean()
        # Plot other series (such as moving averages) as lines
        if otherseries != None:
            if type(otherseries) != list:
                otherseries = [otherseries]
            plotdat.loc[: , otherseries].plot(ax = ax, lw = 2, grid = True)


        ax.xaxis_date()
        ax.autoscale_view()
        #ax.fill_between(ax.xaxis(),plotdat.loc[:,['Bol_lower']], plotdat.loc[:,['Bol_upper']])
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()
menu()
