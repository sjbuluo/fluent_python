'''
    用户定义的可调用类型
        任何Python对象都可以表现得像函数，只需要实现实例方法__call__

'''


import random


class BingoCase:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCase')

    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCase(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))