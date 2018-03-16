#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
#list like [0,1]
def createSource(list):
    source = []
    s = ''
    while len(source) != 16:
        for i in range(0, 4):
            ran = random.randint(0, 1)
            s += str(list[ran])
        if s not in source:
            source.append(s)
        s = ""
    return source

def matchCTarget(sourceList,cTarget):
    flag4 = ""
    for string in sourceList:
        l=list(string)
        l[0],l[1]="-","-"
        flag1="".join(l)
        l = list(string)
        l[0], l[2] = "-", "-"
        flag2 = "".join(l)
        l = list(string)
        l[0], l[3] = "-", "-"
        flag3 = "".join(l)
        flag=[flag1,flag2,flag3]
        for f in flag:
            if f ==cTarget[0]:
               flag4+="0"
            elif f ==cTarget[1]:
                flag4 += "1"
            elif f == cTarget[2]:
                flag4 += "2"
    if flag4.find("0")>-1 and flag4.find("1")>-1 and flag4.find("2")>-1:
        return True
    return False

def matchPTarget(sourceList,pTarget):
    flag1 = ""
    for string in sourceList:
        l=list(string)
        l[0]="-"
        flag="".join(l)
        if flag == pTarget[0]:
            flag1 += "0"
    if flag1.find("0") > -1:
        return True
    return False

pTarget=["-101"]
cTarget=["--01","-1-1","-10-"]

numList=[0,1]
#create all candidates
source=createSource(numList)
# print(source)
#source2=['1111', '1010', '1100', '1110', '0110', '0000', '0010', '1001', '0101', '0011', '0100', '1101', '0001', '1000', '0111', '1011']
#source1=['0010', '1110', '1010', '1111', '0101', '0011', '1000', '1001', '0100', '1011', '0001', '1100', '0000', '1101', '0110', '0111']
numerator,denominator=0,0
numeratorList,denominatorList=[],[]
for i in range(0,len(source)):
    temp=[]
    temp.append(source[i])
    for j in range(i+1, len(source)):
        if matchCTarget(temp,cTarget):
            denominator+=1
            denominatorList.append(temp)
            if matchPTarget(temp,pTarget):
                numerator+=1
                numeratorList.append(temp)
        temp.append(source[j])

print("Result is : " ,str(numerator)+"/"+str(denominator))
print("分子的数组：",numeratorList)
print("分母的数组：",denominatorList)


