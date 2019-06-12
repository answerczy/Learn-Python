#-*- coding:utf-8 -*-
"""
json模块主要有四个比较重要的函数，分别是：
-dump - 将Python对象按照JSON格式序列化到文件中
-dumps - 将Python对象处理成JSON格式的字符串
-load - 将文件中的JSON数据反序列化成对象
-loads - 将字符串的内容反序列化成Python对象
Date:2019/6/12 16:23
"""
import json
import requests

# def main():
#     resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
#     data_model = json.loads(resp.txt)
#     for new in data_model['newslist']:
#         print(new['title'])
#
# if __name__ == '__main__':
#     main()

#json字符串中必须使用双引号“”
json_str = '{"name":"tom", "age":20, "title":"叫兽"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]

    }
    try:
        with open('data.json', 'w', encoding='utf8') as f:
            json.dump(mydict, f)
    except Exception as e:
        print(e)
    print('保存数据完成')

if __name__ == '__main__':
    main()

