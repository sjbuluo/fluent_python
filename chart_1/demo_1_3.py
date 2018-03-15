'''
    Python特殊方法
    一、与运算符无关的特殊方法
    1.字符串/字节序列表示形式
        __repr__
        __str__
        __format__
        __bytes__
    2.数值转换
        __abs__
        __bool__
        __complex__
        __int__
        __float__
        __hash__
        __index__
    3.集合模拟
        __len__
        __getitem__
        __setitem__
        __delitem__
        _contains__
    4.迭代枚举
        __iter__
        __reversed__
        __next__
    5.可调用模拟
        __call__
    6.上下文管理
        __enter__
        __exit__
    7.实例创建和销毁
        __new__
        __init__
        __del__
    8.属性管理
        __getattr__
        __getattribute__
        __setattr__
        __delattr__
        __dir__
    9.属性描述符
        __get__
        __set__
        __delete__
    10.跟类相关的服务
        __prepare__
        __instancecheck__
        __subclasscheck__
    二、跟运算符相关的特殊方法
    1.一元运算符
        __neg__             -
        __pos__             +
        __abs__             abs()
    2.众多比较运算符
        __lt__              <
        __le__              <=
        __eq__              ==
        __ne__              !=
        __gt__              >
        __ge__              >=
    3.算术运算符
        __add__             +
        __sub__             -
        __mul__             *
        __truediv__         /
        __floordiv__        //
        __mod__             %
        __divmod__          divmod()
        __pow__             **或pow()
        __round__           round()
    4.反向算数运算符
        __radd__
        __rsub__
        __rmul__
        __rtruediv__
        __rfloordiv__
        __rmod__
        __rdivmod__

    5.增量赋值算术运算符
        __iadd__
        __isub__
        __imul__
        __itruediv__
        __ifloordiv__
        __imod__
        __ipow__
    6.位运算符
        __invert__          ~
        __lshift__          <<
        __rshift__          >>
        __and__             &
        __or__              |
        __xor__             ^
    7.反向位运算符
        __rlshift__
        __rrshift__
        __rand__
        __ror__
        __rxor__
    8.增量赋值位运算符
        __ilshift__
        __irshift__
        __iand__
        __ior__
        __ixor__
    (当交换两个操作数的位置时，就会调用反向运算符 b * a 而不是 a * b。增量赋值运算符则是一种把中缀运算符变成赋值运算的捷径 a = a * b就变成了 a *= b)
'''


class Test:

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other

    def __iadd__(self, other):
        return other * self.x

    def __radd__(self, other):
        return other - self.x


if __name__ == '__main__':
    t = Test(2)
    print(t + 1)
    print(1 + t)
    print(type(t))
    t += 1
    print(t)
    print(type(t))
