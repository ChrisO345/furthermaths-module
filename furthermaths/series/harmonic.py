"""Harmonic Series"""  # what is a harmonic progression?


def is_harmonic(series: list) -> bool:
    """
    Checks to see if the values in a list follow a harmonic progression

    :param series:
    :return
    """
    if not isinstance(series, list):
        raise ValueError("Input series is not valid, valid series - [1, 2/3, 2]")
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    if len(series) == 1 and series[0] != 0:
        return True
    rec_series = []
    for index in range(len(series)):
        if series[index] == 0:
            raise ValueError("Input series cannot contain 0 as an element")
        rec_series.append(1 / series[index])
    common_diff = rec_series[1] - rec_series[0]
    for index in range(len(rec_series) - 1):
        if rec_series[index + 1] - rec_series[index] != common_diff:
            return False
    return True


def harmonic(nth_term: int) -> list:  # what does this even mean?
    """
    Finds the nth term of a harmonic progression

    :param nth_term:
    :return
    """
    if nth_term == "":
        return []
    series: list = []
    for temp in range(int(nth_term)):
        series.append(f"1/{temp + 1}" if series else "1")
    return series


if __name__ == '__main__':
    print(harmonic(5))
