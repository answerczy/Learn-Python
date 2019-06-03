#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/3 17:11
"""
row = int(input('请输入行数：'))

for i in range(row):
    for j in range(i + 1):
        print('*' , end='')
    print()  #一行完成，打印换行