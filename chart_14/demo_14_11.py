'''
    可迭代归约函数

    接受一个可迭代对象，然后返回单个结果，都可以使用functools.reduce()

    内置      all(it)     it所有真返回真 会短路
    内置      any(it)     it有真则返回真 会短路
    内置      max(it, key=, default=)     返回it中的最大元素，key是排序函数，如果可迭代对象为空则返回default
    内置      ming(it, key=, default)     返回it中的最小元素
    functools reduce(func, it, [initial])
    内置      sum(it, start=0)    计算总和

    
'''