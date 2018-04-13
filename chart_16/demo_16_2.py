'''
    用作协程的生成器的基本行为
        协程可以身处四个状态中的一个
        inspect.getgeneratorstate(...)
        1.'GEN_CREATED' 等待开始执行
        2.'GEN_RUNNING' 解释器正在执行
        3.'GEN_SUSPENDED'   在yield表达式出暂停
        4.'GEN_CLOSED'  执行结束
'''


import inspect


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received: ', x)


def simple_coroutine2(a):
    print('-> started a = ', a)
    b = yield a
    print('-> received b = ', b)
    c = yield a + b
    print('-> received c = ', c)



if __name__ == '__main__':
    # my_coro = simple_coroutine()
    # print(my_coro)
    # next(my_coro)
    # my_coro.send(42)

    my_coro2 = simple_coroutine2(14)
    print(inspect.getgeneratorstate(my_coro2))
    print(next(my_coro2))
    print(inspect.getgeneratorstate(my_coro2))
    print(my_coro2.send(28))
    print(inspect.getgeneratorstate(my_coro2))
    print(my_coro2.send(99))
    print(inspect.getgeneratorstate(my_coro2))
