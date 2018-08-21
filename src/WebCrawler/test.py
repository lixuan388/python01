import pymongo

print("------begin-------")
dbHost="mongodb://www.17ecity.cc:57017/" 
myclient = pymongo.MongoClient(dbHost)
mydb = myclient["WebCrawler"]
mycol = mydb["jd"]


for x in mycol.find():
    
    url=x["WebUrl"]
    print("url:"+url)
    
    for img in x["contentImageUrl2"]:
        print("<img src='http://www.17ecity.cc"+img+"'") 
    
print("------end-------")