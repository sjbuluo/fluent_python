"""
    使用concurrent.futures模块启动进程
    ProcessPoolExecutor类把工作分配给多个Python进程处理，需要CPU密集型处理，使用这个模块能绕开GIL，利用所有可用的CPU核心。
    ProcessPoolExecutor和ThreadPoolExecutor类都实现了通用的Executor接口，因此使用concurrent。futures模块能特别轻松的把基于线程的方案转为基于进程的方案。
    对于ProcessPoolExecutor，默认使用os.cpu_count()函数返回的CPU数量，对于ThreadPoolExecutor则不做限制，最佳线程数取决于做什么事以及可用内存的大小。
    I/O密集型使用ThreadPoolExecutor
    CPU密集型使用ProcessPoolExecutor
    
"""