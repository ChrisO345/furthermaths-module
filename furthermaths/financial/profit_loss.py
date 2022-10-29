""" Profit and Loss """

def profit(cp: int | float, sp: int | float):
    """
    Finds the profit percentage
    :param cp: cost price
    :param sp: selling price
    """
    return (sp-cp)*100/cp

def loss(cp: int | float, sp: int | float):
    """
    Finds the loss percentage
    :param cp: cost price
    :param sp: selling price
    """
    return (cp-sp)*100/cp

if __name__== '__main__':
    print(profit(10, 12))
    print(loss(30, 17))
