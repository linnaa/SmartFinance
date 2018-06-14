import os
from constants import *
import utils
import inputs


def chooseMenu():
    os.system('cls')
    return input(INIT_MENU)


def addCheque():
    amount = inputs.inputAmount()
    date = inputs.inputDate()
    utils.printData(amount, date)


def main():
    choice = chooseMenu()
    if choice == '1':  # хорошо было бы сделать словарем
        addCheque()
    else:
        pass


# START PROGRAMM
main()