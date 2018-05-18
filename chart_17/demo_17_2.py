"""
    阻塞型I/O和GIL
    CPython解释器本身就不是线程安全的，因此有全局解释器锁(GIL)，一次只允许一个线程执行Python字节码。因此，一个Python进程通常不能同时使用多个CPU核心。
    然而，标准库中所有执行阻塞型I/O操作的函数，在等待操作系统返回结果时都会释放GIL。这意味着在Python语言这个层次上可以使用多线程，而I/O密集型Python程序能从中受益，一个Python线程等待网络响应时，阻塞型I/O函数会释放GIL，再运行一个线程。
    
"""