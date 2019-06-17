#-*- coding:utf-8 -*-
"""
Description
Date:2019/6/17 16:33
"""
import os




def main():
    CheckDir = input('Enter the name of the directory to check:')
    print()

    if os.path.exists(CheckDir):
        print('The dir exists')

    else:
        print('No dir found for:' + CheckDir)
        print()
        os.makedirs(CheckDir)
        print('Dir created for:' + CheckDir)
if __name__ == '__main__':
    main()