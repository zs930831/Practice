#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
为最近最少使用（LRU）缓存策略设计一个数据结构，它应该支持以下操作：获取数据（get）和写入数据（set）。

获取数据get(key)：如果缓存中存在key，则获取其数据值（通常是正数），否则返回-1。

写入数据set(key, value)：如果key还没有在缓存中，则写入其数据值。当缓存达到上限，它应该在写入新数据之前删除最近最少使用的数据用来腾出空闲位置。
'''


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
    # do intialization if necessary
        self.capacity=capacity
        self.cache={}
        self.useTimeDict={}
        self.count=0

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
    # write your code here
        if key in self.cache.keys():
            self.count += 1
            self.useTimeDict[key]=self.count
            return self.cache[key]
        return -1



    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
    # write your code here
        if len(self.cache)==self.capacity:
            #False升序
            leastUseItemList=sorted(self.useTimeDict.items(),key=lambda x:x[1],reverse=False)
            del self.cache[leastUseItemList[0][0]]
            del self.useTimeDict[leastUseItemList[0][0]]

        self.count += 1
        if key not in self.cache.keys():
            self.useTimeDict.__setitem__(key,self.count)
            self.cache.__setitem__(key,value)
        else:
            self.useTimeDict[key] = self.count
            self.cache[key]=value

lruCace=LRUCache(3)
lruCace.set(1, 1)
lruCace.set(2, 2)
lruCace.set(3, 3)
lruCace.set(4, 4)
print(lruCace.get(4))
print(lruCace.get(3))
print(lruCace.get(2))
print(lruCace.get(1))
lruCace.set(5, 5)
print(lruCace.get(1))
print(lruCace.get(2))
print(lruCace.get(3))
print(lruCace.get(4))
print(lruCace.get(5))