from bs4 import BeautifulSoup

markup = "<h1>Sacr\xc3\xa9 bleu!</h1>"
soup = BeautifulSoup(markup,"lxml")

# BeautifulSoup 对象的 .original_encoding 属性记录了自动识别编码的结果
print(soup.original_encoding)

# 通过from_encoding参数来指定编码方法
soup = BeautifulSoup(markup, "lxml",from_encoding="iso-8859-8")
print(soup.original_encoding)
