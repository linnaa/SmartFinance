import os
from constants import INIT_MENU, INPUT_AMOUNT, INPUT_DATE, INPUT_CATEGORY, ERROR_MSG_WRONG_FORMAT

import utils
import inputs
from dataservices import saveData


def chooseMenu():
    os.system('cls')
    INPUT_MENU = {1: addCheque, 6: exit}
    while True:
        try:
            operation = int(input(INIT_MENU))
            INPUT_MENU[operation]()
            break
        except KeyError:
            print("This option has not been developed yet. You can only choose 1 now\n")
        except ValueError:
            print(ERROR_MSG_WRONG_FORMAT)


def addCheque():
    day = inputs.inputDate()
    amount = inputs.inputAmount()
    category = inputs.inputCategory()
    utils.printData(day, amount, category)
    saveData(day, amount, category)


def main():
    chooseMenu()

#     # if choice == '1':  # хорошо было бы сделать словарем
#     #     addCheque()
#     # else:
#     #     pass


# START PROGRAMM
main()
