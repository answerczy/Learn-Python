#-*- coding:utf-8 -*-
"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
Date:2019/6/12 15:21
"""
from abc import abstractmethod


class Employee:
    """员工"""
    def __init__(self, name):
        """
        :param name: 姓名
        :return:
        """
        self._name = name
    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        :return:获得月薪
        """
        ...
class Manager(Employee):
    def get_salary(self):
        return 15000.00

class Programmer(Employee):
    """
    定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    限定对象只能绑定_working_hour属性
    """
    __slots__ = ('_working_hour')

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 150.0 * self._working_hour

class Salesman(Employee):
    def __init__(self, name, sales=0):
        Employee.__init__(self, name)
        self._sales = sales
    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1200.00 + self._sales*0.05

def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Manager('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        """
        isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
        isinstance(object, classinfo)参数
        -object -- 实例对象。
        -classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
        isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
        issubclass() 函数用于判断参数是否是类型参数的子类。
        """
        if isinstance(emp, Programmer ):
            emp.working_hour = int(input('请输入%s本月工作时间:'%emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = int(input('请输入{}的销售业绩:'.format(emp.name)))

        print('{}本月的工资为：{}元。'.format(emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()


