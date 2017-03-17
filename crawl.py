import requests
import re
from datetime import datetime

# 加头文件 仿浏览器访问
head = {'User-Agent':
        'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}

# get current time
now = datetime.now()

# 网站上的信息
url = "http://www.safehoo.com/News/News/World/"
sourcesite = "安全管理网"
section = "国际动态"

# 爬虫所得信息汇总
info = []

response = requests.get(url=url,headers=head)
response.encoding = "utf-8"
data = response.text

# 获取页面上的链接
url_list = re.findall(r'href="/News/News/World/(.+?)" target="_blank" title',data)
for i in range(len(url_list)):
	url_list[i] = url + url_list[i]   # 拼接成一个完整的url路径

# 获取具体文章信息
for i in range(len(url_list)):
    response = requests.get(url=url_list[i],headers=head)
    response.encoding = "utf-8"
    data = response.text

    # title
    title = re.findall("<title>(.+?)_",data)
    if not title:
        continue
    else:
        title = title[0]
    # publishing  
    publishing = re.findall(r'来源：(.+)　点击',data)[0]
    # publishing_time
    publishing_time = re.findall(r'更新日期：(.+?)<',data)[0]
    year = re.findall(r'(.+?)年',publishing_time)[0]
    month = re.findall(r'年(.+?)月',publishing_time)[0]
    day = re.findall(r'月(.+?)日',publishing_time)[0]
    publishing_time = "%s-%s-%s" % (year,month,day)

    print(url_list[i])
    Dict = dict()
    Dict["标题"] = title
    Dict["发布单位"] = publishing
    Dict["发布时间"] = publishing_time
    Dict["链接"] = url_list[i]
    Dict["来源网站"] = sourcesite
    Dict["版块"] = section
    Dict["获取时间"] =  "%4d-%02d-%02d %02d:%02d"  % (now.year,now.month,now.day,now.hour,now.minute)

    info.append(Dict)

for each in info:
	print(each)

 