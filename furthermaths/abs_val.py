"""Absolute Value Functions"""


def abs_val(num):
    """
    Find the absolute value of a number

    :param num: real number
    :return:
    """
    return -num if num < 0 else num


def abs_max(x: list):
    """
    Find the number with the largest deviant from zero

    :param x: array of real numbers
    :return:
    """
    if len(x) == 0:
        raise ValueError("abs_max() arg is an empty sequence")
    j = x[0]
    for i in x:
        if abs(i) > abs(j):
            j = i
    return j


def abs_max_sort(x: list):
    """
    Sort a list based of a number's deviance from zero

    :param x: array of real numbers
    :return:
    """
    y: list[int] = x
    if len(y) == 0:
        raise ValueError("abs_max_sort() arg is an empty sequence")
    return sorted(x, key=abs)


def abs_min(x: list):
    """
    Find the number with the smallest deviant from zero

    :param x: array of real numbers
    :return:
    """
    if len(x) == 0:
        raise ValueError("abs_min() arg is an empty sequence")
    j = x[0]
    for i in x:
        if abs(i) < abs(j):
            j = i
    return j


def abs_min_sort(x: list):
    """
    Sort a list based of the inverse of a number's deviance from zero

    :param x: array of real numbers
    :return:
    """
    if len(x) == 0:
        raise ValueError("abs_min_sort() arg is an empty sequence")
    return sorted(x, key=abs, reverse=True)


if __name__ == '__main__':
    print(abs_max_sort([0, 10, -20, -60, -2]))
    print(abs_min_sort([0, 10, -20, -60, -2]))
    print(abs_max([-34, 10, -20, -60, -2]))
    print(abs_min([-34, 10, -20, -60, -2]))
