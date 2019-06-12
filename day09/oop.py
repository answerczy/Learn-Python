#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/12 14:08
"""

class Person:
    """人"""
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

    def play(self):
        print('%s正在快乐地玩耍！'%self._name)

    def watch_tv(self):
        if self._age < 18:
            print('{}只能看熊出没'.format(self._name))

        else:
            print('%s正在看动作片'%self._name)


class Student(Person):
    """学生类继承至人类"""

    def __init__(self, name, age, grade):
        #通过父类的初始化方法进行初始化
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('{}的{}正在学习{}'.format(self._grade, self._name, course))

class Teacher(Person):
    """老师类"""
    def __init__(self, name, age, title):
        Person.__init__(self, name, age)
        #super().__init__(name , age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s'%(self._name, self._title, course))

def main():
    stu = Student('TOM', 15, '初三')
    stu.study('数学')
    stu.watch_tv()

    t= Teacher('罗昊', 30, '老叫兽')
    t.teach('python程序设计')
    t.watch_tv()


if __name__ == '__main__':
    main()