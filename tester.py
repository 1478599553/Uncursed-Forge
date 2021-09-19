from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

#指定chrom的驱动
#执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
driver = webdriver.Chrome(r'C:\Users\Admin\Documents\uncursedforge\chromedriver.exe')
#driver = webdriver.Firefox()#这里是火狐的浏览器运行方法
#get 方法 打开指定网址

#driver.get(r'https://www.curseforge.com/minecraft/mc-mods')
#driver.implicitly_wait(2)
#names = driver.find_elements_by_class_name(r'my-auto')

#names[1].click()

#print(len(names))
idFile = open("ids.txt", "a")
pageNums = 3
for pagecount in range (1,pageNums,1):
    
    driver.get(r'https://www.curseforge.com/minecraft/mc-mods?page='+str(pagecount))
    
    
#print (names[59].text)
#print(names[0].text)
# 打印数据内容
idFile.close()