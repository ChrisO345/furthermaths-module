import math


# function for finding roots
def qequationroots( a:float|int, b:float|int, c: float|int):
    """
    Finds the roots of a quadratic equation

    :param a: coefficient of x**2 in quadratic equation
    :param b: coefficient of x in quadratic equation
    :param c: constant term in quadratic equation
    :return:
    """

	# calculating discriminant using formula
	D = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis))
	
	# checking condition for discriminant
	if D > 0:
		print(" real and distinct roots ")
		print((-b + sqrt_val)/(2 * a))
		print((-b - sqrt_val)/(2 * a))
	
	elif D == 0:
		print(" real and same roots")
		print(-b / (2 * a))
	
	# when discriminant is less than 0
	else:
		print("Complex Roots")
		print(- b / (2 * a), " + i", sqrt_val)
		print(- b / (2 * a), " - i", sqrt_val)


# If a is 0, then equation is incorrect
if a == 0:
		print("Input correct quadratic equation")

else:
	qequationroots(a, b, c)
