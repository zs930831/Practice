#coding=utf-8

def dpa(di, pi, ai):
    num=len(ai)
    count = [0] * (num + 1)
    count[0] = 0
    for j in range(1, num + 1):
        tempPi=0
        for i in range(len(di)):
            if ai[j-1]-di[i] >= 0:
                temp = pi[i]
                if temp > tempPi:
                    tempPi = temp

        count[j] = tempPi

    return count[1:]
# di=[1,10,1000000000]
# pi=[100,1000,1001]
# ai=[9,10,1000000000]
# print(dpa(di,pi,ai))
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = sys.stdin.readline().strip().split()
    worknum,xhbnum=int(n[0]),int(n[1])
    di,pi,ai=[],[],[]
    ans = 0
    for i in range(worknum+1):
        # 读取每一行
        line = sys.stdin.readline().strip().split()
        if i<worknum:
            di.append(int(line[0]))
            pi.append(int(line[1]))
        else:
            for i in line:
                ai.append(int(i))
    result=dpa(di,pi,ai)
    for i in result:
        print(i)