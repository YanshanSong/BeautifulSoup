import bs4
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>','lxml')
tag = soup.b

tag.name = "blockquote"
tag['class'] = 'verybold';
tag['id']=  1
print(tag)

# 给tag的.string尚需经赋值，就相当于用以前的内容替代了原来的内容
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,"lxml")

tag = soup.a
print(tag)
tag.string = "New link text."
print(tag)

# Tag.append() 方法向tag中添加内容,就好像Python的列表的 .append() 方法:
soup = BeautifulSoup("<a>Foo</a>","lxml")
soup.a.append("Bar")

print(soup)
print(soup.a.contents)