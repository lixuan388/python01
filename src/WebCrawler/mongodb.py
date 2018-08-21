#!/usr/bin/python3


import pymongo

import json

 
myclient = pymongo.MongoClient("mongodb://hc.17ecity.cc:57017/")
mydb = myclient["WebData"]

def updateData(tableName,id,dataJson):
    mycol = mydb[tableName]
    result=mycol.update_one({'id':id},{'$set':dataJson},True)
#     print(result)
#     print(result.matched_count,result.modified_count)
    
 
