# co ordinate geometry
from .square_root import sqrt


def distance_from_X_axis(x:int,y:int)->int:
    """
    Gives distance of given from x-axis
    """
    return y

def get_distance_from_Y_axis(x:int,y:int)->int:
    """
    Gives distance of given from y-axis
    """
    return x

def get_distance_from_origin(x:int,y:int)->int:
    """
    Gives distance of given from origin (0,0)
    """
    return sqrt(x**2+y**2)

def distance_between_points(x:list,y:list)->int:
    # x and y should be lists with 2 values only
    """
    Gives distance between given 2 points
    """
    return sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

def get_slope(x:list,y:list)->int:
    # x =[x1,y1] and y =[x2,y2]
    # x and y should be lists with 2 values only
    """
    Gives slope of given line
    """
    try:
        return (y[1]-x[1])/(y[0]-x[0])
    except ZeroDivisionError:
        return float('inf')
