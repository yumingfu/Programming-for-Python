def menu_1():
    p = input("""        1. (fuzzy) looking for a specific stock with ticker name.
	2. (fuzzy) looking for the stock for specific company.
	3. Browse all the stock.
	4. News search
    Please enter your option number: """)
    try:
        if isinstance(int(p), int):
            if int(p) == 1:
                menu_2()
            elif int(p) == 2:
                menu_3()
            elif int(p) == 3:
                menu_4()
            elif int(p) == 4:
                menu_5()
            else:
                print("""you can only choose from given number""")
                menu_1()
    except:
        print("""you can only choose from given number""")
        menu_1()



def menu_2():
    stock_name = int(input("""        please enter the ticker name :
    press 0 to go back!"""))
    # if stock_name in Userinput().correct_ticker_name:
    #     menu_3()
    # else:
    #     menu_2_1()

    if stock_name == 0:
        menu_3()
    else:
        print("""you can only choose from given number""")
        menu_2()

def menu_3():
    stock_range = int(input("""        1.Please enter the date range:
    2. go back to pervious menu."""))
    if stock_range == 1:
        menu_6()
    elif stock_range == 2:
        menu_2()
def menu_2_1():
    #for i in range(len(Userinput().possible_ticker_name)):
        #print(i)
    choice_1 = int(input("""       Sorry we are unsure what you are looking for? Is this what you want:
    1. apple Inc. apple
    2. alphch  aplech
    9. go back to the pervious menu.
    0. not in the list"""))
    if choice_1 == 1:
        menu_6()
    if choice_1 == 2:
        menu_6()
    if choice_1 == 9:
        menu_2()
    if choice_1 == 0:
        menu_7()

def menu_6():
    with_date_range = int(str("""        1. graph it
    2. show the mean
    3. add a new stock to compare!
    4.
    0. go back to pervious slides."""))
    if with_date_range == 1:
        menu_8()
    if with_date_range == 2:
        menu_9()
    if with_date_range == 3:
        menu_10()
    if with_date_range == 4:
        menu_11()
    if with_date_range == 0:
        menu_6()
def menu_8():
    graph = int(input("""        1. only graph the time series (by default).
    2. """))
    if graph == 1:
        menu_12()
    if graph == 2:
        menu_13()
#def menu_4():
#def menu_5():
#def menu_7():
#def menu_9():
#def menu_10():
#def menu_11():
#def menu_12():
#def menu_13():

menu_1()
