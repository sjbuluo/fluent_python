'''
    重载标量惩罚运算符*

    中缀运算符方法名称
        +   __add__     __radd__    __iadd__    加法或拼接
        -   __sub__     __rsub__    __isub__    减法
        *   __mul__     __rmul__    __imul__    乘法
        /   __truediv__ __rtruediv____itruediv__除法
        //  __floordiv____rfloordiv____ifloordiv__整除
        %   __mod__     __rmod__    __imod__    取模
        divmod()    __divmod__  __rdivmod__ __idivmod__ 返回由整除的商和模数组成的元组
        **,pow()    __pow__     __rpow__    __ipow__    取幂
        @   __matmul__  __rmatmul__ __imatmul__ 矩阵乘法
        &   __and__     __rand__    __iand__    位与
        |   __or__      __ror__     __ior__     位或
        ^   __xor__     __rxor__    __ixor__    位异或
        <<  __lshift__  __rlshift__ __ilshift__ 按位左移
        >>  __rshift__  __rrshift__ __irshift__ 按位右移

'''


from array import array
import reprlib
import math
import functools
import operator
import itertools
import numbers


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vector([x * other for x in self])
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other


if __name__ == '__main__':
    pass