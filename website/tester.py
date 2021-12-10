with open('ids_autoFilled.txt') as f:
    testList = f.readlines()


formatList = list(set(testList))
formatList.sort(key=testList.index)
print (len(formatList))
