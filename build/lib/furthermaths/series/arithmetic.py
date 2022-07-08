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


if __name__ == '__main__':
    print(is_arithmetic([2, 4, 6, 8]))
