import pymongo
import json
import urllib.request
import json
import os
from PIL import Image
from io import BytesIO
import hashlib  

###################begin#############################
def LoadImageFromUrl(url,localPath):
    
    Href=url     
    sha = hashlib.sha1(Href.encode('utf-8'))  
    s = sha.hexdigest()
    res = urllib.request.urlopen(url).read()
    file = BytesIO()
    file.write(res)
    img = Image.open(file)  # PIL库加载图片
    print (img.format, img.size, img.mode)
    w,h=img.size
    isExists=os.path.exists(localPath+s+"\\")
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(localPath+s+"\\") 
    imageFileName=s+"."+img.format
    img.save(localPath+imageFileName)
    index=1000
    for i in range(10):
        tempImg = img.crop((0,h /10 *i,w,h /10 *(i+1)))
        tempImg.save(localPath+s+"\\"+s+str(index)+"."+img.format)
        index=index+1;
    return imageFileName
    print("end")
###################end#############################

print("------begin-------")
dbHost="mongodb://www.17ecity.cc:57017/" 
myclient = pymongo.MongoClient(dbHost)
mydb = myclient["WebCrawler"]
mycol = mydb["jd"]


for x in mycol.find():
    
    url=x["WebUrl"]
    Href=url     
    sha = hashlib.sha1(Href.encode('utf-8'))  
    s = sha.hexdigest()
    
    LocalTempImageFile="d:\\Temp\\Images\\contentImage\\"+s+"\\"
    isExists=os.path.exists(LocalTempImageFile)
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(LocalTempImageFile) 
    print(x)
    
    contentImageUrl=[]
    
    for img in x["contentImageUrl"]:        
        print(img)
        imageFileName=LoadImageFromUrl(img,LocalTempImageFile)        
        contentImageUrl.append("/Images/contentImage/"+s+"/"+imageFileName)
    x["contentImageUrl2"]=contentImageUrl;
    
    updateQuery = { "WebUrl": url }
    updateValues = { "$set": x }
    x = mycol.update_one(updateQuery, updateValues) 
    
print("------end-------")
