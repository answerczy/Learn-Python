#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/12 14:33
"""
from abc import abstractmethod, ABCMeta

"""
定义Pet为抽象类
由于python没有抽象类、接口的概念，所以要实现这种功能得abc.py 这个类库
"""
class Pet(metaclass=ABCMeta):
    """宠物类"""
    def __init__(self, nickname):
        self._nickname = nickname

    """
    @abstractmethod：抽象方法，含abstractmethod方法的类不能实例化，
    继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，
    未被装饰的可以不重写
    """
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass

class Dog(Pet):

    def make_voice(self):
        print('%s: 汪汪汪！'%self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('{}：喵...喵...'.format(self._nickname))

def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()