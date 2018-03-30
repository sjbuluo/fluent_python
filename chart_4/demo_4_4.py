'''
    了解编解码问题
        虽然有一般性的UnicodeError异常,但是报告错误时几乎都会指明具体的异常：UnicodeEncodeError(把字符串转换成二进制序列)、UnicodeDecodeError(二进制序列转换为二进制序列)。如果源码的编码与预期不符，则加载Python模块时还可能抛出SyntaxError。
    4.4.1 处理UnicodeEncodeError
        多数非UTF编解码器只能处理Unicode字符的一小部分子集。把文本转换成字节序列时，如果目标编码中没有定义某个字符，就会抛出UnicodeEncodeError异常，除非把errors参数传给编码方法或函数，对错误进行特殊处理。
        'xxx'.encode('charmap', errors='')
        errors:
            ignore 遇到不能编解码的字符则跳过 不显示 通常不可用
            replace 使用?替换不能编解码的字符
            xmlcharrefreplace 无法编码的字符替换成XML实体

    4.4.2 处理UnicodeDecodeError
        不是每一个字节都包含有效的ASCII字符，也不是每一个字符序列都是有效的UTF-8或UTF-16。因此把二进制序列转换为文本时，如果假设是两个编码中的一个，遇到无法转换的字节序列时会抛出UnicodeDecodeError
        另一方面，陈旧的8位编码——如‘cp1252’、‘iso8859_1’和‘kio8_r’——能解码任何字节序列流而不抛出错误，例如随机噪声。因此，如果程序使用错误的8位编码，解码过程消无声息，而得到的是无用输出。

    4.4.3 使用预期之外的编码加载模块时抛出的SyntaxError
        Python3默认使用UTF-8编码源码，Python2(从2.5开始)则默认使用ASCII

    4.4.4 如果找出字节序列的编码
        统一字符编码侦测包Chardet，能够识别所支持的30中编码。

    4.4.5 BOM： 有用的鬼符
        UTF-16编码的序列开头有额外的字节
        b'\xff\xfe'，这是BOM，即字节序标记，指明编码时使用Intel CPU的小字节序
        在小字节序设备中，各个码位的最低有效字节在前面。
        在大字节序CPU中，编码顺序是相反的
        为了避免混淆，UTF-16编码在文本前面加上特殊的不可见字符(U+FEFF),编码器知道用哪种字节序
        UTF-16有两个变种 UTF-16LE，显示指明使用小字节序，UTF-16BE，显式指明使用大字节序
        指明字节序则不会产生BOM
        UTF-8的一大优势是不管设备使用哪种字节序，生成的字节序列始终是一致的，不需要BOM
        
'''


import chardet


if __name__ == '__main__':
    city = 'São Paulo'
    print(city.encode('utf_8'))
    print(city.encode('utf_16'))
    print(city.encode('iso8859_1'))
    #print(city.encode('cp437'))
    print(city.encode('cp437', errors='ignore'))
    print(city.encode('cp437', errors='replace'))
    print(city.encode('cp437', errors='xmlcharrefreplace'))


    octets = b'Montt\xe9al'
    print(octets.decode('cp1252'))
    print(octets.decode('iso8859_7'))
    print(octets.decode('koi8_r'))
    #print(octets.decode('utf_8'))
    print(octets.decode('utf-8', errors='ignore'))

    print(chardet.detect(b'Hello World'))

    print(chardet.detect('你好，世界！'.encode('utf-8')))

    u16 = 'El Niño'.encode('utf-16')
    print(u16)
    print([i for i in u16])
    u16le = 'El Niño'.encode('utf-16le')
    print([i for i in u16le])
    u16be = 'El Niño'.encode('utf-16be')
    print([i for i in u16be])