"""Perms and Combs"""


def perm(n, r):
    """
    Finds the nth permutation of r elements

    :param n:
    :param r:
    :return:
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(r, int):
        raise ValueError("r must be an integer")
    if r < 0:
        raise ValueError("r must be a positive integer")
    if n == 0:
        return 1
    if n == 1:
        return r
    return n * perm(n-1, r)


def comb(n, r):
    """
    Finds the nth combination of r elements

    :param n:
    :param r:
    :return:
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(r, int):
        raise ValueError("r must be an integer")
    if r < 0:
        raise ValueError("r must be a positive integer")
    if n == 0:
        return 1
    if n == 1:
        return r
    return n * comb(n-1, r) / r
