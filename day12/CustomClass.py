#-*- coding:utf-8 -*-
"""
__new__在__init__之前被调用，
__new__的返回值（实例）将传递给__init__方法的第一个参数，
然后__init__给这个实例设置一些参数。
Date:2019/6/17 15:07
"""

class Student():
    def __new__(cls, name, age):
        print('__new__ called')
        return super().__new__(cls)

    def __init__(self, name, age):
        print('__init__ called')
        self.name = name
        self.age = age

    #通过print打印实例
    def __str__(self):
        return 'Student object(name: %s(%s))'%(self.name, self.age)

    #控制台直接输出
    def __repr__(self):
        return 'Student object by print(name: {})'.format(self.name)
s = Student('TOM', 20)
print(s)