import os
from constants import INIT_MENU, INPUT_AMOUNT, INPUT_DATE, INPUT_CATEGORY, ERROR_MSG_WRONG_FORMAT

import utils
import inputs


def chooseMenu():
    os.system('cls')
    return input(INIT_MENU)


def addCheque():
    amount = inputs.inputAmount()
    date = inputs.inputDate()
    category = inputs.inputCategory()
    utils.printData(amount, date, category)


def main():
    choice = chooseMenu()
    if choice == '1':  # хорошо было бы сделать словарем
        addCheque()
    else:
        pass


# START PROGRAMM
main()