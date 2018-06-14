import os
from constants import *


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
