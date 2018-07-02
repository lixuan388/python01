#!/usr/bin/python3
import pymongo

import json

 
myclient = pymongo.MongoClient("mongodb://www.17ecity.cc:57017/")

dblist = myclient.database_names()
for db in dblist:
    print(db)
    
mydb = myclient["WebCrawler"]
 
mycol = mydb["jd"]


for x in mycol.find({},{"_id":0}):
    print(x)
    print(x['ItemsImageUrl'])
    for img in x['ItemsImageUrl']:
        print(img)
 
