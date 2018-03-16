#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
#找到csv路径
logfilenamepath='E:\\csv'
a=os.listdir(logfilenamepath)
csvFileList=[]
for b in a:
    if(b.find("-")>-1):
        csvFileList.append(b)
with open(logfilenamepath+"\\Raw_data.csv","a+") as f:
    f.write("filename,originaldl,improveddl,pc,il,isbuggy,bugnums"+"\n")
with open(logfilenamepath+"\\Raw_data.csv","a+") as f:
    for csvFile in csvFileList:
        logfilenamepath1=logfilenamepath+"\\"+csvFile
        file=open(logfilenamepath1)
        try:
            r=file.readline()
            r1=file.readline()
            f.write(r1+", "+"\n")
        finally:
            file.close()

print("End")