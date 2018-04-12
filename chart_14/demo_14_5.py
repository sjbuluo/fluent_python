'''
    Sentence类第四版：惰性实现

    for循环的过程中先是调用iter() 在不断调用next()直到抛出StopIterator异常
'''

import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


class Foo:

    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < 11:
            self.index += 1
            return self.index
        raise StopIteration


if __name__ == '__main__':
    foo = Foo()
    # for i in iter(foo):
    #     print(i)

    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))
    # print(next(foo))

    # l = [1, 2, 3, 4, 5]
    # print(next(l))
    # print(next(l))
    # print(next(l))
    # print(next(l))
    # print(next(l))


    st = Sentence('Hello World')

    for s in st:
        print(s)

    # print(next(st))

    from collections import abc
    abc.Iterator



