'''
    对于创建自定义映射类型而言，以UserDict为基类，总比以普通dict为基类方便。
    更倾向于UserDict而不是从dict继承的主要原因是，后者有时会在某些方法的实现上走一些捷径，导致不得不在子类中重写这些方法。
    值得注意的是，UserDict并不是dict的子类，但是UserDict有一个叫做data的属性，是dict的实例，这个属性实际上是UserDict最终存储数据的地方。
    因为UserDict继承的是MutableMapping，所以StrKeyDict里剩下的映射类型方法都是从UserDict、MutableMapping和Mapping这些超类继承而来的。特别是Mapping类，虽然是一个抽象基类，但却提供了一些很用的方法
    MutableMapping.update
    这个方法不但可以直接利用，还可以用在__init__里，让构造方法可以利用传入的各种参数(其他映射类型、元素时(key，value)对的可迭代对象和键值参数来新建实例。这个方法实际上是在使用self[key] = value来添加新值的，其实调用的是__setitem__方法。
    Mapping.get
    
'''


import collections


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


if __name__ == '__main__':
    pass