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

a_string = soup.find(string="Lacie")

# find_parents( name , attrs , recursive , string , **kwargs )
# find_parent( name , attrs , recursive , string , **kwargs )
# find_parents()和find_parent()用来搜索当前节点的父辈节点
# 搜索方法与普通tag的搜索方法相同

print(a_string.find_parents("a"))
print(a_string.find_parents("p"))
print(a_string.find_parents("p", class_="title"))
