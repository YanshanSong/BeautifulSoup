from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# SoupStrainer类可以定义文档的某段内容
# 这样搜索文档时就不必解析整篇文档
# 只会解析在SoupStrainer中定义过得文档
# 创建一个SoupStrainer对象并作为parse_only参数给Beautiful的构造方法即可

# SoupStrainer(name , attrs , recursive , string , **kwargs)

only_a_tags = SoupStrainer("a") 

only_tags_with_id_link2 = SoupStrainer(id="link2")

def is_short_string(string):
    return and len(string) < 10

only_short_strings = SoupStrainer(string=is_short_string)

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

print(BeautifulSoup(html_doc, "html.parser", parse_only=only_a_tags).prettify())

print(BeautifulSoup(html_doc, "html.parser", parse_only=only_tags_with_id_link2).prettify())

# print(BeautifulSoup(html_doc, "html.parser", parse_only=only_short_strings).prettify())