#!/usr/bin/python
# -*- coding: UTF-8 -*-
sortList=[49,38,65,97,76,13,27,49]

def BubbleSort(sortList):
    for i in range(len(sortList)-1,-1,-1):
        flag=0
        #注意这个1
        for j in range(1,i+1):
            if sortList[j-1]>sortList[j]:
                tmp=sortList[j-1]
                sortList[j-1]=sortList[j]
                sortList[j]=tmp
            flag=1
        if flag==0:
            return sortList

print(BubbleSort(sortList))