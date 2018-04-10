'''
    默认做浅复制
        复制列表最简单的方式是使用内置的类型构造方法。

    为任意对象做深复制和浅复制
        copy模块中的 copy()和deepcopy()方法
        深复制不是一件简单的事，如果有循环引用，就会进入无限循环。deepcopy函数会记住已经复制的对象，因此能优雅地处理循环引用。
        可以实现特殊方法__copy__()和__deepcopy__()，控制copy和deepcopy的行为。
'''


__part_name__ = '默认浅复制'


import copy


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = list(l1)
    print(l2)
    print(l1 == l2)
    print(l1 is l2)
    print(l1[1] is l2[1])

    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = list(l1)
    l1.append(100)
    l1[1].remove(55)
    print('l1', l1)
    print('l2', l2)
    l2[1] += [33, 22]
    l2[2] += (10, 11)
    print('l1', l1)
    print('l2', l2)

    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))
    bus1.drop('Bill')
    print(bus2.passengers)
    print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
    print(bus3.passengers)

    a = [10, 20]
    b = [a, 30]
    a.append(b)
    print(a)
    c = copy.deepcopy(a)
    print(c)

