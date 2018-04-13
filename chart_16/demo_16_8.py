'''
    yield from的意义
    1.子生成器产出的值都直接传给委派生成器的调用方
    2.使用send()方法发给委派生成器的值都直接传给子生成器。如果发送的值时None，那么会调用子生成器的__next__()方法，如果发送的不是None，则会调用子生成器的send()方法。如果调用的方法抛出StopIteration异常，那么委派生成器恢复运行。任何其他异常都会向上冒泡，传给委派生成器。
    3.生成器退出时，生成器(或子生成器)中的return expr表达式会触发StopIteration(expr)异常抛出
    4.yield from表达式的值时子生成器终止时传给StopIteration异常的第一个参数
    5.传入委派生成器的异常，除了GeneratorExit之外都传给子生成器的throw()方法。如果调用throw()方法时抛出StopIteration异常，委派生成器恢复运行。StopIteration之外的异常会向上冒泡，传给委派生成器。
    6.如果把GeneratorExit异常传入委派生成器，或者在委派生成器上调用close()方法，那么在子生成器上调用close()方法，如果有的话。如果调用close()方法导致异常爬出，则向上冒泡，否则，委派生成器抛出GeneratorExit异常。
    
'''