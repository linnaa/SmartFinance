INIT_MENU = [
    "1. Добавить чек\n", "2. Удалить чек\n", "3. Добавить категорию\n",
    "4. Удалить категорию\n", "5. Отчеты\n", "6. Выход\n"
]


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