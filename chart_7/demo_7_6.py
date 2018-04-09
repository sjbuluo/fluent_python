'''
    nonLocal声明
        def make_average():
            count = 0
            total = 0

            def average(new_value);
                count += 1
                total += new_value
                return total / count
            return average
        count += 1 等价于count = count + 1 因此count被视为本地变量
        对于数字、字符串、元组等不可变类型而言，只能读取不能更新，如果尝试重新绑定，会隐式创建局部变量，则不再是自由变量，不会保存在闭包里。
        因此引入了nonlocal，不保存为局部变量处理。
'''


__part_name__ = 'nonlocal声明'


from dis import dis


def make_averger():
    count = 0
    total = 0

    def averger(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averger


if __name__ == '__main__':
   dis(make_averger)