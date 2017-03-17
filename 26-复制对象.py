from bs4 import BeautifulSoup
import copy

markup = "<p>I want <b>pizza</b> and more <b>pizza</b>!</p>"
soup = BeautifulSoup(markup,"lxml")

p_copy = copy.copy(soup.p)
print(p_copy)

# 复制后的对象与对象是相等的(相等的定义，但指向不同的内容地址)
print(soup.p == p_copy)
# true

print(soup.p is p_copy)
# false

# 源对象和复制对象的区别是源对象在文档树中，二复制后的对象是独立的
# 还没有添加到文档树中，复制后对象的效果跟调用了extract()方法相同

print(p_copy.parent)
# None
