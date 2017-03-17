html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import bs4
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc, 'lxml')

# findall(name, attrs, recursive, string, **kwargs)

# name参数接受字符串，正则表达式，列表，True
print(soup.find("title"))

print(soup.find(re.compile("tle")))

print(soup.find_all(["title","a"]))

# name + attrs
# 返回的是CSS Class为"title"的<p>标签
print(soup.find_all("p","title"))

# print(soup.find_all(string=re.compile("sisters")))

# keyword参数
# 如果一个指定名字的参数不是搜索内置的参数名
# 搜索时会把该参数当作指定名字tag的属性来搜索
# 如果包含一个名字为id的参数，Beautiful Soup会搜索
# 每个tag的"id"属性
print(soup.find(id="link2"))

# 如果传入href参数，Beautiful Soup会搜索每个tag的"href"属性
print(soup.find(href=re.compile("elsie")))

# 在文档树中查找所有包含id属性的tag，无论id的值是什么
print(soup.find_all(id=True))

# 使用多个指定名字的参数可以同时过滤tag的多个属性
print(soup.find_all(href=re.compile("elsie"),id="link1"))

# 有些tag属性在搜索中不能使用，但是可以通过find_all的方法的
# attrs参数定义一个字典参数来搜索包含特殊属性的tag:
# data_soup.find_all(attrs={"data-foo" : "value"})

# 按照CSS类名搜索tag的功能非常实用，但标识CSS类名的关键字class
# 在Python中是保留字，使用class做参数会导致语法错误
# 从BeautifulSoup的4.1.1版本开始，可以通过class_参数搜索有指定
# CSS类名的tag







