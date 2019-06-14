#-*- coding:utf-8 -*-
"""
generator:在Python中，这种一边循环一边计算的机制，称为生成器
1.第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
Date:2019/6/14 16:15
"""
l = [x * x for x in range(10)]
print(l)

#创建一个generator对象
g = (x * x for x in range(10))
print(g)   #<generator object <genexpr> at 0x0055C750>

"""
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
"""
print(next(g))
print(next(g))
#迭代打印
for i in g:
    print(i)

#斐波拉契数列（Fibonacci）
def fib(max):
    n, a, b =0, 0, 1
    while n < max:
        yield b
        #print(b)
        a, b = b, a+b
        n += 1

fib(5)

