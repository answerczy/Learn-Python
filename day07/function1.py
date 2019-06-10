#-*- coding:utf-8 -*-
"""
函数的定义和使用 - 求最大公约数和最小公倍数
Date:2019/6/10 15:25
"""

def gcd(x , y):
    (x , y) = (y , x) if x > y else (x ,y)
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x , y):
    return x*y // gcd(x,y)


print(gcd(15,27))
print(lcm(15,27))