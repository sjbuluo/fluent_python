'''
    众多比较运算符
    Python解释器对众多比较运算符(==、!=、>、<、>=、<=)的处理与前文类型。不过存在重大区别。
    1.正向和反向调用使用的是同一系列方法。
    2.对==和!=来说，如果反向调用失败，Python会比较对象的ID，而不抛出TypeError。
    众多比较运算符，如果正向返回NotImplemented，则调用反向方法
    相等性     a == b          a.__eq__(b)     b.__eq__(a)     比较id(a) == id(b)
                a != b          a.__ne__(b)     b.__ne__(a)     返回not(a == b)
    排序      a > b           a.__gt__(b)     b.__lt__(a)     抛出TypeError
                a < b           a.__lt__(b)     b.__gt__(a)
                a >= b          a.__ge__(b)     b.__le__(a)
                a <= b          a.__le__(b)     a.__ge__(b)

                
'''