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

# 通过string参数可以搜索文档中的字符串内容，与name参数可选值一样
# string参数接受字符串，正则表达式，列表，True
print(soup.find_all(string="Elsie"))

print(soup.find_all(string=["Tillie","Elsie","Lacie"]))

print(soup.find_all(string=re.compile("Dormouse")))

def is_the_only_string_within_a_tag(s):
	"Return True if this string is the only child of its parent tag."
	return (s == s.parent.string)

print(soup.find_all(string=is_the_only_string_within_a_tag))

# limit参数
# 当搜索的结果双达到limit的限制时，就停止搜索返回结果

