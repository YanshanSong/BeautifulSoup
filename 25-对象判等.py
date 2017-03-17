from bs4 import BeautifulSoup

# 两个 NavigableString 或 Tag 对象具有相同的HTML或XML结构时, Beautiful Soup就判断这两个对象相同. 
markup = "<p>I want <b>pizza</b> and more <b>pizza</b>!</p>"
soup = BeautifulSoup(markup, 'html.parser')
first_b, second_b = soup.find_all('b')
print(first_b == second_b)

print(first_b.previous == second_b.previous_element)

# 如果想判断两个对象是否严格的指向同一个对象可以通过is来判断
print(first_b is second_b)