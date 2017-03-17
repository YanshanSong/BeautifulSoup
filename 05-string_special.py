from bs4 import BeautifulSoup

special = "<title>The Dormouse's <span>advanced</span>story</title></head>"

soup =  BeautifulSoup(special,"html.parser")

print(soup.title)

# print(soup.title.string) # None
print(soup.title.strings)
# generator object _all_strings at 0×000001FD170DBBA0>
# 返回一个生成器，通过迭代的方式取得其中的值

str = ''

for string in soup.title.stripped_strings:
	str += ' ' + string;

print(str)
