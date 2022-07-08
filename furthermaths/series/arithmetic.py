"""Arithmetic Series"""


def is_arithmetic(series: list) -> bool:
    """
    Checks to see if the values in a list follow an arithmetic progression

    :param series:
    :return:
    """
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [2, 4, 6]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    if len(series) == 1:
        return True
    common_diff = series[1] - series[0]
    for index in range(len(series) - 1):
        if series[index + 1] - series[index] != common_diff:
            return False
    return True


def arithmetic(nth_term: int, start: float | int, diff: float | int) -> list:
    """
    Finds the nth term of an arithmetic progression

    :param nth_term:
    :param start:
    :param diff:
    :return:
    """
    if not isinstance(nth_term, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(diff, (int, float)):
        raise ValueError("Difference must be a real number")
    if nth_term < 1:
        raise ValueError("Nth term must be greater than 0")
    if diff == 0:
        raise ValueError("Difference cannot be 0")
    series = [start]
    for index in range(nth_term - 1):
        series.append(series[index] + diff)
    return series


if __name__ == '__main__':
    print(is_arithmetic([2, 4, 6, 8]))
