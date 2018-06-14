import os
from constants import *


def chooseMenu():
    os.system('cls')
    return input(INIT_MENU)


def inputAmount():
    amount = 0
    while True:
        os.system('cls')
        amount = input(INPUT_AMOUNT)
        try:
            amount = float(amount)
            break
        except:
            print(ERROR_MSG_WRONG_FORMAT)
            input()
    return amount


def inputDate():
    os.system('cls')
    return input(INPUT_DATE)


def printData(amount, date):
    print('your bill is:')
    print('amount: ', amount)
    print('date: ', date)


def addCheque():
    amount = inputAmount()
    date = inputDate()
    printData(amount, date)


def main():
    choise = chooseMenu()
    if choise == '1':  # хорошо было бы сделать словарем
        addCheque()
    else:
        pass


# START PROGRAMM
main()