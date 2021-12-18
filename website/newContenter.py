
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

idfile = open('ids_autoFilled.txt',mode="r")
#

for id in idfile.readlines():
    idlist.append(id.strip('\n'))
idfile.close()

spiderQueue = queue.Queue(maxsize = 0)
TaskQueue = queue.Queue(maxsize = 0)
for id in idlist:
    spiderQueue.put(id)


def spiderFunc():
    print(spiderQueue.qsize())
    while (int(spiderQueue.qsize())==0)==False:
        try:
            id_to_crawl = spiderQueue.get()
            
            files_info_list = []

            print(id_to_crawl)
            des_url = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(id_to_crawl)+"/description"
            info_url = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(id_to_crawl)
            files_info_url = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(id_to_crawl)+"/files"

            time.sleep(8)
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
            
            for icon_item in info_response_json["attachments"]:
                
                if icon_item['isDefault'] == True:
                    icon_item_list = {}
                    icon_item_list['id'] = id_to_crawl
                    icon_item_list['icon_info'] = icon_item
                    TaskQueue.put(icon_item_list)
                    
            
            
            summary = info_response_json['summary']

            
            infoDict = {}
            infoDict["id"] = id_to_crawl
            infoDict['title'] = title
            infoDict['des'] = des
            infoDict['files'] = files_info_list
            infoDict['summary'] = summary

            
            idFlagDic = {}
            idFlagDic['id'] = id_to_crawl
            

            #collection.insert_one(infoDict)
            
            collection.update_one({"id":id_to_crawl},{"$set":infoDict},True)
            print('还剩'+str(spiderQueue.qsize())+"个")
            spiderQueue.task_done()
        except Exception as e:
            print(repr(e))
            print("发生在"+str(id_to_crawl))
            spiderQueue.put(id_to_crawl)

t_list = []
for i in range(20):
    t = threading.Thread(target=spiderFunc)
    t_list.append(t)
    t.start()
for t in t_list:
    t.join()


def get_icon():
        while TaskQueue.empty()==False:    
            item = TaskQueue.get()
            print(item)
            icon_link = item['icon_info']["thumbnailUrl"]
            full_icon_link = item['icon_info']["url"]
            icon_file_name = item['icon_info']["title"]
            print(icon_link)
            iconFileResponse = requests.get(url=icon_link,  verify=False)
            full_iconFileResponse = requests.get(url=full_icon_link,  verify=False)

            icon_file_obj = open('./assets/icons/'+icon_file_name,mode="wb")
            icon_file_obj.write(iconFileResponse.content)
            icon_file_obj.close()

            full_icon_file_obj = open('./assets/full_icons/'+icon_file_name,mode="wb")
            full_icon_file_obj.write(full_iconFileResponse.content)
            full_icon_file_obj.close()

            icon_info_dic={}
            icon_info_dic['icon_file_name'] = icon_file_name
            collection.update_one({"id":item['id']},{"$set":icon_info_dic},True)
            print(icon_file_name)
            TaskQueue.task_done()
icon_t_list = []

for i in range(15):
    icon_t = threading.Thread(target=get_icon)
    icon_t_list.append(icon_t)
    icon_t.start()
for icon_t in icon_t_list:
    icon_t.join()

