'''
    实现一个简单的装饰器

'''


__part_name__ = '实现简单的装饰器'


import time
import functools


def clock(func):
    def clocked(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (end - start, name, arg_str, result))
        return result
    return clocked


@clock
def print_str(s):
    print(s)


def clock2(func):
    @functools.wraps(func)
    def clocked2(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        param_list = []
        if args:
            param_list.extend([repr(arg) for arg in args])
        if kw:
            param_list.append(','.join(['%s=%s' % (key, repr(value)) for key, value in kw.items()]))
        print('%0.8fs %s(%s) -> %r' % (end - start, func.__name__, ','.join(param for param in param_list), result))
        return result
    return clocked2


@clock2
def print_str2(s, name=None):
    print(s, name)


if __name__ == '__main__':
    print_str('abc')
    print_str2(520, name='World!')
    print_str2('Hello', name='World!')
    print_str2(520, name=250)