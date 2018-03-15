'''
    列表推导是构建列表(list)的快捷方式，而生成器表达式则可以用来创建其他任何类型的序列。

    通常，只用列表推导来创建新的列表，并且尽量保持简短。如果列表推导的代码超过了两行，就需要考虑使用for循环重写。
    句法提示：Python会忽略代码里[]、{}、()中的换行，多行的列表、列表推导、生成器表达式、字典等。可以省略不太好看的续行符\。
    Python2.X中存在变量泄漏问题，在列表推导中使用变量会影响列表推导上下文中的同名变量。
    而在Python3.X中则不存在这种问题。

    虽然也可以使用列表推导来初始化元组、数组或其他序列类型，但生成器表达式是更好的选择。这是因为生成器表达式背后遵守了迭代器协议，可以逐个地产出元素，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里。可以有效的节省内存。
'''

import array


if __name__ == '__main__':
    symbols = 'abcdefg'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)
    codes_new = [ord(symbol) for symbol in symbols]
    print(codes_new)
    l = [(x, y)
            for x in range(0, 11)
            for y in range(1, 11)]
    print(l)
    print(True if 2 > 3 else False)
    print(True if 2 < 3 else False)
    print([ord(symbol) for symbol in symbols if ord(symbol) > 100])
    print(list(filter(lambda num: num > 100, map(ord, symbols))))

    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]
    print([x * y
                for x in l1
                for y in l2])
    print(sum([x * y
                    for x in l1
                    for y in l2]))

    print(tuple(ord(symbol) for symbol in symbols))
    print(array.array('I', (ord(symbol) for symbol in symbols)))

    colors = ['黑色', '白色']
    sizes = ['S', 'M', 'L']
    for tshirt in ('%s %s' % (c, s) for c in colors
                                    for s in sizes):
        print(tshirt)
    g = ('%s %s' % (c, s) for c in colors
                            for s in sizes)
    print(g)
    print(next(g))
