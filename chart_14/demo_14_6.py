'''
    Sentence类第五版：生成器表达式

    生成器表达式可以理解为列表推导的惰性版本，不会迫切地构建列表，而是返回一个生成器，按需惰性生成元素。
'''


import re
import reprlib


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        return (match.gorup for match in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    res1 = [x * 3 for x in gen_AB()]
    for i in res1:
        print('--->', i)
    res2 = (x * 3 for x in gen_AB())
    print(res2)
    for i in res2:
        print('--->', i)