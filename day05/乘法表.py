#-*- coding:utf-8 -*-
"""
Description
Date:2019/5/31 17:49
"""
for i in range(1,10):
    for j in range(1,i + 1):
        print('%d*%d=%d'%(i,j,i*j), end='\t')
    print()