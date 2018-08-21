#coding=utf-8
from selenium import webdriver
import os
import time
# set little time stop and big time stop for viewing changes
little_time_stop = 1
big_time_stop = 2
# 默认广告条数
ads_num_require = 8
# 请求连接
req_url = "https://item.jd.com/7171218.html"
# 打开浏览器

browser = webdriver.Firefox()
# 开始请求
browser.get(req_url)
print(browser.page_source);
#print(browser)
# 获取所有的广告
# browser.find_element_by_css_selector("#J-detail-content").get_attribute(name)
# browser.find_element_by_css_selector("#J-detail-content").text
# aitem=browser.find_elements_by_css_selector("#J-detail-content img")
# print(len(aitem))
# for i in aitem:
#     print(i.get_attribute("data-lazyload"))



# 关闭当前窗口
browser.close()
# 关闭所有已经打开的窗口
browser.quit()