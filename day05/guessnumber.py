#-*- coding:utf-8 -*-
"""
Description
Date:2019/5/31 17:45
"""
import random
answer = random.randint(1,100)
print(answer)
counter = 0
while True:
    counter += 1
    number = int(input('请输入数字：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了！')
        break
print('你总共猜了%d次'%counter)
if counter > 7:
    print('智商余额不足')