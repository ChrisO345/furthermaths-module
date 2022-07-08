"""Degrees Radians Gradians"""
tau = 6.28318530718


def degrees(x, source="rad"):
    """
    Converts Radians and Gradians into degrees

    :param x: a real number
    :param source: either rad or grad
    :return:
    """
    if source == "rad":
        return (x * 360) / tau
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
        return (x * tau) / 360
    elif source == "grad":
        return (x * tau) / 400
    raise SyntaxError()


def gradians(x, source="deg"):
    """
    Converts Radians and Gradians into degrees

    :param x: a real number
    :param source: either rad or grad
    :return:
    """
    if source == "rad":
        return (x * 400) / tau
    elif source == "deg":
        return (x * 400) / 360
    raise SyntaxError()

