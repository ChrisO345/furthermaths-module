"""Square Root"""


def fx(x: float, a: float) -> float:
    return x**2 - a


def fx_derivative(x: float) -> float:
    return 2 * x


def get_initial_point(a: float) -> float:
    start = 2.0

    while start <= a:
        start = start**2

    return start


def sqrt(a: float, max_iter: int = 9999, tolerance: float = 0.00000000000001) -> float:
    """
    Finds the square root

    :param a:
    :param max_iter:
    :param tolerance:
    :return:
    """

    if a < 0:
        raise ValueError("math domain error")
    elif a == 0:
        return 0

    value = get_initial_point(a)

    for i in range(max_iter):
        prev_value = value
        value = value - fx(value, a) / fx_derivative(value)
        if abs(prev_value - value) < tolerance:
            return value

    return value


if __name__ == '__main__':
    print(sqrt(0))
    print(sqrt(1))
    print(sqrt(2))
    print(sqrt(3))
    print()
    print(sqrt(0.1))
    print(sqrt(0.01))
    print(sqrt(0.001))
    print(sqrt(0.0001))
    print(sqrt(0.00001))
    print(sqrt(0.000001))
    print(sqrt(0.0000001))
