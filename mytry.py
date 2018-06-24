import os
from constants import INIT_MENU, INPUT_AMOUNT, INPUT_DATE, ERROR_MSG_WRONG_FORMAT

import utils
import inputs


def chooseMenu():
    os.system('cls')
    return int(input(INIT_MENU))


def addCheque():
    amount = inputs.inputAmount()
    date = inputs.inputDate()
    utils.printData(amount, date)


def main():
    choice = [addCheque(), "to be added", "to be added"]
    return choice[(chooseMenu()) - 1]


# START PROGRAMM
main()