#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
'''
 给定两个长度为 n ( 0 < n <= 8 ) 的 数字串 (由1到9构成)  ，我们希望对第一个数字串做一系列如下操作：

    1、将数字串的某一位加1

    2、将数字串的某一位减1

    3、交换数字串中任意两个数字的位置

最终使得第一个数字串变成第二个数字串， 请问最少需要多少操作。
'''

def swap(list,indexI,indexJ):
    temp=list[indexI]
    list[indexI]=list[indexJ]
    list[indexJ]=temp

    return list

def getMinSteps(sList,dList,startIndex,endIndex):
    if startIndex<0 or endIndex>8 or startIndex>endIndex:
        return 0
    s,d,curLenth=[],[],0
    #record the different elements bwt sList and dList
    for i in range(startIndex,endIndex+1):
        if sList[i]!=dList[i]:
            s.append(sList[i])
            d.append(dList[i])
            curLenth+=1

    #entrance
    if curLenth==1:
        return abs(s[0]-d[0])

    if curLenth==0:
        return 0

    #case1 add or minus
    result1=abs(s[0]-d[0])+getMinSteps(s,d,1,curLenth-1)
    #case2 swap through the whole list
    result2,tempS=sys.maxsize,s
    for i in range(curLenth):
        swap(tempS,0,i)
        tempResult=abs(tempS[0]-d[0])+getMinSteps(s,d,1,curLenth-1)+1
        result2=min(result2,tempResult)

    return min(result2,result1)

def strToIntList(s1,s2):
    s1IntList,s2IntList=[],[]
    for i in s1:
        s1IntList.append(int(i))
    for i in s2:
        s2IntList.append(int(i))
    return s1IntList,s2IntList

s="24"
d="45"
s,d=strToIntList(s,d)
# print(s,d)
result=getMinSteps(s,d,0,len(s)-1)
print(result)
