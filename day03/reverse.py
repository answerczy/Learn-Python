#-*- coding:utf-8 -*-
"""
反转字符串
'www.toutiao.com/p/index.html'
Date:2019-01-01
"""
url = 'www.toutiao.com/p/index.html'
link = url.split('.')
link.reverse()
ll = link[1].split('/')
ll.reverse()
l3 = '/'.join(ll)
link[1] = l3
print('.'.join(link))
