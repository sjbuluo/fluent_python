'''
    contextlib模块中的实用工具
        contextlib - Utilities for with-statement contexts

        closing
            如果对象提供了close()方法，但没有实现__enter__ __exit__协议，那么可以使用这个函数构建上下文管理器
        suppress
            构建临时忽略指定异常的上下文管理器
        @contextmanager
            这个装饰器把简单的生成器函数变成上下文管理器，不用创建类去实现管理器协议
        ContextDecorator
            基类，用于定义基于类的上下文管理器。也能用于装饰函数，在受管理的上下文中运行整个函数。
        ExitStack
            这个上下文管理器能进入多个上下文管理器 with块结束后，按后进先出的顺序调用__exit__方法

        最常见的是@contextmanager装饰器

'''