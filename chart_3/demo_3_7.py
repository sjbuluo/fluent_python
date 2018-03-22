'''
    标准库里所有的映射类型都是可变的，但有时有特殊需求。
    从Python3.3开始，types模块中引入了一个封装类名叫MappingProxyType。如果给这个类一个映射，它会返回一个只读的映射视图。虽然是只读视图，但是它是动态的。这意味着如果对原始映射做出改动，可以通过这个视图观察到，但是无法直接修改这个视图。
'''


from types import MappingProxyType


if __name__ == '__main__':
    d = {1: 'A'}
    d_proxy = MappingProxyType(d)
    print(d_proxy)
    print(d_proxy[1])
    # d_proxy[2] = 'x'
    d[2] = 'B'
    print(d_proxy)
    print(d_proxy[2])