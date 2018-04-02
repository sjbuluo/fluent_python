'''
    把函数视为对象
        函数是fucntion类的一个实例
'''


def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial.__doc__)