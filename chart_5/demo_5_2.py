'''
    高阶函数
        接受函数为参数，或者把函数作为结果返回的函数是高阶函数
        在函数式编程范式中，最为人熟知的高阶函数有map、filter、reduce和apply
        map、filter、reduce的替代品
        map和filter因为有列表推导存在，尽量换掉并避免了使用lambda
        Python2，reduce是内置函数，但是在Python3中移动到了functools模块中。这个函数最长用于求和，但是在2003年发布的Python2.3开始，最好使用内置的sum()函数
        all()和any()也是内置的归约函数
        all(iterable)如果每个元素都是真值则返回True all([])返回True(空列表)
        any(iterable)如果有元素为真则返回True any([])返回False(空列表)

'''


import functools
import operator

def test(func):
    @functools.wraps(func.__name__)
    def wrapper(*args, **kw):
        print('装饰器启用')
        return func(*args, **kw)
    return wrapper


def reverse(word):
    return word[::-1]


@test
def test_decorator():
    print('真实代码部分')


def factoria1(n):
    return 1 if n < 2 else n * factoria1(n - 1)


if __name__ == '__main__':
    test_decorator()

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=len))
    print(sorted(fruits, key=reverse))

    fact = factoria1
    print(list(map(fact, range(6))))
    print([fact(n) for n in range(6)])
    print(list(map(fact, list(filter(lambda x: x % 2, range(6))))))
    print([fact(n) for n in range(6) if n % 2])

    print(functools.reduce(operator.add, range(100)))
    print(functools.reduce(operator.mul, range(1, 10)))
    print(sum(range(100)))

    print(all([]))
    print(all([1, 2, 3, 4, 5]))
    print(all([1, 2, 3, 4, 0]))
    print(any([]))
    print(any([0, 0, 0, 0, 0]))
    print(any([0, 0, 0, 0, 1]))

