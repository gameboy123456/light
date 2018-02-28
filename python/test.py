#!python
def createDataSet():
    dataSet = [
                [1, 1, 'yes', 2, 3],
                [1, 1, 'yes', 3, 4],
                [1, 0, 'no',  4, 5],
                [0, 1, 'no',  5, 6],
                [0, 1, 'no',  6, 7]
              ]
    return dataSet

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

myDat = createDataSet()
ret = splitDataSet(myDat, 2, 'no')
print(ret)

