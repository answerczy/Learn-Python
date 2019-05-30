#-*- coding:utf-8 -*-
"""
Description
Date:2019/5/30 17:46
"""
from random import sample, randint


def display(balls):
    """
    输出列表中的双色球列表
    enumerate() 枚举函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
    同时列出数据和数据下标，一般用在 for 循环当中
    list(enumerate(range(3)) - 0 0  1 1 2 2
    :return:
    """
    for index , ball in enumerate(balls):
        #print(index,ball)
        if index == len(balls) - 1:
            print('|' , end = '')
        print('%02d'%ball , end= '')
    print()

def random_select():
    """
    随机选择一组号码
    :return:
    """

    red_balls = [x for x in range(1,34)]
    selectd_balls = []
    selectd_balls = sample(red_balls , 6)
    selectd_balls.sort()
    selectd_balls.append(randint(1,16))
    return selectd_balls


def main():
    n = int(input('机选几注：'))
    for i in range(n):
        display(random_select())

if __name__ == '__main__':
    main()