#-*- coding:utf-8 -*-
"""
验证输入用户名和QQ号是否有效并给出对应的提示信息
要求：
用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
QQ号是5~12的数字且首位不能为0
Date:2019/6/18 16:12
"""
import re

def main():
    username = input('请输入用户名：')
    qq = input('请输入QQ号：')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('请输入有效的用户名！')

    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号！')

    if m1 and m2:
        print('你输入的信息是有效的')



def email(e):
    if len(e) >= 5:
        if re.match("^[a-z0-9A-Z\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$", e) != None:
            print('邮箱格式正确')
        else:
            print('邮箱格式有误！')


def strings(url):
    listt = ['.php', '.html', '.asp', '.jsp']
    for lis in listt:
        suffix = re.findall(lis, url)
        if len(suffix) > 0:
            print(lis)

# # e = input('请输入email：')
# # print(e)
# # print(type(e))
# #main()
# email('da5da@qq.com')
url = 'http://www.cnblogs.com/fnng/archive/2013/05/20/3089816.html'
a = strings(url)
