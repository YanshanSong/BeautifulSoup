from bs4 import BeautifulSoup
from bs4 import NavigableString
from bs4 import Comment

# 如果想添加一段文本内容到文档中
# 可调用Python的append()方法
# 或调用NavigableString的构造方法
soup = BeautifulSoup("<b></b>","lxml")
tag = soup.b
tag.append("Hello")

new_string = NavigableString(" there")
tag.append(new_string)
print(tag)
# <b>Hello there.</b>
print(tag.contents)
# ['Hello','there']

# 如果想要创建一段注释，或NavigableString的任何子类，只要调用NavigableString
# 的构造方法:
new_comment = Comment("Nice to see you")
tag.append(new_comment)
print(tag)
# <b>Hello there<!--Nice to see you.--></b>
print(tag.contents)
# [u'Hello', u' there', u'Nice to see you.']

# 从创建一个tag最好的方法是调用工厂方法BeautifulSoup.new_tag()
new_tag = soup.new_tag("a",href="http://www.example.com")
tag.append(new_tag)
print(tag)


