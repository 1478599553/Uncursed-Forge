import requests
import json

with  open('ids.txt') as f:
    for line in f.readlines():
        line=line.strip('\n')
        print(line)
        
        #爬取
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
        urlinfo = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(line)
        urldes = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(line)+"/description"
        des = requests.get(url=urldes,headers=headers)
        desText = des.text
        
        info = requests.get(url=urlinfo,headers=headers)
        infoText = info.text
        infoJson = json.loads(infoText)
        iconLink = infoJson.get("attachments")[0].get("thumbnailUrl")
        iconTemp = r'<div align="center"><img src="'+iconLink+'"/></div>'
        #print(desText)
        


        page = open(str(line)+".html", "a")
        page.write(desText)
        page.close()
    f.close()
