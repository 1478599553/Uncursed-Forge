from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)   #隐形等待
driver.get('https://www.baidu.com/')
sleep(1)

#以五种定位方式定位到百度首页的搜索输入框
kw_find = driver.find_element_by_id('kw')
#kw_find= driver.find_element_by_class_name('s_ipt')
#kw_find= driver.find_element_by_name('wd')
#kw_find = driver.find_element_by_xpath('//*[@id="kw"]')
#kw_find = driver.find_element_by_css_selector('#kw') #id用#kw，class用.s_ipt ，与css的简写方式相同

#send_keys() 是selenium自带的方法，用来输入文本
kw_find.send_keys('selenium')

#使用id定位方式定位到搜索按钮
su_find = driver.find_element_by_id('su')

#click() 是selenium自带的方法，用来点击定位的元素
su_find.click()

sleep(1)