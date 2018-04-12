'''
    另一个示例：等差数列生成器

    使用itertools
'''


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def aritprog_gen(begin, step, stop=None):
    result = type(begin + step)(begin)
    index = 0
    forever = stop is None
    while forever or result < stop:
        yield result
        index += 1
        result = begin + step * index


import itertools


def aritprog_gen_with_itertools(begin, step, stop=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if stop is not None:
        ap_gen = itertools.takewhile(lambda x: x < stop, ap_gen)
    return ap_gen


if __name__ == '__main__':
    pass