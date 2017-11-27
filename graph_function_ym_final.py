"""
** graph_function_ym_copy.py for Programming-for-Python in /Users/Yuming/Programming-for-Python
**
** Made by Yuming Fu
** Login   <Yuming@epitech.net>
**
** Started on  Fri Nov 24 19:59:15 2017 Yuming Fu
** Last update Fri Nov 24 19:59:15 2017 Yuming Fu
"""
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MO, date2num
from matplotlib.finance import candlestick_ohlc
import numpy as np
import pandas as pd
import datetime
from sklearn import linear_model
import sys
import string

def menu():
    """Input is input() return p = Getcsv( the real input )."""

    # print(""" press 1 for      """)
    #print("please enter: ")
    #q = Stock(Csvfile("goog",timestart = "2017-05-01", timeend = "2017-10-01").get_data())
    # q.graph()
    # q.candlestick()
    #print(Companylist("Apple", case = True).a1)
    #Stock(Csvfile("GOOG",timestart = "2017-05-01", timeend = "2017-07-31").download("Ishaan3")).candlestick()
    #Predict(Csvfile("GOOG", timestart="2017-09-01", timeend="2017-10-01").get_data()).predict("2017-11-01")
    Stock(Csvfile("GOOG",timestart = "2016-01-01", timeend = "2017-01-25").download("dummy")).graph_with_bb()

class Ticker:
    """Self.correct_ticker_name ()
       self.possible_ticker(should be a list)
       self.possible_company_name(should be a list)"""

    def __init__(self, symbol, condition=False):
        company_list = pd.read_csv(
            "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download", usecols=[0, 1, 3])
        self.company_list = pd.DataFrame(data=company_list)
        user_input = symbol.strip().upper()
        self.a1 = []
        if user_input in set(company_list['Symbol']) and condition == True:
            # if self.company_list['Symbol'].str.match(str(user_input)) is True:
            self.a1 = self.company_list[self.company_list['Symbol'] == str(user_input)]
        else:
            a1 = self.company_list[self.company_list['Symbol'].str.contains(user_input[:-1])]
            self.test = "False"
            self.a1 = a1


class Companylist:
    def __init__(self, name, case=False):
        companylist = pd.read_csv(
            "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download", usecols=[0, 1, 3])
        self.companylist = pd.DataFrame(data=companylist)
        user_input = name
        self.a1 = []
        self.a1 = self.companylist[self.companylist['Name'].str.contains(user_input, case=case)]


