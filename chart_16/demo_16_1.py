'''
    生成器如何进化成协程
        yield关键字可以在表达式中使用，而且生成器API中增加了.send(value)方法。生成器的调用方可以使用.send(...)方法发送数据，发送的数据会成为生成器函数中yield表达式的值。
        除了.send()方法，还添加了.throw()和.close()方法 前者作用是让调用方抛出异常，在生成器中处理，后者的作用是终止生成器
        
'''