'''
    列表不是首选
        面对各种需求，可能会有比列表更好的选择。比如要存放1000万个浮点数的话，使用数组的效率要高得多，因为数组存的并不是float对象，而是数字的机器翻译，也就是字节表述，与C语言的数组一致。
    2.9.1 数组
        如果需要一个只包含数字的列表，那array.array比list更高效。数组支持所有跟可变序列有关的操作，包括.pop、.insert和.extend。另外数组还提供从文件读取和存入文件的更快的方法，如.frombytes和.tofile
        Python数组跟C语言数组一样精简。创建数组需要一个类型码，这个类型码用来表示在底层的C语言应该存放这样的数据类型。比如b类型码表示有符号的字符(signed char)，因此array('b')创建出的数组就只能存放一个字节大小的整数，范围从-128到127，在大量数据时能节省空间。
    Python3.4开始，数组类型不再支持诸如list.sort()这种就地排序方法。要给数组排序的话，得用sorted函数新建一个数组。想要不打乱次序的情况下添加新元素，可以使用disect.insort()
'''


from array import array
from random import random
import pickle


if __name__ == '__main__':
    floats = array('d', (random() for i in range(10 ** 7)))
    print(floats[-1])
    with open('floats.bin', 'wb') as fp:
        floats.tofile(fp)
    floats2 = array('d')
    with open('floats.bin', 'rb') as fp:
        floats2.fromfile(fp, 10 ** 7)
    print(floats2[-1])
    print(floats2 == floats)

    pickle