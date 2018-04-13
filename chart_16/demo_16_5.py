'''
    终止协程和异常处理
        协程中未处理的异常会向上冒泡，传给next函数或send方法的调用方。

        Python2.5开始，客户代码可以在生成函数上调用两个方法，显式地把异常发给协程。
        分别是
        1.throw
        2.close

        1.generator.throw(exc_type, exc_value, exc_tb)
            致使生成器在暂停的yield表达式处抛出指定的异常，如果生成器处理了抛出的异常，代码会向前执行到下一个yield表达式，而产出的值会变成调用.throw方法得到的返回值。没有处理则向上抛出
        2.generator.close()
            致使生成器在暂停的yield表达式处抛出GeneratorExit异常。如果生成器没有处理这个异常，或者抛出stopIteration异常，调用方不会报错。如果收到GeneratorExit异常，生成器一定不能产出值，否则解释器会抛出RuntimeError异常。生成器抛出的其他异常会向上冒泡，传给调用方。

'''


class DemoException(Exception):
    '''演示用异常类型'''
    pass


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled.Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('The line should never run.')


if __name__ == '__main__':
    # exec_coro = demo_exc_handling()
    # print(next(exec_coro))
    # print(exec_coro.send(11))
    # print(exec_coro.send(22))
    # print(exec_coro.send(33))
    # print(exec_coro.close())

    # exec_coro = demo_exc_handling()
    # next(exec_coro)
    # exec_coro.send(11)
    # exec_coro.throw(DemoException)

    exec_coro = demo_exc_handling()
    next(exec_coro)
    exec_coro.send(11)
    exec_coro.throw(ZeroDivisionError)
    exec_coro.close()
