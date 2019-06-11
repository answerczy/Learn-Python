#-*- coding:utf-8 -*-
"""
实例方法和类方法的应用
Date:2019/6/11 17:41
"""
from math import sqrt


class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    #不属于对象方法
    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and b+c>a and c+a>b

    def perimeter(self):
        return self.a + self.b +self.c

    def area(self):
        p =self.perimeter() / 2
        return sqrt( p * (p - self.a) * (p - self.b) * (p - self.c))

if __name__ == '__main__':

    a,b,c = map(float , input('请输入边长， 用空格间隔：').split())
    #调用的时候使用类名点出来
    if Triangle.is_valid(a,b,c):
        tri = Triangle(a,b,c)
        print('周长:%s'%tri.perimeter())
        print('面积:%s'%tri.area())

    else:
        print('不能组合为三角形')