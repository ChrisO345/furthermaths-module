"""Eratosthenes' sieve."""


def eratosthenes_primes(n):
    """
    Finds all the primes up until n

    :param n:
    :return:
    """
    multiples = []
    primes = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return primes


if __name__ == '__main__':
    print(eratosthenes_primes(100))
