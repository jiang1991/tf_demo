#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique
import logging
from functools import reduce

Month = Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member.value)


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):

    def __init__(self, name, gender):
        self._name = name
        if not isinstance(gender, Gender):
            raise TypeError('gender must be Male or Female')
        self._gender = gender

    def to_string(self):
        print('%s is %s' % (self._name,  'Man' if self._gender == Gender.Male else 'Lady'))


try:
    lisa = Student('Lisa', Gender.Female)
    lisa.to_string()

    ben = Student('Ben', Gender.Male)
    ben.to_string()
except TypeError as e:
    logging.exception(e)
finally:
    pass


# test


def str2num(s):
    # return int(s)  // fixed
    return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
