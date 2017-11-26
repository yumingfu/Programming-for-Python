import csv
import pandas as pd
import datetime
import urllib
import sys

def welcome_menu():
	print("Welcome to ONE Stock at a time Analysis")

	return 0

def main():
	choice = stock_menu()
	while True:
		tickr = get_tickr(int(choice))
		if tickr == 1:
			#looping till we get a correct tickr
			print ("Invalid Company, Going back... ")
			continue
		else:
			#we're happy with the value given and ready to exit the loop.
			break
	continue_menu()

	#Taking user input for start date
	while True:
		startdt = validate1(input("Enter Start Date yyyy-mm-dd :"))
		if not startdt:
			print ("Invalid date")
		else:
			break
	#Taking user input for end date
	while True:
		enddt = validate1(input("Enter End Date yyyy-mm-dd :"))
		if not enddt:
			print ("Invalid date")
		else:
			break
    #Downloading the data as needed by user
	get_data(tickr,startdt,enddt)
	print("\nRelevant data for the selected stocks have been downloaded")

def get_tickr(choice):
	if choice == 3:
		exit()
	#reading the companylist and extracting tickr name and company name
	company_list = pd.read_csv('companylist.csv')
	a=pd.DataFrame(data=company_list, columns=['Symbol','Name']) #extracting 2 columns

	if choice == 1:
		name = input("Enter the name of company :")
		a1 = a[a['Name']==name]
		if a1.empty: #if no match
			print("Invalid choice, write exact name of company")
			tickr = 1
		else:
			print(a1, "\nFollowing choice has been made")
			tickr = a1.iloc[0]['Symbol']
		return tickr
	if choice == 2:
		tickr_in = input("Enter the ticker value :").upper() #converting to uppercase by default
		a1 = a[a['Symbol']==tickr_in]
		if a1.empty: #if no match
			print("Invalid ticker value")
			tickr = 1
		else:
			print(a1, "\nFollowing choice has been made")
			tickr = a1.iloc[0]['Symbol']
		return tickr

def stock_menu():
	print("STOCK MENU \n\nEnter Full listed name of company (with caps and punctuations like ., etc) or official ticker")
	print("1. Company Name \n2. Ticker Value \n3. Exit ")
	while True:
		choice_1 = input("Enter your choice (1, 2 or 3): ")
		if choice_1 not in ["1","2","3"] :
			#looping till we get a correct tickr
			print ("Invalid choice, try again... ")
			continue
		else:
			#we're happy with the value given and ready to exit the loop.
			return choice_1

def continue_menu():
	print("\nDo you wish to continue???")
	print("1. Continue \n2. Exit")
	while True:
		choice_2 = input("Enter your choice (1 or 2): ")
		if choice_2 == "2":
			exit()
		elif choice_2 not in ["1","2"] :
			#looping till we get a correct tickr
			print ("Invalid choice, try again... ")
			continue
		else:
			#we're happy with the value given and ready to exit the loop.
			break


def validate1(date_1):
	try:
		return datetime.datetime.strptime(date_1,'%Y-%m-%d')
	except (NameError, ValueError):
		return False
	else:
		return True


def get_data(tickr, startdt, enddt):
	url_ske1='http://finance.google.com/finance/historical?q='
	url_ske2='&num=30&ei=NGoQWtDQFMGKUIuSsYgF&output=csv'
	month_name1 = startdt.strftime("%b")
	month_name2 = enddt.strftime("%b")

	url = url_ske1 + str(tickr) + '&startdate=' + month_name1 + '+' + str(startdt.day) + '%2C+' + str(startdt.year) + '&enddate=' + month_name2 + '+' + str(enddt.day) + '%2C+' + str(enddt.year) + url_ske2
	response = urllib.request.urlopen(url)
	html = response.read()

	with open('output.csv', 'wb') as f:
		f.write(html)
	return 0

#############################################################################################
def main_menu_choice_2():
    print ("Are you sure you would like to choose another stock?\n")
    statistics_choice_2= input("Yes/No")
    if statistics_choice_2 == "Yes":
        print("Bringing you back to Stock Menu.")
        #stock_menu()
    elif statistics_choice_2 == "No":
        main_menu()
    else:
        print("Sorry that option does not exist, please choose again.\n")
        main_menu_choice_2()
################################################################################
def print_top_border():
    print("/" + "-" * 80 + "\\")

def print_skipline():
    print("|"+" "*80 + "|")

def print_separate_line():
    print("|" + "-" * 80 + "|")

def print_choice(S,t): # S argument to input choice required in form of string,t argument to input tabs
    print("| " + S + "\t"*t + " |")

def print_bottom_border():
    print("\\" + "-" * 80 + "/")
#######################################################################################
#put in prediction option
def analysis_menu():
    #print("Welcome to the Main Menu!\n What analysis would you like for the financial data you have chosen? \n 1.Descriptive statistics \n 2.Graphs  \n 3. Choose a different stock \n 4.End Program")
    print_top_border()
    print_skipline()
    print("|\t\t\t Welcome to the Analysis Menu!" + "\t\t\t\t | ")
    print_skipline()
    print_separate_line()
    print_choice("What analysis would you like to perform on the stock you have chosen?", 2)
    print_skipline()
    print_choice("1.Descriptive statistics",7)
    print_choice("2.Graphs", 9)
    print_choice("3.Choose a different stock",7)
    print_choice("4.Exit Program",8)
    print_skipline()
    print_bottom_border()

    analysis_menu_choice= input("Please Enter choice 1,2,3 or 4:\n")

    if analysis_menu_choice == "1":
        print_top_border()
        print_choice("\t You have chosen the Descriptive Statistics Option.",3)
        print_bottom_border()
        Descriptive_statistics_menu()

    elif analysis_menu_choice== "2":
        print_top_border()
        print_choice("\t You have chosen the Graphs option.",5)
        print_skipline()
        print_bottom_border()

    elif analysis_menu_choice == "3":
        print_top_border()
        print_choice("\t\t\t Returning to Main Menu.",5)
        print_skipline()
        print_bottom_border()
        main_menu_choice_2()

    elif main_menu_choice=="4":
        sys.exit()
    else:
        print_top_border()
        print_choice("This choice does not exist. Please choose again.",3)
        print_skipline()
        print_bottom_border()
        print("\n")
        analysis_menu()


