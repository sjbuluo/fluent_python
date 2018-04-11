'''
    Vector类第四版：散列和快速等值测试
    functools.reduce(operator.xor, map(...))
    functools.reduce(operator.xor, (hash(item) for item in xxx))

    x = y && all(...)

    zip函数
        使用for循环迭代元素不用处理索引变量，还能避免很多缺陷。但是需要一些特殊的使用函数协助。zip函数，能轻松的并行迭代两个或更多可迭代对象，返回的元组可以拆包成变量。
        zip()函数迭代长度最短的之后停止
        itertools.zip_longgest()则迭代最长，自己补None

'''