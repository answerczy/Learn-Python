#-*- coding:utf-8 -*-
"""
Description
Date:2019/5/29 14:45
"""
def main():
    fruits = ['grape','apple','strawberry','waxberry']
    print(fruits)
    print(fruits[0])
    print(fruits[-1])
    fruits[1] = 'cherry'
    #添加元素
    fruits.append('pitaya')
    fruits.insert(0,'banana')
    print(fruits)
    #删除元素
    del fruits[0]
    fruits.pop()
    fruits.remove('cherry')
    print(fruits)

if __name__ == '__main__':
    main()