'''
    为什么len不是普通方法
    如果x是一个内置类型的实例，那么len(x)的速度会非常快。背后的原因是CPython会直接从一个C结构体力读取对象的长度， 完全不会调用任何方法。获取一个集合中元素的数量是一个很常见的操作，在str、list、memoryview等类型上，这个操作必须高效。
'''


class Test:

    def __len__(self):
        return 10


if __name__ == '__main__':
    print(len(Test()))
