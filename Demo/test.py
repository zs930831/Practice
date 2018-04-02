#!/bin/python
import sys
import os


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************
class nen:
    def __init__(self, str):
        self.node1 = str[0]
        self.edge = int(str[1])
        self.node2 = str[2]


def calculate(M, strs):
    list = []
    for m in range(M):
        i = 0
        while i < len(strs[m]) - 1:
            tempStr = strs[m][i:i + 3]
            print(tempStr)
            list.append(nen(tempStr))
            i += 2
    if len(list) == 1:
        return list[0].edge
    for j in range(len(list) - 1):
        if list[j].node2 == list[j + 1].node1:
            list[j].node2 = list[j + 1].node2
            list[j].edge = list[j].edge + list[j + 1].edge
        if list[j + 1].node2 == list[j].node1:
            return -1
    max = 0
    for l in list:
        if l.edge > max:
            max = l.edge
    return max


# ******************************结束写代码******************************


_M = int(input())

_strs_cnt = _M
_strs_i = 0
_strs = []
while _strs_i < _strs_cnt:
    try:
        _strs_item = input()
    except:
        _strs_item = None
    _strs.append(_strs_item)
    _strs_i += 1
# print(_strs)
res = calculate(_M, _strs)

print(str(res) + "\n")
