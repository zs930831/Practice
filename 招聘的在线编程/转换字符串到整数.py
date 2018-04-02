#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
实现atoi这个函数，将一个字符串转换为整数。如果没有合法的整数，返回0。
如果整数超出了32位整数的范围，返回INT_MAX(2147483647)如果是正整数，或者INT_MIN(-2147483648)如果是负整数。
'''


class Solution:
    """
    @param str: A string
    @return: An integer
    """

    def atoi(self, str):
        # 1.2-》1
        str1 = ''  # 存放str出现的合法整数
        a = '0123456789'
        b = '-+123456789'
        for i in str:
            if i == ' ':  # 一开始空格,都直接continue
                continue
            if len(str1) == 0 and i in b:
                str1 = str1 + i
                continue
            if i in a:
                str1 = str1 + i
                continue
            break
        try:
            result = int(str1)
            if -2147483648 <= result and result <= 2147483647:
                return result
            if result > 0:
                return 2147483647
            else:
                return -2147483648
        except:
            return 0
str1=['51a','-ab','12.34','+1'," 15+4",'+14']
for i in str1:
    print(Solution().atoi(i))