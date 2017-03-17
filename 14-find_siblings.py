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

# find_next_siblings() 和 find_next_sibling()
# find_next_siblings( name , attrs , recursive , string , **kwargs )
# find_next_sibling( name , attrs , recursive , string , **kwargs )

# 这2个方法通过 .next_siblings 属性对当tag的所有后面解析 的兄弟tag节点进行迭代, 
# find_next_siblings() 方法返回所有符合条件的后面的兄弟节点, 
# find_next_sibling() 只返回符合条件的后面的第一个tag节点.

first_link= soup.a
print(first_link)

print(first_link.find_next_siblings("a"))

first_story_paragraph = soup.find("p","story")
print(first_story_paragraph.find_next_siblings("p"))