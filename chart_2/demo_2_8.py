'''
    用bisect来管理已排序的序列
        bisect模块包含两个主要函数，bisect和insort，两个函数都利用二分查找算法来在有序序列中查找或插入元素。
    用bisect来搜索
        bisect(haystack, needle)在haystack里搜索needle的位置，该位置满足的条件是，把needle插入这个位置之后，haystack还能保持升序，也就是在说这个函数返回的位置前面的值都小于等于needle的值。其中haystack必须是一个有序的序列。可以用bisect(haystack, needle)查找位置index，再用haystack.insert(index, needel)来插入新值。也可以用insort一次完成，速度还比较快。
    用insort出入数据
        bisect和insort方法都有两个可选参数lo和li作为限制范围，lo默认为0 hi默认为长度
'''


import bisect
import sys
import random


HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 6, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}      {2}{0:<2d}'


def demo(bisect_fn):
    for needle in NEEDLES:
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' |'
        print(ROW_FMT.format(needle, position, offset))


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


SIZE = 7


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO: ', bisect_fn.__name__)
    print('haystack -> ', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

    random.seed(1729)
    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE * 3)
        bisect.insort(my_list, new_item)
        print('%2d -> ' % new_item, my_list)
