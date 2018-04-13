'''
    上下文管理器和with块
        上下文管理器对象存在的目的是管理with语句，就像迭代器的存在时为了管理for语句一样
        with语句的目的是简化try/finall模式。这种模式用于保证一段代码运行完毕后执行某项操作，即便代码由于异常，return语句或sys.exit()调用而终止，也会执行指定的操作。finally子句中的代码通常用于释放重要的资源，或者还原临时变更的状态。
        上下文管理器协议包含__enter__和__exit__两个方法。with语句开始运行时，会在上下文管理器对象上调用__enter__方法，with结束时会在上下文管理器上调用__exit__方法，一次扮演finally子句的角色。
        最常见的例子是确保关闭文件对象.

        __exit__返回None或True以外的任何对象，with中的任何异常都会向上冒泡

        def __enter__(self):

        def __exit__(self, exc_type, exc_val, exc_tb):
            exc_type 异常类
            exc_value   异常实例

'''


import array
import sys
import os
import locale
import _io
from chart_15 import mirror


if __name__ == '__main__':
    print(sys.getdefaultencoding())
    print(sys.getfilesystemencoding())
    print(locale.getpreferredencoding())
    with open('mirror.py', encoding='utf-8') as fp:
        src = fp.read(60)
    print(len(src))
    print(fp)
    print(fp.closed, fp.encoding)
    # print(fp.read(60))
    print(dir(_io.TextIOWrapper))

    with mirror.LookingGlass() as what:
        print('1234567890')
        print(what)

    print(what)
    print('返回')

