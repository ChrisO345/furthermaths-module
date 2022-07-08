"""nth Root"""


def root(n, p=2):
    """
    Finds the nth root of a number

    :param n:
    :param p:
    :return:
    """
    start = 0
    end = n

    e = 0.0000001
    while True:

        mid = (start + end) / 2
        if n > mid**p:
            error = n - mid ** p
        else:
            error = mid ** p - n

        if error <= e:
            return mid

        if mid ** p > n:
            end = mid

        else:
            start = mid
