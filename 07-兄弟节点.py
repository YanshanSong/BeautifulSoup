from bs4 import BeautifulSoup

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>","lxml")
print(sibling_soup.prettify())

# <b>标签和<c>标签是同一层，因为他们是同一个元素的子节点

# .next_sibling 和 .previous_sibling
# 在文档树中，使用 .next_sibling 和 .previos_sibling属性来查询兄弟节点
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)


# 实际文档中的tag的.next_sibling和.previous_sibling属性通常是字符创或空白
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

soup = BeautifulSoup(html_doc,'html.parser')
link = soup.a 
print(link)
print(link.next_sibling)  # ,

# 第二个<a>标签是逗号的.next_sibling属性
# print(link.next_sibling.next_sibling)
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>

# .next_siblings和.previous_siblings
# 通过.next_siblings 和 .previous_siblings属性可以对当前节点的兄弟节点迭代输出
for sibling in soup.a.next_siblings:
	print(repr(sibling))

for sibling in soup.find(id="link3").previous_siblings:
	print(repr(sibling))

#print(soup.find('a'))  # 找到第一个a标签即停止
#print('\n\n',soup.find('a',id='link3'))  # 依次查找a标签，直到满足条件为止
last_a_tag = soup.find("a",id="link3")
print("\n\n")
print(last_a_tag.next_sibling)
# '; and they lived at the bottom of a wall'
print(last_a_tag.next_element)
# "Tillie"
# 在原始文档中，字符串"Tillie"在分号前出现，解析器先进入<a>标签
# 然后是字符串"Tillie"，然后关闭</a>标签，然后是分号和剩余部分
# 分号与<a>标签在同一层级，但是字符串"Tillie"会被先解析

# .next_elements 和 .previous_elements
# 通过 .next_elements 和 .previos_elements的迭代器可以向前或者向后
# 访问文档的解析内容，就好像文档正在被解析一样

