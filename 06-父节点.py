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

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'html.parser')

# .parent属性来获取某个元素的父节点
title_tag = soup.title
print(title_tag)
print(title_tag.parent)

# 文档title的字符串也有父节点:<title>标签
print(title_tag.string.parent)

# 文档的顶层节点比如<html>的父亲节点就是Beautiful对象:
print(type(soup.html.parent))
# BeautifulSoup对象的.parent是None
print(soup.parent)
# 通过元素的.parents属性可以递归得到元素的所有父辈节点
link = soup.a
print(link)

for parent in link.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)
