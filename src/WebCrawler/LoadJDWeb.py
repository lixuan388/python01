#!/usr/bin/python3

from pyquery import PyQuery as pq
from selenium import webdriver
import pymongo


import json
import base64

def LoadJDWeb(url):
    
    WebData={}
    WebData["WebUrl"]=url
    browser = webdriver.Firefox()
    browser.get(url)
    htmlData=browser.page_source    
    # 关闭当前窗口
    browser.close()
    # 关闭所有已经打开的窗口
    browser.quit()
    doc = pq(htmlData)
    #print(doc)
    
    #--------------商品图片列表begin-----------------------
    defaultImageUrl="http://img12.360buyimg.com/n1/"
    specItems=doc(".spec-items img").items()
    specItemsImageUrl=[]
    Index=0
    #print(specItems)
    for specItemsInfo in specItems:
        #print(specItemsInfo)
        ImageUrl=specItemsInfo.attr("data-url")
        
        specItemsImageUrl.append(defaultImageUrl+ImageUrl)
        #print(defaultImageUrl+ImageUrl)
        
        Index=Index+1        
    WebData["ItemsImageUrl"]=specItemsImageUrl;
    #--------------商品图片列表end-----------------------
    skuName=doc(".sku-name").text()
    
    WebData["skuName"]=skuName;
    #print(skuName)
    price=doc("span.p-price .price").text()
    WebData["price"]=price;
    #price=doc(".summary-price-wrap")
    #print(price)
    
    #--------------简价图片列表begin-----------------------
    contentImageUrl=[]
    imgItems=doc("#J-detail-content img").items()
    for img in imgItems:
        ImageUrl=img.attr("data-lazyload")
        ImageUrl=ImageUrl.replace("http://","//")
        ImageUrl=ImageUrl.replace("//","http://")
        print(ImageUrl)
        
        contentImageUrl.append(ImageUrl)
    WebData["contentImageUrl"]=contentImageUrl;
    #--------------简价图片列表列表end-----------------------
    
    print(WebData)
    
#     print("------mongodb Post begin-------")
#     
#     myclient = pymongo.MongoClient("mongodb://www.17ecity.cc:57017/")
#     mydb = myclient["WebCrawler"]
#     mycol = mydb["jd"]
#     
#     updateQuery = { "WebUrl": url }
#     updateValues = { "$set": WebData }
# 
# 
#     x = mycol.update_one(updateQuery, updateValues) 
#     print(x)
#     print("------mongodb Post success-------")
        
    
    
LoadJDWeb("https://item.jd.com/7171218.html")    