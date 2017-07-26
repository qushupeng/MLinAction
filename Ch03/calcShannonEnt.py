# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:04:02 2017

@author: sq186002
"""

import math

def calcShannonEnt(dataSet):
    '''
    计算给定数据集的香农熵
    
    熵定义为信息的期望值，信息的定义为 I(xi) = - log2P(xi)，其中P(xi)是选择该分类的概率
    
    dataSet格式为二维数组，每个元素的最后一个元素表示分类，其他表示属性
    [[1,1,'yes'],
     [1,0,'yes'],
     [0,1,'no']
    ]
    '''
    
    #创建字典，求数据集中各元素出现的频率
    labelCounts = {}
    for data in dataSet:
        labelCounts[data[-1]] = labelCounts.get(data[-1],0) + 1

    #求熵
    shannonEnt = 0.0
    
    for key in labelCounts:
        prob = float(labelCounts[key])/len(dataSet)
        shannonEnt -= prob * math.log(prob,2)
        
    return shannonEnt
    
dataSet = [[1,1,'yes'],[1,0,'yes'],[0,1,'no']]

print(calcShannonEnt(dataSet))