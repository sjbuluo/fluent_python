'''
    Sentence类第三版:生成器函数

    生成函数的工作原理
        Python函数的定义体中有yield关键字，该函数就是生成器函数。调用生成器函数时，会返回一个生成器对象。也就是说，生成器函数时生成器工厂。

'''


import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return '{}({})'.format('Sentence', reprlib.repr(self.text))

    def __iter__(self):
        for word in self.words:
            yield word
        return


def gen_123():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    print(gen_123())
    for i in gen_123():
        print(i)
    g = gen_123()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))