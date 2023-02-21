def standard_deviation(list):
    """
    Returns the standard deviation of a list.
    
    """

    m = mean(list)
    tmp = 0
    for i in list:
        tmp+= (i-m)**2

    return (tmp/len(list)) **0.5

def mean(list):
    return sum(list) / len(list)

if __name__== '__main__':
    print(standard_deviation([2,1,3,2,4]))