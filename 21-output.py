from bs4 import BeautifulSoup

# 输出
# 格式化输出
# prettity()方法将BeautifulSoup的文档格式化后移Unicode编码输出
# 每个XML/HTML标签都独占一行
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,"lxml")
print(soup.prettify())
# '<html>\n <head>\n </head>\n <body>\n  <a href="http://example.com/">\n...' 

# 压缩输出
# 如果只想得到结果字符串，不重视格式，那么可以对一个BeautifulSoup
# 对象或Tag对象使用Python的unicode()或str()方法

# str()方法返回UTF-8字符串，可以指定编码的设置
# 还可以调用encode()方法获得字节码或调用decode()方法获得Unicode
print(str(soup))

# BeautifulSoup会将HTML中的特殊字符转换成Unicode，比如"&lquot"(Python2)
# soup = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.","lxml")
# print(unicode(soup))

# Python3会按照HTML解析特殊字符

# get_text()
# 如果只想得到tag中包含的文本内容，那么可以用get_text()方法
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup,"lxml")

print(soup.get_text())
# I linked to example.com
print(soup.i.get_text())
# examole.com
# 可以通过参数指定tag的文本内容的分隔符
print(soup.get_text("|"))
# 还可以去除获得文本的前后空白
print(soup.get_text("|", strip = True))
# 或者使用.stripped_strings生成器，获得文本列表后手动处理列表
print([text for text in soup.stripped_strings])

