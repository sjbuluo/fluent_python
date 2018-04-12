'''
    可迭代的对象与迭代器的对比
        可迭代的对象
            使用iter内置函数可以获取迭代器对象。实现了__iter__或__getitem__函数的对象都是可迭代的
        StopIteration异常表明迭代器到头了。Python语言内部会处理for循环和其他迭代上下文中的StopIteration异常
        标准的迭代器接口有两个方法
            __next__
                返回下一个可用的元素，如果没有元素了，则抛出StopIteration
            __iter__
                返回self，以便在应该使用可迭代对象的地方使用迭代器，如for循环中。

        collections.abc.Iterable Iterator
        Iterable __iter__
        Iterable -> Iterator __next__ __iter__

        一个迭代器抛出StopIteration之后，需要再次创建才能使用

        迭代器
            实现了无参数的__next__方法，返回序列中的下一个元素，如果没有元素了，那么抛出StopIteration异常。Python中的迭代器还实现了__iter__方法，因此迭代器也可以迭代。
'''


from collections import abc


if __name__ == '__main__':
    s = 'ABC'
    for x in iter(s):
        print(x)

    it = iter(s)
    while True:
        try:
            print(next(it))
        except StopIteration:
            del it
            break

    print(list.__dict__)
