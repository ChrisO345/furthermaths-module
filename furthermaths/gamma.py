"""Gamma Function"""

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

def gamma(n):
    """
    Returns the gamma function of n.

    :param n: The value to find the gamma function of (non-complex/positive whole number)
    :return: The gamma function of n.
    """
    if n > 0 and isinstance(n, int): #checks if the number is positive and whole
        return factorial(n-1)
    
if __name__ == '__main__':
    print(gamma(5))
    print(gamma(11))
    print(gamma(25))
