'''
    获取关于参数信息

    def func(*args, **kw):
        pass
    默认值在func.__defaults__ 和 func.__kwdefaults__ 中
    参数在func.__code__.co_varnames 和 func.__code__.co_argcount
    co_varnames 包含函数中的局部变量 co_argcount 则是形式参数的数量

    可以使用inspect模块
    from inspect import signature
    sig = signature(func)
    sig.parameters 是一个有序映射，把参数名和inspect.Parameter对象对应起来
    inspect.Parameter也有自己的属性 name default kind (inspect._empty表示没有默认值 None是有效的默认值)
    _ParameterKind类的五种值:
    1.POSITIONAL_OR_KEYWORD
        可以通过定位参数和关键字参数传入的形参
    2.VAR_POSITIONAL
        定位参数元组
    3.VAR_KEYWORD
        关键字参数字典
    4.KEYWORD_ONLY
        仅限关键字参数
    5.POSITIONAL_ONLY
        仅限定位参数，目前Python声明函数的句法不支持
    inspect.Parameter对象还有annotation属性，通常是inspect._empty，可能包含Python3新的注解句法提供的函数签名元数据
    inspect.Parameter有bind方法，可以把任意个参数绑定到签名中的形参上。框架可以使用此方法在调用函数前验证函数。
    bind()方法获取inspect.Arguments对象
'''


import bobo


@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person


if __name__ == '__main__':
    for attr in dir(hello):
        print('%30s -> %s' % (attr, getattr(hello, attr, None)))
    #for attr in dir(hello.__code__):
        #print('%30s -> %s' % (attr, getattr(hello.__code__, attr, None)))