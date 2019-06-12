#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/11 17:55
"""
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.setter
    def name(self, name):
        self._name = name

    def play(self):
        if self.age < 16:
            print('{}正在玩飞行棋'.format(self._name))
        else:
            print('%s正在玩斗地主'%self._name)


def main():
    person = Person('TOM',10)
    person.play()
    person.age = 22
    person.play()
    #person.name = 'jim'

if __name__ == '__main__':
    main()