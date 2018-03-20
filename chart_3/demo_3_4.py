'''
    映射的弹性键查询
        某个键在映射中不存在，也希望通过这个键读取值的时候能得到一个默认值。
        1.使用defaultdict类
        2.自定义一个dict的子类，并在子类中实现__missing__方法
    3.4.1 defaultdict: 处理找不到键的选择
        collections.defaultdict在创建时，需要配置一个找不到键创造默认值的方法
        比如 dd = defaultdict(list)，如果键在dd中不存在的时候
        1.调用list()方法来建立一个新列表
        2.把这个新列表作为值，new-key作为键，存入dd
        3.返回这个列表的引用
        而这个用来生成默认值的可调用对象存放在名为default_factory的实例属性中
        defaultdict中的default_factory只会在__getitem__里被调用，在其他方法里完全不会发挥作用 dd[k]会返回default_factory结果，而.get(key)则返回None
        这一切背后的功臣其实是特殊方法__missing__。会在defaultdict遇到找不到的键时调用default_factory,而实际上这个特性是所有映射类型都可以选择去支持的。
    3.4.2 特殊方法__missing__
        所有映射类型在处理找不到的键时，都会牵扯到__missing__方法。如果一个类继承自dict，同时提供了__missing__方法，那么在__getitem__碰到找不到键的时候，Python就会自动调用它，而不是抛出一个KeyError异常。


'''


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __get__(self, key, default):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d['2'])
    print(d[4])
   # print(d[1])
    print(d.get('2'))
    print(d.get(4))
   # print(d.get(1))
    print(2 in d)
    print('4' in d)
    print(1 in d)