
# coding: UTF-8

import re

# 数値を返す関数
def index(x):
    return int(x)**2

"""
数値チェック(正規表現)

"""

def num_check(x):
    pattern = re.compile(r'^[0-9]+$')
    return pattern.match(x)

# 文字列を返す関数
def str_output(str1):
    print(str1)

# 3つの引数をもつ関数(2つはオプション引数)
def variables3(x, y=9, z=20):
    return int(x) * y * z

# 4-1
def divide(x):
    return int(x) / 2

# 4-2
def multiple(x):
    return int(x) * 4

# 5
def convert_float(y):
    try:
        return float(y)
    except ValueError:
        print('Could not convert string to float.')
    

x = input()
while not num_check(x):
    print('半角数値を入力してください。')
    x = input()

print( str(int(x)) + 'の2乗は' + str(index(x)) + 'です。')

str1 = input()
str_output(str1)

print(variables3(x))

print(multiple(divide(x)))

y = input('Float型を入力してください')
print(convert_float(y))
