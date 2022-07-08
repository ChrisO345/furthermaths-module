"""Addition and Subtraction"""  # why not


def add(num, *argv):
    """
    Finds the sum of a group of real numbers

    :param num: real base number
    :param argv: all other numbers
    :return:
    """
    if not argv:
        return num
    for i in argv:
        num += i
    return num


def sub(num, *argv):
    """
    Finds the subtraction of a group of real numbers

    :param num: real base number
    :param argv: all other numbers
    :return:
    """
    if not argv:
        return num
    for i in argv:
        num -= i
    return num


if __name__ == '__main__':
    print(add(4, -4))
