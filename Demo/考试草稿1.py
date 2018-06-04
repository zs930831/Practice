# def solution(n):
#     li = [1, 1, 1, 1, 1]
#     for i in range(5, n + 1):
#         li.append(2018 * li[-1] + 2017 * li[-2] + 2016 * li[-3] + 2015 * li[-4] + 2014 * li[-5])
#     print(li[-1] % 1000000003)

#
# list=[0,1,3,5,7,100000]
# for i in list:
#     fin(i)

if __name__ == '__main__':
    num=int(input())
    for i in range(num):
        str1 = ''
        length = int(input())
        for j in range(1,length+1):
             str1+=str(j)
        print(len(str1))
