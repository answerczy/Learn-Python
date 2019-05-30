#-*- coding:utf-8 -*-
"""
Description
Date:2019/5/30 16:38
"""
def is_leap_year(year):
    """

    :param year:
    :return: 闰年为True,非闰年为False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 ==0

def which_day(year,month,date):
    """
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return:第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):  #0,1,2,3
        total += days_of_month[index]
    return total + date


if __name__ == '__main__':
    print(is_leap_year(2018))
    print(which_day(2019,2,1))