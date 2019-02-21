#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

"""learning 2018/9/18"""

_author_ = 'jiang'


def test():
    args = sys.argv
    if len(args) == 1:
        print("hello python")
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()
