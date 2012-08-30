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


def main():
    for i in range(1, 21):
        if i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    _test()
