'''
    函数内省
        使用dir函数可以探知对象具有的属性
        __dict__
            存储用户属性
        函数比普通对象多的属性
        __annotations__     dict                参数和返回值的注解
        __call__            method-wrapper      实现()运算符；即可调用对象协议
        __closure__         tuple               函数闭包，即自由变量的绑定(通常是None)
        __code__            code                编译成字节码的函数元数据和函数定义体
        __defaults__        tuple               形式参数的默认值
        __get__             method-wrapper      实现只读描述符协议
        __globals__         dict                函数所在模块中的全局变量
        __kwdefaults__      dict                仅限关键字形式参数的默认值
        __name__            str                 函数名称
        __qualname__        str                 函数的限定名称

'''


if __name__ == '__main__':
    class C:
        pass
    obj = C()


    def func():
        pass
    print(sorted(set(dir(func)) - set(dir(obj))))