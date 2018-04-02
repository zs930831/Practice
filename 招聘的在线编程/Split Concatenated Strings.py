#!/usr/bin/python
# -*- coding: UTF-8 -*-
# str = ["abc", "xyz"],return "zyxcba"

def splitLoopedString(strs):
    if len(strs)<0:
        return 0
    tempStr=''
    result=''
    for i in strs:
        tempStr+=i
    cList=[]
    for c in tempStr:
        cList.append(c)
    # print(tempStr,cList)
    max,c1,cLength=0,'',len(cList)
    for c in tempStr:
        for count in range(cLength):
            tempLength=abs(ord(cList[count])-ord(c))
            if tempLength>max:
                max=tempLength
                c1=cList[count]
        result+=c1
        cLength-=1
        cList.remove(c1)
        max, c1 = 0, ''
    return result


str = ["abc", "xyz"]
print(splitLoopedString(str))


