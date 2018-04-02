#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目描述
继MIUI8推出手机分身功能之后，MIUI9计划推出一个电话号码分身的功能：首先将电话号码中的每个数字加上8取个位，然后使用对应的大写字母代替
（"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"）， 然后随机打乱这些字母，所生成的字符串即为电话号码对应的分身。
输入描述:
第一行是一个整数T（1 ≤ T ≤ 100)表示测试样例数；接下来T行，每行给定一个分身后的电话号码的分身（长度在3到10000之间）。
输出描述:
输出T行，分别对应输入中每行字符串对应的分身前的最小电话号码（允许前导0）。

示例1
输入
4
EIGHT
ZEROTWOONE
OHWETENRTEO
OHEWTIEGTHENRTEO

输出
0
234
345
0345
'''
def find_num(s):
    res=[0]*10
    res[0]=s.count('Z')
    res[2]=s.count('W')
    res[4]=s.count('U')
    res[6]=s.count('X')
    res[8]=s.count('G')
    res[1]=s.count('O')-res[0]-res[2]-res[4]
    res[7]=s.count('S')-res[6]
    res[5]=s.count('V')-res[7]
    res[3]=s.count('H')-res[8]
    res[9]=s.count('I')-res[5]-res[6]-res[8]
    res1=res[8:]+res[:8]
    #print(res1)
    res2=''
    for i in range(len(res1)):
        if res1[i]>0:
            res2=res2+res1[i]*str(i)
    return res2
import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    alpha=sys.stdin.readline().strip()
    print(find_num(alpha))
