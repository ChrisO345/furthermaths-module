"""Euclidean Distance"""


def dist(*args):
    """
    Calculates the distance between two points

    :param args: the points
    :return:
    """
    if len(args) not in [2, 4]:
        raise ValueError("dist() takes 2 or 4 arguments")
    if type(args[0]) == set or type(args[0]) == list:
        pos1 = args[0]
        pos2 = args[1]
        if len(pos1) == 2 and len(pos2) == 2:
            x1, y1, x2, y2 = pos1[0], pos1[1], pos2[0], pos2[1]
        else:
            raise ValueError("dist() takes 2 sets with length 2")
    else:
        x1, y1, x2, y2 = args[0], args[1], args[2], args[3]
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    
def manhattan_dist(*args):
    """
    Calculates the manhattan distance between two points

    :param args: the points
    :return: manhattan distance
    """
    if len(args) not in [2, 4]:
        raise ValueError("dist() takes 2 or 4 arguments")
    if type(args[0]) == set or type(args[0]) == list:
        pos1 = args[0]
        pos2 = args[1]
        if len(pos1) == 2 and len(pos2) == 2:
            x1, y1, x2, y2 = pos1[0], pos1[1], pos2[0], pos2[1]
        else:
            raise ValueError("dist() takes 2 sets with length 2")
    else:
        x1, y1, x2, y2 = args[0], args[1], args[2], args[3]
    if x1>x2 and y1>y2:
    	return (x1 - x2, y1 - y2)
    elif x1<x2 and y1>y2:
    	return (x2 - x1, y1 - y2)
    elif x1>x2 and y1<y2:
    	return (x1 - x2, y2 - y1)
    else:
    	return (x2 - x1, y2 - y1)


if __name__ == '__main__':
    print(dist(1, 2, 3, 4))
    print(dist([1, 2], [3, 4]))
