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


def lcm(*args):
    """
    Returns the lowest common multiple of values in args
    :param args:
    :return:
    """
    if len(args) == 0:
        raise ValueError("lcm() takes at least 2 arguments")
    if type(args[0]) == list:
        args = args[0]
    if len(args) == 1:
        raise ValueError("lcm() takes at least 2 arguments")
    _factors = []
    for i in args:
        _factors.append(prime_factors(i))
    types = []
    for i in _factors:
        for j in i:
            if j not in types:
                types.append(j)
    multi = []
    for i in types:
        length = 0
        for j in _factors:
            if j.count(i) > length:
                length = j.count(i)
        multi.extend([i] * length)
    total = 1
    for j in multi:
        total *= j
    return total


def gcd(*args):
    """
    Returns the greatest common denominator of values in args
    :param args:
    :return:
    """
    if len(args) == 0:
        raise ValueError("gcd() takes at least 2 arguments")
    if type(args[0]) == list:
        args = args[0]
    if len(args) == 1:
        raise ValueError("gcd() takes at least 2 arguments")
    _factors = []
    for i in args:
        _factors.append(prime_factors(i))
    multi = []
    for i in _factors[0]:
        if all(i in j for j in _factors):
            for k in range(len(_factors)):
                _factors[k].remove(i)
            multi.append(i)
    total = 1
    for j in multi:
        total *= j
    return total


if __name__ == '__main__':
    print(lcm(15, 10, 20, 60))
    print(gcd(15, 10, 20, 60, 19))
