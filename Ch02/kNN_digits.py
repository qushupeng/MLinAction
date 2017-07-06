# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:57:35 2017

@author: sq186002
"""

import numpy as np
import os
import operator

def file2Array(filename):
    
    outputList = []
    with open(filename,'r') as importFile:
        lines = importFile.readlines()
        for line in lines:
            outputList.extend(list(line.replace('\n','')))
    
    return np.array(outputList).astype(int)
    
def files2Array(pathname):

    dataset = []
    labels = []
    for file in os.listdir(pathname):
        dataset.append(file2Array(pathname+'\\'+file))
        labels.append(file[0])
        
    return np.array(dataset),np.array(labels)

def classifyKNN(inX,dataSet,labels,k):
    '''
    kNN: k Nearest Neighbors

    Input:      
            inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)
            
    Output:     
            the most popular class label
    '''
    #矩阵做差
    diffMat = np.tile(inX, (dataSet.shape[0],1)) - dataSet
    #求欧氏距离
    distances = ((diffMat**2).sum(axis=1))**0.5

    sortedDistIndicies = distances.argsort()
    classCount={}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
        
    
trainingFilePath = "E:\\GitHub\\MLinAction\\Ch02\\SampleData\\digits\\trainingDigits\\0_0.txt"

fileArray = file2Array(trainingFilePath)
print(fileArray)

pathname = "E:\\GitHub\\MLinAction\\Ch02\\SampleData\\digits\\trainingDigits"

dataset,labels = files2Array(pathname)
print(dataset)
print(labels)

pathname2 = "E:\\GitHub\\MLinAction\\Ch02\\SampleData\\digits\\testDigits"
inX,answers = files2Array(pathname2)

count = 0
for i in range(len(inX)):
    if classifyKNN(inX[i],dataset,labels,3) == answers[i]:
        count += 1

print(str(count/len(inX) * 100) + "%")