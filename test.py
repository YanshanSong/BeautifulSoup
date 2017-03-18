# L1 = [1,2,3]
# L2 = L1
# L1.append(5)
# print(L1)
# print(L2)

# L1 = [3,4,5]   # L1指向新的地址
# print(L1)
# print(L2)

# import re

# lis = ["cake","pallc","sd"]

# p = lis.index("pallc")
# print(p)
# def int():
# 	a = 3
# 	b = 4
# 	return a, b

# a, b = int()
# print(a, b)

import pymysql

connection = pymysql.connect(host="localhost",
                                 port=3306,
                                 user="root",
                                 password="123456",
                                 db = "crawl",
                                 charset="UTF8")

