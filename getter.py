from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome(r'C:\Users\Admin\Documents\uncursedforge\chromedriver.exe')
option = webdriver.ChromeOptions()
option.add_argument('-enable-webgl --no-sandbox --disable-dev-shm-usage')
#driver.get(r'https://www.curseforge.com/minecraft/mc-mods')
#driver.implicitly_wait(2)
#names = driver.find_elements_by_class_name(r'my-auto')

#names[1].click()

#print(len(names))
idFile = open("ids.txt", "w")
idFile.close()
pageNums = 50 + 1 #页数 + 1
for pagecount in range (1,pageNums,1):
    print("begin pagebased loop")
    
    driver.get(r'https://www.curseforge.com/minecraft/mc-mods?page='+str(pagecount))
    for num in range(0, 60, 3):
        #print (names[num].text)
        print("Current count is : ")
        print(int(num/3))
        driver.get(r'https://www.curseforge.com/minecraft/mc-mods?page='+str(pagecount))
        names = driver.find_elements_by_class_name(r'my-auto')
        driver.execute_script("arguments[0].scrollIntoView();",names[num])
        print("scrolled")
        names[num].click()
        print("clicked")
        driver.implicitly_wait(2)
        id = driver.find_element_by_xpath(r"/html/body/div[1]/main/div[1]/div[2]/section/aside/div[2]/div/div[1]/div[2]/div[1]/span[2]")
        print(id.text)
        
        #写入文件
        idFile = open("ids.txt", "a")
        idFile.write(id.text)
        idFile.write('\n')
        idFile.close()

        print("writed")

        driver.back()
    
#print (names[59].text)
#print(names[0].text)