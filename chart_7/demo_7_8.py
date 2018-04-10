'''
    标准库中的装饰器
        Python内置了三个用于装饰方法的函数：property、classmethod和staticmethod
        另一个常见的装饰器是functools.wraps 作用是协助构建行为良好的装饰器
        还有值得关注的装饰器是lru_cache和singledispatch都在functools模块中
    7.8.1 使用functools.lru_cache做备忘
        functools.lru_cache非常实用，实现了备忘功能。把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。
        lru = Least Recently Used 缓存不会无限增长，一段时间不用的缓存条目将被抛弃。
        除了优化递归算法 lru_cache在从Web中获取信息的应用中也能发挥巨大作用
        lru_cache可以使用两个可选参数来配置
            maxsize参数指定存储多少个调用的结果 超出则删除最老的数据
            typed(True Or False) True则把不同类型的结果分开保存
    7.8.2 单分派泛函数

'''


__part_name__ = '标准库中的装饰器'


import functools
import time
from collections import abc
import numbers
import html


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        param_list = []
        if args:
            param_list.extend([repr(arg) for arg in args])
        if kw:
            param_list.append(','.join('%s=%s' % (key, repr(value)) for key, value in kw.items()))
        print('%0.8fs %s(%s) -> %r' % (end - start, func.__name__, ','.join(param_list), result))
        return result
    return clocked


@clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache()
@clock
def fibonacci2(n):
    return n if n < 2 else fibonacci2(n - 2) + fibonacci2(n - 1)


@functools.singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br />\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<url>\n<li>' + inner + '</li>\n</ul>'


if __name__ == '__main__':
    print(fibonacci(6))
    print(fibonacci2(6))
    print(htmlize(abs))
    print(htmlize('Hello World!\n'
                  'Next Line!'))
    print(htmlize(520))
    print(htmlize(['A', 'B', 'C']))
