"""Vectors"""


class Vector:
    def __init__(self, dimension=2, *args):
        self.dimension = dimension
        self.values = args
        if len(self.values) != self.dimension:
            raise IndexError("Dimensions specified does not match those given")

    def __repr__(self):
        return f"Vector[{', '.join(str(x) for x in self.values)}]"

    def __len__(self):
        return self.dimension

    def __abs__(self):
        return sum(i**2 for i in self.values)**0.5

    def contains(self, _value):
        if _value in self.values:
            return True
        return False

    def __add__(self, other):
        return Vector(self.dimension, *(i + j for i, j in zip(self.values, other.values)))

    def __sub__(self, other):
        return Vector(self.dimension, *(i - j for i, j in zip(self.values, other.values)))

    def __neg__(self):
        return Vector(self.dimension, *(-i for i in self.values))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return  # TODO add multiplication of 2 vectors
        return Vector(self.dimension, *(i * other for i in self.values))


if __name__ == '__main__':
    x = Vector(2, 5, 7)
    y = Vector(2, 8, 8)
