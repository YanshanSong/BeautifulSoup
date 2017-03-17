from bs4 import BeautifulSoup

# PageElement.wrap() 方法可以对指定的tag元素进行包装 [8] ,并返回包装后的结果:
soup = BeautifulSoup("<p>I wish I was bold.</p>","lxml")
print(soup.p.string.wrap(soup.new_tag("b")))
# <b>I wish I was bold.</b>

print(soup.p.wrap(soup.new_tag("div")))
# <div><p><b>I wish I was bold.</b></p></div>

# Tag.unwrap()方法与wrap()相反，将移除tag内的所有tag标签
# 该方法常被用来进行标记的解包

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup,"lxml")
a_tag = soup.a
print(a_tag)
print(a_tag.i.unwrap())
# 与replace_with()方法相同，unwrap()方法返回被移除的tag
print(a_tag)
# <a href="http://example.com/">I linked to example.com</a>
