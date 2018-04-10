'''
    可散列的Vector2d

'''


_part_name = '可散列的Vector2d'


import functools


def my_property(func):
    @functools.wraps(func)
    def decorate(*args, **kw):
        return func(*args, **kw)
    return decorate(getattr(func, '__self__', None))


class Test:

    @my_property
    def x(self):
        return 10

    @property
    def y(self):
        return 10

    def z(self):
        return 10


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


if __name__ == '__main__':
    t = Test()
    print(t.y)
    print(t.x)
    print(dir(t.z))
    for key in dir(t.z):
        print(key, getattr(t.z, key))

    v1 = Vector2d(3, 4)
    v3 = Vector2d(4, 4)
    v2 = Vector2d(3.1, 4.2)
    print(hash(v1), hash(v2), hash(v3))
    print(set(v1, v2))

    int