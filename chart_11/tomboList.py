from random import randrange

from chart_11 import demo_11_7


@demo_11_7.Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


if __name__ == '__main__':
    print(issubclass(TomboList, demo_11_7.Tombola))
    tl = TomboList([randrange(n + 1) for n in range(100)])
    print(tl)
    print(tl.pick())
    print(tl)
    print(tl.inspect())
    print(tl)
    print(isinstance(tl, demo_11_7.Tombola))
