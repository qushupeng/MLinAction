# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:23:53 2017

@author: sq186002

将外部文本文件导入，以numpy的ndarray形式存储

"""

import numpy as np
import operator

def importFile2Array(filename,split = '\t'):
    '''
    filename:外部文件路径及文件名，格式（windows）为'D:\XXX\XXXXX.TXT'
    split:分隔符，默认为tab
    '''
    outputList = []
    #将文本内容按行写入list
    with open(filename,'r') as importFile:
        x = importFile.readlines()
        for line in x:
            outputList.append(line.replace('\n','').split(split))
    
    return np.array(outputList)
    
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

def normalizeArray(inX,axis=0):
    maxArray = np.amax(inX,axis)
    minArray = np.amin(inX,axis)
    

if __name__ == '__main__':
    
    filename = 'E:\GitHub\MLinAction\Ch02\SampleData\datingTestSet.txt'
    outputList = importFile2Array(filename,'\t')
    print(outputList)