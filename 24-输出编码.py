from bs4 import BeautifulSoup

# 通过Beautiful Soup输出文档时,不管输入文档是什么编码方式,输出编码均为UTF-8编码

markup = b'''
<html>
  <head>
    <meta content="text/html; charset=ISO-Latin-1" http-equiv="Content-type" />
  </head>
  <body>
    <p>Sacr\xe9 bleu!</p>
  </body>
</html>
'''
soup = BeautifulSoup(markup,"lxml")
print(soup.prettify())

# 如果不想用UTF-8编码输出，可以将编码方式传入prettify()方法
print(soup.prettify("latin-1"))

# 还可以调用BeautifulSoup对象或任意对象的encode()方法，就像Python的字符串
# 调用encode()方法一眼
print(soup.p.encode("latin-1"))
# '<p>Sacr\xe9 bleu!</p>'
print(soup.p.encode("utf-8"))
# '<p>Sacr\xc3\xa9 bleu!</p>'