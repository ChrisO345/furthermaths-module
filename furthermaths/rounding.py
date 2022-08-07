"""Simple Rounding Functions"""


def floor(x):
    """
    Return the largest integer less than or equal to x

    :param x:
    :return:
    """
    return int(x)


def ceiling(x):
    """
    Return the largest integer greater than or equal to x

    :param x:
    :return:
    """
    if int(x) == x:
        return x
    return int(x) + 1
