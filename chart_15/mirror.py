'''
    测试上下文管理
'''


from array import array
import random
import itertools


class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


if __name__ == '__main__':
    arr = array('d', [random.randint(1, 100) for i in itertools.repeat(1, times=100)])
    with open('numbers.txt', 'wb') as fb:
        arr.tofile(fb)

    from_file_arr = array('d')
    with open('numbers.txt', 'rb') as fb:
         from_file_arr.fromfile(fb, 100)
    print(from_file_arr)