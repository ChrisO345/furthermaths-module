"""Vectors"""


class Vector:
    def __init__(self, dimension, *args):
        self.dimension = dimension
        self.values = args
        print(self.dimension)
        print(self.values)
        if len(self.values) != self.dimension:
            raise IndexError("Dimensions specified does not match those given")

    def __repr__(self):
        return f"Vector[{', '.join(str(x) for x in self.values)}]"


if __name__ == '__main__':
    x = Vector(2, 5, 7)
    y = Vector(2, 8, 8)
    print(x)

