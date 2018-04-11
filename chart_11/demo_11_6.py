'''
    标准库中的抽象基类
        从Python2.6开始，标准库提供了抽象基类。大多数抽象基类在collections.abc模块中定义，其他地方也有定义，如numbers和io
    11.6.1 collections.abc模块中的抽象基类
        Python3.4之后有两个abc,collections.abc和abc
        abc中定义了ABC，所有抽象基类都依赖这个类，但是不用导入，除非定义新的抽象基类。
        collections.abc中定义了16个抽象基类
        Iterable
        Container
        Sized
        Callable
        Hashable
        Iterator
        Sequence
        Mapping
        Set
        MappingView
        MutableSequence
        MutableMapping
        MutableSet
        ItemsView
        KeysView
        ValuesView

        1.Iterable、Container、Sized
            各个集合应该继承这三个抽象基类，或者至少实现兼容的协议。
            __iter__
            __contains__
            __len__
        2.Sequence、Mapping、Set
            主要的不可变集合类型，各自都有可变的子类。
        3.MappingView
            在Python3中，映射方法.items()、.keys()、.values()返回ItemsView、KeyView和ValueItem的实例
        4.Callable、Hashable
            重要放在collections.abc中，基本没有继承类型，主要用于isinstance判断是否可以执行和散列
        5.Iterator
            Iterable的子类
    11.6.2 抽象基类的数字塔
        numbers包定义的是数字塔(即各个抽象基类的层次结构是线性的),其中Number是位于最顶端的超类，随后是Complex，依次往下，最低端是Integral
        Number
        Complex
        Real
        Rational
        Integral


'''


import numpy
import numbers


if __name__ == '__main__':
    print(isinstance(True, numbers.Integral))
    print(isinstance(1.1, numbers.Real))
    r = numpy.arange(12)
    print(r)
    print(r.shape)
    r.shape = 6, 2
    print(r)
    print(isinstance(numpy, numbers.Number))
    print(type(r))