'''
    匿名函数
        lambda关键字在Python表达式内创建匿名函数
        然而，Python简单的句法限制了lambda函数的定义体只能使用纯表达式。lambda函数的定义体内不能赋值，也不能使用while和try等Python语句。
        参数列表中最适合使用匿名函数
        除了作为参数传给高阶函数之外，Python很少使用匿名函数。
        
'''


if __name__ == '__main__':
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=lambda fruit: fruit[::-1]))
