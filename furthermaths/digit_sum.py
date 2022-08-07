"""Sum of Digits in a number"""


def sum_digits(number: int) -> int:
    """
    Returns the sum of the digits in a number.

    :param number:
    :return:
    """
    return sum(int(i) for i in str(number))
