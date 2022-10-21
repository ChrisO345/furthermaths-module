"""Logarithm Functions -> approximation functions"""


def log10(x):
    """
    Returns the base 10 logarithm of x.

    :param x: The value to find the logarithm of.
    :return: The base 10 logarithm of x.
    """
    pass


def log2(x):
    """
    Returns the base 2 logarithm of x.

    :param x: The value to find the logarithm of.
    :return: The base 2 logarithm of x.
    """
    pass


def log3(x):
    """
    Returns the base 3 logarithm of x.

    :param x: The value to find the logarithm of.
    :return: The base 3 logarithm of x.
    """
    pass


def log(x, b):
    """
    Returns the base b logarithm of x.

    :param x: The value to find the logarithm of.
    :param b: The base of the logarithm.
    :return: The base b logarithm of x.
    """
    if b == 0:
        return 1

    end = x

    prev = 0

    accuracy = 1

    e = 0.0000001
    while True:
        start = prev + accuracy
        _curr = b ** start

        if _curr >= end:
            error = _curr - end
        else:
            error = end - _curr

        if error <= e:
            return start

        if _curr > end:
            accuracy /= 10
        else:
            prev = start


def ln(x):
    """
    Returns the natural logarithm of x.

    :param x: The value to find the logarithm of.
    :return: The natural logarithm of x.
    """
    pass


def log_e(x):
    """
    Returns the logarithm of e.

    :param x: The value to find the logarithm of.
    :return: The logarithm of e.
    """
    return ln(x)


# TODO complete these functions
if __name__ == '__main__':
    print(log(32, 2))
    print(log(100, 10))
    print(log(2937846, 3))
    print(log(0.5, 6))
