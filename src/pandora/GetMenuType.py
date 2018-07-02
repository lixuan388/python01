from pyquery import PyQuery as pq
import pandora.productType as productType
import json
import hashlib  

def loadMenuType(url):  
    doc = pq(url)
    typeJson=[]
    productTypeJson=[]
    li_level_1=doc("ul.level-1>li").items()
    print("begin")
    for li1 in li_level_1:
        level1={}
        Name_level_1=li1("a>span").text();
#         print("1:"+Name_level_1)
        
        level1["Name"]=Name_level_1
        
        Href="https://hk.pandora.net"+li1("a").attr("href").replace("https://hk.pandora.net","")     
        level1["Href"]=Href;
        sha = hashlib.sha1(Href.encode('utf-8'))  
        s = sha.hexdigest()  
        level1["Key"]=s;
#         print(s)
        productTypeJson=productTypeJson+productType.loadProductTypeData(s,Href+"?sz=200&start=0&format=page-element")
        level2=[]
#         print(li1("ul.level-2_inner li").html())
        li_level_2=li1("ul.level-2_inner li").items()
        
        for li2 in li_level_2:            
            Name_level_2=li2("a").text();
            
            level2Li={}
            level2Li["Name"]=li2("a").text()
            Href="https://hk.pandora.net"+li2("a").attr("href").replace("https://hk.pandora.net","")     
            level2Li["Href"]=Href;
            sha = hashlib.sha1(Href.encode('utf-8'))  
            s = sha.hexdigest()  
            level2Li["Key"]=s;
            
            productTypeJson=productTypeJson+productType.loadProductTypeData(s,Href+"?sz=200&start=0&format=page-element")
        
            level2.append(level2Li)
        level1["level"]=level2;
        
        img=li1(".flymenu_right img").attr("src");
        level1["image"]=img;
        typeJson.append(level1)
        
    
    JsonData=json.dumps(typeJson)
    print(JsonData)
    
    f = open("D:\图片\pandora\json\menuType.json", 'w') # 若是'wb'就表示写二进制文件
    f.write(JsonData)
    
    JsonData=json.dumps(productTypeJson)
    print(JsonData)
    
    f = open("D:\图片\pandora\json\productType.json", 'w') # 若是'wb'就表示写二进制文件
    f.write(JsonData)
    
    
    print("end")


f = open("D:\图片\pandora\menu\menu.html", 'r', encoding='UTF-8') # 若是'wb'就表示写二进制文件
menu=f.read()   
# print(menu)
loadMenuType(menu)        