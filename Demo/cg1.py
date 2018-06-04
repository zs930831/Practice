#!/usr/bin/python
# -*- coding: UTF-8 -*-
def solution(doneList, undoList):
    d = dict()
    for i in doneList:
        d[i] = "1"
    for j in undoList:
        if d.get(j) == "1":
            print('NO')
        else:
            d.__setitem__(j, "1")
            print("YES")


# l1=['he','she']
# l2=['me','she','it','me']
# solution(l1,l2)
if __name__ == '__main__':
    doneList, undoList = list(), list()
    array =list(map(int,input().split()))
    doNum, undoNum = array[0], array[1]
    for i in range(doNum):
        doneList.append(input())
    for j in range(undoNum):
        undoList.append(input())
    solution(doneList, undoList)
