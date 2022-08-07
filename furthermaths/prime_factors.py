"""Prime Factors"""


def prime_factors(n):
    """
    Returns a list of the prime factors of n.

    :param n:
    :return:
    """
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors


# TODO extend to n arguments
def lcm(a, b):
    """
    Returns the lowest common multiple of a and b
    :param a:
    :param b:
    :return:
    """
    _a = prime_factors(a)
    _b = prime_factors(b)
    _c = []
    for i in _a:
        _c.append(i)
        if i in _b:
            _b.remove(i)
    _c.extend(_b)
    total = 1
    for j in _c:
        total *= j
    return total


def gcd(a, b):
    """
    Returns the greatest common denominator of a and b
    :param a:
    :param b:
    :return:
    """
    _a = prime_factors(a)
    _b = prime_factors(b)
    _c = []
    for i in _a:
        if i in _b:
            _b.remove(i)
            _c.append(i)
    total = 1
    for j in _c:
        total *= j
    return total


if __name__ == '__main__':
    print(lcm(15, 10))
    print(gcd(15, 10))
