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

    def __len__(self):
        return self.dimension

    def __abs__(self):
        return sum(i**2 for i in values)**0.5

    def __contains__(self, _value):
        if _value in self.values:
            return True
        return False

if __name__ == '__main__':
    x = Vector(2, 5, 7)
    y = Vector(2, 8, 8)
    print(x)

