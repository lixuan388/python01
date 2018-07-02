#!/usr/bin/python3

from pyquery import PyQuery as pq
import json
import base64
 
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

def loadProductDetil(url):
     
    doc = pq(url)
    attributes=doc(".product-main-attributes>ul>li").items()
    
    attributesData=[]
    for attributesInfo in attributes:
        label=attributesInfo(".label").text()
        value=attributesInfo(".value").text()
        
        Data={label:value}
        attributesData.append(Data)
    
    thumbnails=doc("#thumbnails>ul>li>a").items()
    
    thumbnailsData=[]
    for thumbnailsInfo in thumbnails:
#         print(thumbnailsInfo)
        value=thumbnailsInfo.attr("href")        
        Data={"image":value}
        thumbnailsData.append(Data)
        
    
    primaryImage="None" if doc(".product-primary-image>.product-image") is None else doc(".product-primary-image>.product-image").attr("href")
        
    
    Detil={"attributes":attributesData,"thumbnails":thumbnailsData,"primaryImage":primaryImage}
    
    return Detil
            
        
        

#print(li(".product-tile").attr("data-itemid"))

# p=loadProductDetil("https://hk.pandora.net/zh/rings/stacking-rings/Mixed-Metals-Enchanted-Crown-Ring-Set/R800151.html?cgid=8be7f669-99b0-4cf3-925c-a0c9008c114a&src=categorySearch")
# Json=json.dumps(p)
# print(Json)
# f = open("d:/Temp/Detil.json", 'w') # 若是'wb'就表示写二进制文件
# f.write(Json)

# print("length:"+str(len(p)))
# for id in p:
#     
#     print("ID1:"+id['data-itemid'])
#     