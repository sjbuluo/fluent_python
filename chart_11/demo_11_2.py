'''
    Python喜欢序列
        class Foo:

            def __getitem__(self, pos):
                return range(0, 30, 10)[pos]

    虽然Foo类没有实现__iter__方法，但是Foo的实例对象依然是可迭代对象。因为有__getitem__方法，Python会调用，传入从0开始的整数索引，畅视迭代对象(这是一个备选方案，排在__iter__之后)。虽然没有实现__contain__方法，依然可以使用in关键字，Python足够智能做全面检查
'''


import collections


def print_base(cls):
    if cls is not None:
        print(cls.__name__)
        for base_cls in cls.__bases__:
            print_base(base_cls)


class Foo:

    def __getitem__(self, item):
        return range(0, 30, 10)[item]


if __name__ == '__main__':
    print_base(list)
    print('---------------------')
    print_base(collections.UserDict)
    print('---------------------')
    print_base(collections.MutableSequence)
    print('---------------------')
    for i in Foo():
        print(i)
    print(10 in Foo())