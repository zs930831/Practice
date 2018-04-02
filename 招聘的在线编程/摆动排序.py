#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
给你一个没有排序的数组，请将原数组就地重新排列满足如下性质

nums[0] <= nums[1] >= nums[2] <= nums[3]....
 注意事项

请就地排序数组，也就是不需要额外数组

样例
给出数组为 nums = [3, 5, 2, 1, 6, 4] 一种输出方案为 [1, 6, 2, 5, 3, 4]
'''

nums = [3, 5, 2, 1, 6, 4]
class Solution(object):
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if i % 2 == 1 and nums[i] < nums[i - 1] or \
               i % 2 == 0 and nums[i] > nums[i - 1] :
               nums[i],nums[i-1]=nums[i-1],nums[i]
        return nums
r=Solution().wiggleSort(nums)
print(r)
