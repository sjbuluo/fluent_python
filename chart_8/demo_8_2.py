'''
    标识、相等性和别名
        a is b 比较的是a、b的id值（id()函数返回，在CPython中返回的是内存地址，不同解释器可能不同，但一定是唯一的数值标注，且在对象的生命周期中绝对不会改变。
    8.2.1 在==和is之间选择
        ==常用 而is一般被用于变量和单例值之间比较，最常见的就是xx is None
        is运算符比==速度快，因为is不能重载，而==则是调用__eq__方法。
    8.2.2 元组的相对不可变性
        元组保存的物理内容不变
'''


__part_name__ = '标识、相等性和别名'


if __name__ == '__main__':
    charles = { 'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    print(lewis is charles)
    print(id(charles), id(lewis))
    lewis['balance'] = 950
    print(charles)
    print(type(charles))
    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    print(charles == alex)
    print(charles is alex)
