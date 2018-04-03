'''
    函数属性用途
'''


def clip(text, max_len=80):
    '''在max_len前面或后面的第一个空格处截断文本'''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


from inspect import signature


if __name__ == '__main__':
    sig = signature(clip)
    print(type(sig))
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
