#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
有n个需要在同一天使用同一个教室的活动a1,a2,…,an，教室同一时刻只能由一个活动使用。每个活动ai都有一个开始时间si和结束时间fi 。一旦被选择后，活动ai就占据半开时间区间[si,fi)。
如果[si,fi]和[sj,fj]互不重叠，ai和aj两个活动就可以被安排在这一天。该问题就是要安排这些活动使得尽量多的活动能不冲突的举行
'''
#我们的贪心策略应该是每次选取结束时间最早的活动。直观上也很好理解，按这种方法选择相容活动为未安排活动留下尽可能多的时间
# 。这也是把各项活动按照结束时间单调递增排序的原因。

class Act:
    def __init__(self,start,end):
        self.start=start
        self.end=end


def greedy_activity_selector(actlist):
    num,i,temp=1,1,[]
    for j in range(2,len(actlist)):
        if actlist[j].start>actlist[i].end:
            num+=1
            i=j
            temp.append(actlist[i])
    return num,temp
actlist=[]
actlist.append(Act(-1,-1))
actlist1=[Act(1,4),Act(0,6),Act(5,7),Act(3,5),Act(3,8),Act(6,10),Act(5,9),Act(3,8),
         Act(8,11),Act(12,14),Act(2,13),Act(8,12)]

actlist.extend(actlist1)
actlist=sorted(actlist,key=lambda act:act.end)
# for i in actlist:
#     print('start is {},end is {}'.format(i.start,i.end))

result,actualAct=greedy_activity_selector(actlist)
print('total num is {}'.format(result))
for i in actualAct:
    print('start is {},end is {}'.format(i.start,i.end))