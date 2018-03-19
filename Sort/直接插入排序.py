#!/usr/bin/python
# -*- coding: UTF-8 -*-

#和左边的比较，左边如果大，就往后移动一位
def InsertSort(sortList):
    for i in range(1,len(sortList)):
        tmp=sortList[i]
        j=i-1
        while(j>=0 and sortList[j]>tmp):
            sortList[j+1]=sortList[j]
            j-=1
        sortList[j+1]=tmp
    return sortList

sortList=[49,38,65,97,76,13,27,49]

print(InsertSort(sortList))