'''
    del和垃圾回收
        del语句删除名称，而不是对象。del命令可能会导致对象被当做垃圾回收，但是仅当删除的变量保存的是对象的最后一个引用，或者无法得到对象时。重新绑定也可能会导致对象的引用数量归零，导致对象被摧毁。
        __del__特殊方法，不会销毁实例，不应该在代码中调用。即将销毁实例时，Python解释器会调用__del__方法，给实例最后机会，释放资源。
        CPython中，垃圾回收使用的主要算法是引用计数。实际上，每个对象会统计有多少引用指向自己，当引用归零后，对象立即被销毁:CPython会在对象上调用__del__方法，然后释放分配给对象的内存。CPython2.0增加了分代垃圾回收算法。
'''


__part_name__ = 'del和垃圾回收'


import weakref


if __name__ == '__main__':
    s1 = {1, 2, 3}
    s2 = s1
    def bye():
        print('销毁')
    ender = weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'spam'
    print(ender.alive)