class Csvfile:
    """Get csv file from """

    def __init__(self, Ticker="GOOG", timestart="2017-09-01", timeend="2017-11-01"):
        assert pd.to_datetime(timeend) - pd.to_datetime(timestart) >= pd.Timedelta('0 days'),\
            "sorry your enddate is earler than you startdate"
        self.ticker_name = Ticker.upper().strip()
        self.startdt = datetime.datetime.strptime(timestart, '%Y-%m-%d')
        self.startmonth = (self.startdt.strftime("%b"))
        self.enddt = datetime.datetime.strptime(timeend, '%Y-%m-%d')
        self.endmonth = (self.enddt.strftime("%b"))

    def get_data(self):
        url1 = 'http://finance.google.com/finance/historical?q='
        url2 = '&startdate='
        url3 = '&num=30&ei=NGoQWtDQFMGKUIuSsYgF&output=csv'
        self.url = url1 + self.ticker_name + url2 + self.startmonth + '+' + str(self.startdt.day) + '%2C+' + str(
            self.startdt.year) + '&enddate=' + str(self.endmonth) + '+' + str(self.enddt.day) + '%2C+' + str(self.enddt.year) + url3
        #self.url = url1 + str(ticker_name) + url2 + month_name1 + '+' + str(startdt.day) + '%2C+' + str(startdt.year) + '&enddate=' + month_name2 + '+' + str(enddt.day) + '%2C+' + str(enddt.year) + url3
        return self.url

    def download(self, name):
        df = pd.read_csv(self.get_data())
        df.to_csv(path_or_buf=str(name) + ".csv")
        return str(name) + ".csv"
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
        self.close_price = self.x.Close
        self.Date = pd.to_datetime(self.x['Date'])
        self.enddate = pd.to_datetime("2017-10-01")#pd.to_datetime(self.x.Date)
        self.std = np.std(self.x.Close)
        self.mean = np.mean(self.x.Close)
        self.percentile = self.x.Close.quantile([.25, .50, .75])
        self.describe = self.x.Open.describe()
        self.coef = self.std/self.mean
    def graph_with_MA(self):
        """this will plot graph for every element that is the class stock"""
        transdat = self.x.loc[:, ["Date", "Open", "High", "Low", "Close"]]
        transdat['Date'] = pd.to_datetime(transdat['Date'])
        transdat.set_index('Date', inplace=True)
        transdat["5d"] = np.round(transdat["Close"].rolling(window=5, center=False).mean(), 2)
        transdat["10d"] = np.round(transdat["Close"].rolling(window=10, center=False).mean(), 2)
        plt.plot(transdat.index, transdat.Close, lw = 1.8,label='Price')
        transdat["5d"].plot(lw=2, label= '5 day Moving average')
        transdat["10d"].plot(lw=1.9, label = '10 day Moving average')
        #plt.plot(self.Date, self.close_price[:], lw=1.8)
        #plt.xlim((-1, 5))
        #plt.ylim((-1, 5))
        # plt.axis("equal")
        plt.legend()
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()
        # plt.close()
        # graph(data,"test.png")
    def graph_without_ti(self):
        """this will plot graph for every element that is the class stock"""
        transdat = self.x.loc[:, ["Date", "Open", "High", "Low", "Close"]]
        transdat['Date'] = pd.to_datetime(transdat['Date'])
        transdat.set_index('Date', inplace=True)
        plt.plot(transdat.index, transdat.Close, lw = 1.8,grid = True ,lable = 'Price')
        plt.legend()
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()
    def graph_with_bb(self):
        transdat = self.x.loc[:, ["Date", "Open", "High", "Low", "Close"]]
        transdat['Date'] = pd.to_datetime(transdat['Date'])
        transdat.set_index('Date', inplace=True)
        transdat["bu"] = pd.rolling_mean(
            transdat['Close'], window=5) + 2 * pd.rolling_std(transdat['Close'], 5, min_periods=3)
        transdat["bd"] = pd.rolling_mean(
            transdat['Close'], window=20) - 2 * pd.rolling_std(transdat['Close'], 20, min_periods=20)
        plt.plot(transdat.index, transdat.Close, lw = 1.8,label='Price')
        transdat["bu"].plot(lw=2, label= 'Upper bollinger')
        transdat["bd"].plot(lw=1.9, label = 'Lower bollinger')
        #plt.plot(self.Date, self.close_price[:], lw=1.8)
        #plt.xlim((-1, 5))
        #plt.ylim((-1, 5))
        # plt.axis("equal")
        plt.legend()
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()
    def statistics(self):
        print(self.mean, self.std,self.describe)

    def candlestick(self, stick="day", otherseries=['5d', '10d', '20d', 'w5d', "Bol_upper", "Bol_lower"]):

        # Create a new DataFrame which includes OHLC data for each period specified by stick input
        transdat = self.x.loc[:, ["Date", "Open", "High", "Low", "Close"]]
        transdat['Date'] = pd.to_datetime(transdat['Date'])
        transdat.set_index('Date', inplace=True)
        if (type(stick) == str):
            if stick == "day":
                plotdat = transdat
                stick = 1  # Used for plotting
            elif stick in ["week", "month", "year"]:
                if stick == "week":
                    transdat["week"] = pd.to_datetime(transdat.index).map(
                        lambda x: x.isocalendar()[1])  # Identify weeks
                elif stick == "month":
                    transdat["month"] = pd.to_datetime(transdat.index).map(
                        lambda x: x.month)  # Identify months
                transdat["year"] = pd.to_datetime(transdat.index).map(
                    lambda x: x.isocalendar()[0])  # Identify years
                # Group by year and other appropriate variable
                grouped = transdat.groupby(list(set(["year", stick])))
                # Create empty data frame containing what will be plotted
                plotdat = pd.DataFrame({"Open": [], "High": [], "Low": [], "Close": []})
                for name, group in grouped:
                    plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0, 0],
                                                           "High": max(group.High),
                                                           "Low": min(group.Low),
                                                           "Close": group.iloc[-1, 3]},
                                                          index=[group.index[0]]))
                if stick == "week":
                    stick = 5
                elif stick == "month":
                    stick = 30
                elif stick == "year":
                    stick = 365

        elif (type(stick) == int and stick >= 1):
            transdat["stick"] = [np.floor(i / stick) for i in range(len(transdat.index))]
            grouped = transdat.groupby("stick")
            # Create empty data frame containing what will be plotted
            plotdat = pd.DataFrame({"Open": [], "High": [], "Low": [], "Close": []})
            for name, group in grouped:
                plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0, 0],
                                                       "High": max(group.High),
                                                       "Low": min(group.Low),
                                                       "Close": group.iloc[-1, 3]},
                                                      index=[group.index[0]]))

        else:
            raise ValueError(
                'Valid inputs to argument "stick" include the strings "day", "week", "month", "year", or a positive integer')

        mondays = WeekdayLocator(byweekday=MO)        # major ticks on the mondays
        alldays = DayLocator()              # minor ticks on the days
        dayFormatter = DateFormatter('%d %b')
        weekFormatter = DateFormatter('%b %d')

        # Set plot parameters, including the axis object ax used for plotting
        fig, ax = plt.subplots()
        fig.subplots_adjust(bottom=0.2)
        if plotdat.index[-1] - plotdat.index[0] < pd.Timedelta('730 days'):
            ax.xaxis.set_major_locator(mondays)
            # ax.xaxis.set_major_locator(alldays)
            # ax.xaxis.set_minor_locator(alldays)
            ax.xaxis.set_major_formatter(weekFormatter)

        else:
            weekFormatter = DateFormatter('%b %d')
            ax.xaxis.set_major_formatter(weekFormatter)

        ax.grid(True)
        # Create the candelstick chart

        candlestick_ohlc(ax, list(zip(list(date2num(plotdat.index.tolist())), plotdat["Open"].tolist(), plotdat["High"].tolist(),
                                      plotdat["Low"].tolist(), plotdat["Close"].tolist())),
                         colorup="green", colordown="red", width=stick * .6, alpha=0.5)

        plotdat["5d"] = np.round(plotdat["Close"].rolling(window=5, center=False).mean(), 2)
        plotdat["10d"] = np.round(plotdat["Close"].rolling(window=10, center=False).mean(), 2)
        plotdat["20d"] = np.round(plotdat["Close"].rolling(window=20, center=False).mean(), 2)
        plotdat["50d"] = np.round(plotdat["Close"].rolling(window=50, center=False).mean(), 2)
        plotdat["200d"] = np.round(plotdat["Close"].rolling(window=200, center=False).mean(), 2)
        plotdat['Bol_upper'] = pd.rolling_mean(
            plotdat['Close'], window=5) + 2 * pd.rolling_std(plotdat['Close'], 5, min_periods=3)
        plotdat['Bol_lower'] = pd.rolling_mean(
            plotdat['Close'], window=20) - 2 * pd.rolling_std(plotdat['Close'], 20, min_periods=20)
        #plotdat['Bol_BW'] = ((plotdat['Bol_upper'] - plotdat['Bol_lower']) / plotdat['20d']) * 100
        # plotdat['Bol_BW_200MA'] = pd.rolling_mean(plotdat['Bol_BW'], window=50)#cant get the 200 daa
        # plotdat['Bol_BW_200MA'] = plotdat['Bol_BW_200MA'].fillna(method='backfill')##?? ,may not be good
        plotdat["w5d"] = plotdat["Close"].ewm(span=5, adjust=False).mean()
        plotdat["w10d"] = plotdat["Close"].ewm(span=10, adjust = False).mean()
        # Plot other series (such as moving averages) as lines
        if otherseries != None:
            if type(otherseries) != list:
                otherseries = [otherseries]
            plotdat.loc[:, otherseries].plot(ax=ax, lw=2, grid=True)

        ax.xaxis_date()
        ax.autoscale_view()
        #ax.fill_between(ax.xaxis(),plotdat.loc[:,['Bol_lower']], plotdat.loc[:,['Bol_upper']])
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.show()




