#-*- coding:utf-8 -*-
"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
Date:2019/6/3 17:30
"""
import math

for num in range(100,1000):
    low = num % 10  #得到个位数
    middle = num // 10 % 10 #得到十位数
    high = num // 100 #得到百位数
    if num == low**3 + middle**3 +high**3:
        print(num)


for i in range(100,1000):
    b = math.floor(i/100)  #取百位
    s = math.floor((i - (b*100))/10) #取十位
    g = i % 10  #取个位
    #g = i - math.floor(i/10) * 10
    if b**3 + s**3 + g**3 == i:
        print(i,end=',')
