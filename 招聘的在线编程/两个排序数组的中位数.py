#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
俩个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，要求时间复杂度应为O(log (m+n))。

给出数组A = [1,2,3,4,5,6] B = [2,3,4,5]，中位数3.5

给出数组A = [1,2,3] B = [4,5]，中位数 3
'''


class Solution(object):
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def quickSort(self, list, low, high):
        i, j = low, high
        if high > low:
            temp = list[low]
            while j > i:
                while j > i and list[j] > temp: j -= 1
                if j > i:
                    list[i] = list[j]
                    i += 1
                while j > i and list[i] < temp: i += 1
                if j > i:
                    list[j] = list[i]
                    j -= 1
            list[i] = temp
            Solution().quickSort(list, low, i - 1)
            Solution().quickSort(list, i + 1, high)
        return list

    def findMedianSortedArrays(self, A, B):
        # write your code here
        A.extend(B)
        resultList = Solution().quickSort(A, 0, len(A) - 1)
        if len(resultList) % 2 == 0:
            return float((A[int(len(resultList) / 2)] + A[int(len(resultList) / 2)- 1])) / 2
        return A[int(len(resultList) / 2)]


# A = [1, 2, 3, 4, 5, 6]
# B = [2, 3, 4, 5]
A = [1,2,3]
B = [4,5]
result = Solution().findMedianSortedArrays(A, B)
print(result)
