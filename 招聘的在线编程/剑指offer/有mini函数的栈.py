#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.list=list()
    def push(self, node):
        # write code here
        self.list.append(node)
    def pop(self):
        # write code here
        #remove删除第一个满足条件的值
        # del 来说，它是根据索引（元素所在位置）来删除的
        #pop和del一样可以删除索引，但是要有返回值，返回值为被删除的函数。
        del self.list[-1]
    def top(self):
        # write code here
        return self.list[-1]
    def min(self):
        # write code here
        return min(self.list)

