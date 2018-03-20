'''
    列表不是首选
        面对各种需求，可能会有比列表更好的选择。比如要存放1000万个浮点数的话，使用数组的效率要高得多，因为数组存的并不是float对象，而是数字的机器翻译，也就是字节表述，与C语言的数组一致。
    2.9.1 数组
        如果需要一个只包含数字的列表，那array.array比list更高效。数组支持所有跟可变序列有关的操作，包括.pop、.insert和.extend。另外数组还提供从文件读取和存入文件的更快的方法，如.frombytes和.tofile
        Python数组跟C语言数组一样精简。创建数组需要一个类型码，这个类型码用来表示在底层的C语言应该存放这样的数据类型。比如b类型码表示有符号的字符(signed char)，因此array('b')创建出的数组就只能存放一个字节大小的整数，范围从-128到127，在大量数据时能节省空间。
    Python3.4开始，数组类型不再支持诸如list.sort()这种就地排序方法。要给数组排序的话，得用sorted函数新建一个数组。想要不打乱次序的情况下添加新元素，可以使用disect.insort()
    2.9.2 内存视图
        memoryview是一个内置类，能让用户在不复制内容的情况下操作同一个数组的不同切片。memoryview的概念受到NumPy的启发。
        内存视图其实是泛华和去数字化的NumPy数组。可以在不需要复制内容的前提下，在数据结构之间共享内存。其中数据结构可以是任何形式，比如PIL图片，SQLite数据库和NumPy的数组等等。这个功能在处理大型数据集合的时候非常重要。
        memoryview.cast的概念跟数组模块类似，能用不同的方式读写同一块内存数据。会把同一块内存中的内容打包成一个全新的memoryview对象。
        array('h') 16进制 2个字节
        array('B') 无符号整型
        array('b') 8位 1个字节
    2.9.3 NumPy和SciPy
        凭借NumPy和SciPy提供的高阶数组和矩阵操作，Python成为科学计算应用的主流语言。NumPy实现了多维同质数组和矩阵，这些数据结构不但能处理数字，还能存放其他由用户定义的记录。
        SciPy是基于NumPy的另一个库，提供了很多跟科学计算有关的算法，专为线性代数、数值积分和统计学而设计。
    2.9.4 双向队列和其他形式的队列
        collections.deque类是一个线程安全、可以快速从两端添加或者删除元素的数据类型。如果想要一种数据类型来存放最近使用过的几个元素，deque也是一个很好的选择。这个因为在新建双向队列时，可以指定这个队列的大小。如果这个队列满员，还可以从反向端删除过期的元素，然后在微端添加新的元素。

'''


from array import array
import random
import numpy
import scipy
from time import perf_counter as pc
from collections import deque


if __name__ == '__main__':
    #floats = array('d', (random.random() for i in range(10 ** 7)))
    #print(floats[-1])
    #with open('floats.bin', 'wb') as fp:
    #    floats.tofile(fp)
    #floats2 = array('d')
    # with open('floats.bin', 'rb') as fp:
    #     floats2.fromfile(fp, 10 ** 7)
    # print(floats2[-1])
    # print(floats2 == floats)

    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0])
    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(numbers)

    a = numpy.arange(12)
    print(a)
    print(type(a))
    print(a.shape)
    a.shape = 3, 4
    print(a)
    print(a[2])
    print(a[2][1])
    print(a[:, 1])
    print(a.transpose())
    print(a.shape)
    a.shape = 2, 6
    print(a)

    #floats = array('d', [(random.randint(1000000, 10000000) + random.random()) for i in range(1, 10 ** 7)])
    #with open('floats-10M-lines.txt', 'wb') as fb:
    #    for num in ((random.randint(1000000, 10000000) + random.random()) for i in range(1, 10 ** 7)) :
    #        fb.write(('%s\r\n' % num).encode('gbk'))
    # floats = numpy.loadtxt('floats-10M-lines.txt')
    # print(floats[-3:])
    # floats *= .5
    # print(floats[-3:])
    # t0 = pc()
    # floats /= 3
    # print(pc() - t0)
    # numpy.save('floats-10M', floats)
    # floats2 = numpy.load('floats-10M.npy', 'r+')
    # floats2 *= 6
    # print(floats2[-3:])

    dq = deque(range(10), maxlen=10)
    print(dq)
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)
    dq.appendleft(-1)
    print(dq)
    dq.extend([11, 22, 33])
    print(dq)
    dq.extendleft([10, 20, 30, 40])
    print(dq)

