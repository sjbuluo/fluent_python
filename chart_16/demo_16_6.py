'''
    让协程返回值

    return 会抛出StopIteration异常 value为返回值

    yield from结构会在内部自动捕获StopIteration异常，还会把value变为yield from的值
'''


import collections


Result = collections.namedtuple('Result', 'count average')


def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


if __name__ == '__main__':
    gen_avg = averager()
    next(gen_avg)
    gen_avg.send(10)
    gen_avg.send(6.5)
    gen_avg.send(30)
    try:
        gen_avg.send(None)
    except StopIteration as err:
        print(err.value)
