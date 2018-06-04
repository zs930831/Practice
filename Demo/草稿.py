#!/usr/bin/python
# -*- coding: UTF-8 -*-
# l=[]
def solution(lowerstr, low, high):
    # global l
    if low > high:
        return
    max = ord(lowerstr[low])
    for s in lowerstr[low:high + 1]:
        if ord(s) > max:
            max = ord(s)
    print(chr(max), end='')
    # l.append(chr(max))
    index = lowerstr.index(chr(max))
    lowerstr.replace(chr(max), 'A', 1)
    low = index + 1
    solution(lowerstr, low, high)


str1 = 'asdqqv'
low, high = 0, len(str1)-1
solution(str1, low, high)
