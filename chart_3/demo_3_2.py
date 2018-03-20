'''
    Python2.7以来，列表推导和生成器表达式的概念就移植到了字典上，从而有了字典推导。字典推导可以从任何以键值对作为元素的可迭代对象中构建出字典。
'''


DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]


if __name__ == '__main__':
    country_code = {country: code for code, country in DIAL_CODES}
    print(country_code)
    print({code: country.upper() for country, code in country_code.items() if code < 65})
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    chars = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh']
    d = {num: char.lower() for num in nums
                    for char in chars
                    if num < 5}
                    #else num: char.upper()}
    print(d)
    t = 'UPPER' if 5 > 6 else 'LOWER'
    print(t)
    d = {num: char for num in range(1, 10)
         for char in ['a']
         if num < 5}
    print(d)