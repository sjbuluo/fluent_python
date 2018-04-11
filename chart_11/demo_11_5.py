'''
    定义抽象基类的子类
        (bisect二分查找)
'''


import collections


Card = collections.namedtuple('Card', 'rank suit')


class FrenchDeck(collections.MutableSequence):
    ranks = [str(rank) for rank in range(2, 11)] + list('JQKA')
    suits = '方片 梅花 红桃 黑桃'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                        for rank in self.ranks
                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, index, value):
        self._cards.insert(index, value)


if __name__ == '__main__':
    collections.MutableSequence()