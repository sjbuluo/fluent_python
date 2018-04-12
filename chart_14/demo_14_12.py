'''
    深入分析iter函数

        Python中迭代对象x时会调用iter()

        iter函数还有一个鲜为人知的用法 传入两个参数
        第一个参数必须是可调用对象，用于不断调用产出各种值，第二个值是哨符，标记值，当可调用对象返回这个值时，触发迭代器抛出StopIteration异常

'''


import random


def d6():
    return random.randint(1, 6)


if __name__ == '__main__':
    d6_iter = iter(d6, 1)
    for i in d6_iter:
        print(i)