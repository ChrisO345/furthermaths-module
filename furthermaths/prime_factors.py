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
