#-*- coding:utf-8 -*-
"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
Date:2019/6/3 17:48
"""
import time
import math

start = time.clock()
for num in range(1,10000):
    sum = 0
    for i in range(1 , int(math.sqrt(num) + 1)):
        if num % i == 0:
            sum += i
            if i > 1 and num / i != i:
                sum += num / i
    if sum == num:
        print(num)
end = time.clock()
print('执行时间：',(end - start),'秒')

# for i in range(1,1000):
#     s = 0
#     for k in range(1,i):
#         if i % k == 0:
#             s = s+k
#     if s == s:
#         print(i)