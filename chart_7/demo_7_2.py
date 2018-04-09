'''
    Python合适执行装饰器
        装饰器的一个关键特性是，在被装饰的函数定义之后立即运行。这通常是在导入时（即Python加载模块时）
'''


__part_name = 'Python何时执行装饰器'


registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()