# -*- coding:utf-8 -*-
"""
Description
Date:2019/6/19 15:46
"""

name = ''


# while name != 'your name':
#     print('pls type your name.')
#     name = input()
# print('thanks')

def get_status():
    status = {200: 'OK', 202: 'Accepted', 400: 'Bad Request',
              403: 'Forbidden', 404: 'Not Found', 500: 'Internal Server Error', 502: 'Bad Gateway'
              }
    s = int(input('请输入状态码：'))
    print(status.get(s))
    return (status.get(s))


get_status()
