from bs4 import BeautifulSoup

# Tag.clear方法移除当前tag的内容(所有子节点)
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,"lxml")
tag = soup.a

tag.clear()
print(tag)
# <a href="http://example.com/"></a>

# PageElement.extract() 方法将当前tag移除文档树,并作为方法结果返回:
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,"lxml")
a_tag = soup.a

i_tag = soup.i.extract()

print(a_tag)
print(i_tag)

# 这个方法实际山产生了2个文档树:一个是用来解析原始文旦的BeautifulSoup对象
# 另一个是被移除并且返回的tag
# 被移除并返回的tag可以继续使用extract方法

my_string = i_tag.string.extract()
print(my_string)
print(my_string.parent)

# Tag.decompose() 方法将当前节点移除文档树并完全销毁:
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,"lxml")
a_tag = soup.a
# 将i节点删除
soup.i.decompose()
print(a_tag)

# PageElement.replace_with() 方法移除文档树中的某节点,并用新tag或文本节点替代它
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,"lxml")
a_tag = soup.a

new_tag = soup.new_tag("b")
# new_tag = soup.new_tag("b",string="example.net")
# print(new_tag)
new_tag.string = "example.net"
a_tag.i.replace_with(new_tag)
print(a_tag)
# <a href="http://example.com/">I linked to <b>example.net</b></a>

