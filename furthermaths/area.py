"""Finds the surface area of given shape"""
from trigonometry import tan


def area_rect(w: int | float, h: int | float):
    """
    Finds the area of rectangle

    :param w: width of shape
    :param h: height of shape
    :return:
    """
    if w < 0 or h < 0:
        raise ValueError("area_rect() only accepts non-negative values")
    return w * h


def area_square(a: int | float):
    """
    Finds the area of square

    :param a: length of shape
    :return:
    """
    if a < 0:
        raise ValueError("area_square() only accepts non-negative values")
    return a**2


def area_circle(r: int | float):
    """
    Finds the area of circle
    
    :param r: radius of shape
    :return: 
    """
    if r < 0:
        raise ValueError("area_circle() only accepts non-negative values")
    return 3.141592653589793 * r**2


def area_trapezium(a: int | float, b: int | float, h: int | float):
    """
    Finds the area of trapezium

    :param a: base 1 of shape
    :param b: base 2 of shape
    :param h: height of shape
    :return:
    """
    if a < 0 or b < 0 or h < 0:
        raise ValueError("area_trapezium() only accepts non-negative values")
    return (a + b) * h / 2


def area_triangle(a: int | float, b: int | float = 0, c: int | float = 0):
    """
    Finds the area of triangle

    :param a: side 1 of shape
    :param b: side 2 of shape
    :param c: side 3 of shape
    :return:
    """
    if a < 0 or b < 0 or c < 0:
        raise ValueError("area_triangle() only accepts non-negative values")
    if b == 0:
        b, c = a
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def area_pentagon(a: int | float, b: int | float, c: int | float, d: int | float, e: int | float) -> float:
    """
    Finds the area of pentagon

    :param a: side 1 of shape
    :param b: side 2 of shape
    :param c: side 3 of shape
    :param d: side 4 of shape
    :param e: side 5 of shape
    :return:
    """
    if a < 0 or b < 0 or c < 0 or d < 0 or e < 0:
        raise ValueError("area_pentagon() only accepts non-negative values")
    s = (a + b + c + d + e) / 2
    return (s * (s - a) * (s - b) * (s - c) * (s - d) * (s - e)) ** 0.5


def area_regular_polygon(n: int, a: int | float):
    """
    Finds the area of regular polygon

    :param n: number of sides of shape
    :param a: length of shape
    :return:
    """
    if n < 0 or a < 0:
        raise ValueError("area_regular_polygon() only accepts non-negative values")
    return n * a**2 / (4 * tan(180 / n))


def area_ellipse(w: int | float, h: int | float):
    """
    Finds the area of ellipse

    :param w: width of shape
    :param h: height of shape
    :return:
    """
    if w < 0 or h < 0:
        raise ValueError("area_circle() only accepts non-negative values")
    return area_circle(w / 2) * h


def area_parallelogram(base: float, height: float) -> float:
    """
    Finds the area of parallelogram

    :param base:
    :param height:
    :return:
    """
    if base < 0 or height < 0:
        raise ValueError("area_parallelogram() only accepts non-negative values")
    return base * height


def area_rhombus(diagonal_1: float, diagonal_2: float) -> float:
    """
    Finds the area of rhombus

    :param diagonal_1:
    :param diagonal_2:
    :return:
    """
    if diagonal_1 < 0 or diagonal_2 < 0:
        raise ValueError("area_rhombus() only accepts non-negative values")
    return 1 / 2 * diagonal_1 * diagonal_2


if __name__ == '__main__':
    pass
