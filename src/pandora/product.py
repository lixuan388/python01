#!/usr/bin/python3

from pyquery import PyQuery as pq
import json
import base64

import pandora.productDetil as productDetil
 
#url='https://hk.pandora.net/zh/collections/high-summer/?sz=200&start=0&format=page-element'
#url2=
"""
<div class="product-tile" id="a0767c3e757ce7a375f852aec5" data-itemid="797183MPR" data-cgid="high-summer-collection">
<div class="badge_section">
</div>
<div class="flagTop">
<span class="flagValue"><div style="position:absolute; top: -3PX; right: 10PX ;pointer-events: none;"><img src="https://staging-apacestore-pandora.demandware.net/on/demandware.static/-/Sites-en-HK-Library/default/v0170199e9a35dabfce7752dfa26eada35c5b926e/images/badges/20180531_Badge_Drop3_zh.png" style="height: 30px;"/></div></span>
</div>
<div class="product-image">
<a class="thumb-link" href="/zh/collections/high-summer/%E5%BD%A9%E8%89%B2%E9%A6%AC%E2%80%8B%E2%80%8B%E8%B3%BD%E5%85%8B%E4%B8%B2%E9%A3%BE/797183MPR.html?cgid=high-summer-collection&amp;src=categorySearch" title="彩色馬​​賽克串飾">
<img src="https://hk.pandora.net/dw/image/v2/AAWM_PRD/on/demandware.static/-/Sites-pandora-master-catalog/default/dw5f3e7930/images/productimages/797183MPR-1.jpg?sw=170&amp;sh=170&amp;sm=fit" alt="彩色馬​​賽克串飾" title="彩色馬​​賽克串飾"/>
</a>
</div>
<div class="product-name text-line-3">
<a class="name-link" href="/zh/collections/high-summer/%E5%BD%A9%E8%89%B2%E9%A6%AC%E2%80%8B%E2%80%8B%E8%B3%BD%E5%85%8B%E4%B8%B2%E9%A3%BE/797183MPR.html?cgid=high-summer-collection&amp;src=categorySearch" title="彩色馬​​賽克串飾">
彩色馬​​賽克串飾
</a>
</div>
<div class="product-pricing">
<div class="product-price normal">
<span class="label-price-checkout">商品價格:</span>
<span class="price-standard-sales">
<span class="price-sales">
HK$599.00
</span>
<span class="No-Promotion"/>
</span>
<input type="hidden" value="HK$" id="currency" site="en-HK"/>
<input type="hidden" value="599.0" class="saleprice"/>
<input type="hidden" value="599.0" class="stdprice"/>
</div>
</div>
</div>
"""

def loadProductData(name,url):
     
    doc = pq(url)
    a=doc(".product-tile").items()
    
    ProductData=[]
    for productInfo in a:
        #productInfo=next(a)
        #print("类型为:%s"%type(productInfo))
#        print(productInfo)
        dataItemid="None" if productInfo(".product-tile").attr("data-itemid") is None else productInfo(".product-tile").attr("data-itemid")
#             print("data-itemid:"+dataItemid)
        productImage="None" if productInfo(".thumb-link img").attr("src") is None else productInfo(".thumb-link img").attr("src")
        
        priceStandard="None" if productInfo(".price-standard").html() is None else productInfo(".price-standard").text()
        priceSales="None" if productInfo(".price-sales").html() is None else productInfo(".price-sales").text()
#             print("product-image:"+productImage)
        nameLink="None" if productInfo(".name-link").attr("href") is None else  productInfo(".name-link").attr("href") 
#             print("name-link:"+nameLink)
        productName="None" if productInfo(".name-link").html() is None else productInfo(".name-link").text()
        standardprice="None" if productInfo(".standardprice").html() is None else  productInfo(".standardprice").text()
#             print("productName:"+productName)
        currency="None" if productInfo("#currency").attr("value") is None else productInfo("#currency").attr("value")
#             print("currency:"+currency)
        saleprice="None" if productInfo(".saleprice").attr("value") is None else  productInfo(".saleprice").attr("value")
#             print("saleprice:"+saleprice)
        stdprice="None" if productInfo(".stdprice").attr("value") is None else productInfo(".stdprice").attr("value")
#             print("stdprice:"+stdprice)    
#             print("price-sales:"+priceSales)            
        maxprice="None" if productInfo(".maxprice").attr("value") is None else productInfo(".maxprice").attr("value")
        minprice="None" if productInfo(".minprice").attr("value") is None else  productInfo(".minprice").attr("value")
        saleminprice="None" if productInfo(".saleminprice").attr("value") is None else productInfo(".saleminprice").attr("value")
        salemaxprice="None" if productInfo(".salemaxprice").attr("value") is None else productInfo(".salemaxprice").attr("value")
        stdminprice="None" if productInfo(".stdminprice").attr("value") is None else productInfo(".stdminprice").attr("value")
        stdmaxprice="None" if productInfo(".stdmaxprice").attr("value") is None else  productInfo(".stdmaxprice").attr("value")
        
        Data={}
        Data["Html"]=str(base64.b64encode(productInfo.html().encode('utf-8')),'utf-8')
        Data["data-itemid"]=dataItemid
        Data["product-image"]=productImage
        Data["name-link"]=nameLink
        Data["productName"]=productName
        Data["priceStandard"]=priceStandard
        Data["priceSales"]=priceSales
        Data["standardprice"]=standardprice
        Data["currency"]=currency
        Data["saleprice"]=saleprice
        Data["stdprice"]=stdprice
        Data["maxprice"]=maxprice
        Data["minprice"]=minprice
        Data["saleminprice"]=saleminprice
        Data["salemaxprice"]=salemaxprice
        Data["stdminprice"]=stdminprice
        Data["stdmaxprice"]=stdmaxprice
        
        detil=productDetil.loadProductDetil("https://hk.pandora.net"+nameLink)        
        Data["productDetil"]=detil
        ProductData.append(Data)
        
        
    
    return ProductData
            
        
        
'''

#print(li(".product-tile").attr("data-itemid"))

p=loadProductData("手鏈","https://hk.pandora.net/zh/bracelets/?sz=200&start=0&format=page-element")
Json=json.dumps(p)

# f = open("d:/Temp/手鏈.json", 'w') # 若是'wb'就表示写二进制文件
# f.write(Json)

print("length:"+str(len(p)))
for id in p:
    
    print("ID1:"+id['data-itemid'])
    
'''