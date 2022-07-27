"""Fibonacci Sequence"""


def fibonacci(n):
    """
    Finds the nth fibonacci number
    :param n:
    :return:
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
