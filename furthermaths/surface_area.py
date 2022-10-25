"""Surface Area of 3d shapes"""


def surface_area_cuboid(w: int | float, h: int | float, d: int | float) -> float:
    """
    Finds the surface area of a cuboid

    :param w: width of shape
    :param h: height of shape
    :param d: depth of shape
    :return:
    """
    if w < 0 or h < 0 or d < 0:
        raise ValueError("surface_area_cuboid() only accepts non-negative values")
    return 2 * (w * h + w * d + h * d)


def surface_area_cylinder(r: int | float, h: int | float) -> float:
    """
    Finds the surface area of a cylinder
    
    :param r: radius of shape
    :param h: height of shape
    :return: 
    """
    if r < 0 or h < 0:
        raise ValueError("surface_area_cylinder() only accepts non-negative values")
    return 2 * 3.141592653589793 * r * h + 2 * 3.141592653589793 * r**2


def surface_area_cube(a: int | float) -> float:
    """
    Finds the surface area of a cube

    :param a: length of shape
    :return:
    """
    if a < 0:
        raise ValueError("surface_area_cube() only accepts non-negative values")
    return 6 * a**2


def surface_area_sphere(r: int | float) -> float:
    """
    Finds the surface area of a sphere
    
    :param r: radius of shape
    :return: 
    """
    if r < 0:
        raise ValueError("surface_area_sphere() only accepts non-negative values")
    return 4 * 3.141592653589793 * r**2


def surface_area_pyramid_square(a: int | float, h: int | float) -> float:
    """
    Finds the surface area of a square pyramid

    :param a: length of shape
    :param h: perpendicular height of shape
    :return:
    """
    if a < 0 or h < 0:
        raise ValueError("surface_area_pyramid_square() only accepts non-negative values")
    return a**2 + 4 * a * h / 2


def surface_area_pyramid_triangle(a: int | float, h: int | float) -> float:
    """
    Finds the surface area of a square pyramid

    :param a: length of shape
    :param h: perpendicular height of shape
    :return:
    """
    if a < 0 or h < 0:
        raise ValueError("surface_area_pyramid_triangle() only accepts non-negative values")
    return 4 * a * h / 2


def surface_area_hemisphere(radius: float) -> float:
    """
    Finds the surface area of a hemisphere

    :param radius:
    :return:
    """
    if radius < 0:
        raise ValueError("surface_area_hemisphere() only accepts non-negative values")
    return 3 * 3.141592653589793 * radius**2


def surface_area_cone(radius: float, height: float) -> float:
    """
    Finds the surface area of a cone

    :param radius:
    :param height:
    :return:
    """
    if radius < 0 or height < 0:
        raise ValueError("surface_area_cone() only accepts non-negative values")
    return 3.141592653589793 * radius * (radius + (height**2 + radius**2) ** 0.5)


# TODO: function for a nth based pyramid, nth based prism, ovular cylinder, cone, ovular cone, ovular torus, torus,
#  nth based cylinder, nth based polygon

def surface_area_ovular_cylinder(a : int | float, b: int | float, h: int | float) -> float:
    """
    Finds the surface area of an ovular cylinder
    For perimeter of ellipse used the formula: 2 * pi * sqrt((a^2 + b^2) / 2)
    :param a:
    :param b:
    :param h:
    :return:
    """
    if (a < 0 or b<0 or h < 0):
        raise ValueError("surface_area_ovular_cylinder() only accepts non-negative values")
    perimeter = 2 * 3.141592653589793 * ((a**2 + b**2) / 2)**0.5
    return perimeter * h + 2 * 3.141592653589793 * a * b

def surface_area_ellipsoid(a: int | float, b: int | float, c: int | float) -> float:
    """
    Finds the approximate surface area of an ellipsoid using Knud Thomsen's formula
    :param a:
    :param b:
    :param c:
    :return:
    """
    if (a < 0 or b < 0 or c < 0):
        raise ValueError("surface_area_ellipsoid() only accepts non-negative values")
    p = 1.6075
    return 4 * 3.141592653589793 * (((a**p*b**p + b**p*c**p + a**p*c**p) / 3)**(1/p))

def surface_area_paraboloid(a: int | float, b: int | float) -> float:
    """
    Finds the surface area of a paraboloid
    a stands for axis length and b stands for cross radius
    :param a:
    :param b:
    :return:
    """
    if (a < 0 or b < 0):
        raise ValueError("surface_area_paraboloid() only accepts non-negative values")
    return 3.141592653589793 * b**2 + (3.141592653589793 * b)/(6*a**2)*((b**2 + 4*a**2)**(3/2) - b**3)


if __name__ == '__main__':
    pass
