def csvTo2dArray(fileName):
    array = []
    with open(fileName, "r") as f:
        for line in f:
            current = line.rstrip('\n').split(',')
            array.append(current)
    
    return array

#print(csvTo2dArray('csvtest.csv'))