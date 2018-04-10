'''
    叠放装饰器
        把@d1和@d2两个装饰器按顺序应用到f函数上，作用相当于f = d1(d2(f))
'''


__part_name__ = '叠放装饰器'


def d1(func):
    def d1_inner(*args, **kw):
        return func(*args, **kw)
    return d1_inner


def d2(func):
    def d2_inner(*args, **kw):
        return func(*args, **kw)
    return d2_inner


@d1
@d2
def test():
    pass


if __name__ == '__main__':
    t = test
    print(t.__name__)