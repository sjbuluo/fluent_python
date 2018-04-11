import doctest

from chart_11 import demo_11_7, bingo, lotto, tomboList


TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} - {2}'


def main(argv):
    verbose = '-v' in argv
    real_subclasses = demo_11_7.Tombola.__subclasses__()
    virtual_subclasses = list(demo_11_7.Tombola._abc_registry)

    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)


def test(cls, verbose=False):
    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))


if __name__ == '__main__':
    import sys
    main(sys.argv)
    # print(demo_11_7.Tombola.__subclasses__())