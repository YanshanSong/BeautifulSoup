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

# 按照CSS类名搜索tag的功能非常实用，但标识CSS类名的关键字class
# 在Python中是保留字，使用class做参数会导致语法错误
# 从BeautifulSoup的4.1.1版本开始，可以通过class_参数搜索有指定CSS类名的tag

print(soup.find_all("a",class_="sister"))

# class_参数同样接受不同类型的过滤器，字符串，正则表达式，方法或True
print(soup.find_all(class_=re.compile("itl")))

def has_six_characters(css_class):
	return css_class is not None and len(css_class) == 6
print(soup.find_all(class_=has_six_characters))

def has_four_characters(css_class):
	return css_class is not None and len(css_class) == 4
print(soup.find_all(class_=has_six_characters))

# tag的class属性是多值属性。
# 按照CSS类名搜索tag时，可以分别搜索tag中的每个CSS类名
css_soup = BeautifulSoup('<p class="body strikeout"></p><p class="royal"></p>','lxml')
print(css_soup.find_all("p",class_="strikeout"))

print(css_soup.find_all("p",class_=has_four_characters)) 
# [<p class-"body strikeout"></p>]

# 搜索class属性时也可以通过CSS值完全匹配
# 完全匹配class的值时，如果CSS类名的顺序与实际不符，将搜素不到结果
print(css_soup.find_all("p",class_="body strikeout"))

# class_参数同样接受列表，依次匹配不同的class类名
print(css_soup.find_all(class_=["body","strikeout","royal"]))

