""" Simple Interest """

def simple_interest(p: int | float, r: int | float , t: int| float):
    """
    Finds Simple Interest per annum
    
    :param p: principal
    :param r: rate of interest per annum
    :param t: time in years
    """
    return p*r*t/100

if __name__== '__main__':
    print(simple_interest(900, 3, 4))