class Predict(Stock):
    def __init__(self,csvfile="GOOG.csv"):
        Stock.__init__(self)

    def predict_linear(self, date):
        linear_mod = linear_model.LinearRegression()
        dates = np.reshape(date2num(self.Date.tolist()), (len(self.Date), 1))  # converting to matrix of n X 1
        #dates = np.reshape(self.x.Date.tolist()), (len(self.x.Date), 1))
        # dates = self.x.Date
        # date2 = []
        # for row in dates:
        #     date2.append(int(row[0].split('-')[0]))
        # date2 = np.reshape(date2, (len(date2), 1))
        prices = np.reshape(self.close_price, (len(self.close_price), 1))
        linear_mod.fit(dates, prices)  # fitting the data points in the model
        #x = date2num(pd.to_datetime(date)) - date2num(self.enddate)
        x = pd.to_datetime(date) - self.enddate
        predicted_price = linear_mod.predict(736460+1000)
        plt.scatter(dates, prices, color='red')  # plotting the initial datapoints
    # plotting the line made by linear regression
        plt.plot(dates, linear_mod.predict(dates), color='blue', linewidth=3)
        plt.ylabel("")
        plt.xlabel("")
        plt.show()
        print(linear_mod.score(dates, prices),predicted_price[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0])
        print(prices[-1])



punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
data = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download")

def printLine (text = ''):
    print('X {: ^56} X'.format(text))

def printSelTitle (text = '', title = None):
    print('X{: ^9}'.format(text), end = ""),

def printSelCheck (text = '', title = None):
    print('X   [ ]   '.format(text), end = "")

def printBorder (title = None):
    print('X' * 60)

def printBox (*lines, title = None, showBottomBorder = False):
    printBorder(title)
    printLine()
    for line in lines:
        printLine(line)
    printLine()
    if showBottomBorder:
        printBorder()
def menu_1():
    printBox('Stock Analysis - Choose your stock' , showBottomBorder = False)
    printBox('Are you ready to start?', '-' * 21,\
             'Enter any key(except 1) to continue', '-' * 21,\
             'Enter 1 to quit' ,showBottomBorder = False)
    printBorder()
    p = input()
    if p == '1':
        printBox('Are you sure?', '-' * 21,\
        'press 1 to continue', '-' * 21,\
        'press any key to choose again(except 1)', showBottomBorder = True)
        p = str(input())
        if p == '1':
            print("\nThank you, hope you enjoyed our software!\n")
        else:
            menu_1()
    else:
        menu_2()
def menu_2():
    printBox('Stock Analysis',showBottomBorder = False)
    printBox('To analyze:' , '-' *21,\
             '1.Enter the name stock:', '-' * 21,\
             '2.Enter the name of the company:' , '-' * 21,\
             'To predict:','-' * 21,\
             '3.Enter the name stock:', '-' * 21,\
             '4.Enter the name of the company:' , '-' * 21,\
             '0.Quit.',showBottomBorder = False)
    printBox('please enter your option:', '-' * 21, showBottomBorder = False)
    p = str(input())
    if p == '1':
        menu_3()
    elif p == '2':
        menu_4()
    elif p == '0':
        menu_5()
    elif p == '3':
        menu_18()
    elif p == '4':
        menu_19()
    else:
        printBox('you can only choose from given number!',
        'Press any key to go back!', showBottomBorder = True )
        p = input()
        if input:
            menu_2()

def menu_3():
    printBox('Please enter the stock name:','-' * 21,\
    'press 0 to go back!',showBottomBorder = True)
    name = input()
    for i in punctuation:
        name = name.replace(i,"")
    if name == '0':
        menu_2()
    else:
        menu_17(name)
