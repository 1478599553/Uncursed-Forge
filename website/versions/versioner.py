from os import name
import requests
import json
import os
import ssl


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

urlVer = "https://addons-ecs.forgesvc.net/api/v2/minecraft/version"
Ver = requests.get(url=urlVer,headers=headers)
VerText = Ver.text
JsonVer  = json.loads(VerText)
for i in range (0,len(JsonVer)):
    #print(JsonVer)
    verString = JsonVer[i].get("versionString")
    #print(verString)
    VerFile = open(os.getcwd()+r"\\versions.txt", "a",encoding="utf-8")
        
    VerFile.write(verString+"\n")

    VerFile.close()