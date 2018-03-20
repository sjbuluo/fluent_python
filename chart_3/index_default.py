'''
    创建一个从单词到其出现情况的映射
'''


import sys
import re
import collections


WORD_RE = re.compile(r'\w+')


if __name__ == '__main__':
    index = collections.defaultdict(list)
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                index[word].append((line_no, column_no))
    for word, location in index.items():
        print(word, location)
