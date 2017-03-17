from bs4 import BeautifulSoup
from bs4 import CData

markup = "<b><!--Hey,buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,"html.parser")

comment = soup.b.string
print(comment)
#print(comment == soup.b.string) #true

#print(type(comment))       # <class 'bs4.element.Comment'>
#print(soup.b.prettify())  # 以缩进形式输出

#comment.replace_with("你好")
#print(comment == soup.b.string) #fals

cdata = CData("A CDATA block")
comment.replace_with(cdata)
print(soup.b.prettify())

