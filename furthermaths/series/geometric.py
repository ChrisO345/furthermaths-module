"""Geometric Series"""


def is_geometric(series: list) -> bool:
    """
    Checks to see if the values in a list follow a geometric progression

    :param series:
    :return:
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


def geometric(nth_term: int, start: float | int, ratio: float | int) -> list:
    """
    Finds the nth term of a geometric progression

    :param nth_term:
    :param start:
    :param ratio:
    :return:
    """
    if not isinstance(nth_term, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(ratio, (int, float)):
        raise ValueError("Ratio must be a real number")
    if nth_term < 1:
        raise ValueError("Nth term must be greater than 0")
    if ratio == 0:
        raise ValueError("Ratio cannot be 0")
    series = [start]
    for index in range(nth_term - 1):
        series.append(series[index] * ratio)
    return series
