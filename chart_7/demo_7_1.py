'''
    装饰器时刻调用的对象，其参数是另一个函数(被装饰的函数)。装饰器可能会处理被装饰的函数，然后返回，或者将其替换成另一个函数或可调用对象。
    @decorate
    def target():
        print('running target()')
    def target():
        print('running target()')
    target = decorate(target)
    效果一致

    严格而言，装饰器只是语法糖。
    装饰器的特性：
    1.能把被装饰的函数替换成其他函数
    2.装饰器在加载模块时立即执行
'''


__part_name__ = '装饰器基础知识'


def deco(func):
    print('立即执行')
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


if __name__ == '__main__':
    pass
    #target()
    #print(target)


