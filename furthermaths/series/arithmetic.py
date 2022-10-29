"""Arithmetic Series"""


def is_arithmetic(series: list) -> bool:
    """
    Checks to see if the values in a list follow an arithmetic progression

    :param series: The list of values to check
    :return: True if the values follow an arithmetic progression, False otherwise
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


def arithmetic(n: int, start: float | int, diff: float | int) -> list:
    """
    Finds the nth term of an arithmetic progression

    :param n: The number of terms in the series
    :param start: The first term in the series
    :param diff: The difference between each term
    :return: Arithmetic progression
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(diff, (int, float)):
        raise ValueError("Difference must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    series = [start]
    for index in range(n - 1):
        series.append(series[index] + diff)
    return series

def arithmetic_sum(n: int, start: float | int, diff: float | int) -> float:
    """
    Finds the sum of an arithmetic progression

    :param n: The number of terms in the series
    :param start: The first term in the series
    :param diff: The difference between each term
    :return: The sum of the series
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(diff, (int, float)):
        raise ValueError("Difference must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    return (n / 2) * ((2 * start )+ (n - 1) * diff)

def arithmetic_nth_term(n: int, start: float | int, diff: float | int) -> float:
    """
    Finds the nth term of an arithmetic progression

    :param n: Index of the term to find
    :param start: The first term in the series
    :param diff: The difference between each term
    :return: The nth term of the series
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(diff, (int, float)):
        raise ValueError("Difference must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    return start + (n - 1) * diff

def arithmetic_first_term(n: int, end: float | int, diff: float | int) -> float:
    """
    Finds the first term of an arithmetic progression

    :param n: The number of terms in the series
    :param end: The last term in the series
    :param diff: The difference between each term
    :return: The first term of the series
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(end, (int, float)):
        raise ValueError("End term must be a real number")
    if not isinstance(diff, (int, float)):
        raise ValueError("Difference must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    return end - (n - 1) * diff

def arithmetic_difference(n: int, start: float | int, end: float | int) -> float:
    """
    Finds the difference between each term of an arithmetic progression

    :param n: The number of terms in the series
    :param start: The first term in the series
    :param end: The last term in the series
    :return: The difference between each term of the series
    """
    if not isinstance(n, int):
        raise ValueError("Nth term must be an integer")
    if not isinstance(start, (int, float)):
        raise ValueError("Start term must be a real number")
    if not isinstance(end, (int, float)):
        raise ValueError("End term must be a real number")
    if n < 1:
        raise ValueError("Nth term must be greater than 0")
    return (end - start) / (n - 1)

if __name__ == '__main__':
    print(is_arithmetic([2, 4, 6, 8]))
    print(arithmetic_sum(10, 1, 1))
