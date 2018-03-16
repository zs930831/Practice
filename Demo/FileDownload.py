#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
print("Begin Download")
targetUrl = "http://ah.download.cycore.cn/rrt/9adf4470ce5dfa71756d73196bf4a6fd/16445441480904517792/046d02feeb871148feb5a8fc99074a66.ppt?filename=%E3%80%8A%E5%A4%A9%E4%B8%8A%E7%9A%84%E8%A1%97%E5%B8%82%E3%80%8Bppt%E8%AF%BE%E4%BB%B6.ppt"
#localPath=targetUrl.split("?")
r = requests.get(targetUrl)
with open("E:/a.ppt", "wb") as code:
     code.write(r.content)
print("Download End")