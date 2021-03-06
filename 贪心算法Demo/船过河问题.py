#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目大意是只有一艘船，能乘2人，船的运行速度为2人中较慢一人的速度，过去后还需一个人把船划回来，问把n个人运到对岸，最少需要多久。
先将所有人过河所需的时间按照升序排序，我们考虑把单独过河所需要时间最多的两个旅行者送到对岸去，有两种方式：
1.最快的和次快的过河，然后最快的将船划回来；次慢的和最慢的过河，然后次快的将船划回来，所需时间为：t[0]+2*t[1]+t[n-1]；
2.最快的和最慢的过河，然后最快的将船划回来，最快的和次慢的过河，然后最快的将船划回来，所需时间为：2*t[0]+t[n-2]+t[n-1]。
算一下就知道，除此之外的其它情况用的时间一定更多。每次都运送耗时最长的两人而不影响其它人，问题具有贪心子结构的性质。
'''

if __name__ == '__main__':
    t = [1, 5, 4, 2, 3, 6, 7, 9, 8]
    t = sorted(t, key=lambda x: x)
    # print(t)
    sum,people=0,len(t)
    while people>3:
        sum+=min(t[0]+2*t[1]+t[people-1],2*t[0]+t[people-2]+t[people-1])
        people-=2
    if people==3:
        sum+=t[0]+t[1]+t[2]
    elif people==2:
        sum+=t[1]
    else:
        sum+=t[0]

    print(sum)
