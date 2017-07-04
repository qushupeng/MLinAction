# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:46:50 2017

@author: sq186002
"""


import os
import numpy as np
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
    
    filePath = "E:\\GitHub\\MLinAction\\Ch02\\SampleData\\digits\\trainingDigits"

    fileName = []

    for file in os.listdir(filePath):
        fileName.append([filePath+"\\"+file,file[0]])

    print(fileName[0][0])
    
    file1 = importFile2Array(fileName[0][0])
    print(file1)