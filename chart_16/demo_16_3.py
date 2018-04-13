'''
    示例：使用协程计算移动平均值
        必须预激活协程(即第一次需要next())
        之后才能使用gen.send(xxx)来使用协程
'''


import inspect


def distance_avg():
    total = 0
    count = 0
    while True:
        forward = yield total / (count if count != 0 else 1)
        total += forward
        count += 1


if __name__ == '__main__':
    print(1 / 0 if 0 != 0 else 1)
    try:
        da = distance_avg()
        print(inspect.getgeneratorstate(da))
        next(da)
        print(inspect.getgeneratorstate(da))
        for i in range(10, 21):
            print('平均距离:', da.send(i))
    except StopIteration:
        print('结束')
    finally:
        da.close()

