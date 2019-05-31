#-*- coding:utf-8 -*-
"""
判断输入的边长能否构成三角形
如果能则计算边长及面积
计算面积的公式为海伦公式
s = math.sqrt(p(p-a)(p-b)(p-c))  p为半周长
Date:2019/5/31 17:30
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a+b > c and a+c >b and b+c >a:
    print('周长：%.2f'%(a+b+c))
    p = (a+b+c)/2
    area = math.sqrt(p * (p - a) *(p - b) * (p - c ))
    print('面积：%.2f'%area)
else:
    print('不能构成三角形')