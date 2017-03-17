from bs4 import BeautifulSoup

print(BeautifulSoup("<a><b /></a>", "xml"))
# <?xml version="1.0" encoding="utf-8"?>
# <a><b/></a>))

print(BeautifulSoup("<a></p>", "lxml"))
# <html><body><a></a></body></html>

print(BeautifulSoup("<a></p>", "html5lib"))
# <html><head></head><body><a><p></p></a></body></html>

print(BeautifulSoup("<a></p>", "html.parser"))
# <a></a>