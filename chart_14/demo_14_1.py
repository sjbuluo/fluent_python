'''
    Sentence类第一版：单词序列

    序列可迭代的原因：iter函数
        解释器需要迭代对象x时，会自动调用iter(x)。
        内置的iter函数作用：
        1.检查对象是否实现__iter__方法，如果实现了就调用，获取一个迭代器
        2.如果没有实现__iter__方法，但是实现了__getitem__方法，Python会创建一个迭代器，尝试按顺序（默认从索引0开始）获取元素
        3.如果尝试失败，则抛出TypeError异常。

        任何Python序列都可迭代的原因是，都实现了__getitem__方法。其实，标准序列也都实现了__iter__方法，也应该这么做。之所以对__getitem__方法做特殊处理，是为了向后兼容。

        鸭子理论中，需要实现__iter__和__getitem__方法
        白鹅理论中，只需要实现__iter__方法，abc.Iterable类实现了__subclasshook__方法，根据__iter__方法判断

        Python3.4开始，检查对象x能否迭代，最准确的方法是，调用iter(x)函数，如果不可迭代，在处理TypeError异常。这比使用isinstance更准确。iter(x)函数会考虑遗留的__getitem__方法，而collections.abc.Iterable不会考虑
'''


import re
import reprlib
from collections import abc


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return '{0}({1})'.format(type(self).__name__, reprlib.repr(self.text))


class Foo:

    def __iter__(self):
        pass


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)

    foo = Foo()
    print(isinstance(foo, abc.Iterable))