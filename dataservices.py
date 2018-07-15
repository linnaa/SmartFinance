MODEL_FILE_PATH = 'data.txt'

def saveData(day, amount, category):
    modelFile = open(MODEL_FILE_PATH, 'a')
    modelFile.write('%s\t%.2f\t%s\n' % (day, amount, category))
    modelFile.close()
