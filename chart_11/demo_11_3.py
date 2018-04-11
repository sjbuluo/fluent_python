'''
    使用猴子补丁在运行时实现协议
        random.shuffle(iterable) 实现序列的无序化
        可以在运行中给对象赋值
            def setCard(self, pos, card):
                self._cards[pos] = card
            frenchDeck.__setitem__ = setCard
        这种运行时修改类或模块，而不改动源码的叫做猴子补丁
'''


import collections
import random


Card = collections.namedtuple('Card', 'num icon')


class FrenchDeck:

    nums = list(range(2, 11)) + list('JQKA')
    icons = '方片 梅花 红桃 黑桃'.split()

    def __init__(self):
        self._cards = [Card(num, icon)
                        for num in self.nums
                        for icon in self.icons]

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return str(self._cards)


if __name__ == '__main__':
    fd = FrenchDeck()
    for card in fd:
        print(card)
    print(fd[1:])
    print(fd[:-1])
    print(fd[::2])
    print(fd)
    random.shuffle(fd)
    print(fd)
