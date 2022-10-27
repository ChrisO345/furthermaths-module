""" Compound Interest """

def compound_interest(p: int | float, r: int | float , t: int | float):
    """
    Finds Compound Interest per annum
    :param p: principal
    :param r: rate of interest per annum
    :param t: time in years
    """
    return p*((1+r/100)**t))-p

if __name__== '__main__':
    print(compound_interest(1000, 2, 5))
