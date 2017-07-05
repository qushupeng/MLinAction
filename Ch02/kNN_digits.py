# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:46:50 2017

@author: sq186002
"""


import os
import numpy as np
import operator
'''

'''
def importFile2Array(filename):
    '''
    filename:外部文件路径及文件名，格式（windows）为'D:\XXX\XXXXX.TXT'
    split:分隔符，默认为tab
    '''
    outputList = []
    #将文本内容按行写入list
    with open(filename,'r') as importFile:
        x = importFile.readlines()
        for line in x:
            outputList.append(list(line.replace('\n','')))
    
    return np.array(outputList).astype(int)


def fileDistance(fileName1,fileName2):
    pass

if __name__ == '__main__':
    
    trainingFilePath = "E:\\GitHub\\MLinAction\\Ch02\\SampleData\\digits\\trainingDigits"
    testFilePath = "E:\\GitHub\\MLinAction\\Ch02\\SampleData\\digits\\testDigits"

    trainingFileName = []
    for file in os.listdir(trainingFilePath):
        trainingFileName.append([trainingFilePath+"\\"+file,file[0]])
        
    testFileName = []
    for file in os.listdir(testFilePath):
        testFileName.append([testFilePath+"\\"+file,file[0]])

    print(trainingFileName[0][0])
    
    file1 = importFile2Array(trainingFileName[0][0])
    print(file1)
    
    classCount = {}
    
    for filePath1 in testFileName:
        fileName1 = filePath1[0][0]
        for filePath2 in trainingFileName:
            fileName2 = filePath2[0]
            distance = fileDistance(fileName1,fileName2)
            classCount[filePath2[1]] = classCount.get(filePath2[1],0) + 1

        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    
            







