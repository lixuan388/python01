import requests

from pyquery import PyQuery as pq
 
 
 
url='https://hk.pandora.net/zh/charms/?src=categorySearch&postion=top'
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding 
    print(r.text) #部分信息
    doc = pq(r.text)
    print("-----------------doc----------------------")
    print(doc)
    print("-----------------doc('head')----------------------")
    print(doc('head'))    
    
except:
    print("失败")
    
    
