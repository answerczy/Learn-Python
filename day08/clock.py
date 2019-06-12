#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/11 19:30
"""
import time


class Clock():
    def __init__(self,hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = time.localtime(time.time())
        print(ctime)
        print(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
        print(cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec))
        #通过返回类对象才可调用方法
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d'%(self._hour, self._minute, self._second)


if __name__ == '__main__':
    clock = Clock.now()
    print(type(clock))
    print(clock.show())
