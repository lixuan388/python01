#!/usr/bin/python3

import urllib.request
import json
import os
from PIL import Image
from io import BytesIO
import hashlib  

 
url="http://img14.360buyimg.com/cms/jfs/t20110/321/438940667/296860/37d0ea9c/5af55032N16ea0c25.jpg"

Href=url     
sha = hashlib.sha1(Href.encode('utf-8'))  
s = sha.hexdigest()  
    
    
res = urllib.request.urlopen(url).read()
file = BytesIO()
file.write(res)
img = Image.open(file)  # PIL库加载图片
print (img.format, img.size, img.mode)
w,h=img.size

imageFile="d:\\Temp\\"+s+"\\"
    
index=1000
for i in range(10):
    tempImg = img.crop((0,h /10 *i,w,h /10 *(i+1)))
    isExists=os.path.exists(imageFile)
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(imageFile) 
    tempImg.save(imageFile+s+str(index)+".jpg")
    index=index+1;
    
img.save(imageFile+s+".jpg")

print("end")