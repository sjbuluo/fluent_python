'''
    一元运算符
        -(__neg__)
            一元取负算术运算符 x = -1 则 -x = 1
        +(__pos__)
            一元取正算术运算符 如使用decimal中途改变上下文的精度 collections.Counter使用+counter将会删除0或负值的key
        ~(__invert__)
            对整数按位取反,定义为~x == -(x+1) x = 2 则~x = -3
        支持一元运算符很简单，只需实现相应的特殊方法。这些特殊方法只有一个参数就是self。不过，要遵守运算符的一个基本规则：始终返回一个新对象，也就是说不能修改self，要创建并返回合适类型的新实例。

'''


import math
import decimal
import collections


class Vector:

    def __init__(self, components):
        self._components = components

    def __iter__(self):
        return iter(self._components)

    def __abs__(self):
        math.sqrt(x * x for x in self)

    def __neg__(self):
        return Vector((-x for x in self))

    def __pos__(self):
        return Vector(self)

    def __str__(self):
        return str(tuple(self))


if __name__ == '__main__':
    v = Vector((3, 4, 5))
    print(v)
    print(-v)
    print(+v)

    ctx = decimal.getcontext()
    ctx.prec = 40
    one_third = decimal.Decimal('1') / decimal.Decimal('3')
    print(one_third)
    print(one_third == +one_third)
    ctx.prec = 28
    print(one_third == +one_third)
    print(+one_third)

    ct = collections.Counter('abracadabra')
    print(ct)
    ct['r'] = -3
    ct['d'] = 0
    print(ct)
    print(ct == +ct)
    print(+ct)