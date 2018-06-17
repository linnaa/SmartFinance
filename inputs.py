import os
from constants import INIT_MENU, INPUT_AMOUNT, INPUT_DATE, ERROR_MSG_WRONG_FORMAT
import datetime


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
    date = 0
    while True:
        os.system('cls')
        date = input('input the date in YYYY-MM-DD format: ')
        try:
            date = datetime.datetime.strptime(date, '%y-%m-%d')
            break
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            input()
