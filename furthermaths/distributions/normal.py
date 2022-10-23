"""Normal Distribution"""


def normal(mu: int or float, variance: int or float, x: int or float) -> float:
    """
    :param mu: mean of the data
    :param variance: variance of the data
    :returns: -> the value of Normal Probability Distribution Function at given "x".
              -> The value of p.d.f depends on "x", "mu", "variance" and "sd"
    """
    if variance < 0:
        raise ValueError("variance must be a positive number")
    sd = variance ** 0.5  # standard deviation
    e = 2.71828182846
    pi = 3.14159265359
    return (1/(variance*2*pi) ** 0.5) * e ** (-0.5 * (x-mu/sd)**2)


def zscore(mu: int or float, variance: int or float, x: int or float) -> float:
    """
    :param mu: mean of the data
    :param variance: variance of the data
    :param x: datapoint for which Z-score is to be calculated
    :return: the Z-score for the corresponding "x"
    """
    if variance < 0:
        raise ValueError("variance must be a positive number")
    sd = variance**0.5
    return (x - mu)/sd


if __name__ == "__main__":
    print(normal(3.3, 9.99, 3))
    print(zscore(3.3, 9.99, 3))
