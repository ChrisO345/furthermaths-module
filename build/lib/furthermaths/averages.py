"""Measures of Averages"""


def mean(x: list):
    """
    Returns the sum of a list divided by its quantity

    :param x: a list of real numbers
    :return:
    """
    num = len(x)
    total = 0
    for i in x:
        if type(i) not in [int, float]:
            print(type(i))
            raise ValueError("mean() must be a sequence of numbers")
        total += i
    if total % num == 0:
        return int(total / num)
    return total / num


def mode(x: list):
    """
    Returns the most popular number in a list

    :param x: a list of real numbers
    :return:
    """
    weight = 0
    value = []
    for item in x:
        _ = x.count(item)
        if item in value:
            continue
        if _ > weight:
            value.clear()
            value.append(item)
            weight = _
        elif _ == weight:
            value.append(item)
    return value if len(value) > 1 else value[0]


def diff(x: list):
    """
    Finds the range between the smallest and largest

    :param x: a sequence of real numbers
    :return:
    """
    if len(x) == 0:
        raise ValueError("diff() must be a sequence of numbers")
    return max(x) - min(x)


def median(x: list):
    """
    Finds the middle value of the sequence

    :param x:
    :return:
    """
    n = len(x)
    mid = n // 2
    x.sort()
    if n % 2 != 0:
        return x[mid]
    return sum(x[mid - 1:mid + 1]) / 2


def lq(x: list):
    """
    Finds the lower quartile of a sequence

    :param x: a sequence of real numbers
    :return:
    """
    x.sort()
    x = x[0:len(x) // 2]
    n = len(x)
    mid = n // 2
    if n % 2 != 0:
        return x[mid]
    return sum(x[mid - 1:mid + 1]) / 2


def uq(x: list):
    """
    Finds the upper quartile of a sequence

    :param x: a sequence of real numbers
    :return:
    """
    x.sort()
    if len(x) % 2 != 0:
        x = x[len(x) // 2 + 1::]
    else:
        x = x[len(x) // 2::]
    n = len(x)
    mid = n // 2
    if n % 2 != 0:
        return x[mid]
    return sum(x[mid - 1:mid + 1]) / 2


def irq(x: list):
    """
    Finds the interquartile range of a sequence

    :param x: a sequence of real numbers
    :return:
    """
    return uq(x) - lq(x)


if __name__ == '__main__':
    print(mean([5, 6, 7, 8]))
    print(mode([1, 1, 2, 2, 3, 3, 3, 4]))
    print(diff([4, 8, 3, 7, 10]))
    print(median([1, 3, 4, 5, 6, 2, 7]))
    print(lq([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(uq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(irq([1, 2, 3, 4, 5, 6, 7, 8]))

