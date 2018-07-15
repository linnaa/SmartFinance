import os
from constants import INIT_MENU, INPUT_AMOUNT, INPUT_DATE, INPUT_CATEGORY, ERROR_MSG_WRONG_FORMAT
import datetime


def inputDate():
    day = 0
    os.system('cls')
    while True:
        day = input(INPUT_DATE)
        try:
            if day == 't':
                day = datetime.date.today()
            else:
                day = datetime.datetime.strptime(day, '%d.%m.%Y')
            break
        except ValueError:
            print(ERROR_MSG_WRONG_FORMAT)
    return day


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


# переформатировать под ввод даты и нескольких чеков


def inputCategory():
    category = 0
    os.system('cls')
    while True:
        try:
            for key in sorted(INPUT_CATEGORY):
                print(key, INPUT_CATEGORY[key])
            category = int(input('Choose category:\n'))
            category = INPUT_CATEGORY[category]
            break
        except:
            print(ERROR_MSG_WRONG_FORMAT)
    return category