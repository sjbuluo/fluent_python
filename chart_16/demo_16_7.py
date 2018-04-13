"""
    使用yield from

        在生成器gen中使用了yield from subgen() 控制权交给subgen 产出的值返回给gen的调用方 gen暂停知道subgen停止

        yield from x表达式对x对象所做的第一件事是调用iter(x)，从中获取迭代器

        yield from的主要功能是打开双向通道，把最外层的调用方与最内层的子生成器连接起来，这样两者可以直接发送和产出值，还可以直接传入异常

        子生成器
        委派生成器
        客户端代码

        子生成器不终止，委派生成器永远都在yield from处等待


"""


def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i


def gen2():
    yield from 'AB'
    yield from range(1, 3)


def gen3(*iterable):
    for it in iterable:
        yield from it


# def chef(w):
#     for i in range(5):
#         print('做饭')
#         yield from w
#     print('做饭结束')
#     w.close()
#
#
# def waiter():
#     while True:
#         yield
#         print('送餐')
#     print('送餐结束')


import  collections
import random


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


def grouper(results, key):
    while True:
        results[key] = yield from averager()


def main():
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for i in values:
            group.send(i)
        group.send(None)
    report(results)


def report(results):
    for key, value in sorted(results.items()):
        group, unit = key.split(';')
        print('{:6}{:3} 平均 {:0.5f}{:3}'.format(group, value.count, value.average, unit))


data = {
    'girls;kg': [random.randint(6000, 8000) / 100 for i in range(random.randint(10, 20))],
    'girls;cm': [random.randint(15000, 18000) / 100 for i in range(random.randint(10, 20))],
    'boys;kg': [random.randint(6000, 10000) / 100 for i in range(random.randint(10, 20))],
    'boys;cm': [random.randint(16000, 19000) / 100 for i in range(random.randint(10, 20))]
}



if __name__ == '__main__':
    print(list(gen()))
    print(list(gen2()))
    print(list(gen3([1, 2, 3], 'ABC')))

    # w = waiter()
    # c = chef(w)
    # next(w)
    # next(c)

    main()