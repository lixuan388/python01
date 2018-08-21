#!python3

from pyquery import PyQuery as pq
from selenium import webdriver


import urllib.request
import hashlib  
import time
import os
from WebCrawler import mongodb

# import pymongo
# import json
# import base64

JDUrl='https://m.jd.com/'
BasePath='D:\\Temp\\Images\\'




def LoadJDWebMall(url):
    try:
        browser = webdriver.Firefox()
    #     browser.implicitly_wait(30)
        browser.get(url)
    #     time.sleep(30)
        
    #     body=browser.find_element_by_tag_name("body");
    #     print(body)
    #     print(body.size)
    #     for i in range(10):
    #         browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    #         time.sleep(2)
    #         print(body.size)
    #     htmlData=browser.page_source
        webData={}
        LoadScrollImage(browser,webData)
        print(webData)
    finally:
        # 关闭当前窗口
        browser.close()
        # 关闭所有已经打开的窗口
        browser.quit()

def LoadScrollImage(browser,webData):
    print("LoadScrollImage");
    html=browser.page_source
    doc = pq(html)
#     print(doc);
    img=doc(".new-slide.j_slide_list li img[init_src]").items();
    while (len(list(img))>0):
        time.sleep(2)        
        html=browser.page_source
        doc = pq(html)        
        img=doc(".new-slide.j_slide_list li img[init_src]").items();
        print("wait src load")
            
    
    img=doc(".new-slide.j_slide_list li img").items();
    sliderWrapper=[]
    for ImgTtem in img:
#         print(ImgTtem)
        src=ImgTtem.attr("src")
#         print(src)
        imgJson={}
        
        Href="http:"+src     
          
        sha = hashlib.sha1(Href.encode('utf-8'))  
        id = sha.hexdigest()  
        
        imgJson["id"]=id
        imgJson["src"]=src
        imgJson["Img"]=loadUrlImage(Href,id)
        print(imgJson)
        mongodb.updateData("sliderWrapper", id, imgJson)
        
        sliderWrapper.append(imgJson)
    webData["sliderWrapper"]=sliderWrapper
    
    
    
    
    
def loadUrlImage(ImageUrl,id): 
    
    s = ""+id+".jpg"
    filename= BasePath+s
    if not os.path.exists(filename):    
        res = urllib.request.urlopen(ImageUrl).read()
        f = open(filename, 'wb') # 若是'wb'就表示写二进制文件
        f.write(res)   
    return s
    
    
LoadJDWebMall(JDUrl)    