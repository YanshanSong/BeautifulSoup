html_doc = '''
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
...
'''
import bs4
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc, 'lxml')

# 调用tag的find_all方法时，BeautifulSoup会检索当前tag的
# 所有子孙节点，如果只想搜索tag的直接子节点，可以使用
# 参数recursive = false

print(soup.html.find_all("title"))
print(soup.html.find_all("title",recursive = False))

# 只有find_all() 和 find()支持recursive参数

# 像调用find_all()一样调用tag
# find_all()的简写方法
print(soup.find_all("a") == soup("a"))
print(soup.title.find_all(string=True) == soup.title(string=True))

# 使用find_all方法并设置limit=1参数不如直接调用find()方法
print(soup.find_all("title",limit=1))
print(soup.find('title'))

print("\n\n\n",soup.head.title)
# 原理
# soup.find("head").find("title")
print(soup.title)
print(soup.head.title == soup.title)