'''
    3.1 泛映射类型
        collections.abc模块中有Mapping和MutableMapping这两个抽象基类，作用是为dict和其他类似的类型定义形式接口
        非抽象映射类型一般不会直接继承这些抽象基类，会直接对dict或collections.User.Dict进行扩展。这些抽象基类的主要作用是作为形式化的文档，定义了构建一个映射类型锁需要的最基本的接口，还可以配合isinstance判断是否是广义上的映射类型。
        标准库里的所有映射类型都是利用dict来实现的，有个共同的限制，即只有可散列的数据类型才能用作这些映射里的键
        可散列的数据类型
            如果一个对象是可散列的，那么在这个对象的生命周期中，散列值是不变的，而且这个对象需要实现__hash__()方法。另外可散列对象还需要有__eq__()方法，才能跟其他键作比较。
            原子不可变数据类型(str、bytes和数值类型）都是可散列类型。frozenset也是可散列的，根据其定义，frozenset里只能容纳可散列类型。元组的话，只有一个元组包含的所有元素都是可散列类型的情况下，才是可散列的。
        一般用户自定义的类型的对象都是可散列的，散列值就是id()函数返回值，所以所有对象在比较的时候都是不相等的。如果一个对象实现了__eq__()方法，并且在方法中用到这个对象的内部状态的话，那么只有当所有这些内部状态都是不可变的情况下，这个对象才是可散列的。
'''



import collections



class Test:
    pass


if __name__ == '__main__':
    my_dict ={}
    print(isinstance(my_dict, collections.abc.Mapping))

    tt = (1, 2, (10, 20))
    print(hash(tt))
    tl = (1, 2, [10, 20])
    #print(hash(tl))
    tf = (1, 2, frozenset([30, 40]))
    print(hash(tf))

    t = Test()
    print(id(t))

    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    print(a == b == c == d == e)