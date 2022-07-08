"""Factorial Functions"""


def factorial(n) -> int:
    """
    finds the factorial of n -> n!

    :param n: any real positive integer
    :return:
    """
    if type(n) != int or n < 0:
        raise ValueError("factorial() must be a positive integer")
    elif n == 0:
        return 1
    return n * factorial(n-1)
