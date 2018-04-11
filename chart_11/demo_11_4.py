'''
    为了让抽象基类识别子类，甚至无需注册
    抽象基类的本质就是几个特殊方法
'''


from collections import abc


class Struggle:

    def __len__(self):
        return 23


if __name__ == '__main__':
    print(isinstance(Struggle(), abc.Sized))