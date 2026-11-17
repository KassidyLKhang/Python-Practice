"""
Chapter 6 Read Along Code

Basic code to help solidify chapter concepts.
"""

import math

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1
    
#print(compare(2,1))
#print(compare(1,1))
#print(compare(1,2))

def distance(x1, y1, x2, y2):
    x_diff = x2-x1
    y_diff = y2-y1

    print(x_diff)
    print(y_diff)

    x_squared = x_diff**2
    y_squared = y_diff**2

    print(x_squared)
    print(y_squared)

    squared_added = x_squared + y_squared

    print(squared_added)

    square_root = math.sqrt(squared_added)

    print(square_root)

    return square_root

#distance(0,0,1,5)


def hypotenuse(a,b):
    a_squared = a**2
    b_squared = b**2

    print(a_squared)
    print(b_squared)

    ab_sum = a_squared + b_squared

    print(ab_sum)

    c = math.sqrt(ab_sum)

    print(c)

#hypotenuse(5,12)



def is_between(x, y, z):
    return x <= y <= z

#print(is_between(1,2,3))
#print(is_between(1,2,1))