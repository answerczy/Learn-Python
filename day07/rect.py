#-*- coding:utf-8 -*-
"""
定义和使用矩形类
Date:2019/6/10 17:02
"""

class Rect():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def perimeter(self):
        """计算周长"""
        return (self.width * self.height)*2

    def area(self):
        """计算面积"""
        return self.width * self.height

    def __str__(self):
        return '矩形[%s , %s]'%(self.width, self.height)

    def __del__(self):
        print('销毁矩形对象')

if __name__ =='__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())

    rect2 = Rect(3.5,4.3)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())