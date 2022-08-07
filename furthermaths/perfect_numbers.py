"""Perfect Numbers"""


def is_perfect(number: int) -> bool:
    """
    Checks to see if a number is a perfect number.

    :param number:
    :return:
    """
    return sum(i for i in range(1, number // 2 + 1) if number % i == 0) == number
