#!/usr/bin/python
# -*- coding: UTF-8 -*-
sortList = [49, 38, 65, 97, 76, 13, 27, 49]


def QuickSort(sortList, low, high):
    i, j = low, high
    if low < high:
        temp=sortList[low]
        while j > i :
            while sortList[j]>=temp and j>i: j-=1
            if j>i:
                sortList[i]=sortList[j]
                i+=1
            while sortList[i]<temp and j>i: i+=1
            if j>i:
                sortList[j]=sortList[i]
                j-=1

        sortList[i]=temp
        QuickSort(sortList,low,i-1)
        QuickSort(sortList,i+1,high)

    return sortList

print(QuickSort(sortList,0,len(sortList)-1))



