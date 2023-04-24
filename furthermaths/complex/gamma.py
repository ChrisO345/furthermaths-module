"""Gamma Function"""

from cmath import sin, sqrt, exp

_table = (676.5203681218851
    ,-1259.1392167224028
    ,771.32342877765313
    ,-176.61502916214059
    ,12.507343278686905
    ,-0.13857109526572012
    ,9.9843695780195716e-6
    ,1.5056327351493116e-7
    )

PI = 3.141592653589793

def gamma(x: complex) -> complex:
    """
    Returns the gamma function of x

    :param x: the value to find the gamma function of
    :returns: gamma value
    """
    if x.real < 0 and isinstance(x.real, int):
        raise ValueError("The Value will be Undefined")
    x = complex(x)
    if x.real < 0.5:
        z = PI / (sin(PI * x) * gamma(1 - x)) 
    else:
        x = x - 1
        y = 0.99999999999980993
        for (i, pval) in enumerate(_table):
            y += pval / (x + i + 1)
        t = x + len(_table) - 0.5
        z = sqrt(2 * PI) * t ** (x + 0.5) * exp(-t) * y

    if abs(z.imag) <= 0.0000001:
        z = z.real
    return z

if __name__ == "__main__":
    print(gamma(-4.5))
    print(gamma(11))
    print(gamma(-1/2))
    print(gamma(2/5))
