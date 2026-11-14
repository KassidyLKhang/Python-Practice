"""

Python Programming Problems, Practice, and Prep


This is a collection of Python exercises.

"""

import math
from operator import le
import turtle
import random



screen = turtle.Screen()
bowser = turtle.Turtle()
"""

bowser.circle(100)
bowser.fd(200)
bowser.circle(100)

def square(turtle, length):
    for i in range(4):
        turtle.fd(length)
        turtle.lt(90)

square(bowser, 200)




def polygon(turtle, length, n):
    angle = 360/n
    for i in range(n):
        turtle.fd(length)
        turtle.lt(angle)

#polygon(turtle, 200, 5)


def circle(turtle, radius):
    circumference = 2 * math.pi * radius
    n = int(circumference / 3) + 3 # This is apparently the answer
    length = circumference / n

    polygon(turtle, length, n)
    
    #circumference = length * n

    #length * n = circumference
    #2 * pi * r = length * n
    #2 * pi * r = length * angle

    #2 * math.pi * radius = cirumference
    #length = circumference / n
    #n = circumference / length
    #n / circumference = 1 / length

#circle()

circle(turtle, 40)
"""

"""

def triangle_no_angle(turtle, length):
    for i in range(3):
        turtle.fd(length)
        turtle.lt(120)

#triangle_no_angle(turtle, 50)
"""
def triangle(turtle, length, angle):
    for i in range(3):
        turtle.fd(length)
        turtle.lt(angle)

triangle(turtle, 100, 120)


#Not the solution, but it looked pretty so I saved it
"""
def polygon_with_triangles(turtle, length, n):
    angle = 360/n
    for i in range(n):
        triangle_no_angle(turtle, length)
        turtle.fd(length)
        turtle.lt(angle)

polygon_with_triangles(turtle, 40, 5)
"""
""""""
def polygon_with_triangles(turtle, length, n):
    angle = 360/n
    for i in range(n):
        triangle(turtle, length, angle)
        turtle.fd(length)
        turtle.lt(angle)

polygon_with_triangles(turtle, 100, 5)


screen.exitonclick()


"""
#Some floor division tricks

#x = int(input("Type a number for modulus: "))
#y = int(input("Type a second number for modulus: "))

x = random.randint(0,100)
y = random.randint(0,100)

if x % 2 == 1:
    print(f"{x} is odd!")
elif x % 2 == 0:
    print(f"{x} is even!")


if x % y == 0:
    print(f"{x} is divisible by {y}")
else: 
    print(f"{x} ain't divisible by {y}")


print(f"{x}'s rightmost digit is: {x % 10}")
print(f"{x}'s last two digits are: {x % 100}")


#Conditionals 

if x == y:
    pass
elif x > y:
    pass
elif x < y:
    pass
else:
    pass


#Newest Python verions have match case

fruit = "orange"

#input("Enter the name of a fruit (not case sensitive and removes accidental spaces at the beginning and end): ").lower().strip()

match fruit:
    case "apple":
        print(f"It's a {fruit}!")
    case "orange":
        print(f"It's a {fruit}!")
    case "strawberry":
        print(f"It's a {fruit}!")
    case _:
        print(f"Not a known fruit. Might not be a fruit at all.")


if x == y or x > y and x != y:
    pass

if not x == y:
    print(f"{x} and {y} are not equal.")

"""

#Recursion

"""
One of the more tricky, yet interesting programming concepts.

Most if not  all languages allow functions to call themselves. To write an effective recursion:

1. Base Case / Exit condition
2. Always progress towards exit condition

It can be used to traverse binary trees.

If you can define it recursively, it probably can be written as such.
An example includes factorials.



def basic_recursion(x):
    if x is 0:
        print(f"The number is now {x}. It has been reduced to ashes.")
        return
    else:
        print(f"{x} has been decremented by 1.")
        basic_recursion(x-1)

basic_recursion(5)



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

distance(0,0,1,5)

def is_between(x, y, z):
    return x <= y <= z

print(is_between(1,2,3))
print(is_between(1,2,1))
"""

"""

Factorials are a good example for being recursively definable.

n! = n(n-1)!

3! = 3 * 2 * 1

You'll notice that the function below is basically n(n-1)! translated to code.



def factorial(n):
    if n == 0: #You can also just write n == 1
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))


"""

#Turtle exercises
#5th chapter exercises

#Code and debug -> Extra Resource

#Try 7?
#I am very, very tired
#Half my brain is still at work
#Oh
#hm....
#8am~


