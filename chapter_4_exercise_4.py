"""
Chapter 4 Exercise 4
"""

"""
Attempts

Make alphabet with turtle.
"""

import turtle
import math

screen = turtle.Screen()

def draw_a(t, length):
    t.lt(60)
    t.forward(length/2)

    #Middle Bar
    t.rt(60)
    t.forward(length/2)

    #Return
    t.backward(length/2)

    t.lt(60)
    t.forward(length/2)

    t.rt(120)
    t.forward(length)


def draw_a_alt_1(t, length):
    t.lt(60)
    t.forward(length)

    t.rt(120)
    t.forward(length)

    t.penup()
    t.rt(120)
    t.forward(length)
    t.rt(120)
    t.forward(length/2)

    t.pendown()
    t.rt(60)
    t.forward(length/2)


def draw_a_alt_2(t, length):
    t.lt(60)
    t.forward(length)

    t.rt(120)
    t.forward(length)

    t.backward(length/2)
    t.lt(60)
    t.backward(length/2)

#draw_a(turtle, 100)

#draw_a_alt(turtle, 100)

#draw_a_alt_2(turtle, 100)

def draw_b(t, length):
    t.lt(90)
    t.forward(length)
    t.backward(length)
    t.rt(90)

    t.circle(length/4, 180)
    t.lt(180)
    t.circle(length/4, 180)
    

#draw_b(turtle, 100)

def draw_c(t, length):
    t.penup()
    t.circle(length/2, 140)
    t.pendown()
    t.circle(length/2, 270)

#draw_c(turtle, 100)




def draw_z(t, length):
    t.forward(length)
    t.rt(135)
    t.forward(length * math.sqrt(2)) #Trig
    t.lt(135)
    t.forward(length)



def archimediean_spiral(t, origin, length, max_angle):
    a = origin
    b = length
    theta = 0
    step = 0.05
    
    while theta <= max_angle:
        r = a + b * theta
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        t.goto(x, y)
        theta += step
    
        

        #theta = math.radians(i)

        #t.goto(math.cos(theta) * i * length, math.sin(theta) * i * length)


        #cos(theta) * 
        #t.goto(math.cos(math.radians(i)) * i * length, math.sin(math.radians(i)) * i * length)

    #print(math.cos(math.radians(i)))
        

archimediean_spiral(turtle, 0, 3, 4*2*math.pi)


screen.exitonclick()