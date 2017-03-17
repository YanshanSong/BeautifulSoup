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

# 使用find_all类似的方法可以查找想要查找的文档内容

# 用于查找文档中所有的<b>标签
print(soup.find_all('b'))

# 传入正则表达式作为参数,Beautiful Soup会通过正则表达式的
# match()来匹配内容
# 下面例子可用来找出所有b开头的标签
for tag in soup.find_all(re.compile("^b")):
	print(tag.name)

for tag in soup.find_all(re.compile("t")):
	print(tag.name)

# 列表
# 如果传入参数列表，Beautiful Soup会将与列表中任一元素
# 匹配的内容返回
print(soup.find_all(["a","b"]))

# True
# True可以匹配任何值，下面代码查找所有的tag，但是不会返回字符串节点
for tag in soup.find_all(True):
	print(tag.name)

# 方法
# 如果没有合适的过滤器，那么还可以定义一个方法 
# 方法只接受一个元素参数，如果这个方法返回True
# 表示当前元素被找到，如果不是则返回false

# 下面方法校验了当前元素，如果包含class属性却不包含id
# 属性，那么返回True
def has_class_but_no_id(tag):
	return tag.has_attr('class') and not tag.has_attr('id')

# 将这个方法作为参数传入find_all()方法，将得到所有的p标签
# 因为p标签满足函数的返回值为True
print(soup.find_all(has_class_but_no_id))

# 通过一个方法来过滤一类标签属性的时候，这个方法的参数
# 是要被过滤的数据的值，而不是这个标签
# 下面的例子是找出href属性不符合指定正则的a标签
def not_lacie(href):
	return href and not re.compile("lacie").search(href)
print(soup.find_all(href=not_lacie))

# 标签过滤的方法可以使用复杂方法
# 下面的例子可以过滤出前后都有文字的标签
def surrended_by_strings(tag):
	return (isinstance(tag.next_element,bs4.element.NavigableString) and isinstance(tag.previous_element,bs4.element.NavigableString))

for tag in soup.find_all(surrended_by_strings):
	print(tag.name)