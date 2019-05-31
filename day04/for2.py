#-*- coding:utf-8 -*-
"""
掷筛子决定做什么事
Date:2019/5/31 17:25
"""
import random

face = random.randint(1,6)
if face == 1:
    result = '唱歌'
elif face == 2:
    result = '跳舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲笑话'
print(result)