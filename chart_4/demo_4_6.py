'''
    为了正确比较二规范化Unicode字符串
        使用unicodedata.normalize函数提供的Unicode规范化
        这个函数的第一个参数是这4个字符串中的一个 NFC NFD NFKC NFKD
        NFC(Normalization Form C)使用最少的码位构成等价的字符串
        NFD(Normailzation Form D)把组合字符分解成基字符和单独的组合字符

        默认输入文本时NFC形式的，在保存文本之前最好使用normalize('NFC', user_text)清洗字符串。
        使用NFC时，有些单字符会被规范成另一个单字符。

        在另外两个规范化形式(NFKC和NFKD)的首字母缩略词中，字母K表示"compatibility"(兼容性)。这两种是较严格的规范化形式，对兼容字符有影响。为了兼容现有的标准，有些字符会出现多次。这两种形式中，各个兼容字符会被替换成一个或多个兼容分解字符，即便这样格式损失，但仍是首选。
    4.6.1 大小写折叠
        大小写折叠其实就是把所有文本变成小写，再做其他转换。这个功能由str.casefold()方法支持。
        对于只包含latin1字符的字符串s，s.casefold()得到的结果与s.lower()方法得到的结果相同。

    4.6.3 极端规范化：去掉变音符号

'''


from unicodedata import normalize,name


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())


if __name__ == '__main__':
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1, s2)
    print(len(s1), len(s2))
    print(s1 == s2)
    print(normalize('NFC', s1), normalize('NFC', s2))
    print(len(normalize('NFC', s1)), len(normalize('NFD', s2)))
    print(normalize('NFC', s1) == normalize('NFC', s2))
    print(normalize('NFD', s1), normalize('NFD', s2))
    print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
    print(normalize('NFD', s1) == normalize('NFD', s2))

    ohm = '\u2126'
    print(name(ohm))
    ohm_c = normalize('NFC', ohm)
    print(name(ohm_c))
    print(ohm == ohm_c)
    print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

    str1 = '\u00BD'
    print(str1)
    print(normalize('NFKC', str1))
    str2 = '\u00B5'
    print(str2)
    print(normalize('NFKC', str2))

    half = '½'
    print(ord(half))
    print(normalize('NFKC', half))
    four_squared = '4²'
    print(normalize('NFKC', four_squared))
    micro = 'μ'
    micro_kc = normalize('NFKC', micro)
    print(micro, micro_kc)
    print(ord(micro), ord(micro_kc))
    print(name(micro), name(micro_kc))

    s1 = 'café'
    s2 = 'cafe\u0301'
    print(nfc_equal(s1, s2))
    print(fold_equal(s1, s2))