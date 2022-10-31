"""Geometric Series"""


def is_geometric(series: list) -> bool:
    """
    Checks to see if the values in a list follow a geometric progression

    :param series: Geaometric progression
    :return: True if the values follow an geomtric progression, False otherwise
    """
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [2, 3, 5]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    if len(series) == 1:
        return True
    common_ratio = series[1] / series[0]
    for index in range(len(series) - 1):
        if series[index + 1] / series[index] != common_ratio:
            return False
    return True


def geometric(n: int, start: float | int, ratio: float | int) -> list:
    """
    Finds the nth term of a geometric progression

    :param n: The number of terms in the series
    :param start: The first term in the series
    :param ratio: Common ratio of two consecutive term of progression
    :return: Geometric progression
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(ratio, (int, float)):
        raise ValueError("Ratio must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    if ratio == 0 or ratio == 1:
        raise ValueError("Ratio of geometric progression cannot be 0 or 1")
    series = [start]
    for index in range(n - 1):
        series.append(series[index] * ratio)
    return series

def geometric_sum(n: int, start: float | int, ratio: float | int) -> float:
    """
    Finds the sum of an geometric progression

    :param n: The number of terms in the series
    :param start: The first term in the series
    :param ratio: Common ratio of two consecutive term of progression
    :return: The sum of the series
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(ratio, (int, float)):
        raise ValueError("Ratio must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    if ratio == 0 or ratio == 1:
        raise ValueError("Ratio of geometric progression cannot be 0 or 1")
    return start * ((pow(ratio, n) - 1) / (ratio - 1))

def geometric_nth_term(n: int, start: float | int, ratio: float | int) -> float:
    """
    Finds the nth term of an geometric progression

    :param n: Index of the term to find
    :param start: The first term in the series
    :param ratio: Common ratio of two consecutive term of progression
    :return: The nth term of the series
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(ratio, (int, float)):
        raise ValueError("Ratio must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    if ratio == 0 or ratio == 1:
        raise ValueError("Ratio of geometric progression cannot be 0 or 1")
    return start * pow(ratio, n - 1)

def geometric_first_term(n: int, end: float | int, ratio: float | int) -> float:
    """
    Finds the first term of an geometric progression

    :param n: The number of terms in the series
    :param end: The last term in the series
    :param ratio: Common ratio of two consecutive term of progression
    :return: The first term of the series
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(end, (int, float)):
        raise ValueError("End term must be a real number")
    if not isinstance(ratio, (int, float)):
        raise ValueError("Ratio must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    if ratio == 0 or ratio == 1:
        raise ValueError("Ratio of geometric progression cannot be 0 or 1")
    return end / pow(ratio, n - 1)

def geometric_ratio(n: int, start: float | int, end: float | int) -> float:
    """
    Finds the ratio between each term of an geometric progression

    :param n: The number of terms in the series
    :param start: The first term in the series
    :param end: The last term in the series
    :return: The ratio between each term of the series
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(end, (int, float)):
        raise ValueError("End term must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    return pow((end / start), n - 1)