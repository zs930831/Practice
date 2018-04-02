#coding=utf-8
import sys
for line in sys.stdin:
    a = line.split()
    l,r=int(a[0]),int(a[1])
    start=''
    for i in range(1,l+1):
        start+=str(i)
    list=[]
    list.append(start)
    for j in range(l+1,r+1):
        start+=str(j)
        list.append(start)
    count = 0
    for temp in list:
        if int(temp) % 3 == 0:
            count += 1
    print(count)