def menu_3_1():
    printBox('Please enter the stock name:','-' * 21,\
    'press 0 to go back!',showBottomBorder = True)
    name = input()
    for i in punctuation:
        name = name.replace(i,"")
    if name == '0':
        menu_2()
    else:
        menu_17_1(name)
def menu_4():
    printBox('Please enter the company name:','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_7(p)

def menu_4_1():
    printBox('Please enter the company name:','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_7_1(p)

def menu_5():
    printBox('Are you sure?', '-' * 21,\
    'press 1 to continue', '-' * 21,\
    'press any key to choose again(except 1)',showBottomBorder = True)
    p = str(input())
    if p == '1':
        print("Thank you, hope you enjoyed our software!")
    else:
        menu_2()

def menu_6(ticker = "419"):
    printBox('Please enter the start year for the stock(in format YYYY):','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    Y = input()
    for i in punctuation:
        Y = Y.replace(i,"")
    for i in letter:
        Y = Y.replace(i,"")
    if Y == '0':
        menu_2()
    elif len(str(Y)) == 4 and int(Y) < 2018:
        printBox('Please enter the start month for the stock(in format MM):','-' * 21,\
        'press 0 to go back!', showBottomBorder = True)
        printBox('{}-MM-DD'.format(Y),showBottomBorder = True)
        M = input()
        for i in punctuation:
            M = M.replace(i,"")
        for i in letter:
            M = M.replace(i,"")
        if M == '0':
            menu_2()
        elif len(str(M)) == 2 and 0 < int(M) < 13:
            printBox('Please enter the start day for the stock(in format DD):','-' * 21,\
            'press 0 to go back!')
            printBox('{}-{}-DD'.format(Y,M), showBottomBorder = True)
            D = input()
            for i in punctuation:
                D = D.replace(i,"")
            for i in letter:
                D = D.replace(i,"")
            if D == '0':
                menu_2()
            elif len(str(D)) == 2 and 0 < int(D) < 32:
                start_date = Y + '-' + M +'-' + D
                printBox('{}-{}-{}'.format(Y,M,D))
                menu_9(ticker,Y,M,D)
            else:
                go_back_6()
        else:
            go_back_6()
    else:
        print("you are here")
        go_back_6()
    #return start_date
def go_back_6():
    printBox('Please enter it in correct format!','-' * 21,\
    'Press anykey to go back!', showBottomBorder = True)
    p = input()
    if p:
        menu_6()
    else:
        menu_6()

def menu_9(ticker = "419",Y = "2017",D = "09"  ,M = "09"):
    printBox('Please enter the end year for the stock(in format YYYY):','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    y = input()
    for i in punctuation:
        y = y.replace(i,"")
    for i in letter:
        y = y.replace(i,"")
    if y == '0':
        menu_2()
    elif len(str(y)) == 4 and int(y) < 2018:
        printBox('Please enter the end month for the stock(in format MM):','-' * 21,\
        'press 0 to go back!')
        printBox('{}-MM-DD'.format(y), showBottomBorder = True)
        m = input()
        for i in punctuation:
            m = m.replace(i,"")
        for i in letter:
            m = m.replace(i,"")
        if m == '0':
            menu_2()
        elif len(str(m)) == 2 and 0 < int(m) < 13:
            printBox('Please enter the end day for the stock(in format DD):','-' * 21,\
            'press 0 to go back!', showBottomBorder = False)
            printBox('{}-{}-DD'.format(y,m), showBottomBorder = True)
            d = input()
            for i in punctuation:
                d = d.replace(i,"")
            for i in letter:
                d = d.replace(i,"")
            if d == '0':
                menu_2()
            elif len(str(d)) == 2 and 0 < int(d) < 32:
                end_date = y + '-' + m +'-' + d
                printBox('{}-{}-{}'.format(m,y,d), showBottomBorder = True)
                #return end_date
                menu_8(ticker,Y,D,M,y,d,m)
            else:
                printBox('Please enter it in correct format!','-' * 21,\
                'press any key to go back!', showBottomBorder = True)
                if input():
                    menu_9()
        else:
            printBox('Please enter it in correct format!','-' * 21,\
            'press any key to go back!', showBottomBorder = True)
            if input():
                menu_9()
    else:
        printBox('Please enter it in correct format!','-' * 21,\
        'press any key to go back!', showBottomBorder = True)
        if input():
            menu_9()
    #return end_date

def menu_8(ticker,Y,D,M,y,d,m):
    printBox('1.Visualise it in candlestick without technique indicators','-' * 21,\
    '2.Visualise it in candlestick with Moving averages!','-' * 21,\
    '3.Visualise it in candlestick with MA and Weighted MA','-' * 21,\
    '4.Visualise it in candlestick with all technique indicaters','-' * 21,\
    '5.Visualise it in candlestick with only bollinger bands', '-' * 21, \
    '6.Visualise it in lines with no technique indicators', '-' * 21, \
    '7.Visualise it in lines with moving averages' , '-' *21, \
    '8.Visualise it in lines with another stock to compare' , '-' * 21, \
    '9.Go to statistics menu', '-' * 21, \
    '0. go back to pervious slides',showBottomBorder = True )
    p = input()
    if p == '1':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=None)
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '2':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=['5d', '10d', '20d'])
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '3':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=['5d', '10d', '20d','w5d','w10d'])
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '4':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=['10d', '20d','w5d',"Bol_upper", "Bol_lower"])
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '5':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=["Bol_upper", "Bol_lower"])
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '6': #line
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).graph_without_ti()
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '7':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).graph_with_MA()
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '8':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).graph_with_bb()
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '9':
        menu_sta(ticker,Y,D,M,y,d,m)
    elif p == '0':
        menu_6()
    else:
        printBox('you can only choose from given number!',
        'Press any key to go back!', showBottomBorder = True )
        p = input()
        if input:
            menu_8(ticker,Y,D,M,y,d,m)
