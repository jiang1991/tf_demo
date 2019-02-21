#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print('please input your name')
# s = input('please input your money: ')

# print('your name is: ', name)

# print('hello %s, you have $%d' % ('jiang', 1000))
# import math
#
#
# def my_sum(*x):
#     sum = 0
#     for i in x:
#         sum = sum + i*i
#     return sum
#
#
# def move(x, y, step, angle=30):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# # for i in range(10):
# #     my_sum(i)
#
# x, y = move(100, 100, 60)
# print(x, y)
#
# nums = [1, 4, 7]
# print(my_sum(*nums))


# 递归
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))


# 切片
# L = [1, 2, 4, 7, 8, 10]
# print(L[-2:])


# def trim(s):
#     if len(s) == 0:
#         return ''
#     if s[0] == ' ':
#         return trim(s[1:])
#     elif s[-1] == ' ':
#         return trim(s[:-1])
#
#
# print(trim('  000 22  '))
# print(trim('   '))


# def find_min_and_max(L):
#     if len(L) == 0:
#         return (None,None)
#     xmax = xmin = L[0]
#     for x in L:
#         if x > xmax:
#             xmax = x
#         if x < xmin:
#             xmin = x
#     return (xmax, xmin)
#
#
# L = [12, 1, 2, 4, 7, 8, 10]
#
# print(find_min_and_max(L))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(tu):
    return tu[0]


def by_score(tu):
    return tu[1]


l2 = sorted(L, key=by_score)

print(l2)
