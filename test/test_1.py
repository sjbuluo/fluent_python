'''
    1.移动圆盘
    2.杨辉三角形
'''

def func_1(count, nameA = 'A', nameB = 'B', nameC = 'C'):
    if count == 0:
        return
    func_1(count-1, nameA, nameC, nameB)
    print(nameA, '->', nameC)
    func_1(count-1, nameB, nameA, nameC)


def func_2(max=20):
    arr = [1]
    for x in range(max):
        yield arr
        arr.append(0)
        arr = [arr[i - 1] + arr[i] for i in range(len(arr))]


if __name__ == '__main__':
    func_1(1)
    print('------------------')
    func_1(2)
    print('------------------')
    func_1(3)
    print('------------------')
    func_1(4)

    for arr in func_2():
        print(arr)
