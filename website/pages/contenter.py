import requests
with  open('ids.txt') as f:
    for line in f.readlines():
        line=line.strip('\n')
        print(line)
        
        #爬取
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}

        url = "https://addons-ecs.forgesvc.net/api/v2/addon/"+str(line)+"/description"
        des = requests.get(url=url,headers=headers)
        desText = des.text
        print(desText)
        page = open(str(line)+".html", "a", encoding="utf-8")
        page.write(desText)
        page.close()
    f.close()
