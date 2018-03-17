'''
    在Python中，像列表(list)、元组(tuple)和字符串(str)这类序列类型都支持切片操作
    2.4.1 切片和区间忽略最后一个元素
        当只有最后一个位置信息时，可以快速看出切片和区间里有几个元素：range(3)和my_list[:3]都返回3个元素
        当起止位置信息都可见时，可以快速计算出切片和区间的长度，用后一个数减去第一个下标(stop-start)即可
        可以利用任意一个下标把序列分割成不重叠的两部分，只要写成my_list[:x]和my_list[x:]就可以了

    2.4.2 可以用s[a:b:c]的形式对s在a和b之间以c为间隔取值。c的值可以为负，负值意味着反向取值
        a:b:c这种用法只能作为索引坐着下标用在[]中来返回一个切片对象:slice(a, b, c)。对seq[start:stop:step]进行求值的时候，Python会调用seq.__getitem__(seq(a, b, c))
    2.4.3 多维切片和省略
        []运算符里还可以使用以逗号分开的多个索引或者是切片
    2.4.4 给切片赋值
        如果

'''


import numpy


if __name__ == '__main__':
    l = [10, 20, 30, 40, 50, 60]
    print(l[:2])
    print(l[2:])
    print(l[:3])
    print(l[3:])
    s = 'bicycle'
    print(s[::3])
    print(s[::-1])
    print(s[::-2])

    print(s[1:5:2])
    print(s.__getitem__(slice(1, 5, 2)))

    l = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], ['A', 'B', 'C', 'D', 'E']]
    arr = numpy.ndarray((2, 2, 2, 2))
    #print(arr)
    #print(arr[0, ...])

    l = list(range(10))
    print(l)
    l[2:5] = [20, 30]
    print(l)
    del l[5:7]
    print(l)
    l[3::2] = [11, 22]
    print(l)
    l[2:5] = 100
    print(l)