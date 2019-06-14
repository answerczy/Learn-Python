#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/14 16:31
"""
def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5

o = odd()
for i in o:
    print(i)