def menu_sta(ticker,Y,D,M,y,d,m):
    printBox('1. Describe statistics', '-' * 21,\
    '2.Mean of the period', '-' * 21,\
    '3.Quantile', '-' * 21,\
    '4.Standard variation', '-' *21,\
    '5.Coefficient of variation', '-' *21,\
    '0. go back to pervious menu', showBottomBorder = False)
    p = input()
    if p == '1':
        tickern = data.Symbol.iloc[int(ticker)]
        print(Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).describe)
        menu_sta(ticker,Y,D,M,y,d,m)
    elif p == '2':
        tickern = data.Symbol.iloc[int(ticker)]
        print(Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).mean)
        menu_sta(ticker,Y,D,M,y,d,m)
    elif p == '3':
        tickern = data.Symbol.iloc[int(ticker)]
        print(Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).percentile)
        menu_sta(ticker,Y,D,M,y,d,m)
    elif p == '4':
        tickern = data.Symbol.iloc[int(ticker)]
        print(Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).mean)
        menu_sta(ticker,Y,D,M,y,d,m)
    elif p == '5':
        tickern = data.Symbol.iloc[int(ticker)]
        print(Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).coef)
        menu_sta(ticker,Y,D,M,y,d,m)

    elif p == '0':
        menu_8(ticker,Y,D,M,y,d,m)

    else:
        printBox('you can only choose from given number!',
        'Enter any key to go back!', showBottomBorder = True )
        p = input()
        if p:
            menu_sta()
        else:
            menu_sta()

def menu_14():
    printBox('1. only graph the time series', '-' * 21,\
    '2.      ', '-' * 21,\
    '0. go back to pervious slides', showBottomBorder = True)
    p = input()
    if p == '1':
        menu_15()
    elif p == '2':
        menu_16()
    elif p == '0':
        menu_8()
    else:
        printBox('you can only choose from given number!',
        'Press any key to go back!', showBottomBorder = True )
        p = input()
        if input:
            menu_14()

def menu_7(p):
    print(Companylist(p, case=False).a1)
    print("Is the company there?")
    ticker = input("If yes please enter the index number of the stock, if you see an empty list \n \
    or your stock is not here please enter the world: back to try again: ")
    if ticker == "back":
        menu_4_1()
    else:
        menu_6(ticker)
