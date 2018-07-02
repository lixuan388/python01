#!/usr/bin/python3

from pyquery import PyQuery as pq
import json
import base64

import pandora.productDetil as productDetil
 

def loadProductTypeData(key,url):
     
    doc = pq(url)
    a=doc(".product-tile").items()
    
    ProductData=[]
    for productInfo in a:
        #productInfo=next(a)
        #print("类型为:%s"%type(productInfo))
#        print(productInfo)
        dataItemid="None" if productInfo(".product-tile").attr("data-itemid") is None else productInfo(".product-tile").attr("data-itemid")
        
        Data={}
             
        Data["dataItemid"]=dataItemid   
        Data["key"]=key
        ProductData.append(Data)
        
        
    
    return ProductData
            
        
        
'''

#print(li(".product-tile").attr("data-itemid"))

p=loadProductData("手鏈","https://hk.pandora.net/zh/bracelets/?sz=200&start=0&format=page-element")
Json=json.dumps(p)

# f = open("d:/Temp/手鏈.json", 'w') # 若是'wb'就表示写二进制文件
# f.write(Json)

print("length:"+str(len(p)))
for id in p:
    
    print("ID1:"+id['data-itemid'])
    
'''