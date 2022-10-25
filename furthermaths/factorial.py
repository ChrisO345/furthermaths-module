"""Factorial Functions"""
from .eratosthenes import eratosthenes_primes


def factorial(n) -> int:
    """
    finds the factorial of n -> n!

    :param n: any real positive integer
    :return:
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("factorial() must be a positive integer")
    elif n == 0:
        return 1
    return n * factorial(n-1)


def double_factorial(n) -> int:
    """
    finds the double factorial of n -> n!!

    :param n: any real positive integer
    :return:
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("double_factorial() must be a positive integer")
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    return n * double_factorial(n-2)


def nth_factorial(n, k) -> int:
    """
    finds the nth factorial of n -> n!k

    :param n: any real positive integer
    :param k: any real positive integer
    :return:
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("nth_factorial() must be a positive integer")
    elif type(k) != int or k < 0:
        raise ValueError("nth_factorial() must be a positive integer")
    elif n == 0:
        return 1
    elif n < k:
        return k
    return n * nth_factorial(n-k, k)


def subfactorial(n) -> int:
    """
    Finds the subfactorial of n -> !n

    :param n:
    :return:
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("subfactorial() must be a positive integer")
    elif n == 0 or n == 1:
        return 0
    nums = range(2, n+1)
    a = 1
    total = 0
    for i in nums:
        total += a * (1 / factorial(i))
        a = -a
    return int(factorial(n) * total)


def primorial(n) -> int:
    """
    Finds the primorial of n -> n#
    multiplication of primes

    :param n:
    :return:
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("primorial() must be a positive integer")
    if n <= 1:
        return n
    primes = eratosthenes_primes(n)
    total = 1
    for i in primes:
        total *= i
    return total


def exponential_factorial(n) -> int:
    """
    Finds the exponential factorial

    :param n:
    :return:
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("exponential_factorial() must be a positive integer")
    elif n == 0:
        return 1
    return n ** exponential_factorial(n-1)


def hyper_factorial(n) -> int:
    """
    Finds the hyper factorial

    :param n:
    :return:
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("hyper_factorial() must be a positive integer")
    elif n == 0:
        return 1
    return n**n * hyper_factorial(n-1)


if __name__ == '__main__':
    print(nth_factorial(9, 3))
    print(subfactorial(4))
    print(exponential_factorial(4))
    print(hyper_factorial(4))
    print(primorial(7))
