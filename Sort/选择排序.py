#!/usr/bin/python
# -*- coding: UTF-8 -*-
sortList = [49, 38, 65, 97, 76, 13, 27, 49]


def selectSort(sortList):
    for i in range(len(sortList)):
        k = i
        for j in range(i + 1, len(sortList)):
            if sortList[j] < sortList[k]:
                k = j
        temp = sortList[k]
        sortList[k] = sortList[i]
        sortList[i] = temp
    return sortList

print(selectSort(sortList))
