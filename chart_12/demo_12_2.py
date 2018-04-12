'''
    多重继承和方法解析顺序
        Python按照特定顺序遍历继承图，这个顺序叫做方法解析顺序(Method resolution order, MRO)。类都有一个名为__mro__的属性，值时一个元组。按照方法解析顺序列出各个超类，从当前类一直向上，直到object类
        一个方法的具体实现时用__mro__从前到后搜索的.
'''


class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super.pong()
        C.pong(self)


if __name__ == '__main__':
    d = D()
    print(d)
    d.pong()
    C.pong(d)
    print(D.__mro__)

    print(bool.__mro__)