#def statistics_menu():
    #print("Statistics Menu /n 1. Descriptive statistics /n 2.Graphical Statistics  /n 3. Back to Analytics Menu")

    #tatistics_choice= input("Please Enter choice 1,2 or 3 :")

    #if statistics_choice == "1":
        #print("You have chosen the Descriptive Statistics Menu")
        #Descriptive_statistics_menu()
    #elif statistics_choice == "2":
        #print("correct choice")
    #elif statistics_choice == "3":
        #print ("correct choice")
    #else:
        #print ("Incorrect choice")
############################################################
#functions for each choice within Descriptive_Statistics menu
def Descriptive_choice_1():
    print("Descriptive_Statistics for Open prices:\n")
    print(df.Open.describe(percentiles= [.25,.5,.75]))

def Descriptive_choice_2():
    print("Descriptive_Statistics for High prices:\n")
    print(df.High.describe(percentiles= [.25,.5,.75]))

def Descriptive_choice_3():
    print("Descriptive_Statistics for Low prices:\n")
    print(df.Low.describe(percentiles= [.25,.5,.75]))

def Descriptive_choice_4():
    print("Descriptive_Statistics for Close prices:\n")
    print(df.Close.describe(percentiles= [.25,.5,.75]))

#def Descriptive_choice_5():
    #print("Descriptive_Statistics for Open prices:")
    #print(data.Adj Close.describe(percentiles= [.25,.5,.75]))

def Descriptive_choice_6():
    print("Descriptive_Statistics for Volume:\n")
    print(df.Volume.describe(percentiles= [.25,.5,.75]))

def Descriptive_choice_7():
    print("Descriptive Statistics for all: \n")

    print(df.describe(percentiles= [.25,.5,.75]))

def Descriptive_sub_menu():
    print("Descriptive statistics executed. \n\n What would you like to do next?:\n\n 1.Return to Descriptive Statistics Menu \n 2.Exit Program \n")
    input_choice_sub_menu=input("Please choose option number from above:")
    if input_choice_sub_menu=="1":
        Descriptive_statistics_menu()
    elif input_choice_sub_menu=="2":
        sys.exit()
    else:
        print("This choice does not exist, please choose again.")



############################################################################################
#Descriptive Statistics Menu function

def Descriptive_statistics_menu():
    #print("Descriptive Statistics Menu \n 1.Open \n 2.High \n 3.Low \n 4.Close \n 5.Adj Close \n 6.Volume \n 7.All \n 8.Back to Main Menu\n 9.End Program\n")
    print_top_border()
    print_skipline()
    print_choice("\t\t\t Descriptive Statistics Menu",4)
    print_skipline()
    print_separate_line()
    print("|1.Open"+"\t"*10+" |"+"\n"+ "|2.High"+"\t"*10+" |"+ "\n"+ "|3.Low"+"\t"*10+" |" )
    print("|4.Close"+"\t"*9+" |"+"\n"+ "|5.Adj Close"+"\t"*9+" |"+ "\n"+ "|6.Volume"+"\t"*9+" |" )
    print("|7.All"+"\t"*10+" |"+"\n"+ "|8.Back to Main Menu"+"\t"*8+" |"+ "\n"+ "|9.End Program"+"\t"*9+" |" )
    #print("Descriptive Statistics Menu \n 1.Open \n 2.High \n 3.Low \n 4.Close \n 5.Adj Close \n 6.Volume \n 7.All \n 8.Back to Main Menu\n 9.End Program\n")
    print_bottom_border()
    print("\n")

    Descriptive_choice = input('Please choose:')

    if Descriptive_choice == "1":
        print("fetching Descriptive Statistics for:Open\n")
        Descriptive_choice_1()
        print("\n")
        Descriptive_sub_menu()
    elif Descriptive_choice== "2":
        print("fetching Descriptive Statistics for:High\n")
        Descriptive_choice_2()
        print("\n")
        Descriptive_sub_menu()
    elif Descriptive_choice == "3":
        print("fetching Descriptive Statistics for:Low\n")
        Descriptive_choice_3()
        print("\n")
        Descriptive_sub_menu()
    elif Descriptive_choice == "4":
        print("fetching Descriptive Statistics for:Close\n")
        Descriptive_choice_4()
        print("\n")
        Descriptive_sub_menu()
    elif Descriptive_choice == "5":
        print("fetching Descriptive Statistics for: Adj Close")
    elif Descriptive_choice == "6":
        print("fetching Descriptive Statistics for: Volume")
        Descriptive_choice_6()
        print("\n")
        Descriptive_sub_menu()
    elif Descriptive_choice == "7":
        print("fetching Descriptive Statistics for: All")
        Descriptive_choice_7()
        print("\n")
        Descriptive_sub_menu()

    elif Descriptive_choice == "8":
        print("Returning to Main Menu ")
        analysis_menu()
    elif Descriptive_choice == "9":
        sys.exit()

    else:
        print("Sorry this choice does not exist, please choose again")
        Descriptive_statistics_menu()


welcome_menu()
main()
df= pd.read_csv("output.csv")
print(df.head())

analysis_menu()
