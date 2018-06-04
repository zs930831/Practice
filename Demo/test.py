# print("my wife's name is {}".format('wxs'))
# print('my salary is {:.2f},{:.3f}'.format(3.1213213,4.3213))
#import numpy as np
#自己当作成一位数组
# List=[[1,2,3],[4,5,6],[7,8,9]]
#
# print([np.column_stack([i for i in l])for l in List])
# print([np.column_stack([i for i in l]).mean(axis=1)for l in List])
# print(np.column_stack([np.column_stack([i for i in l]).mean(axis=1)for l in List]))


#print(list(map(lambda x,y:x+y, [1,2,3],[4,5,6])))

# for num in range(10,-1,-1):
#     print(num)

# print(17/100)

#Python 3.x前要加list
# n = int(input())
# arr = map(int, input().split())
# K, D = map(int, input().split())

#a=[1,2,3,5,4]
# a.pop(-1)
# print(a,len(a))
#print(a.index(1))

#
# a='ewqe'
# print(a.index('e'))
# str='test'
# print(str.replace('t','s',1))

# a,b=[1,2,3],[4,5,6]
# for c,d in zip(a,b):
#     print(c,d)

a=set()
a.add(1)
a.add(2)
a.add(1)
print(list(a))