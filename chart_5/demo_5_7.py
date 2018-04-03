'''
    从定位参数到仅限关键字参数
        Python最好的特性之一是提供了即为灵活的参数处理机制，而且Python3进一步提供了仅限关键字参数(keyword-only argument)
'''


from inspect import signature


def tag(name, *content, cls=None, **attrs):
    '''生成一个或多个HTML标签'''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    print(tag('img', cls=None, src='www.xxx.com'))
    print(tag('span', 'Hello World', cls='col-4', style='color:red'))


    sig = signature(tag)
    my_rag = {
        'name': 'img',
        'title': 'Sunset Boulevard',
        'src': 'sunset.jpg',
        'cls': 'framed'
    }
    bound_args = sig.bind(**my_rag)
    print(type(bound_args))
    print(str(bound_args))
    print(bound_args)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)