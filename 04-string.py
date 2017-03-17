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

# 如果一个tag只有一个NavigableString类型子节点 
# 那么这个tag可以使用.string得到子节点
title_tag = soup.title
print(title_tag.string)    # <class 'bs4.element.NavigableString'>

# 如果一个tag不只有一个，NavigableString类型子节点
# .string方法失效
# 例如special = "<title>The Dormouse's <span>story<span></title"
# 此时tag无法确定.string方法应该调用哪个子节点的内容
# .string的输出结果是None

# 可以使用.strings得到所有NavigableString类型子节点 
# for string in soup.strings:
# 	print(repr(string))

# 输出的字符串中可能包含了很多空格或空行，使用.stripped_strings可以
# 去除多余空白内容 
# 全部是空格的行会被忽略掉，段首和段末的空白会删掉
for string in soup.stripped_strings:
	print(repr(string))

