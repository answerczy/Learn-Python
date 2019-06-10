#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/10 16:29
"""

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print('%s正在学习%s'%(self.name ,course_name))

    def watch_tv(self):
        if self.age < 18:
            print('%s只能观看熊出没'%self.name)
        else:
            print('%s可以观看其他类型的电影'% self.name)


def main():
    s1 = Student('Tom' , 20)
    s1.study('Python程序设计')
    s1.watch_tv()

    s2 = Student('Jerry' ,15)
    s2.study('思想品德')
    s2.watch_tv()


if __name__ == '__main__':
    main()