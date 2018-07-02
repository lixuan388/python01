from pyquery import PyQuery as pq
import pandora.product as product
import json


def loadMenu(url):  
    doc = pq(url)
    a=doc(".sidecar_menu .level-1[href]").items()
    print("begin")
    Json=[]
    for menu in a:
        Name=menu.text();
        Href="https://hk.pandora.net"+menu.attr("href").replace("https://hk.pandora.net","")+"?sz=200&start=0&format=page-element"
        print(Name+":"+Href)
        Json=Json+product.loadProductData(Name,Href)
        
    print("end")
    JsonData=json.dumps(Json)
    f = open("d:/Temp/pandora.json", 'w') # 若是'wb'就表示写二进制文件
    f.write(JsonData)   

loadMenu("https://hk.pandora.net/zh/home")        