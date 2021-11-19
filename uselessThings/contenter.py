import requests
import json
import os
import ssl
import time
import datetime
import re

with  open('ids.txt') as f:
    for line in f.readlines():
        line=line.strip('\n')

        print(line)

        ssl._create_default_https_context = ssl._create_unverified_context
        #爬取
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        proxies = {'http': 'http://localhost:10808', 'https': 'http://localhost:10808'}

        urlinfo = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(line)
        urldes = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(line)+"/description"
        des = requests.get(url=urldes,headers=headers)
        print(des)
        desText = des.text
        

        info = requests.get(url=urlinfo,headers=headers)
        infoText = info.text
        infoJson = json.loads(infoText)
        try:
            iconLink = infoJson.get("attachments")[0].get("thumbnailUrl")
        except IndexError:
            log = open(os.getcwd()+r"uncursedforge.log", "a",encoding="utf-8")

            log.write(str(line)+"因为 IndexError 爬取失败")

            log.close()

        iconTemp = r'<div align="center"><img src="'+iconLink+'"/></div><link href="main.css" rel="stylesheet" type="text/css"/>'
        #print(desText)

        modNameHtml = requests.get(url=urlinfo,headers=headers)
        nameText = modNameHtml.text
        nameJson = json.loads(nameText)
        modName = infoJson.get("name")
        nameTemp = r'<div align="center"><h1 style="font-size: 150px;font-family:px;">'+modName+'</h1></div><HR SIZE=10>'
        
        '''
        #downloader
        fileRes = requests.get(url="https://addons-ecs.forgesvc.net/api/v2/addon/"+str(line)+"/files",headers=headers)
        fileInfo = json.loads(fileRes.text)
        
        dateDic = []

        for i in range (0,len(fileInfo)):
            #Fix me
            #print(fileInfo[i])
            dateDic.insert(i , fileInfo[i]['fileDate'] + str(i))
            
        print(dateDic)
        dateDic.sort(reverse=True)
        latestFileOrder = dateDic[0][-1]

        print(fileInfo)

        latestFileLink = fileInfo[latestFileOrder].downloadUrl

        #downloader finished
        '''
        
        pathPart = '\\en\\'
        pagesPart = '\\pages\\'
        page = open(os.getcwd()+pagesPart+pathPart+str(line)+".html", "a",encoding="utf-8")
        
        page.write(iconTemp)
        page.write(nameTemp)
        page.write(desText)

        page.close()

        hrefTemp = r'<html><head><meta http-equiv="refresh" content="0;url=/pages/en/'+str(line)+r'.html"></head><html>'
        
        pageZh = open(os.getcwd()+pagesPart+str(line)+r"_zh.html", "a",encoding="utf-8")
        
        pageZh.write(hrefTemp)

        pageZh.close()


        
        
        
        
    f.close()
