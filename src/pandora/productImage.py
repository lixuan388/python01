#!/usr/bin/python3

import urllib.request
import json
import os
 

import hashlib  

def loadProductImage(url):
    print(url)
    
    Href=url     
    sha = hashlib.sha1(Href.encode('utf-8'))  
    s = sha.hexdigest()  
    filename= "D:\\图片\\pandora\\image\\product\\"+s+".jpeg"
    if not os.path.exists(filename):    
        res = urllib.request.urlopen(url).read()
        f = open(filename, 'wb') # 若是'wb'就表示写二进制文件
        f.write(res)   
        
ImageList=[]       
        
f=open("D:\\图片\\pandora\\json\\pandora.json", 'r')
Json=f.read()
# print(Json)
JsonStr=json.loads(Json)
print(len(JsonStr))        
for j in JsonStr:
#     print(j["product-image"])
    ImageList.append(j["product-image"])
#     loadProductImage(j["product-image"])
    productDetil=j["productDetil"]
    ImageList.append(j["product-image"])
    thumbnails=j["productDetil"]["thumbnails"]
    for t in thumbnails:
#         print(t["image"])
        ImageList.append(t["image"])
         

f=open("D:\\图片\\pandora\\json\\menuType.json", 'r')
Json=f.read()        
        
JsonStr=json.loads(Json)
print(len(JsonStr))        
for j in JsonStr:
#     print(j["product-image"])
    ImageList.append(j["image"])
    
        
print(len(ImageList))        
for img in ImageList:
    loadProductImage(img)
    
print("end")