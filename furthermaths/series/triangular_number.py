def triangular_number(n):
    """
    Find the nth triangular number, starting from 1.
    """
    
    return int((n*(n+1))/2)

if __name__ == '__main__':
    print(triangular_number(6))
    print(triangular_number(10))