'''
    处理文本文件
        处理文本的最贱实践是Unicode三明治。意思是，要尽早把输入(例如读取文件时)的字节序列解码成字符串对象。在其他处理过程中，一定不能编码或解码。对输出来说，则要尽量晚地把字符串编码成字节序列。
        Python3中内置的open函数会在读取文件时做必要的解码，以文本模式写入文件时还会做必要的编码。
        在没有指定encoding的情况下，会使用操作系统默认的编码格式

        默认情况下，open函数采用文本模式，返回一个TextIOWrapper对象
        rb返回一个BufferedRaader对象

        默认情况下使用locale.getpreferredencoding()作为文件读写的默认编码
        二进制数据和字符串之间转换时 使用sys.getdefaultencoding()(很少设置)
        编译解码文件名 使用sys.getfilesystemcoding()
'''


import os


if __name__ == '__main__':
    with open('cafe.txt', 'w', encoding='utf8') as f:
        f.write('café')
    with open('cafe.txt', 'r') as f:
        print(f.read())
    with open('cafe.txt', 'r', encoding='utf8') as f:
        print(f.read())

    try:
        fp = open('cafe.txt', 'w', encoding='utf8')
        print(fp)
        fp.write('café')
    finally:
        if fp:
            fp.close()

    os.stat('cafe.txt').st_size
    try:
        fp2 = open('cafe.txt')
        print(fp2)
        print(fp2.encoding)
        print(fp2.read())
    finally:
        if fp2:
            fp2.close()

    try:
        fp3 = open('cafe.txt', 'r', encoding='utf8')
        print(fp3)
        print(fp3.encoding)
        print(fp3.read())
    finally:
        if fp3:
            fp3.close()

    try:
        fp4 = open('cafe.txt', 'rb')
        print(fp4)
        print(fp4.read())
    finally:
        if fp4:
            fp4.close()