#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/10 17:36
"""
class Demo():
    def __init__(self, foo):
        self.foo = foo

    """
    在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，
    如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
    """
    def __bar(self):
        print(self.foo)
        print('_bar')


def main():
    test = Demo('hello')
    #test.__bar()  #AttributeError: 'Demo' object has no attribute '__bar'
    print(test.foo)

def main2():
    demo = Demo('hi')
    #通过下划线类名显示
    demo._Demo__bar()

if __name__ == '__main__':
    main()
    main2()