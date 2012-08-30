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


def holder(x):
    return lambda f: f(x)


def get_zero():
    """
    >>> get_zero()(lambda x: x)
    0
    """
    zero = int(int != int)
    return holder(zero)


def succ(x):
    """
    >>> get_zero()(succ)
    1
    """
    one = int(int == int)
    return x + one


def double(x):
    """
    >>> holder(get_zero()(succ))(double)
    2
    """
    return x + x


def get_one():
    """
    >>> get_one()(lambda x: x)
    1
    """
    ret = get_zero()
    return holder(ret(succ))


def get_two():
    """
    >>> get_two()(lambda x: x)
    2
    """
    ret = get_one()
    return holder(ret(double))


def get_three():
    """
    >>> get_three()(lambda x: x)
    3
    """
    ret = get_two()
    return holder(ret(succ))


def get_five():
    """
    >>> get_five()(lambda x: x)
    5
    """
    ret = get_two()
    ret = holder(ret(double))
    return holder(ret(succ))


def get_twenty():
    """
    >>> get_twenty()(lambda x: x)
    20
    """
    ret = get_five()
    ret = holder(ret(double))
    return holder(ret(double))


def positiveIntegerRange(frm, to):
    end = holder(to(succ))
    # assert end.i > frm.i
    value = frm(lambda x: end(lambda y: range(x, y)))
    return iter(value)


def print_(s):
    print s
    return s


def equal_zero(i):
    return i == -i


def dividable(by):
    return lambda i: by(lambda j: equal_zero(i % j))


def foo(i):
    d3 = i(dividable(get_three()))
    d5 = i(dividable(get_five()))
    d3 and d5 and print_("FizzBuzz") or \
    d3 and print_("Fizz") or \
    d5 and print_("Buzz") or \
    i(print_)


def succ_and_foo(old_i):
    global i
    i = holder(old_i(succ))
    foo(i)


def main():
    global i
    i = get_zero()
    range = positiveIntegerRange(get_one(), get_twenty())
    [succ_and_foo(i) for _i in range]


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    _test()
