'''
    支持函数式编程的包
        operator和functools等包的支持，函数式编程风格也可以实现。
    5.10.1 operator模块
        函数式编程中，需要把算术运算符当做函数使用
        operator模块为多个算术运算符提供了对应的函数，从而避免编写平凡的匿名函数
        operator模块中还有一类函数，能替代从序列中取出元素或读取对象属性的lambda表达式
            itemgetter和attrgetter会自行构建函数
            methodcaller创建的函数会在对象上调用参数指定的方法。

    5.10.2 使用functools.partial 冻结参数
        functools模块提供了一系列高阶函数，
        其中最有名的是reduce
        其余最有用的是partial及其变体，partialmethod
        functools.partial高级函数用于部分应用函数。
        部分应用是指，基于一个函数创建一个新的可调用对象，把原函数的某些参数固定。使用这个函数可以把接受一个或多个参数的函数改编成需要回调的API
'''


import functools
import operator
import collections
import unicodedata

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


LatLong = collections.namedtuple('LatLong', 'lat long')
Metropolis = collections.namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for
               (name, cc, pop, (lat, long)) in metro_data]


def fact(n):
    return functools.reduce(lambda a, b: a * b, range(1, n + 1))


def fact2(n):
    return functools.reduce(operator.mul, range(1, n + 1))


def sum2(n):
    return functools.reduce(operator.add, range(1, n + 1))


if __name__ == '__main__':
    print(fact(5))
    print(fact2(5))
    print(sum2(10))

    for city in sorted(metro_data, key=operator.itemgetter(1)):
        print(city)

    for city in sorted(metro_areas, key=operator.attrgetter('cc')):
        print(city)

    s = 'The time has come'
    upcase = operator.methodcaller('upper')
    print(s)
    print(upcase(s))
    print(s.upper())

    triple = functools.partial(operator.mul, 3)
    print(triple(7))
    print(list(map(triple, range(1, 11))))
    tweentyOne = functools.partial(operator.mul, 3, 7)
    print(tweentyOne())

    nfc = functools.partial(unicodedata.normalize, 'NFC')
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1, s2)
    print(s1 == s2)
    print(nfc(s1), nfc(s2))
    print(nfc(s1) == nfc(s2))

    # print(triple(1, 2)) 无效