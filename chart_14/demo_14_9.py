'''
    标准库中的生成器函数
        标准库提供了很多生成器，有用语逐行迭代纯文本文件的对象，还有出色的os.walk函数

        用于过滤的生成器函数：从输入的可迭代对象中产出元素的子集，而且不修改元素本身
        大多数都接受一个断言参数（predicate），一个布尔函数，作用于输入的每个元素上，判断是否在输出中

        itertools           compress(it, selector_it)           并行处理两个可迭代的对象，如果selector_it中的元素是真值，则产出it中对应的元素
        itertools           dropwhile(predicate, it)            处理it，跳过predicate结果为真的元素，产出剩下的元素
        内置                filter(predicate, it)               把it中的各个元素传给predicate，结果为真则产出对应元素，如果predicate为None，则只产出真值元素
        itertools           filterfalse(predicate, it)          与filter函数的作用类似，但逻辑相反，predicate为False则产出元素
        itertools           islice(it, stop)                    传出it的切片 类似于s[:stop] s[begin:stop:step] 不过it可以是任何可迭代对象，而且这个函数实现的是惰性操作
                            islice(it, start, stop, end)
        itertools           takewhile(predicate, it)            predicate返回真值产出元素，然后立即停止不再做任何检查

        映射的生成器函数：在输入单个可迭代对象中的各个元素上做计算，然后返回结果

        itertools           accumulate(it, [func])              产出累积的总和，如果提供了func，那么把前两个元素传给它，然后把计算结果和下一个元素传给它，一次类推，最后产出结果
        内置                  enumerate(iterable, start=0)        产出由两个元素组成的元祖，结构是(index, item),其中index从start开始计数，item则从iterable中获取
        内置                  map(func, it1, it2, ..., itN)       把it中的各个元素传给func，产出结果,如果传入N个可迭代对象，那么func必须能接受N个参数，而且要并行处理各个可迭代对象
        itertools           starmap(func, it)                   把it中的各个元素传给func，产出结果，输入的可迭代对象应该产出可迭代元素iit，然后以func(*iit)这种形式调用func


        合并多个可迭代对象的生长期函数 都从输入的多个可迭代对象中产出元素

        itertools           chain(it1, ...., itN)               先产出it1中的所有元素，然后是it2，最后全部无缝连接在一起
        itertools           chain.from_iterable(it)             产出it生成的各个可迭代对象中的元素，无缝连接
        itertools           product(it1, ..., itN, repeat=1)    计算笛卡尔积，从输入的各个可迭代对象中获取元素，合并成由M个元素组成的元祖，与嵌套的for循环效果一样，repeat指明重复处理多少次输入的可迭代对象
        内置                  zip(it1, ..., tiM)                  并行从输入的各个可迭代对象中获取元素，产出由N个元素组成的元祖，其中一个到头则停止
        itertools           zip_longgest(it1, ...itN, filevalue=None) 并行获取，等到最长的元素到头后停止，空缺的值由fillvalue填充

        把输入的各个元素扩展成多个输出元素的生成器函数

        itertools           combinations(it, out_len)           排列（不重复）把it产出的out_len个元素组合在一起，然后产出
        itertools           combinations_with_replacement(it, out_len)  排列（可重复） 把it产出的out_len个元素组合在一起，然后产出，包含相同元素的组合
        itertools           count(start=0, step=1)              从start开始不断产出数字，按step指定的步幅增加
        itertools           cycle(it)                           从it中产出各个元素，存储各个元素的副本，然后按顺序重复不断地产出各个元素
        itertools           permutations(it, out_len=None)      (组合 不可重复)把out_len个it产出的元素排列在一起，然后产出这些排列 out_len的默认值是len(list(it))
        itertools           repeat(item, [times])               重复不断的产出指定的元素，除非指定times

        用于重新排列元素的生成器函数

        itertools           groupby(it, key=None)               产出由两个元素组成的元素，形式为(key, group) key是分组标准，group是生成器，哦你关于产出分组里的数据
        内置                  reversed(seq)                       倒序输出 seq必须是序列或者实现__reversed__特殊方法
        itertools           tee(it, n=2)                        产出一个由N个生成器组成的元祖，每个生成器用于单独产出输入的可迭代对象中的元素

'''


def vowel(c):
    return c.lower() in 'aeiou'


if __name__ == '__main__':
    print(list(filter(vowel, 'Aardvark')))

    import itertools

    print(list(itertools.filterfalse(vowel, 'Aardvark')))
    print(list(itertools.dropwhile(vowel, 'Aardvark')))
    print(list(itertools.takewhile(vowel, 'Aardvark')))
    print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
    print(list(itertools.islice('Aardvark', 4)))
    print(list(itertools.islice('Aardvark', 4, 7)))
    print(list(itertools.islice('Aardvark', 1, 7, 2)))


    for index, item in enumerate(range(0, 11)):
        print(index, item)

    sample = [5, 4, 2, 8, 7, 6, 3, 0, 9 ,1]
    print(list(itertools.accumulate(sample)))
    print(list(itertools.accumulate(sample, min)))
    print(list(itertools.accumulate(sample, max)))

    import operator
    print(list(itertools.accumulate(sample, operator.mul)))
    print(list(itertools.accumulate(range(1, 11), operator.mul)))

    print(list(enumerate('Aardvark', 1)))
    print(list(map(operator.mul, range(11), range(11))))
    print(list(itertools.starmap(operator.mul, enumerate('Aardvark', 1))))

    print(list(itertools.chain('ABC', range(2))))
    print(list(itertools.chain.from_iterable(enumerate('ABC'))))
    print(list(zip('ABC', range(5))))
    print(list(zip('ABC', range(5), [10, 20 ,30 ,40])))
    print(list(itertools.zip_longest('ABC', range(5))))
    print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))

    print(list(itertools.product('ABC', range(2))))
    print(list(itertools.product('ABC', range(2), repeat=2)))

    ct = itertools.count()
    print(next(ct))
    print(next(ct))
    print(next(ct))
    print(next(ct))
    print(list(itertools.islice(itertools.count(1, .3), 3)))
    cy = itertools.cycle('ABC')
    print(next(cy))
    print(list(itertools.islice(cy, 7)))
    rp = itertools.repeat(7)
    print(next(rp))
    print(next(rp))
    print(next(rp))
    print(list(itertools.repeat(8, 4)))
    print(list(map(operator.mul, range(11), itertools.repeat(5))))

    print(list(itertools.combinations('ABC', 2)))
    print(list(itertools.combinations_with_replacement('ABC', 2)))
    print(list(itertools.permutations('ABC', 2)))
    print(list(itertools.product('ABC', repeat=2)))


    print(list(itertools.groupby('LLLLAAGGG')))
    print(list(itertools.tee('ABC')))
    g1, g2 = itertools.tee(('ABC'))
    print(next(g1))
    print(next(g2))
    print(next(g2))
    print(list(g1))
    print(list(g2))
    print(list(zip(*itertools.tee('ABC'))))
