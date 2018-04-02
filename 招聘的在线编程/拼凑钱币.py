#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
给你六种面额 1、5、10、20、50、100 元的纸币，假设每种币值的数量都足够多，编写程序求组成N元（N为0~10000的非负整数）的不同组合的个数。
输入描述:
输入包括一个整数n(1 ≤ n ≤ 10000)

输出描述:
输出一个整数,表示不同的组合方案数

输入例子1:
1

输出例子1:
1
'''

#
while True:
    try:
        N=int(input())
        coins=[1,5,10,20,50,100]
        h=len(coins)
        dp=[0 for i in range(10001)]
        dp[0]=1
        for i in range(h):
            for j in range(1,N+1):
                if j>=coins[i]:
                    dp[j]+=dp[j-coins[i]]
        print (dp[N])
    except:
        break