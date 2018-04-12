'''
    子类化内置类型很麻烦
        Python2.2之前，内置类型（如list、dict）不能子类化。Python2.2之后可以子类化，但是内置类型（使用C语言编写）不会调用用户定义的类覆盖的特殊方法。
        例如：dict的子类覆盖__getitem__方法不会被内置类型的get()方法调用
        原生类型的这种行为违背了面向对象编程的一个基本原则：始终应该从实例(self)所属的类开始搜索方法，即使在超类实现的类中调用也一样。__missing__方法始终获得预期结果（特例）
        不只实例内部的调用有问题，内置类型的方法调用其他类的方法，也不会被调用。

        直接子类化内置类型容易出错，因为内置类型的方法通常会忽略用户覆盖的方法，不要子类化内置类型。应该继承自collections模块中的类，例如UserDict、UserList、UserString。

'''


import collections


class MyDict(dict):

    def __getitem__(self, item):
        return 'Hello World'


class DoppelDict(dict):

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class AnswerDict(dict):

    def __getitem__(self, item):
        return 42


class DoppelDict2(collections.UserDict):

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class AnswerDict2(collections.UserDict):

    def __getitem__(self, item):
        return 42


if __name__ == '__main__':
    mydict = MyDict()
    print(mydict['a'])
    print(mydict.get('a'))

    dd = DoppelDict(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)

    ad = AnswerDict(a='foo')
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)

    dd = DoppelDict2(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)

    ad = AnswerDict2(a='foo')
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)
