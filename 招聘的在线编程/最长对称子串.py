#!/usr/bin/python
# -*- coding: UTF-8 -*-
def function(string):
    i, j, countlist = 0, len(string) - 1, []
    while j > i:
        low, high, count, flag = i, j, 0, 0
        while high > low:
            if string[high] != string[low]:
                high -= 1
                if flag == 1:
                    return 0
            else:
                if flag == 0:
                    flag = 1
                high -= 1
                low += 1
                if high == low:
                    count += 1
                count += 2
        i += 1
        countlist.append(count)
    sorted(countlist)
    return countlist[0]


string = ['12321abc', 'abc12cba','11as']
for s in string:
    print(function(s))
