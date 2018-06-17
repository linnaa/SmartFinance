import os
from constants import INIT_MENU, INPUT_AMOUNT, INPUT_DATE, ERROR_MSG_WRONG_FORMAT
import datetime


def inputAmount():
    amount = 0
    os.system('cls')
    while True:
        amount = input(INPUT_AMOUNT)
        try:
            amount = float(amount)
            break
        except:
            print(ERROR_MSG_WRONG_FORMAT)
    return amount


def inputDate():
    date = 0
    os.system('cls')
    while True:
        date = input(INPUT_DATE)
        try:
            date = datetime.datetime.strptime(date, '%d.%m.%Y')
            break
        except ValueError:
            print(ERROR_MSG_WRONG_FORMAT)
    return date
