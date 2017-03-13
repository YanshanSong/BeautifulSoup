html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" id="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were 
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,"html.parser")  #得到一个BeautifulSoup对象

#print(soup.prettify())   
#按照标准的缩进格式的结构输出
print(soup.title)
# <title>The Dormouse's story</title>
print(soup.title.name)
# 'title' 
# name指的是标签类型名，非HTML中的name属性
print(soup.title.string)       # 'The Dormouse's story' # 相当于innerHTML
print(type(soup.title.string)) # <class 'bs4.element.NavigableString'>
# 可以直接遍历
# 不能被编辑，但是可以被替换成其他的字符串，用replace_with()方法

print(soup.title.parent.name)
# 'head'
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>
# 注意只返回第一个p标签
print(soup.find_all('p'))
# 返回所有p标签组成的一个列表
#------------------------------------
print(soup.p['class'])
soup.p['class'] = 'nihao'
print(soup.p['class'])
# 获得p的class属性名 'title'
# 由于class是多值属性，故返回值一个列表
print(soup.p['id'])
# 获得p的id属性名 'title'
print(soup.p.attrs)
# 一个由p的属性名和属性值组成的字典
#------------------------------------
print(soup.a)
# 返回第一个a标签
print(soup.find_all('a'))
# 返回所有a标签组成的一个列表
print(soup.find(id='link3'))
# 返回ID为指定值的a标签

# 从文档中获取所有a标签
for link in soup.find_all('a'):
	print(link.get('href'))

# 从文档中获取所有文字内容
print(soup.get_text)

