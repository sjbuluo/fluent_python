"""
    使用concurrent.futures模块下载
    concurrent.futures模块的主要特色是ThreadPoolExecutor和ProcessPoolExecutor类，这两个类实现的接口能分别在不同的线程或进程中执行可调用的对象。这两个类在内部维护一个工作线程或进程池，以及要执行的任务队列。不过，这个接口抽象的层级很高么无需关系实现细节。

"""

import os
import sys
import time

from concurrent import futures

import requests


POP20_CC = ('CC IN US ID BR PK NG BD RU JP MX PH VN ET DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'

MAX_WORKER = 20


def save_flag(image, filename):
    path = os.path.join(DEST_DIR, filename)
    if not os.path.exists(DEST_DIR):
        os.mkdir(DEST_DIR)
    with open(path, 'wb') as fp:
        fp.write(image)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc = cc.lower())
    response = requests.get(url)
    return response.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc + '.gif')
    return cc


def download_many(cc_list):
    worker = min(MAX_WORKER, len(cc_list))
    with futures.ThreadPoolExecutor(worker) as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\nFLAG {} used {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)