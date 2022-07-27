"""Hexagonal Numbers"""


def hexagonal_numbers(n: int, multiple: bool = False):
    """
    Finds the nth hexagonal number

    :param n:
    :param multiple:
    :return:
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a positive integer")
    if multiple:
        return [hexagonal_numbers(index) for index in range(1, n+1)]
    return n * (2 * n - 1)


if __name__ == '__main__':
    print(hexagonal_numbers(5, True))
