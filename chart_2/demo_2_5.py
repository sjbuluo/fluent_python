'''
    Python默认序列是支持+、*操作的。通常+号两侧的序列由相同的数据所构成，在拼接的过程中，两个操作的序列都不会被修改。Python会新建一个包含同样类型数据的序列来作为拼接的结果。

'''


if __name__ == '__main__':
    l = [1, 2, 3]
    print(l * 5)
    print(5 * 'abcdefg')
    print([[]] * 3)
    a = []
    print([a] * 3)

    board = [['-'] * 3 for i in range(3)]
    print(board)
    board[1][2] = 'X'
    print(board)
    weired_board = [['-'] * 3] * 3
    print(weired_board)
    weired_board[1][2] = 'O'
    print(weired_board)

    row = ['_'] * 3
    board = []
    for i in range(3):
        board.append(row)
    print(board)
    board[1][1] = 'X'
    print(board)

    row = []
    board = []
    for i in range(3):
        row = ['-'] * 3
        board.append(row)
    print(board)
    board[1][1] = 'X'
    print(board)