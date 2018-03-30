'''
    基本的编解码器
        Python自带了超过100中编解码器(codec,encoder/decoder)，用于在文本和字节之间相互转换。每个编解码器都有一个名称，如'utf_8',而且经常有几个别名，如'utf8'、'utf-8’和'U8'。这些名称可以传给open()，str.encode()，bytes.decode()等函数。

'''


if __name__ == '__main__':
    for codec in ['latin_1', 'utf_8', 'utf_16']:
        print(codec, 'El Niño'.encode(codec), sep='\t')