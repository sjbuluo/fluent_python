import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

card_score = {'方块': 0, '梅花': 1, '红桃': 2, '黑桃': 3}


def order_card(card):
    card_num = FrenchDeck.ranks.index(card.rank)
    return card_num * len(card_score) + card_score[card.suit]


class FrenchDeck:

    ranks = [str(i) for i in range(1, 11)] + list('JQKA')

    suits = '方块 梅花 红桃 黑桃'.split(' ')

    def __init__(self):
        self.__index = 0
        self.__cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position):
        return self.__cards[position]

    def __next__(self):
        result = self.__cards[self.__index]
        self.__index += 1
        return result


if __name__ == '__main__':
    poker = FrenchDeck()
    for card in poker:
        print(card)

    for card in poker[:3]:
        print(card)

    for card in poker[11::13]:
        print(card)

    for card in sorted(poker, key=order_card):
        print(card)

    print(next(poker))
    print(next(poker))
    print(next(poker))
    print(next(poker))
    print(next(poker))

    l1 = [i for i in range(1, 11)]
    l2 = [i for i in range(101, 111)]
    l = l1 + l2
    print(l)
