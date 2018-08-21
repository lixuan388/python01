import pymysql
import json
import hashlib
 


# 
# 打开数据库连接
db = pymysql.connect("localhost","root","root","storagedb" )
 
 
###################更新商品图片信息################### 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT * from agi_goodsinfo ")  
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
while data!=None:
    print(data)
    print(data[16])     
    
    hash_sha1 = hashlib.sha1(data[16].encode("utf8"))
    image=hash_sha1.hexdigest()
    print(image)
    
    sql ="update agi_goodsinfo set agi_goodsimage1='/image/pandora/"+image+".jpg' where agi_id='"+data[0]+"'";
    try:
       # 执行sql语句
       curUpdate = db.cursor()
       
       curUpdate.execute(sql)
       # 提交到数据库执行
       db.commit()
    except:
       # 如果发生错误则回滚
       db.rollback()
       
    data = cursor.fetchone()

###################更新商品图片信息 end ################### 
###################更新商品价格 ################### 

try:
   # 执行sql语句
   
    sql ="update agi_goodsinfo set AGI_SaleMoney1=agi_item3,AGI_SaleMoney2=agi_item4 where agi_item3<>'None'";
    
    curUpdate.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()
       
try:
   # 执行sql语句
   
    sql ="update agi_goodsinfo set AGI_SaleMoney1=agi_item5,AGI_SaleMoney2=agi_item6 where agi_item5<>'None'";    
    
    curUpdate.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()
    
try:
   # 执行sql语句
   
    sql ="update agi_goodsinfo set AGI_SaleMoney1=REPLACE(REPLACE(agi_item7,'HK$',''),',',''),AGI_SaleMoney2=0 where agi_item7<>'None'";    
    
    curUpdate.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()
       
###################更新商品价格  end  ################### 

    
print("end")      
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