def menu_7_1(p):
    print(Companylist(p, case= True).a1)
    print("Is the company there?")
    ticker = input("If yes please enter the index number of the stock, if you see an empty list \n \
    or your stock is not here please enter the world: back to try again: ")
    if ticker == "back":
        menu_4_1()
    else:
        menu_6(ticker)

def menu_17(name):
    """ stock name"""
    print(Ticker(name, condition = True).a1)
    print("Is your stock there?")
    ticker = input("If yes please enter the index number of the stock, if you see an empty list \n \
    or your stock is not here please enter back to try again: ")
    if ticker == "back":
        menu_3_1()
    else:
        menu_6(ticker)
def menu_17_1(name):
    """ stock name"""
    print(Ticker(name, condition = False).a1)
    print("Is your stock there?")
    ticker = input("if yes Please enter the index number of the stock, or enter back to enter the ticker name again")
    if ticker == "back":
        menu_3_1()
    else:
        menu_6(ticker)
#def menu_10():graph it
#def menu_11():mean
#def menu_12():add a new stock compare
#def menu_13():
#def menu_15():only graph series
#def menu_16():
#def menu_20(): stock name --> menu_22
#def menu_21(): company name --> menu_22
def menu_18():
    printBox('Please enter the stock name:','-' * 21,\
    'press 0 to go back!',showBottomBorder = True)
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_18_1(p)
def menu_18_3():
    printBox('Please enter the stock name:','-' * 21,\
    'press 0 to go back!',showBottomBorder = True)
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_18_2(p)

def menu_18_1(name):
    """ stock name"""
    print(Ticker(name, condition = True).a1)
    print("Is your stock there?")
    ticker = input("If yes please enter the index number of the stock, if you see an empty list \n \
    or your stock is not here please enter back to try again: ")
    if ticker == "back":
        menu_18_3()
    else:
        menu_20(ticker)
def menu_18_2(name):
    """ stock name"""
    print(Ticker(name, condition = False).a1)
    print("Is your stock there?")
    ticker = input("if yes Please enter the index number of the stock, or enter back to enter the ticker name again")
    if ticker == "back":
        menu_18_3()
    else:
        menu_20(ticker)

