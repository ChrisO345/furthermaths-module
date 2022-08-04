"""Extra Equality Functions"""


def almost_equals(a, b, diff=1e-5):
    """
    Returns whether a value and another are almost equal

    :param a:
    :param b:
    :param diff:
    :return:
    """
    return abs(a - b) <= diff


if __name__ == "__main__":
    print(almost_equals(3.1415926, 3.141))
