'''
    变量作用域规则
        Python的设计选择，不要求声明变量（如Javascript中的var)，但是假定在函数定义体中赋值的变量是局部变量而不是全局变量。
        Javascript如果在函数体中不使用变量声明为局部变量，会在不知情的情况下获取全局变量，此时操作可能会影响整个环境。

        如果在函数中赋值时想让解释器把b当成全局变量，要使用global关键字声明
        dis.dis(func_name) 对方法进行反编译获得字节码
        一些常见的字节码:
            LOAD_GLOBAL 获取全局名称 可能是方法、类、变量、模块
            LOAD_FAST 获取本地名称
            CALL_FUNCTION 执行函数
            POP_TOP 执行栈弹出栈顶
            LOAD_CONST 加载常量
            STORE_FAST 保存本地变量
            STORE_GLOBAL 保存全局变量
            RETURN_VALUE 函数返回(没有显示return会默认return None)
'''


__part_name__ = '变量作用域规则'


from dis import dis


def f1(a):
    print(a)
    print(b)


def f2(a):
    print(a)
    print(b)
    b = 9


def f3(a):
    global b
    print(a)
    print(b)
    b = 9


if __name__ == '__main__':
    b = 6
    f1(3)
    dis('f2(3)')
    #f2(3)
    f3(3)
    print(b)
    dis('f1(3)')
    dis('f3(3)')
    dis(f1)
    dis(f2)
    dis(f3)