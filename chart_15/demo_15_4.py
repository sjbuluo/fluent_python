'''
    使用@contextmanager
        @contextmanager装饰器能减少创建上下文管理器的样板代码量，因为不用编写一个完整的类，定义__enter__和__exit__方法，只需实现一个yield语句的生成器，生成想让__enter__方法返回的值

        在@contextmanager装饰的生成器中，yield语句的作用是把函数的定义体分为两部分，yield语句前面的所有代码在with开始执行__enter__,之后在with结束后__exit__

        @contextmanager装饰器会把生成器函数包装成实现__enter__和__exit__方法的类
        这个类的__enter__方法:
        1.调用生成器函数，保存生成器对象
        2.调用next(gen)，执行到yield关键字所在位置
        3.返回产出结果，以便把产出的值绑定到with/as语句中的目标变量上

        with块终止时，__exit__方法会做：
        1.检查有没有把异常传给exc_type，如果有，调用gen.throw(exception)，在生成器函数定义体中包含yield关键字那一行抛出异常
        2.否则调用next(gen)，继续执行生成器函数定义体中yield之后的语句

        不想让contextmanager压制异常，必须在被装饰的函数中显式重新抛出异常
        使用@contextmanager装饰器时，要把yield语句放在try/finally中，这是不可避免的


'''


import contextlib
import sys
import csv
import os


def gen1():
    print('enter')
    yield 1
    print('exit')


@contextlib.contextmanager
def looking_glass():
    origin_write = sys.stdout.write
    sys.stdout.write = lambda text: origin_write(text[::-1])
    yield 'ABCDEFG'
    sys.stdout.write = origin_write
    return True


@contextlib.contextmanager
def looking_glass2():
    origin_write = sys.stdout.write
    sys.stdout.write = lambda text: origin_write(text[::-1])
    try:
        yield 'ABCDEFGH'
    except ZeroDivisionError:
        print('')
    finally:
        sys.stdout.write = origin_write
        return True


@contextlib.contextmanager
def inplace(filename=None, mode='r', encoding='utf-8', *args, newline=None):
    outfp = open(filename, 'a', encoding=encoding)
    infp = open(filename, 'r', encoding=encoding)
    try:
        yield infp, outfp
    except BaseException:
        print('出错')
    finally:
        if infp:
            infp.close()
        if outfp:
            outfp.close()


if __name__ == '__main__':
    g = gen1()
    print(next(g))
    # print(next(g))

    with looking_glass() as what:
        print('Hello World!')
        print(what)

    print(what)
    print('Hello World!')

    with inplace('test.txt', 'r', newline='') as (infp, outfp):
        print(infp, outfp)
        print(infp.read())
        for line in infp.readlines():
            print(line)
        for word in 'Hello World It is OK'.split():
            outfp.write(word + '\n')
