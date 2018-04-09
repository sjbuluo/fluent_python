'''
    闭包
        闭包至延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体重定义的非全局变量。

        闭包使得本地变量变为自由变量：指未在本地作用域绑定的变量。闭包会延伸到函数的作用域之外，包含自由变量的绑定。

        闭包返回的函数对象的__code__属性中保存局部变量和自由变量的名称
            xxx.__code__.co_varnames
            xxx.__code__.co_freevars
            xxx.__closure__ (对应__code__.co_freevars中的每一个名称,这些元素都是cell对象，有cell_contents属性，保存着真正的值。)
        闭包是一种函数，会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义作用域不可用，但仍然可以使用这些绑定。
'''


__part_name__ = '闭包'


from dis import dis


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    local_var = None
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager


if __name__ == '__main__':
    avg = Averager()
    print(avg(10.0))
    print(avg(11.0))
    print(avg(12.0))

    avg = make_averager()
    print(avg(10.0))
    print(avg(11.0))
    print(avg(12.0))

    dis(make_averager)
    print(avg.__code__.co_varnames)
    print(avg.__closure__)
    print(avg.__code__.co_freevars)
    for c in avg.__closure__:
        print(c.cell_contents)

