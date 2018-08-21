#!python3

from pyquery import PyQuery as pq
from selenium import webdriver



from WebCrawler import mongodb

# import pymongo
# import json
# import base64

JDUrl='https://pro.m.jd.com/mall/active/3nxcGU8mCsjXN5MjTGQ1AX2LbdfF/index.html?has_native=0'
BasePath='D:\\Temp\\Images\\'




def LoadJDWebMall_item(url):
    try:
        browser = webdriver.Firefox()
        browser.get(url)
        
        webData={}
        LoadScrollItem(browser,webData)
        print(webData)
    finally:
        # 关闭当前窗口
        browser.close()
        # 关闭所有已经打开的窗口
        browser.quit()

def LoadScrollItem(browser,webData):
    print("LoadScrollItem");
    html=browser.page_source
    doc = pq(html)
#     print(doc);
    item=doc(".basement_item_con").items();
    itemList=[]
    for itemData in item:
        
        datasku=itemData.find('a').attr('data-sku')
        datahref=itemData.find('a').attr('data-href')
        print(datahref)
#         print(ImgTtem)
        item_pic=itemData.find('.item_pic img')
#         print(item_pic)
        dataSrc=item_pic.attr('data-src')
        src=item_pic.attr('src')
        GoodsImage=''
        if dataSrc==None:
#             print(src)
            GoodsImage=src
        else:
#             print(dataSrc)
            GoodsImage=dataSrc
        
        item_text=itemData.find('.item_text .text');
        GoodsName=item_text.html()
#         print(GoodsName)
        
        item_price =itemData.find('.item_price');        
        GoodsPrice2=item_price('span:last').text().replace('.','')
        item_price('span').remove()
        GoodsPrice1=item_price.text()
        
        itemJson={}
        itemJson['SrcFrom']='JD'
        itemJson['SrcInfoHref']=datahref
        itemJson['DataSku']=datasku
        itemJson['GoodsKeyID']='JD'+datasku
        itemJson['GoodsImage']=GoodsImage
        itemJson['GoodsName']=GoodsName
        itemJson['GoodsPrice1']=GoodsPrice1
        itemJson['GoodsPrice2']=GoodsPrice2
        
        infoJson=LoadItemInfo(datahref,browser)
        
        itemJson['GoodsDescInfo']=infoJson
        itemList.append(itemJson)
        print(itemJson)
        
        mongodb.updateData("GoodsList", itemJson['GoodsKeyID'], itemJson)
        
        
    webData['Data']=itemList

def LoadItemInfo(url,browser):    
    browser.get('https:'+url)    
    html=browser.page_source
    doc = pq(html)
    infoJson={}
    loopImgList=[]
    loopImgUl=doc("#loopImgUl li img").items()
    for img in loopImgUl:
#         print(img)
        imgJson={}
        imgSrc=img.attr('src')
        backSrc=img.attr('back_src')
        imgJson['ImgSrc']=imgSrc;
        imgJson['ImgBackSrc']=backSrc;
        loopImgList.append(imgJson)        
    infoJson['LoogImageList']=loopImgList
    
    itemName=doc("#itemName").text()
    infoJson['ItemName']=itemName
    
    priceSaleChoice=doc("#priceSaleChoice").text()
    infoJson['ItemSalePrice']=priceSaleChoice
    
    commDesc=doc("#commDesc").html()
    infoJson['ItemDesc']=commDesc
#     print(infoJson)
    return infoJson
    
    
    
    
LoadJDWebMall_item(JDUrl)    