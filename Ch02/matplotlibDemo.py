# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 20:35:40 2017

@author: Administrator
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

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

filename = 'E:\GitHub\MLinAction\Ch02\SampleData\datingTestSet.txt'
outputList = importFile2Array(filename,'\t')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(outputList[:,1],outputList[:,2])
plt.show()
