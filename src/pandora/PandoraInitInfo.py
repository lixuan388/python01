import pymysql
import json
import hashlib
 


# 
# 打开数据库连接
db = pymysql.connect("localhost","root","root","storagedb" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
productFile = open("D:\\Temp\\pandora.json", "r")
product=productFile.read()
productJson= json.loads(product)
MaxC=len(productJson)  
for i in range(MaxC):    
    dataitemid=productJson[i]["data-itemid"]
    hash_md5 = hashlib.md5(dataitemid.encode("utf8"))
    AGI_ID=hash_md5.hexdigest()
    AGI_ThirdPartyID=productJson[i]["data-itemid"]
    AGI_GoodsName=productJson[i]["productName"]
    AGI_Item1=productJson[i]["product-image"]
    AGI_Item2=productJson[i]["name-link"]
    AGI_Item3=productJson[i]["saleprice"]
    AGI_Item4=productJson[i]["stdprice"]
    AGI_Item5=productJson[i]["stdminprice"]
    AGI_Item6=productJson[i]["stdmaxprice"]      
    AGI_Item7=productJson[i]["standardprice"]      
      

    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT * from agi_goodsinfo where agi_id='"+AGI_ID+"'")
      
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    if data==None:
        print("插入新记录")
        sql ="INSERT INTO agi_goodsinfo(AGI_ID,AGI_BrandName,AGI_GoodsName,AGI_BarCode,AGI_ThirdPartyID,AGI_Item1,AGI_Item2,AGI_Item3,AGI_Item4,AGI_Item5,AGI_Item6,AGI_Item7,_Status)\
        VALUES\
        ('"+AGI_ID+"','PANDORA','"+AGI_GoodsName+"','"+AGI_ThirdPartyID+"','"+AGI_ThirdPartyID+"','"+AGI_Item1+"','"+AGI_Item2+"','"+AGI_Item3+"','"+AGI_Item4+"','"+AGI_Item5+"','"+AGI_Item6+"','"+AGI_Item7+"','I')";
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except:
           # 如果发生错误则回滚
           db.rollback()
    else :
        print("已存在记录:"+AGI_ID)    
 
  
# 关闭数据库连接
db.close()



"""
"data-itemid": "791722NOP",
"product-image": "https://hk.pandora.net/dw/image/v2/AAWM_PRD/on/demandware.static/-/Sites-pandora-master-catalog/default/dwf6b6efb4/images/productimages/791722NOP-1.jpg?sw=170&sh=170&sm=fit",
"name-link": "/zh/new-jewellery/SALE---Opalescent-Pink-Geometric-Facets-Charm/791722NOP.html?cgid=NEW&src=categorySearch", 
"productName": "SALE - Opalescent Pink Geometric Facets Charm",
"priceStandard": "HK$449.00", 
"priceSales": "HK$229.00", 
"standardprice": "None", 
"": "HK$", 
"": "229.0", 
"": "449.0", 
"": "None", 
"": "None", 
"": "None", 
"": "None", 
"": "None", 
"": "None", 
"": {"attributes": [{"\u5546\u54c1\u7de8\u865f": "791722NOP"}, {"\u984f\u8272:": "\u7c89\u7d05\u8272"}, {"\u7269\u6599:": "\u7121\u5176\u4ed6\u6750\u8cea"}, {"\u91d1\u5c6c:": "925\u9280"}, {"\u5bf6\u77f3:": "\u6c34\u6676"}, {"\u4e3b\u9898:": "\u6642\u5c1a\u98a8\u683c"}], 
         "thumbnails": [], 
         "primaryImage": "https://hk.pandora.net/dw/image/v2/AAWM_PRD/on/demandware.static/-/Sites-pandora-master-catalog/default/dwf6b6efb4/images/productimages/791722NOP-1.jpg?sw=1000&sh=1000&sm=fit"}},

"""