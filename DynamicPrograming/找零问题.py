#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
　找零问题：需找零金额为W，硬币面值有(d1, d2, d3，…，dm)，最少需要多少枚硬币。

　　问题：需找零金额为8，硬币面值有(1, 3, 2, 5)，最少需要多少枚硬币。

　　设F(j)表示总金额为j时最少的零钱数，F(0) = 0，W表示找零金额，有零钱一堆{d1, d2, d3，…，dm}。同样根据之前的经验，要达到为j，
    那么必然是j – di(1 <= i <= m)面值的硬币数再加1个di面值的硬币，当然j >= di，即F(j) = F(j - di) + 1, j >= di。


             | F(0)=0
    F(j) =   |
             | F(j-dj)+1

'''
def charge_making(money, num):
    '''
    找零问题
    '''
    count = [0] * (num + 1)
    count[0] = 0
    for j in range(1, num + 1):
        minCoins = j
        for i in range(len(money)):
            if j - money[i] >= 0:
                temp = count[j - money[i]] + 1
                if temp < minCoins:
                    minCoins = temp

        count[j] = minCoins

    return count[num]


money = [1, 3, 2, 5]
num = 8
count = charge_making(money, num)
print(count)