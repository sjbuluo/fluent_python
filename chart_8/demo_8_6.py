'''
    弱引用
        因为引用，对象才会在内存中存在，当对象的引用数量归零后，垃圾回收程序会把对象销毁。但是，有时需要引用对象，而不让对象存在的时间超过所需时间。常用于缓存。
        弱引用不会增加对象的引用数量，引用的目标对象称为所指对象，因此弱引用不会妨碍对象被当做垃圾回收。
        weakref.ref实例获取所指对象,如果对象存在，调用弱引用可以获取对象，否则返回None。
        weakref.ref是低层接口，不要自己使用，而是使用weakref集合和finalize
    8.6.1 WeakValueDictionary简介
        WeakValueDictionary类实现的是一种可变映射，里面的值是对象的弱引用。被引用的对象在程序中的其他地方呗当做垃圾回收之后，对应的键会自动从WeakValueDictionary中删除，常用于缓存。
        与WeakValueDictionary对应的是WeakKeyDictionary，后者的键时弱引用。（可以为应用中其他部分拥有的对象附加数据，这样就无需为对象添加属性）
        还提供WeakSet类，保存元素弱引用的集合类。
    8.6.2 弱引用的局限
        不是每个Python对象都可以作为弱引用的目标。基本的list和dict实例不能作为所指对象，但子类可以解决。
        


'''


__part_name__ = '弱引用'


import weakref


class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


if __name__ == '__main__':
    # a_set = {0, 1}
    # wref = weakref.ref(a_set)
    # print(wref)
    # print(wref())
    # a_ser = {2, 3, 4}
    # print(wref())
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # print(wref() is None)
    # while wref() is not None:
    #     print(wref() is None)

    stock = weakref.WeakValueDictionary()
    catalog = [Cheese('R'), Cheese('T'), Cheese('B'), Cheese('P')]
    for cheese in catalog:
        stock[cheese.kind] = cheese
    print(sorted(stock.keys()))
    del catalog
    print(sorted(stock.keys()))
    del cheese
    print(sorted(stock.keys()))