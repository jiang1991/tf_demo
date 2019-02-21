#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Object Oriented Programming


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def print_grade(self):
        print('%s: %s, %s' % (self.name, self.score, self.get_grade()))

    def student2dict(self):
        return {
            'name': self.name,
            'score': self.score,
            'grade': self.get_grade()
        }


def dict2student(d):
    return Student(d['name'], d['score'])


Lisa = Student('Lisa', 80)
Ben = Student('Ben', 98)

Ben.print_grade()
print(Ben.student2dict())


# class Animal(object):
#
#     def run(self):
#         print("Animal is running...")
#
#
# class Dog(Animal):
#
#     def run(self):
#         print("Dog is running...")
#
#     def eat(self):
#         print("Eating meat...")
#
#
# class Cat(Animal):
#
#     def run(self):
#         print('Cat is running slowly...')
#
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
#
# dog = Dog()
# run_twice(dog)
#
# cat = Cat()
# run_twice(cat)
#
#
# class Timer(object):
#
#     def run(self):
#         print("tick tick tick...")
#
#
# timer = Timer()
# run_twice(timer)


class Screen(object):

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

