"""Dot Product of 2 Vectors"""
from .Vectors import Vector

def dot(v1, v2):
    if not isinstance(v1,Vector) or not isinstance(v2,Vector):
        return  ValueError("not a vector")
    if v1.dimension!=v2.dimension:
        raise ValueError("Dimensions of vectors should be equal")
    return sum(i * j for i, j in zip(v1.values, v2.values))


if __name__ == '__main__':
    pass
