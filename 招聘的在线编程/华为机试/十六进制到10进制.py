#!/usr/bin/python
# -*- coding: UTF-8 -*
# def jc(n):
#     if n==0:
#         return 1
#     return n*jc(n-1)
# print(jc(4))

def solution(str):
    dict16 = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
    result, count = 0, 0
    for i in range(len(str)-1, 1, -1):
        try:
            num = int(dict16.get(str[i]))
            result += num * (16 ** count)
        except:
            result += int(str[i]) * (16 ** count)
        count += 1
    return result


if __name__ == '__main__':
    while True:
        try:
            str = input()
            print(solution(str))
        except:
            break

# while True:
#     try:
#         print(int(input(),16))
#     except:
#         break