'''
    Vector第二版：可切片序列
        切片slice是内置类型
        dir(slice)得知slice有start stop step indices()
        indices(有迭代对象长度) 会将start stop step都转为正整数 方便使用
'''


import array
import math
import reprlib
import numbers


class Vector:
    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array.array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return '{}({})'.format(type(self).__name__, components)

    def __str__(self):
        return str(tuple(self))

    def __abs__(self):
        return math.sqrt(x * x for x in self)

    def __bool__(self):
        return abs(self)

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    @classmethod
    def frombytes(cls, octets):
        typecode= chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        if isinstance(item, numbers.Integral):
            return self._components[item]

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut_names.find(item)
            if 0 <= pos < len(cls.shortcut_names):
                return self._components[pos]
        raise AttributeError('{.__name__!r}object has no attribute {!r}'.format(cls, item))

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = 'can\'t set attributes \'a\' to \'z\' in {cls_name!r}'
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        super().__setattr__(key, value)



if __name__ == '__main__':
    v1 = Vector([3, 4, 5])
    print(v1)
    print(repr(v1))
    print(bytes(v1))
    print(len(v1))
    print(v1[0], v1[-1])
    v7 = Vector(range(7))
    print(v7[1:4])

    print(v7.x)
    v1.aa = 'a'
    v1.x = 1