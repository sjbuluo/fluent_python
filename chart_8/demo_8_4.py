'''
    函数的参数作为引用时
        Python唯一支持的参数传递模式是共享传参(基本类型传值，其他传内存地址)
    不要使用可变类型作为参数的默认值


'''


def f(a, b):
    a += b
    return a


class HauntedBus:

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    x = 1
    y = 2
    print(f(x, y))
    print(x, y)

    a = [1, 2]
    b = [3, 4]
    print(f(a, b))
    print(a, b)

    t = (10, 20)
    u = (30, 40)
    print(f(t, u))
    print(t, u)

    bus1 = HauntedBus()
    bus1.pick('A')
    bus2 = HauntedBus()
    print(bus2.passengers)