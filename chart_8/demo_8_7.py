'''
    Python对不可变类型施加的把戏
    不可变对象使用构造函数或[:]方式会返回同一个对象引用 如tuple，str, bytes,frozenset
    共享字符串字面量是一种优化措施，称为驻留，CPython还会在小的整数上使用这个优化措施，防止重复创建热门数字，如0、-1/42.不会驻留所有字符串和整数。不要使用is判断int和str，是Python解释器内部使用的特性
'''


class Test:

    def __getitem__(self, item):
        if isinstance(item, slice):
            print(slice)


if __name__ == '__main__':
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    print(t2 is t1)
    t3 = t1[:]
    print(t3 is t1)

    t = Test()
    t[:]
    t[1:]
    t[:3]
    t[1:3]
    t[:-1]
    t[-3:]
    t[-3:-1]
    t[::]
    t[::1]
    t[1:3:1]

    print(dir(slice))