def menu_19():
    printBox('Please enter the company name:','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_19_1()

def menu_19_3():
    printBox('Please enter the company name:','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_19_2()

def menu_19_1(p):
    print(Companylist(p, case=False).a1)
    print("Is the company there?")
    ticker = input("If yes please enter the index number of the stock, if you see an empty list \n \
    or your stock is not here please enter the world: back to try again: ")
    if ticker == "back":
        menu__19_3()
    else:
        menu_20(ticker)
def menu_19_2(p):
    print(Companylist(p, case= True).a1)
    print("Is the company there?")
    ticker = input("If yes please enter the index number of the stock, if you see an empty list \n \
    or your stock is not here please enter the world: back to try again: ")
    if ticker == "back":
        menu_19_1()
    else:
        menu_20(ticker)


def menu_20(ticker = "419"):
    printBox('Please enter the start year for the stock(in format YYYY):','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    Y = input()
    for i in punctuation:
        Y = Y.replace(i,"")
    for i in letter:
        Y = Y.replace(i,"")
    if Y == '0':
        menu_2()
    elif len(str(Y)) == 4 and int(Y) < 2018:
        printBox('Please enter the start month for the stock(in format MM):','-' * 21,\
        'press 0 to go back!', showBottomBorder = True)
        printBox('{}-MM-DD'.format(Y),showBottomBorder = True)
        M = input()
        for i in punctuation:
            M = M.replace(i,"")
        for i in letter:
            M = M.replace(i,"")
        if M == '0':
            menu_2()
        elif len(str(M)) == 2 and 0 < int(M) < 13:
            printBox('Please enter the start day for the stock(in format DD):','-' * 21,\
            'press 0 to go back!')
            printBox('{}-{}-DD'.format(Y,M), showBottomBorder = True)
            D = input()
            for i in punctuation:
                D = D.replace(i,"")
            for i in letter:
                D = D.replace(i,"")
            if D == '0':
                menu_2()
            elif len(str(D)) == 2 and 0 < int(D) < 32:
                start_date = Y + '-' + M +'-' + D
                printBox('{}-{}-{}'.format(Y,M,D))
                menu_21(ticker,Y,M,D)
            else:
                go_back_20()
        else:
            go_back_20()
    else:
        print("you are here")
        go_back_20()
    #return start_date
def go_back_20():
    printBox('Please enter it in correct format!','-' * 21,\
    'Press anykey to go back!', showBottomBorder = True)
    p = input()
    if p:
        menu_20()
    else:
        menu_20()

def menu_21(ticker = "419",Y = "2017",D = "09"  ,M = "09"):
    printBox('Please enter the end year for the stock(in format YYYY):','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    y = input()
    for i in punctuation:
        y = y.replace(i,"")
    for i in letter:
        y = y.replace(i,"")
    if y == '0':
        menu_2()
    elif len(str(y)) == 4 and int(y) < 2018:
        printBox('Please enter the end month for the stock(in format MM):','-' * 21,\
        'press 0 to go back!')
        printBox('{}-MM-DD'.format(y), showBottomBorder = True)
        m = input()
        for i in punctuation:
            m = m.replace(i,"")
        for i in letter:
            m = m.replace(i,"")
        if m == '0':
            menu_2()
        elif len(str(m)) == 2 and 0 < int(m) < 13:
            printBox('Please enter the end day for the stock(in format DD):','-' * 21,\
            'press 0 to go back!', showBottomBorder = False)
            printBox('{}-{}-DD'.format(y,m), showBottomBorder = True)
            d = input()
            for i in punctuation:
                d = d.replace(i,"")
            for i in letter:
                d = d.replace(i,"")
            if d == '0':
                menu_2()
            elif len(str(d)) == 2 and 0 < int(d) < 32:
                end_date = y + '-' + m +'-' + d
                printBox('{}-{}-{}'.format(y,d,m), showBottomBorder = True)
                #return end_date
                menu_pred(ticker,Y,D,M,y,d,m)
            else:
                printBox('Please enter it in correct format!','-' * 21,\
                'press any key to go back!', showBottomBorder = True)
                if input():
                    menu_21(ticker,Y,M,D)
        else:
            printBox('Please enter it in correct format!','-' * 21,\
            'press any key to go back!', showBottomBorder = True)
            if input():
                menu_21(ticker,Y,M,D)
    else:
        printBox('Please enter it in correct format!','-' * 21,\
        'press any key to go back!', showBottomBorder = True)
        if input():
            menu_21(ticker,Y,M,D)

def menu_pred(ticker,Y,D,M,y,d,m):
    printBox('1.Visualise it in candlestick without technique indicators','-' * 21,\
    '2.Visualise it in candlestick with Moving averages!','-' * 21,\
    '3.Go to Analysis menu', '-' * 21, \
    '0. go back to pervious slides',showBottomBorder = True )
    p = input()
    if p == '1':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=None)
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '2':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=['5d', '10d', '20d'])
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '3':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=['5d', '10d', '20d','w5d','w10d'])
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '4':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=['10d', '20d','w5d',"Bol_upper", "Bol_lower"])
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '5':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).candlestick(otherseries=["Bol_upper", "Bol_lower"])
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '6': #line
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).graph_without_ti()
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '7':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).graph_with_MA()
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '8':
        tickern = data.Symbol.iloc[int(ticker)]
        Stock(Csvfile(str(tickern),timestart = Y+'-'+D+'-'+ M, timeend = y+'-'+d+'-'+ m).download(str(tickern))).graph_with_bb()
        menu_8(ticker,Y,D,M,y,d,m)
    elif p == '9':
        menu_sta(ticker,Y,D,M,y,d,m)
    elif p == '0':
        menu_6()
    else:
        printBox('you can only choose from given number!',
        'Press any key to go back!', showBottomBorder = True )
        p = input()
        if input:
            menu_8(ticker,Y,D,M,y,d,m)
    #return end_date
#def menu_23(): predict

menu_1()
# menu()
