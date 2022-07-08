"""Trigonometric Functions"""
from factorial import factorial
from angle_units import radians
from square_root import sqrt


def sin(deg: float, accuracy: int = 18, rounded_values_count: int = 10) -> float:
    """
    Gives the sine of the angle in degrees

    :param deg:
    :param accuracy:
    :param rounded_values_count:
    :return:
    """
    deg = deg - ((deg // 360.0) * 360.0)
    rad = radians(deg)
    result = rad
    a = 3
    b = -1
    for _ in range(accuracy):
        result += (b * (rad ** a)) / factorial(a)
        b = -b
        a += 2
    return round(result, rounded_values_count)


def cos(deg: float, accuracy: int = 18, rounded_values_count: int = 10) -> float:
    """
    Gives the cosine of the angle in degrees

    :param deg:
    :param accuracy:
    :param rounded_values_count:
    :return:
    """
    sine = sin(deg, accuracy, rounded_values_count)
    sine = sine ** 2
    sine = 1 - sine
    return round(sqrt(sine), rounded_values_count)


def tan(deg: float, accuracy: int = 18, rounded_values_count: int = 10) -> float:
    """


    :param deg:
    :param accuracy:
    :param rounded_values_count:
    :return:
    """
    if (deg - 90) % 180 == 0:
        raise ValueError()
    sine = sin(deg, accuracy, rounded_values_count)
    cosine = cos(deg, accuracy, rounded_values_count)
    return round(sine/cosine, rounded_values_count)


if __name__ == '__main__':
    print(sin(90))
    print(cos(90))
    # print(tan(90))
    print()
    print(sin(30))
    print(cos(30))
    print(tan(30))
