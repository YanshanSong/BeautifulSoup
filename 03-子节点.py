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

# print(soup.head)
# print(soup.title)
# print(soup.a)

# 通过点取属性的方式只能获取当前名字的第一个tag
# 如果想要得到所有的<a>标签，或是通过名字得到一个比tag
# 更多的内容的时候，就需要用到Searching the tee中藐视的方法
# 比如:find_all()

# .contents
head_tag = soup.head
print(head_tag)
print(head_tag.string)         # The Dormouse's house
#print(type(head_tag.string))  # <class 'bs4.element.NavigableString'>

# tag的.contents属性可以将tag的子节点以列表的方式输出
print(head_tag.contents)  # [<title>The Dormouse's story</title>]
 
title_tag = head_tag.contents[0] 
print(title_tag)          # <title>The Dormouse's story</title>

print(title_tag.string)   # The Dormouse's house
print(title_tag.contents) # ["The Dormouse's house"]
print(title_tag.string == title_tag.contents[0]) # True

# BeautifulSoup对象本身一定会包含子节点
# 也就是说<html>标签也是BeautifulSoup对象的子节点
print(len(soup.contents))
#print(soup.contents[2])

# 字符串没有.contents属性，因为字符串没有子节点
# text = title_tag.contents[0].contents

# .children 用于对tag的子节点进行循环
for child in title_tag.children:
	print(child)

for child in title_tag.contents:
	print(child)

# .contents 和 .children属性仅包含tag的直接子节点
# 例如，<head>标签只有一个直接子节点<title>
#print(head_tag.contents)
# [<title>The Dormouse's story</title>]

# .descendants属性可以对所有tag的子孙节点进行递归循环
for child in head_tag.descendants:
	print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story>
# Beautiful有一个直接子节点(<html>)，却有很多子孙对象