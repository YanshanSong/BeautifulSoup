from bs4 import BeautifulSoup

# Tag.insert()方法与Tag.append()方法类似
# 区别是不会把新元素添加到父节点.contents属性的最后，而是把元素插入到指定位置

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,"lxml")
tag = soup.a

tag.insert(1,"but did not endorse")
print(tag)

# insert_before() 和 insert_after()方法
# insert_before()方法在当前tag或文本节点前插入内容：
soup = BeautifulSoup("<b>stop</b>","lxml")
tag = soup.new_tag("i")
tag.string = "Don't"
soup.b.string.insert_before(tag)
print(soup.b)
# insert_after()方法在当前tag或文本节点后插入内容
soup.b.i.insert_after(soup.new_string(" ever"))
print(soup.b)
print(soup.b.contents)


