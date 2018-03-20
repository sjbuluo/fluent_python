'''
    常见的映射方式
        dict、defaultdict、OrderedDict，后面两个数据类型是dict的变种，位于collections模块内
    用setdefault处理找不到的键
        当字典d[k]不能找到正确的键的时候，Python会抛出异常，这个行为符合Python所信奉的快速失败的哲学。可以使用d.get(k, default)来代替d[k],但是这样不自然且效率低。
'''