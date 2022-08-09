"""Complex Number Class. Yes I do realise python already has one of these"""
# ok i kinda hate this


class Complex:
    def __init__(self, real=None, imaginary=None):
        self.real = real if real else 0
        self.imaginary = imaginary if imaginary else 0
        if isinstance(self.imaginary, complex):
            pass

    def __repr__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        return f"{self.real} + {self.imaginary}i"


if __name__ == '__main__':
    x = Complex(2, 7)
