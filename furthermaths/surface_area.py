"""Surface Area of 3d shapes"""


def surface_cuboid(w: int | float, h: int | float, d: int | float) -> float:
    """
    Finds the surface area of a cuboid

    :param w: width of shape
    :param h: height of shape
    :param d: depth of shape
    :return:
    """
    return 2 * (w * h + w * d + h * d)


def surface_cylinder(r: int | float, h: int | float) -> float:
    from .constants import pi
    """
    Finds the surface area of a cylinder
    
    :param r: radius of shape
    :param h: height of shape
    :return: 
    """
    return 2 * pi * r * h + 2 * pi * r**2


def surface_cube(a: int | float) -> float:
    """
    Finds the surface area of a cube

    :param a: length of shape
    :return:
    """
    return 6 * a**2


def surface_sphere(r: int | float) -> float:
    from .constants import pi
    """
    Finds the surface area of a sphere
    
    :param r: radius of shape
    :return: 
    """
    return 4 * pi * r**2


def surface_pyramid_square(a: int | float, h: int | float) -> float:
    """
    Finds the surface area of a square pyramid

    :param a: length of shape
    :param h: perpendicular height of shape
    :return:
    """
    return a**2 + 4 * a * h / 2


def surface_pyramid_triangle(a: int | float, h: int | float) -> float:
    """
    Finds the surface area of a square pyramid

    :param a: length of shape
    :param h: perpendicular height of shape
    :return:
    """
    return 4 * a * h / 2


# TODO: function for a nth based pyramid, nth based prism, ovular cylinder, cone, ovular cone, ovular torus, torus,
#  nth based cylinder, nth based polygon


if __name__ == '__main__':
    pass
