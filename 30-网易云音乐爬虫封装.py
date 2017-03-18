import requests
from bs4 import BeautifulSoup
import json
import re
import pymysql

# 头文件
headers = {'User-Agent':
        'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}

def change_time(sec):
    string = "%02d:%02d" % (sec/60,sec%60)
    return string

def crawl(url, headers):
	# 发送requests请求
	r = requests.get(url=url, headers=headers)
	# 将爬取的网页传递给BeautifulSoup进行解析
	soup = BeautifulSoup(r.text,"lxml")
	# 先获取歌名和id
	ul = soup.select("ul.f-hide")[0]
    # 存放歌名和id的列表
	song_list = []

	for each in ul.select("a"):
		Dict = dict()
		Dict["id"] = each.get("href")[9:]
		Dict["title"] = each.string
		song_list.append(Dict)
   
    # 获取其他数据
    # 根据id进行匹配查找
	data = soup.find("textarea",style="display:none;").string
	# 将字符串解析成json数据
	data = json.loads(data)

	for each_song in song_list:
		for each_data in data:
			if int(each_song["id"]) == each_data["id"]:
				# 持续时间
				# 需要考虑将持续时间转换成xx:xx的形式
				# duration = 歌曲时长(s) * 1000
				each_song["time"] = change_time(each_data["duration"] / 1000)
				# 歌手
				# 需要考虑一首歌有多位歌手的情况
				artists = ""
				for artist in each_data["artists"]:
					artists += artist["name"] + " "
				artists.strip()
				each_song["artists"] = artists 
				# each_song["artists"] = each_data["artists"][0]["name"]
				# 专辑
				each_song["album"] = each_data["album"]["name"]


	# 由于控制台无法正确输出韩文、日文
	f = open("song_" + url[30:] + ".txt","w",encoding = "utf8")
	for each in song_list:
		f.write(each["title"] + "\t" + each["time"] + "\t" + each["artists"] + "\t" + each["album"] +"\n")
	# for each in song_list:
	# 	print(each["title"])

	print("写入文件"+"song_" + url[30:] + ".txt")

	return song_list

# 连接数据库
def mysql_connect(login_info):
	try:
		connection = pymysql.connect(host = login_info["host"],
									 port = login_info["port"],
									 user = login_info["user"],
									 password = login_info["passwd"],
									 database = login_info["db"],
									 charset = "UTF8")
		cursor = connection.cursor()
		print("数据库连接成功")
		return connection, cursor
	except:
		print("数据库连接失败")

# 向数据库中插入数据
def mysql_insert(song_list, login_info):
	connection, cursor = mysql_connect(login_info)
	sql = "INSERT INTO `wangyiyun`(`title`, `time`, `artists`, `album`) VALUES (%s,%s,%s,%s)"
	insert_list = []
	for each in song_list:
		insert_list.append((each["title"],
                            each["time"],
                          	each["artists"],
                            each["album"]))


	cursor.executemany(sql, insert_list)

	cursor.close()
	connection.commit()
	connection.close()

if __name__  == "__main__":
	# 获得信息
	song_list = crawl(url="http://music.163.com/playlist?id=317113391",headers=headers)

	# 插入数据库 
	login_info = {
	"host":"localhost",
	"port":3306,
	"user":"root",
	"passwd":"123456",
	"db":"wangyiyun"
	}
	mysql_insert(song_list, login_info)
	
