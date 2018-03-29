'''
    字符问题

'''


if __name__ == '__main__':
    s = 'café'
    print(len(s))
    b = s.encode('utf8')
    print(b)
    print(len(b))
    print(b.decode('utf8'))