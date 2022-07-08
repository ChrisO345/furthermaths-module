"""Degrees Radians Gradians"""
import constants


def degrees(x, source="rad"):
    """
    Converts Radians and Gradians into degrees

    :param x: a real number
    :param source: either rad or grad
    :return:
    """
    if source == "rad":
        return (x * 360) / constants.tau
    elif source == "grad":
        return (x * 360) / 400
    raise SyntaxError()


def radians(x, source="deg"):
    """
    Converts Radians and Gradians into degrees

    :param x: a real number
    :param source: either rad or grad
    :return:
    """
    if source == "deg":
        return (x * constants.tau) / 360
    elif source == "grad":
        return (x * constants.tau) / 400
    raise SyntaxError()


def gradians(x, source="deg"):
    """
    Converts Radians and Gradians into degrees

    :param x: a real number
    :param source: either rad or grad
    :return:
    """
    if source == "rad":
        return (x * 400) / constants.tau
    elif source == "deg":
        return (x * 400) / 360
    raise SyntaxError()

