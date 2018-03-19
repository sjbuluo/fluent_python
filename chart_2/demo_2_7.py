'''
    list.sort方法和内置函数sorted
        list.sort方法会就地排序列表，也就是不会把原列表复制一份。着也是方法返回None的原因，提醒你本方法不会新建一个列表。返回None是Python的一个惯例，如果一个函数或者方法对对象进行的是就地改动，就应该返回None。
        用返回None的一个弊端是调用者无法将其串联调用。
        与list.sort相反的是内置函数sorted，会新建一个列表作为返回值。这个方法可以接受任何的可迭代对象作为参数，甚至包括不可变序列或生成器。
        不管是list.sort方法还是sorted函数，都有两个可选的关键字参数。
        reverse
            如果被设定为True，被排序的序列里的元素会以降序输出。默认值为False
        key
            一个只有一个参数的函数，这个函数会被用在序列里的每一个元素上，所产生的结果将是排序算法依赖的对比关键字。
'''


if __name__ == '__main__':
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print(fruits)
    print(sorted(fruits))
    print(fruits)
    print(sorted(fruits, reverse=True))
    print(sorted(fruits, key=len))
    print(sorted(fruits, key=len, reverse=True))
    print(fruits)
    print(fruits.sort())
    print(fruits)