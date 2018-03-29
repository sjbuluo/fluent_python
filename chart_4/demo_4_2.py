'''
    字节概要
        Python内置了两种基本的二进制序列类型，Python3引入的不可变bytes类型和Python2.6添加的可变bytearray类型。(Python2.6也引入了bytes类型，但只是str的别名）
        bytes或bytearray对象的各个元素时介于0-255之间的整数，而不像Python2的str对象那样是单个字符。然而，二进制序列的切片始终是同一类型的二进制序列，包括长度为1的切片。
        bytes对象可以从str对象使用给定的编码构建
        各个元素时range(256)内的整数
        bytes对象的切片还是bytes对象，即使只有一个字节的切片
        bytearray对象没有字面量句法，而是以bytearray()和字节序列字面量参数的形式显示
        bytearray对象的切片还是bytearray对象
        虽然二进制序列其实是整数序列，但字面量表示法表明其中有ASCII文本。
        各个字节的值可能会使用下列三种不同的方式显示
        a.可打印的ASCII范围内的字节(从空格到~)，使用ASCII字符本身
        b.制表符、换行符、回车符和\对应的字节，使用转义序列\t、\n、\r和\\
        c.其他字节的值，使用十六进制转义序列(例如,\x00是控字节)

        二进制序列有个类方法是str没有的，名为fromhex，作用是解析十六进制数字对(数字对之间的空格是可选的),构建二进制序列
        构建bytes或bytearray实例还可以调用各自的构造方法。
        a.一个str对象和一个encoding关键字参数
        b.一个可迭代对象，提供0-255之间的数值
        c.一个实现了缓冲协议的对象(如bytes、bytearray、memoryview、array.array)；此时，把原对象中的字节序列赋值到新建的二进制序列中

        使用缓冲类对象创建bytes或bytearray对象时，始终赋值源对象中的字节序列。与之相反，memoryview对象允许在二进制数据结构之间共享内存。 想从二进制序列中提取结构化信息，struct模块是重要的工具

    结构体和内存视图
        struct模块提供了一些函数，把打包的字节序列转化成不同类型字段组成的元组。还有一系列函数用于执行反向转换、把元组转换成打包的字节序列。struct模块能处理bytes、bytearray、和memoryview对象。
        结构体的格外 <是小字节序，3s3s是两个3字节序列 HH是两个16位二进制整数
'''


import array
import struct


if __name__ == '__main__':
    bs = b'abcdefghijklmnopqrstuvwxyz'
    for i in bs:
        print(i)

    cafe = bytes('café', encoding='utf8')
    print(cafe)
    print(cafe[0])
    print(cafe[:1])
    print(type(cafe[:1]))
    cafe_arr = bytearray(cafe)
    print(cafe_arr)
    print(cafe_arr[-1:])
    print(type(cafe_arr[-1:]))

    print(' '.join([chr(num) for num in range(0, 128)]))

    print(bytes.fromhex('31 4B CE A9'))

    numbers = array.array('h', [-2, -1, 0, 1, 2])
    octets = bytes(numbers)
    print(octets)

    fmt = '<3s3sHH'
    with open('demo_4_2.gif', 'rb') as fp:
        img = memoryview(fp.read())

    header = img[:10]
    print(bytes(header))
    print(struct.unpack(fmt, header))
    del header
    del img

