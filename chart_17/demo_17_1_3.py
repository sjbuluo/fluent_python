"""
期物
期物是concurrent.futures模块和asyncio包的重要组件
从Python3.4起，标准库中有两个名为Future的类：concurrent.future.Future和asyncio.Future。这两个类的作用相同：实例都表示可能已经完成或者尚未完成的延迟计算。
应该记住，通常情况下不应自己创建期物，而由并发框架(concurrent.futures或asyncio）实例化。原因是期物表示终将发生的事情，而确定某件事会发生的唯一方式是执行的时间已经排定。因此，只有排定把某件事交给concurrent.futures.Executor子类处理时，才会创建concurrent.futures.Future实例。Executor.submit()方法的参数是一个可调用的对象，调用这个方法后会为可调用对象排期，并返回一个期物。
客户端代码不应该改变期物的状态，并发框架在期物表示的延迟计算结束后会改变期物的状态，而无法控制计算合适结束。
期物都有.done()方法，不阻塞，返回值是布尔值，表明期物链接的可调用对象是否已经结束。客户端代码通常不会徐闻期物是否运行结束，而是会等待通知。一次，两个Future类都有.add_done_callback()方法，只有一个参数，类型是可调用的对象，期物运行结束后会调用指定的可调用对象。
此外还有.result方法，在期物运行结束后调用的话，这个方法在两个Future类中的作用相同：返回可调用对象的结果，或者重新抛出执行可调用的对象时抛出的异常。如果期物没有运行结束，则差异很大。concurrent.futures.Future会阻塞调用方所在的线程，知道有结果可返回。此时，result方法可以接受可选的timeout参数，如果在指定时间内期物没有运行完毕则会抛出TimeoutError异常。而asyncio则不会，asyncio获取期物的结果最好使用yield from结构。
"""

from concurrent import futures
from chart_17.demo_17_1_2 import download_one, main

def downloads_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(3) as executor:
        to_do = []
        for cc in cc_list:
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(results)
    return len(results)


if __name__ == '__main__':
    main(downloads_many)


