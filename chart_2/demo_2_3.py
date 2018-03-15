'''
    有些地方把元组称为“不可变列表”，然而这并没有完全概括元组的特点。除了用作不可变的列表，还可以用于没有字段名的记录。

    元组其实是对数据的记录， 元组中的每个远古三都存放了记录中的一个字段的数据，外加这个字段的位置。正是这个位置信息给数据赋予了意义。
'''

from collections import namedtuple

if __name__ == '__main__':
    lax_coordinates = (33.9425, -118.408056)
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for country, code in traveler_ids:
        print('%s/%s' % (country, code))
    for passport, _ in sorted(traveler_ids):
        print(passport)

    latitude, longitude = lax_coordinates
    print(latitude)
    print(longitude)
    a = 1
    b = 2
    b, a = a, b # 优雅的写法 不使用中间变量交换两个变量的值
    # 还可以使用*运算符把一个可迭代对象拆开作为函数的参数
    divmod(20, 8)
    t = (20, 8)
    print(divmod(*t))
    quotient, remainder = divmod(*t)
    print(quotient)
    print(remainder)

    a, b, *rest = range(5)
    print(a, b, rest)
    a, b, *rest = range(2)
    print(a, b, rest)

    # 在Python中，函数用*args来获取不确定数量的参数算是一种经典写法。
    # 在Python3中，这个概念被扩展到了平行赋值中，*前缀只能用在一个变量名前面，但是这个变量可以出现在赋值表达式的任意位置。
    a, *body, b = range(1, 10)
    print(a, body, b)
    # 元组拆包还可以应用在嵌套结构中

    # collections.namedtuple是一个工厂函数，可以用来构建一个带字段名的元组和一个有名字的类
    # 用namedtuple构建的类的实例所消耗的内存跟元组是一样的，因为字段名都被存在对应的类里面。这个实例跟普通的对象实例比起来也要小一些，因为Python不会用__dict__来存放这些实例的属性。

    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', '36.933', (35.689722, 139.691667))
    print(tokyo)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo[1])

    # 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可以是有数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串
    # 可以通过字段名或者位置来获取一个字段的信息
    # 除了普通元组哪里继承来的属性之外，具名元组还有一些自己专有的属性 _fields _make(iterable) _asdict
    print(City._fields)
    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data)
    print(delhi._asdict())
    # _fields 属性是一个包含这个类所有字段名称的元组
    # _make()通过接受一个可迭代对象来生成这个类的一个实例 作用跟City(*delhi_data)是一样的
    # _asdict()把具名元组以collections.OrderedDict的形式返回

    # 作为不可变列表的元组
    # 除了跟增减元素相关的方法之外，元组支持列表的其他所有方法，除了__reversed__方法，但这个方法只是个优化而已，revere(my_tuple)这个用法在没有__reversed__的情况下也是合法的。
    # 列表或元组的方法和属性
