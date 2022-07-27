"""Finds the surface area of given shape"""
from trigonometry import tan


def area_rect(w: int | float, h: int | float):
    """
    Finds the area of rectangle

    :param w: width of shape
    :param h: height of shape
    :return:
    """
    return w * h


def area_square(a: int | float):
    """
    Finds the area of square

    :param a: length of shape
    :return:
    """
    return a**2


def area_circle(r: int | float):
    from .constants import pi
    """
    Finds the area of circle
    
    :param r: radius of shape
    :return: 
    """
    return pi * r**2


def area_trapezium(a: int | float, b: int | float, h: int | float):
    """
    Finds the area of trapezium

    :param a: base 1 of shape
    :param b: base 2 of shape
    :param h: height of shape
    :return:
    """
    return (a + b) * h / 2


def area_triangle(a: int | float, b: int | float = 0, c: int | float = 0):
    """
    Finds the area of triangle

    :param a: side 1 of shape
    :param b: side 2 of shape
    :param c: side 3 of shape
    :return:
    """
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
    s = (a + b + c + d + e) / 2
    return (s * (s - a) * (s - b) * (s - c) * (s - d) * (s - e)) ** 0.5


def area_regular_polygon(n: int, a: int | float):
    """
    Finds the area of regular polygon

    :param n: number of sides of shape
    :param a: length of shape
    :return:
    """
    return n * a**2 / (4 * tan(180 / n))


def area_ellipse(w: int | float, h: int | float):
    """
    Finds the area of ellipse

    :param w: width of shape
    :param h: height of shape
    :return:
    """
    return area_circle(w / 2) * h


if __name__ == '__main__':
    pass
