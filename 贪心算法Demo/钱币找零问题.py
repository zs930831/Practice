#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
假设1元、2元、5元、10元、20元、50元、100元的纸币分别有c0, c1, c2, c3, c4, c5, c6张。
现在要用这些钱来支付K元，至少要用多少张纸币？用贪心算法的思想，
很显然，每一步尽可能用面值大的纸币即可。在日常生活中我们自然而然也是这么做的。
在程序中已经事先将Value按照从小到大的顺序排好。
'''
#countList:纸币的张数，valueList:纸币的面值（ascending），money：需要支付的钱数
#countList,valueList一一对应
def solve(countList,valueList,money):
    count=0
    for value in range(len(valueList)-1,-1,-1):
        '''  
        Python3的除法      
        无论是否整除返回的都是float ，暂且叫它精确除法
        例如 ： 10 / 5，的到的结果是 2.0
        无论是否整除返回的都是 int ，而且是去尾整除
        例如 ：5 // 2，得到的结果是 2
        '''
        moneycounts=min(money//valueList[value],countList[value])
        money=money-moneycounts*valueList[value]
        count+=moneycounts

    if money>0:return -1

    return count

countList=[3,0,2,1,0,3,5]
valueList=[1,2,5,10,20,50,100]

result=solve(countList,valueList,17)
print("result is {}".format(result))

