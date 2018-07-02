from pyquery import PyQuery as pq
 
url='https://hk.pandora.net/zh/charms/?src=categorySearch&postion=top'
 
doc = pq(url)
a=doc(".flymenu_left a").items()

for li in a:    
    print("--------------")
    print(li.attr("href"))
    
    
