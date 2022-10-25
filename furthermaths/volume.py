"""Find volumes of Various Shapes."""


def volume_cube(side_length: int | float) -> float:
    """
    Returns the volume of a cube.

    :param side_length:
    :return:
    """
    return side_length**3


def volume_spherical_cap(height: float, radius: float) -> float:
    """
    Returns the volume of a spherical cap.

    :param height:
    :param radius:
    :return:
    """
    return 1 / 3 * 3.141592653589793 * (height**2) * (3 * radius - height)


def volume_spheres_intersect(radius_1: float, radius_2: float, centers_distance: float) -> float:
    """
    Returns the volume of the intersection of two spheres.

    :param radius_1:
    :param radius_2:
    :param centers_distance:
    :return:
    """
    if centers_distance == 0:
        return volume_sphere(min(radius_1, radius_2))

    h1 = (
            (radius_1 - radius_2 + centers_distance)
            * (radius_1 + radius_2 - centers_distance)
            / (2 * centers_distance)
    )
    h2 = (
            (radius_2 - radius_1 + centers_distance)
            * (radius_2 + radius_1 - centers_distance)
            / (2 * centers_distance)
    )

    return volume_spherical_cap(h1, radius_2) + volume_spherical_cap(h2, radius_1)


def volume_cuboid(width: float, height: float, length: float) -> float:
    """
    Returns the volume of a cuboid.

    :param width:
    :param height:
    :param length:
    :return:
    """
    return float(width * height * length)


def volume_cone(area_of_base: float, height: float) -> float:
    """
    Returns the volume of a cone.

    :param area_of_base:
    :param height:
    :return:
    """
    return area_of_base * height / 3.0


def volume_right_circ_cone(radius: float, height: float) -> float:
    """
    Returns the volume of a right circular cone.

    :param radius:
    :param height:
    :return:
    """
    return 3.141592653589793 * (radius**2) * height / 3.0


def volume_prism(area_of_base: float, height: float) -> float:
    """
    Returns the volume of a prism.

    :param area_of_base:
    :param height:
    :return:
    """
    return float(area_of_base * height)


def volume_pyramid(area_of_base: float, height: float) -> float:
    """
    Returns the volume of a pyramid.

    :param area_of_base:
    :param height:
    :return:
    """
    return area_of_base * height / 3.0


def volume_sphere(radius: float) -> float:
    """
    Returns the volume of a sphere.

    :param radius:
    :return:
    """
    return 4 / 3 * 3.141592653589793 * (radius**3)


def volume_hemisphere(radius: float):
    """
    Returns the volume of a hemisphere.

    :param radius:
    :return:
    """
    return 2 / 3 * 3.141592653589793 * (radius**3)


def volume_circular_cylinder(radius: float, height: float) -> float:
    """
    Returns the volume of a circular cylinder.

    :param radius:
    :param height:
    :return:
    """
    return 3.141592653589793 * (radius**2) * height


def volume_conical_frustum(height: float, radius_1: float, radius_2: float):
    """
    Returns the volume of a conical frustum.

    :param height:
    :param radius_1:
    :param radius_2:
    :return:
    """
    return 1 / 3 * 3.141592653589793 * height * ((radius_1 ** 2) + (radius_2 ** 2) + radius_1 * radius_2)

def volume_ellipsoid(a: float, b: float, c: float) -> float:
    """
    Returns the volume of an ellipsoid.
    ellipsoid equation of the form (x/a)^2 + (y/b)^2 + (z/c)^2 = 1
    :param a:
    :param b:
    :param c:
    :return:
    """
    return 4 / 3 * 3.141592653589793 * a * b * c