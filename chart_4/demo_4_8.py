'''
    Unicode数据库
        Unicode标准提供了一个完整的数据库(格式化的文本文件),不仅包括码位与字符名称之间的映射，还有各个字符的元数据，以及字符之间的关系。
        例如：unicdoe数据库记录了字符是否可以打印、是不是字母、是不是数字，或者是不是其他数值符号。
        字符串的isidentifier、isprintable、isdecimal和isnumeric等方法就是靠这些信息判断的。str.casefold方法也用到了Unicode表中的信息。
        unicodedata模块中的几个函数用于获取字符的元数据。例如，字符在标准中的官方名称是不是组合字符，以及符号对应的人类可读数值。
'''


import unicodedata
import re


re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'


if __name__ == '__main__':
    for char in sample:
        print('U+%04x'  % ord(char),
              char.center(6),
              're_dig' if re_digit.match(char) else '-',
              'isdig' if char.isdigit() else '-',
              'isnum' if char.isnumeric() else '-',
              format(unicodedata.numeric(char), '5.2f'),
              unicodedata.name(char),
              sep='\t')
