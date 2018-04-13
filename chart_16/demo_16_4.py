'''
    预激协程的装饰器

    使用yield from句法调用协程时，会自动预激。
    Python3.4标准库里的asyncio,coroutine装饰器不会预激协程
'''


from functools import wraps
import inspect


def coroutine(func):
    @wraps(func)
    def primer(*args, **kw):
        gen = func(*args, **kw)
        next(gen)
        return gen
    return primer


@coroutine
def distance_avg():
    total = 0
    count = 0
    avg = None
    while True:
        term = yield avg
        total += term
        count += 1
        avg = total / count


if __name__ == '__main__':
    try:
        da = distance_avg()
        print(inspect.getgeneratorstate(da))
        for i in range(10, 21):
            print(inspect.getgeneratorstate(da))
            print(da.send(i))
    except StopIteration:
        pass
    finally:
        if da:
            da.close()

    print(locals())