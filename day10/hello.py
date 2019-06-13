#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/13 16:42
"""
import sys


def test():
    args = sys.argv

    """args[0] 默认为文件位置"""
    if len(args) == 1:
        print('hello world!')
    elif len(args) == 2:
        print('hello , %s!'%args[1])
    else:
        print('too many arguments')

if __name__ == '__main__':
    test()