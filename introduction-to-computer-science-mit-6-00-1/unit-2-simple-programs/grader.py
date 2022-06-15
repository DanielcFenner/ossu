import math

def polysum(n,s):
    """
    Input: n, number of sides. s, length of each side.
    Output: Returns the sum of the area and square of the perimeter of the inputted polygon
    """
    area = (0.25 * n * s ** 2) / math.tan(math.pi/n)
    perimeterSquared = (n * s) ** 2
    sum = area + perimeterSquared
    return round(sum, 4)