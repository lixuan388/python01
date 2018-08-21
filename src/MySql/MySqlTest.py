import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='s2.17ecity.cc', port=53306, user='storage', password='storage@17ecity.cc', db='storagedb')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT * from aus_users")
 
 
#获取字段信息
print("记录条数："+str(cursor.rowcount))


#获取字段信息
print(cursor.description)

FieldName={}
FieldNameByIndex=[]


FieldSize=len(cursor.description)
print("字段个数："+str(FieldSize))


for i in range(FieldSize): 
    field=cursor.description[i]
    FieldName[field[0]]=i;
    FieldNameByIndex.append(field[0])
#     data_dict.append({field[0]:1})
print(FieldName)
print(FieldNameByIndex[0])
# data_dict["AUS_ID"]
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print(data)
print("AUS_ID:"+data[FieldName["AUS_ID"]])
print("AUS_UserName:"+data[FieldName["AUS_UserName"]])
print("AUS_UserCode:"+data[FieldName["AUS_UserCode"]])
print("AUS_PassWord:"+data[FieldName["AUS_PassWord"]])


if data==None:
    print("插入新记录")
#     sql ="""
#     INSERT INTO aus_users(AUS_ID,AUS_UserName,AUS_UserCode,AUS_PassWord,_Status)
#     VALUES
#     ('1','test1','testcode','testpass','I');
#     """
#     try:
#        # 执行sql语句
#        cursor.execute(sql)
#        # 提交到数据库执行
#        db.commit()
#     except:
#        # 如果发生错误则回滚
#        db.rollback()
else :
    print("已存在记录")    
#     data[data_dict["AUS_ID"]]

 
# 关闭数据库连接
db.close()