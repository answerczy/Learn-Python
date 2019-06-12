#-*- coding:utf-8 -*-
"""
多重继承
- 通过多重继承可以给一个类的对象具备多方面的能力
- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系
Date:2019/6/12 14:50
"""
class Father:
    def __init__(self, name):
        self._name = name

    def gamble(self):
        print('{}在打麻将'.format(self._name))

    def eat(self):
        print('%s在大吃大喝'%self._name)

class Monk:
    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s在吃斋。'%self._name)

    def chant(self):
        print('%s在念经。'%self._name)

class Musician:
    def __init__(self, name):
        self._name = name

    def eat(self):
        print('{}在细嚼慢咽'.format(self._name))

    def play_piano(self):
        print('%s在弹钢琴'%self._name)

class Son(Father, Monk, Musician):
    def __init__(self, name):
        Father.__init__(self, name)
        """
        等价于Monk.__init__(self, name)
        super在多继承中的使用
        """
        super(Monk,self).__init__(name)
        #Monk.__init__(self, name)
        Musician.__init__(self, name)


son = Son('TOM')
son.gamble()
# 调用继承自Father的eat方法
son.eat()
son.chant()
son.play_piano()
