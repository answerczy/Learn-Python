#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/12 16:07
"""
from datetime import datetime

"""
ctrl+alt+t:添加try/catch 快捷键
"""
try:
    with open('test.txt', 'w', encoding='utf8') as f:
        f.write('今天是：')
        f.write(datetime.now().strftime('%Y-%m-%d'))
except Exception as e:
    print(e)

try:
    with open('test.txt', 'r', encoding='utf8') as f:
        s = f.read()
        print('open for read')
        print(s)
except:
    pass

with open('test.txt', 'rb') as f:
    b = f.read()
    print('open as binary for read')
    print(b)



# from datetime import datetime
#
# with open('test.txt', 'w') as f:
#     f.write('今天是 ')
#     f.write(datetime.now().strftime('%Y-%m-%d'))
#
# with open('test.txt', 'r') as f:
#     s = f.read()
#     print('open for read...')
#     print(s)
#
# with open('test.txt', 'rb') as f:
#     s = f.read()
#     print('open as binary for read...')
#     print(s)