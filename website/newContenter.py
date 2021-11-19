
import requests
import json
import os
import ssl
import time
import datetime
import re
import pymongo
import queue
import asyncio
import threading

from fake_useragent import UserAgent

from pymongo import MongoClient
#client = MongoClient()
ua = UserAgent()
client = MongoClient('localhost', 27017)
db = client.uncursedforge
collection = db.modsinfo
idlist = []
idfile = open('ids.txt',mode="r")
for id in idfile.readlines():
    idlist.append(id.strip('\n'))
idfile.close()

spiderQueue = queue.Queue(maxsize = 0)
for id in idlist:
    spiderQueue.put(id)


def spiderFunc():
    while True:
        id_to_crawl = spiderQueue.get()
        
        print(id_to_crawl)
        des_url = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(id_to_crawl)+"/description"
        info_url = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(id_to_crawl)
        time.sleep(5)
        header = {"user-agent": ua.random,"Connection":"close"}
        
        des_response = requests.get(url=des_url,headers = header)
        info_response = requests.get(url=info_url,headers = header)
        
        info_response_json = json.loads(info_response.text)

        title = info_response_json["name"]
        des = des_response.text
        
        #icon
        '''icon_link = info_response_json["attachments"][0]["url"]
        icon_file_name = info_response_json["attachments"][0]["title"]
        print(icon_link)
        iconFileResponse = requests.get(url=icon_link)
        
        icon_file_obj = open('./assets/icons/'+icon_file_name,mode="wb")
        icon_file_obj.write(iconFileResponse.content)'''
        
        infoDict = {}

        infoDict['title'] = title
        infoDict['des'] = des

        '''infoDict['icon_file_name'] = icon_file_name'''
        
        collection.insert_one(infoDict)

t_list = []
for i in range(5):
    t = threading.Thread(target=spiderFunc)
    t_list.append(t)
    t.start()
for t in t_list:
    t.join()
