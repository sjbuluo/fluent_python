'''
    格式化显示
        内置的format()函数和str.format()方法把各个类型的格式化凡是委托给相应的.__format__(format_spec)方法。
        format(my_obj, format_spec)
        str.format() {}里带环字段中冒号后面的部分

        如果没有定义__format__方法，从object继承的方法会返回str(my_object)
'''


_part_name = '格式化显示'


from datetime import datetime


class Test:

    def __format__(self, format_spec):
        return format_spec.replace('%P', 'NEWBEE')


if __name__ == '__main__':
    brl = 1 / 2.43
    print(brl)
    print(format(brl, '0.4f'))
    print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

    print(format(42, 'b'))
    print(format(42, 'x'))
    print(format(2 /3, '.1%'))

    now = datetime.now()
    print(format(now, '%H:%M:%S'))
    print('It\'s now {:%I:%M %p}'.format(now))

    t = Test()
    print(format(t, '%P'))