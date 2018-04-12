'''
    重载向量加法运算符+
        a + b
        如果a有__add__调用 a.__add__(b)
        没有__add__或结果为NotImplemented 如果b有__radd__调用 b.__radd__(a)
       _没有__radd__或返回NotImplemented 则抛出TypeError并在错误消息中指明操作数类型不支持

       NotImplemented和NotImplementedError，前者是特殊的单例值，如果中缀运算符不能处理给定的操作数，那么要把它返回给解释器。而NotImplementedError是一种异常，抽象类中的占位方法把它抛出，提示子类必须覆盖。

'''


import itertools


class Vector:

    def __init__(self, components):
        self._components = components

    def __iter__(self):
        return iter(self._components)

    def __add__(self, other):
        try:
            return Vector([a + b for a, b in itertools.zip_longest(self, other, fillvalue=0.0)])
        except ValueError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)


if __name__ == '__main__':
    v1 = Vector([3, 4, 5])
    v2 = Vector([6, 7, 8])
    v3 = v1 + v2
    print(v3)
    print(v3 == Vector([3 + 6, 4 + 7, 5 + 8]))
    print(v1 + (10, 20, 30))
