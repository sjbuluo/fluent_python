'''
    Unicode文本排序
        Python比较任何类型的序列时，会一一比较序列里的各个元素。对字符串，比较的是码位，比较非ASCII字符是，得到的结果不尽如人意。
        在Python中，非ASCII文本的标准排序方式是使用locale.strxfrm函数，这个函数会把字符串转换成适合所在区域进行比较的形式
        使用locale.strxfrm函数之前，必须纤维应用设定合适的区域设置，要需要操作系统支持这项设置
        在使用locale.strxfrm之前 需要调用locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
        需要注意:
            a,区域设置是全局的，因此不推荐在库中调用setlocale函数，应用或框架应该在进程启动时设定区域设置，而且此后不再修改。
            b.操作系统必须支持区域设置
            c.必须知道如何拼写区域名称 通过language_code.encoding获取
                Windows中比较复杂 Language Name-Language Variant_Region Name.codepage
        使用Unicode排序算法排序
            PyUCA库
            没有考虑区域设置，定制排序方式，可以把自定义的排序表路径传给Collator()构造方法。
'''


import sys, os, locale, pyuca


if __name__ == '__main__':
    locale.getpreferredencoding()
    coll = pyuca.Collator()
    fruits = ['a', 'b', 'c', 'd', 'e']
    sorted_fruits = sorted(fruits, key=coll.sort_key)
    print(sorted_fruits)