__author__ = 'JS'

import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return 'Vector(%d, %d)' % (self.x, self.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        raise TypeError('需要乘以整数')

    def __bool__(self):
        '''
            任何对象都可以被用于需要布尔值的上下文中， 比如if或者while语句， 或者and、or和not运算符， 为了判断一个值为真或假，Python会调用bool(x)方法，这个函数只能返回True或者False。默认情况下，自定义的类总被认为真， 除非有自己实现的__bool__或__len__， 先调用__bool__， 不存在的情况下调用__len__。
        '''
        return bool(abs(self))
        # return bool(self.x or self.y)


if __name__ == '__main__':
    print(Vector)
    print(repr(Vector(3, 4)))
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    v3 = v1 + v2
    print(v3)
    print(abs(v3))
    v = Vector(3, 4)
    print(v)
    print(v * 3)
    print(abs(v))
    print(abs(v * 3))
