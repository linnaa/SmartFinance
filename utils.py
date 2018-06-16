def printData(amount, date):
    print('New bill added:')
    print('amount: {0}'.format(amount))
    print('date: {0}{1}.{2}{3}.{4}{5}{6}{7}'.format(date[0], date[1], date[3],
                                                    date[4], date[6], date[7],
                                                    date[8], date[9]))