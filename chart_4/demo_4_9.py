'''
    支持字符串和字节序列的双模式API
        标准库中的一些函数能接受字符串或字节序列为参数，然后根据类型展现不同的行为。re和os模块中就有这样的函数。
    4.9.1 正则表达式中的字符串和字节序列
        如果使用字节序列构建正则表达式，\d和\w等模式只能匹配ASCII字符；如果是字符串模式，就能匹配ASCII之外的Unicode数字或字母。
    4.9.2 os函数中的字符串和字节序列
        os模块中的所有函数、文件名或路径名参数既能使用字符串，也能使用字节序列。如果使用字符串参数调用，则会使用sys,getfilesystemencoding()得到的编解码器自动编码，然后操作系统会使用相同的编解码器解码。
        使用字符串返回字符串结果 使用字节序列参数返回字节序列结果
'''


import re
import os


if __name__ == '__main__':
    re_numbers_str = re.compile(r'\d+')
    re_word_str = re.compile(r'\w+')
    re_numbers_bytes = re.compile(rb'\d+')
    re_word_bytes = re.compile(rb'\w+')

    text_str = ('Ramanujan saw \u0be7\u0be8\u0bef'
                ' as 1729 = 1³ + 12³ = 9³ +８³．')
    text_bytes = text_str.encode('utf8')
    print('Text', repr(text_str), sep='\n')
    print('Numbers')
    print(' str :', re_numbers_str.findall(text_str))
    print(' bytes :', re_numbers_bytes.findall(text_bytes))
    print('Words')
    print(' str :', re_word_str.findall(text_str))
    print(' bytes :', re_word_bytes.findall(text_bytes))

    print(os.listdir('.'))
    print(os.listdir(b'.'))
