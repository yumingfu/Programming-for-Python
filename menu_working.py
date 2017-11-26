import sys
import string
punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

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
    printBox('Stock Analysis - Choose your stock')
    printBox('Are you ready to start?', '-' * 21,\
             'Press any key(except 1) to continue', '-' * 21,\
             'Press 1 to quit' ,showBottomBorder = True)
    printSelTitle('TASK1'), printSelTitle('TASK2'),\
            printSelTitle('TASK3'), printSelTitle('TASK4'),\
            printSelTitle('TASK5'), print("X")
    printSelCheck(), printSelCheck(), printSelCheck(),\
                     printSelCheck(), printSelCheck(), print("X")
    printBorder()
    p = input()
    if p == '1':
        printBox('Are you sure?', '-' * 21,\
        'press 1 to continue', '-' * 21,\
        'press any key to choose again(except 1)', showBottomBorder = True)
        p = input()
        if int(p) == 1:
            print("\nThank you, hope you enjoyed our software!\n")
        else:
            menu_1()
    else:
        menu_2()
def menu_2():
    printBox('Stock Analysis',showBottomBorder = False)
    printBox('To analyze:',showBottomBorder = False)
    printBox('1.Enter the name stock:', '-' * 21,\
             '2.Enter the name of the company:' , '-' * 21,\
             '0.Quit.',showBottomBorder = False)
    printBox('To predict:', showBottomBorder = False)
    printBox('3.Enter the name stock:', '-' * 21,\
             '4.Enter the name of the company:' , '-' * 21,\
             '0.Quit.',showBottomBorder = False)
    printBox('please enter your option:', '-' * 21, showBottomBorder = True)
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
    punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_17()
def menu_4():
    printBox('Please enter the company name:','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_7()



def menu_5():
    printBox('Are you sure?', '-' * 21,\
    'press 1 to continue', '-' * 21,\
    'press any key to choose again(except 1)',showBottomBorder = True)
    p = input()
    if int(p) == 1:
        print("XXX  Thank you, hope you enjoyed our software! XXXXX")
    else:
        menu_2()

def menu_6():
    printBox('Please enter the start year for the stock(in format YYYY):','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
    letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
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
        punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
        letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
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
            #punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
            #letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
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
                menu_9()
            else:
                printBox('Please enter it in correct format!','-' * 21,\
                'press any key to go back!', showBottomBorder = True)
                if input():
                    menu_6()
        else:
            printBox('Please enter it in correct format!','-' * 21,\
            'press any key to go back!', showBottomBorder = True)
            if input():
                menu_6()
    else:
        printBox('Please enter it in correct format!','-' * 21,\
        'press any key to go back!', showBottomBorder = True)
        if input():
            menu_6()
    return start_date


def menu_9():
    printBox('Please enter the end year for the stock(in format YYYY):','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
    letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
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
        punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
        letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
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
            punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
            letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
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
                return end_date
                menu_8()
            else:
                printBox('Please enter it in correct format!','-' * 21,\
                'press any key to go back!', showBottomBorder = True)
                if input():
                    menu_6()
        else:
            printBox('Please enter it in correct format!','-' * 21,\
            'press any key to go back!', showBottomBorder = True)
            if input():
                menu_6()
    else:
        printBox('Please enter it in correct format!','-' * 21,\
        'press any key to go back!', showBottomBorder = True)
        if input():
            menu_6()
    return end_date

def menu_8():
    printBox('1. graph it !','-' * 21,\
    '2. show the mean!','-' * 21,\
    '3. add a new stock to compare','-' * 21,\
    '4.     ','-' * 21,\
    '0. go back to pervious slides',showBottomBorder = True )
    p = input()
    if p == '1':
        menu_10()
    elif p == '2':
        menu_11()
    elif p == '3':
        menu_12()
    elif p == '4':
        menu_13()
    elif p == '0':
        menu_6()
    else:
        printBox('you can only choose from given number!',
        'Press any key to go back!', showBottomBorder = True )
        p = input()
        if input:
            menu_8()

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

#def menu_7():searching company name --> menu_9
#def menu_17(): stock name  --> menu_9
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
    punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_20()

def menu_19():
    printBox('Please enter the company name:','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
    p = input()
    for i in punctuation:
        p = p.replace(i,"")
    if p == '0':
        menu_2()
    else:
        menu_21()
def menu_22():
    printBox('Please enter the year of the predict date(in format YYYY):','-' * 21,\
    'press 0 to go back!', showBottomBorder = True)
    punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
    letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    Y = input()
    for i in punctuation:
        Y = Y.replace(i,"")
    for i in letter:
        Y = Y.replace(i,"")
    if Y == '0':
        menu_2()
    elif len(str(Y)) == 4:
        printBox('Please enter the month of the predict date(in format MM):','-' * 21,\
        'press 0 to go back!', showBottomBorder = True)
        printBox('{}-MM-DD'.format(Y),showBottomBorder = True)
        punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
        letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
        M = input()
        for i in punctuation:
            M = M.replace(i,"")
        for i in letter:
            M = M.replace(i,"")
        if M == '0':
            menu_2()
        elif len(str(M)) == 2 and 0 < int(M) < 13:
            printBox('Please enter the day of the predict date(in format DD):','-' * 21,\
            'press 0 to go back!')
            punctuation = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';',':','"',"'",',','.','/','<','>','?']
            letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
            printBox('{}-{}-DD'.format(Y,M), showBottomBorder = True)
            D = input()
            for i in punctuation:
                D = D.replace(i,"")
            for i in letter:
                D = D.replace(i,"")
            if D == '0':
                menu_2()
            elif len(str(D)) == 2 and 0 < int(D) < 32:
                predict_date = Y + '-' + M +'-' + D
                printBox('{}-{}-{}'.format(Y,M,D),showBottomBorder = True)
                menu_23()
            else:
                printBox('Please enter it in correct format!','-' * 21,\
                'press any key to go back!', showBottomBorder = True)
                if input():
                    menu_22()
        else:
            printBox('Please enter it in correct format!','-' * 21,\
            'press any key to go back!', showBottomBorder = True)
            if input():
                menu_22()
    else:
        printBox('Please enter it in correct format!','-' * 21,\
        'press any key to go back!', showBottomBorder = True)
        if input():
            menu_22()
    return predict_date
#def menu_23(): predict





menu_1()
