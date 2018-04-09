'''
    参数化装饰器
        解析源码中的装饰器时，Python把被装饰的函数作为第一个参数传给装饰器函数。让装饰器接受其他参数，需要创建一个装饰器工厂函数，把参数传给她，再返回一个装饰器
    7.10.1 一个参数化的注册装饰器
        为了方便启用或禁用register执行的函数注册功能，提供一个可选的active参数。默认False
'''


__part_name__ = '参数化装饰器'


registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


if __name__ == '__main__':
    print('running main()')
    print('registry ->', registry)
    f1()