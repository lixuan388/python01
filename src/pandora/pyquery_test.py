#!/usr/bin/python3

from pyquery import PyQuery as pq

import json
 
#url='https://hk.pandora.net/zh/collections/high-summer/?sz=200&start=0&format=page-element'
url2="""
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
     
doc = pq(url2)
productInfo=doc(".product-tile")
     
dataItemid="None" if productInfo(".product-tile").attr("data-itemid") is None else productInfo(".product-tile").attr("data-itemid")
#             print("data-itemid:"+dataItemid)
productImage="None" if productInfo(".thumb-link img").attr("src") is None else productInfo(".thumb-link img").attr("src")

priceSales="None" if productInfo(".price-sales").html() is None else productInfo(".price-sales").text()


    
print(priceSales)
    
#         print("----------------------------------------")




    

