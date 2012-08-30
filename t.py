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
FizzBuzz
16
17
Fizz
19
Buzz
"""


class PositiveInteger(object):
    def __init__(self):
        self.i = int(self != self)  # zero

    def succ(self):
        self.i += int(self == self)  # add one

    def double(self):
        self.i += self.i

    def dividable(self, by):
        v = self.i % by.i
        return v == -v  # mean: v == 0

    def __str__(self):
        return str(self.i)


class PositiveIntegerRange(object):
    def __init__(self, frm, to):
        end = to
        end.succ()
        assert end.i > frm.i
        self.value = range(frm.i, end.i)

    def __iter__(self):
        return iter(self.value)


def get_one():
    ret = PositiveInteger()
    ret.succ()
    return ret


def get_three():
    ret = PositiveInteger()
    ret.succ()
    ret.succ()
    ret.succ()
    return ret


def get_five():
    ret = PositiveInteger()
    ret.succ()
    ret.succ()
    ret.succ()
    ret.succ()
    ret.succ()
    return ret


def get_twenty():
    ret = get_five()
    ret.double()
    ret.double()
    return ret


def print_(s):
    print s
    return s


def foo(i):
    d3 = i.dividable(get_three())
    d5 = i.dividable(get_five())
    (d3 and d5 and print_("FizzBuzz") or
     d3 and print_("Fizz") or
     d5 and print_("Buzz") or
     print_(i))


def succ_and_foo(i):
    i.succ()
    foo(i)


def main():
    i = PositiveInteger()
    range = PositiveIntegerRange(get_one(), get_twenty())
    for _i in range: succ_and_foo(i)


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    _test()
