'''
    集合论
        集合的本质是许多唯一对象的聚集，因此集合可以用于去重。
        集合中的元素必须是可散列的，set类型本身是不可散列的，但是frozenset可以。因此可以创建一个包含不同frozenset的set。
        除了保证唯一性，集合还实现了很多基础的中缀运算符。给定两个集合a和b，a | b返回合计，a & b返回交集，a - b返回差集。
    3.8.1 集合字体量
        除空集之外，集合的字面量——{1}、{1, 2}，看起来和数学形式一样。但如果是空集，那么必须写成set()形式。
        字面量句法相比构造方法要更快且更易读。像字面量，Python会利用一个专门的叫做BUILD_SET的字节码来创建集合。
    3.8.1 集合推导
        Python2.7带来的集合推导
    3.8.3 集合的操作
        中缀运算符需要两侧的被操作对象都是集合类型，但是其他的所有方法则只要参数是可迭代对象。
        setA = {1, 2, 3, 4, 5}
        setB = {5, 6, 7, 8. 9}
        setA | setB = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        setA & setB = {5}
        setA - setB = {1, 2, 3, 4}
        setA ^ setB = {1, 2, 3, 4, 6, 7, 8, 9}

'''


import collections
import dis
from unicodedata import name


if __name__ == '__main__':
    l = ['spam', 'spam', 'eggs', 'spam']
    print(set(l))
    print(list(set(l)))

    needles = set()
    haystack = set()
    print(len(needles & haystack))

    print(dis.dis('{1}'))
    print(dis.dis('set([1])'))

    print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})
    print(name('a'))
    print(name('>'))
    print([1, 2] in [0, 1, 2, 3])
    print('bc' in 'abcd')

    print(collections.MutableSet.__bases__);
    print(collections.abc.Set.__bases__)
    print(collections.abc.Collection.__bases__)

    print(dir(set))

    print({1, 2, 3, 4, 5} | {5, 6, 7, 8, 9})
    print({1, 2, 3, 4, 5} & {5, 6, 7, 8, 9})
    print({1, 2, 3, 4, 5} - {5, 6, 7, 8, 9})
    print({1, 2, 3, 4, 5} ^ {5, 6, 7, 8, 9})
