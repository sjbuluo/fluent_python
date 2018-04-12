'''
    Python3.3中芯出现的句法：yield from
        如果生成器函数需要产出另一个生成器生成的值，传统方法是用for
'''


def chain(*iterable):
    for it in iterable:
        for i in it:
            yield i


def chain2(*iterable):
    for i in iterable:
        yield from i


if __name__ == '__main__':
    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))
    print(list(chain2(s, t)))