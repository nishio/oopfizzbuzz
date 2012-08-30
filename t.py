"""
>>> main()
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz
16
17
Fizz
19
Buzz
"""


class PositiveInteger(object):
    def __init__(self, i):
        assert i > 0
        self.i = i

    def dividable(self, by):
        return self.i % by == 0

    def __str__(self):
        return str(self.i)


def foo(i):
    if i.dividable(3):
        print "Fizz"
        return
    if i.dividable(5):
        print "Buzz"
        return
    print i


def main():
    for i in range(1, 21):
        foo(PositiveInteger(i))


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    _test()
