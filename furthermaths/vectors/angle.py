"""Angle between two vectors"""
from math import acos,sqrt
from Vectors import Vector
pi = 3.14159265359

def angle(v1, v2):
    if not isinstance(v1,Vector) or not isinstance(v2,Vector):
        return  ValueError("not a vector")
    if v1.dimension!=v2.dimension:
        raise ValueError("Dimensions of vectors should be equal")
    dotProduct = sum(i * j for i, j in zip(v1.values, v2.values))
    modOfVectors = (sum(i*i for i in v1.values) * sum(i*i for i in v2.values))**0.5
    x = dotProduct / modOfVectors
    return (acos(x) * 180) / pi

if __name__ == '__main__':
    x = Vector(2, 3, 4)
    y = Vector(2, 5, 2)
    # print(angle(x,y))
