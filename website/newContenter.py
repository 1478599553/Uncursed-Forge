
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
requests.packages.urllib3.disable_warnings()
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
    
    while spiderQueue.empty()==False:
        try:
            id_to_crawl = spiderQueue.get()
            
            files_info_list = []

            print(id_to_crawl)
            des_url = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(id_to_crawl)+"/description"
            info_url = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(id_to_crawl)
            files_info_url = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(id_to_crawl)+"/files"

            time.sleep(4)
            header = {"user-agent": ua.random,"Connection":"close"}
            
            des_response = requests.get(url=des_url,headers = header,  verify=False)
            info_response = requests.get(url=info_url,headers = header,  verify=False)
            files_info_response = requests.get(url=files_info_url,headers= header,  verify=False)
            
            
            info_response_json = json.loads(info_response.text)
            files_info_json = json.loads(files_info_response.text)

            title = info_response_json["name"]
            des = des_response.text
            

            for single_file_info in files_info_json:
                fileDate = single_file_info['fileDate']
                downloadUrl = single_file_info['downloadUrl']
                temp_dic = {"FileDatetime": fileDate,"DownloadLink": downloadUrl}
                files_info_list.append(temp_dic)
            
            
            files_info_list.sort(key= lambda x:x["FileDatetime"],reverse=True)

            #icon
            icon_link = info_response_json["attachments"][0]["thumbnailUrl"]
            full_icon_link = info_response_json["attachments"][0]["url"]
            icon_file_name = info_response_json["attachments"][0]["title"]
            
            print(icon_link)
            iconFileResponse = requests.get(url=icon_link,  verify=False)
            full_iconFileResponse = requests.get(url=full_icon_link,  verify=False)

            icon_file_obj = open('./assets/icons/'+icon_file_name,mode="wb")
            icon_file_obj.write(iconFileResponse.content)
            
            full_icon_file_obj = open('./assets/full_icons/'+icon_file_name,mode="wb")
            full_icon_file_obj.write(full_iconFileResponse.content)
            
            summary = info_response_json['summary']

            
            infoDict = {}
            infoDict["id"] = id_to_crawl
            infoDict['title'] = title
            infoDict['des'] = des
            infoDict['files'] = files_info_list
            infoDict['summary'] = summary

            infoDict['icon_file_name'] = icon_file_name
            idFlagDic = {}
            idFlagDic['id'] = id_to_crawl
            

            #collection.insert_one(infoDict)
            
            collection.update_one({"id":id_to_crawl},{"$set":infoDict},True)
            print('还剩'+str(spiderQueue.qsize())+"个")
            
        except Exception as e:
            print(repr(e))
            print("发生在"+str(id_to_crawl))
            spiderQueue.put(id_to_crawl)

t_list = []
for i in range(10):
    t = threading.Thread(target=spiderFunc)
    t_list.append(t)
    t.start()
for t in t_list:
    t.join()
