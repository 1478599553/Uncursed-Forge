import datetime
from os import replace
import re
import time
import json

str_p = '2017-05-28T02:04:53.117Z1'
str_p2 = '2018-05-28T02:04:53.117Z2'
str = "a123b"

date = re.findall(r"(.+?)T",str_p)
fileTime = re.findall("T(.+?)\.",str_p)

date2 = re.findall(r"(.+?)T",str_p2)
fileTime2 = re.findall("T(.+?)\.",str_p2)
#print(date)
#print(fileTime)
date0 = date[0]
date20 = date2[0]


replacedDate = date0.replace('-','')
replacedTime = fileTime[0].replace(":","")

replacedDate2 = date20.replace('-','')
replacedTime2 = fileTime2[0].replace(":","")

r1 = replacedDate + replacedTime
r2 = replacedDate2 + replacedTime2
print(r1)
print(r2)

s = [str_p,str_p2]
s.sort(reverse=True)
print(s)
print(s[0][-1])
