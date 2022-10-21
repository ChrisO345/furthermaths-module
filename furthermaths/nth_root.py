"""nth Root"""


def root(n, p=2) -> float:
    """
    Finds the nth root of a number

    :param n: number
    :param p: power n is raised to
    :return:
    """
    return n ** (1 / p)
