#!/usr/bin/python3
import book.loadhtml as loadhtml

from selenium import webdriver
url='http://172.10.10.17/book/6481250.62/gb/lasp.htm'

site='http://172.10.10.17/book/6481250.62/gb/'


loadhtml.loadData(site,url)

# browser2= webdriver.Firefox();
# data2=[]
# loadhtml.loadChildHrefData("http://172.10.10.17/book/6481250.62/gb/files/story/1asp.htm",browser2,data2)
# print(data2)
# # 关闭当前窗口
# browser2.close()
# # 关闭所有已经打开的窗口
# browser2.quit()   

