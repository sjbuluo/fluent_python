'''
    函数注解
        Python3提供了一种句法，用于为函数声明中的参数和返回值附加元数据。

        函数声明中的各个参数可以在:之后增加注解表达式。如果参数有默认值，注解放在参数名和=之间。如果想注解返回值，在)和函数声明末尾的:之间添加->和表达式。表达式可以是任何类型，注解中最常用的类型是类（str和int）和字符串

        注解不会做任何处理，只是存储在函数的__annotations__属性
        Python不做检查，不做强制，不做验证，换句话说，注解对Python解释器没有任何意义。注解只是元数据。

        为静态类型检查功能提供额外的类型信息
'''


def clip(text: str, max_len: 'int > 0'=80) -> str:
    ''' 在max_len前面或后面的第一个空格处截断文本'''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = max_len
    return text[:end].rstrip()


from inspect import signature


if __name__ == '__main__':
    sig = signature(clip)
    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)
