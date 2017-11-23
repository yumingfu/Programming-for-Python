def printLine (text = ''):
    print('X {: ^60} X'.format(text))

def printSelTitle (text = '', title = None):
    print('X{: ^10}'.format(text), end = ""),

def printSelCheck (text = '', title = None):
    print('X   [ ]   '.format(text), end = "")

def printBorder (title = None):
    print('X' * 68)

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
             'Press any key to continue', '-' * 21, showBottomBorder = True)
    printSelTitle('TASK1'), printSelTitle('TASK2'),\
            printSelTitle('TASK3'), printSelTitle('TASK4'),\
            printSelTitle('TASK5'), print("X")
    printSelCheck(), printSelCheck(), printSelCheck(),\
                     printSelCheck(), printSelCheck(), print("X")
    printBorder()
    p = input()
    if input:
        menu_2()
def menu_2():
    printBox('Stock Analysis')
    printBox('1.Enter the name stock:', '-' * 21,\
             '2.Enter the name of the tickr:', '-' * 21,\
             '3.Enter the name of the company:' , showBottomBorder = True)
    printBorder()
    printBox('please enter your option:', '-' * 21, showBottomBorder = False)
    p = int(input())
    if p == 0:
        menu_1()
menu_1()
