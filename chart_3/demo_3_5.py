'''
    字典的变种
        collections.OrderedDict
            这个类型在添加键的时候会保持顺序，因此键的迭代次序总是一直的。OrderedDict的popitem方法默认删除并返回的是字典里的最后一个元素，但是如果想my_odict.popitem(last=False)这样调用，会删除第一个被添加进去的元素。
        collections.ChainMap
            该类型可以容纳数个不同的映射对象，然后在进行键查找操作的时候，这些对象会被当做一个整体被逐个查询，直到键被找到为止。这个功能在给有嵌套作用域的语言做解释器的时候很有用。
        collections.Counter
            这个映射类型会给键准备一个整数计数器。每次更新一个键的时候都会增加这个计数器。所以这个类型可以用来给可散列表对象计数，或者是当成多重集来用——多重集合就是集合里的元素可以出现不止一次。Counter实现了+和-运算符用来合并记录，还有像most_comon([n])这类很有用的方法。这个方法会返回映射里最常见的n个键和它们的计数。
        collections.UserDict
            这个类其实就是把标准dict用纯Python实现了一遍。跟开箱即用的类型不同，UserDict是让用户继承写子类的。

'''


import builtins
import collections


if __name__ == '__main__':
    pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
    print(pylookup)
    ct = collections.Counter('abracadabra')
    print(ct)
    ct.update('aaaaaazzz')
    print(ct)
    print(ct.most_common(3))