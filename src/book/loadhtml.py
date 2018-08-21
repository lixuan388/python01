#!/usr/bin/python3

from pyquery import PyQuery as pq

from selenium import webdriver

import urllib.request
import json
import base64
 
 


    

def loadData(site,url):
     
    browser= webdriver.Firefox();
    browser.get(url)
    htmlData=browser.page_source    
            
    doc = pq(htmlData)
#     print(doc)
    
    a=doc("a").items()

    dataJson=[];
     
    browser2= webdriver.Firefox();
     
    for ahref in a:
#         print(ahref);
        print(ahref.attr("href"))
#         print(ahref.html())
        data={};
        data["href"]=ahref.attr("href")
        data["title"]=ahref.html()
        data2=[]
        loadChildHrefData(site+data["href"],browser2,data2);
        data["child"]=data2
         
        dataJson.append(data);
#     print(dataJson)
#      
    # 关闭当前窗口
    browser2.close()
    # 关闭所有已经打开的窗口
    browser2.quit()   
    JsonString=json.dumps(dataJson)
        
    f = open("D:\href.json", 'w') # 若是'wb'就表示写二进制文件
    f.write(JsonString)
    
    # 关闭当前窗口
    browser.close()
    # 关闭所有已经打开的窗口
    browser.quit()
    

def loadChildHrefData(url,browser,dataJson):    
    browser.get(url)
    htmlData=browser.page_source    
            
    doc = pq(htmlData)    
    
    loadHrefData(url,browser,dataJson)

    pos = url.rfind("/")
    site=url[:pos] 
#     print(site)

    a=doc("body>font>a").items()
#     print(a);   
    for ahref in a:
        href=ahref.attr("href")
        html=ahref.html()
        if html!="以上载时间排序":      
            loadHrefData(site+"/"+ahref.attr("href"),browser,dataJson)
            
#     print(dataJson)    
    return dataJson; 
        
def loadHrefData(url,browser,dataJson):    
    
    print(url)
    browser.get(url)
    htmlData=browser.page_source    
            
    doc = pq(htmlData)
#     print(doc)
    
    a=doc("tr>td:first>font>a").items()
 
    for ahref in a:
#         print(ahref);
#         print(ahref.attr("href"))
#         print(ahref.html())
          
        data={};
        data["href"]=ahref.attr("href")
        data["title"]=ahref.html()
          
        dataJson.append(data);
#     print(dataJson)

 
    return dataJson; 
        