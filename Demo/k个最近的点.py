#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

a = [1, 3, 2]


class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        rdic = {}
        result = []
        result1 = []
        for j in range(len(points)):
            r = str(math.sqrt(abs(points[j][0] - origin[0])) + math.sqrt(abs(points[j][1] - origin[1])))
            rdic[r] = points[j]
            result.append(r)
        result = sorted(result)
        for i in range(k):
            result1.append(rdic[result[i]])
        return result1


points = [[4, 6], [4, 7], [4, 4], [2, 5], [1, 1]]
origin = [0, 0]
k = 3
r = Solution().kClosest(points, origin, k)
print (r)
