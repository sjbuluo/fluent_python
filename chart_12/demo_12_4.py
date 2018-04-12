'''
    处理多重继承
        1.把接口继承和实现继承区分开
        2.使用抽象基类显式表示接口
        3.通过混入重用代码
        4.在名称中明确指明混入
        5.抽象基类可以作为混入，反过来则不成立
        6.不要子类化多个具体类
        7.为用户提供聚合类
        8.优化使用对象组合，而不是类继承
'''


class Base:

    def f1(self):
        print('f1 in Base')

    def f2(self):
        print('f2 in Base')


class C0:

    def f2(self):
        print('f2 in C0')


class C1(C0):

    def f1(self):
        print('f1 in C1')


if __name__ == '__main__':
    c1 = C1()
    c1.f1()
    c1.f2()
    print(C1.__mro__)
    C1.__bases__ = (Base,) + C1.__bases__
    print(C1.__mro__)
    c1.f1()
    c1.f2()