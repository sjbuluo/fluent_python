'''
    定义并使用一个抽象基类
        import abc
        @abc.abstractmethod 抽象方法

    11,7,1 抽象基类句法详解
        声明抽象基类最简单的方式是继承abc.ABC或其他抽象基类
        然而，abc.ABC是Python3.4新增的类，旧版需要使用metaclass=abc.ABCMeta
        Python3引入的metaclass Python2需要在类中__metaclass__ = abc.ABCMeta
        abc还定义了装饰器
        1.@abstractclassmethod
        2.@abstractstaticmethod
        3.@abstractproperty

    11.7.2 定义Tombola抽象基类的子类
        

'''


import abc


class Tombola(abc.ABC):

    @abc.abstractclassmethod
    def load(self, iterable):
        '''从可迭代对象中添加元素'''

    @abc.abstractclassmethod
    def pick(self):
        '''随机删除元素，然后将其返回'''

    def loaded(self):
        '''如果至少有一个元素，返回True，否则返回False'''
        return bool(self.inspect())

    def inspect(self):
        '''返回一个有序元组，由当前元素构成'''
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))