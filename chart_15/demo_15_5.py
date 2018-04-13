'''
    小结
    __enter__ __exit__
    with as
    @contextlib.contextmanager
    yield
    try
    except
    finally
'''


if __name__ == '__main__':
    for i in range(2):
        pass
    else:
        print('A for 正常结束')

    for i in range(2):
        break
    else:
        print('B for 正常结束')

    i = 1
    while i < 3:
        i += 1
    else:
        print('A while 正常结束')

    i = 1
    while i < 3:
        i += 1
        break
    else:
        print('B while 正常结束')

    try:
        pass
    except BaseException:
        pass
    else:
        print('A 没有捕获异常')

    try:
        raise IndexError
    except BaseException:
        pass
    else:
        print('B 没有捕获异常')