#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
#找到csv路径
logfilenamepath='C:\\Users\\CHOSEN1\\Desktop\\jp\\BugDl\\data\\dataset\\dataset'
a=os.listdir(logfilenamepath)
csvFileList=[]
for b in a:
    if(b.find("-")>-1):
        csvFileList.append(b)
with open(logfilenamepath+"\\newbug.csv","a+") as f:
    f.write("project_name,version,wmc,dit,noc,cbo,rfc,lcom,ca,ce,npm,lcom3,loc,dam,moa,mfa,cam,ic,cbm,amc,max_cc,avg_cc,fi-changes,ostrand,scattering,ana,acm,arl,bugnums"+"\n")
    for csvFile in csvFileList:
        logfilenamepath1=logfilenamepath+"\\"+csvFile
        file=open(logfilenamepath1)
        try:
            lines=file.readlines()
            bugnum=ana=acm=arl=scattering=ostrand=fichange=wmc=dit=noc=cbo=rfc=lcom=ca=ce=npm=lcom3=loc=dam=moa=mfa=cam=ic=cbm=amc=max_cc=avg_cc=0
            for line in lines:
                if line.find("version")>-1:
                    continue
                wmc += float(line.split(",")[3])
                dit += float(line.split(",")[4])
                noc += float(line.split(",")[5])
                cbo += float(line.split(",")[6])
                rfc += float(line.split(",")[7])
                lcom += float(line.split(",")[8])
                ca += float(line.split(",")[9])
                ce += float(line.split(",")[10])
                npm += float(line.split(",")[11])
                lcom3 += float(line.split(",")[12])

                loc += float(line.split(",")[13])
                dam += float(line.split(",")[14])
                moa += float(line.split(",")[15])
                mfa += float(line.split(",")[16])
                cam += float(line.split(",")[17])
                ic += float(line.split(",")[18])
                cbm += float(line.split(",")[19])
                amc += float(line.split(",")[20])
                max_cc += float(line.split(",")[21])
                avg_cc += float(line.split(",")[22])

                p_name=line.split(",")[0]
                version=line.split(",")[1]
                bugnum+=float(line.split(",")[-3])
                ana += float(line.split(",")[-7])
                acm += float(line.split(",")[-6])
                arl += float(line.split(",")[-5])
                scattering += float(line.split(",")[-9])
                ostrand += float(line.split(",")[-10])
                fichange += float(line.split(",")[-11])
            f.write(p_name+","+version+","+str(wmc)+","+str(dit)+","+str(noc)+","+str(cbo)+","+str(rfc)+","+
                    str(lcom) + "," + str(ca) + "," + str(ce) + "," + str(npm) + "," + str(lcom3) + ","+
                    str(loc) + "," + str(dam) + "," + str(moa) + "," + str(mfa) + "," + str(cam) + ","+
                    str(ic) + "," + str(cbm) + "," + str(amc) + "," + str(max_cc) + "," + str(avg_cc) + ","+
                    str(fichange)+","+str(ostrand)+","+str(scattering)+","+str(ana)+","+str(acm)+","+str(arl)+","+str(bugnum)+"\n")
        finally:
            file.close()

print("End")