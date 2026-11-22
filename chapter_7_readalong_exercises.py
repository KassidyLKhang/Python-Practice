"""
Chapter 7 Readalong Exercises
"""

import math

a = 1
b = 2

#print(a,b)

a = b

#print(a,b)

b += b
a -= 1

#print(a,b)

c = b = a #a = 1, so b & c = 1

#print(a,b,c)

a, d = b, c #can swap vars this way without a temporary variable

#print(a,b,c,d)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blastoff!")

#countdown(10)

def type_done():
    while True:
        line = input("Type done to make the suffering end:\n")
        if line == "done":
            break
        print("The suffering continues.")

#type_done()


#Note: "is" keyword compares if the two variables point to the same object in memory, so it actually can't be used for a lot of comparison cases. I found this out trying to use it for the if statement above.


"""
Exercise 1
"""

"""

    
if y == x:
            break    
"""

def mysqrt(a):
    x = a/2
    epsilon = 0.0000001
    while True:
        #print(x)
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y

    return x

#print(mysqrt(9))

def test_square_root():
    print(f"a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------- ----")
    for a in range(1,10):
        print(f"{float(a)} {mysqrt(a):.11f} {math.sqrt(a):.11f} {mysqrt(a) - math.sqrt(a)}")

#test_square_root()



"""
Exercise 2
"""

def eval_loop():
    last_expression = "No expression was evaluated."
    while True:
        prompt = input("Input line to be evaluated here:\n")
        if prompt == "done":
            print(last_expression)
            break
        else:
            last_expression = eval(prompt)
            print(last_expression)

#eval_loop()

"""
Exercise 3
"""
#print(10**-15)

def estimate_pi():
    #while % (10**15)
    multiply_sum_by = (2 * math.sqrt(2)) / 9801
    #print(multiply_sum_by)

    k = 0

    summation = 0

    while True:
        numerator = math.factorial(4*k) * (1103 + (26390 * k))
        #print(numerator)
        denominator = (math.factorial(k) ** 4) * (396**(4*k))
        #print(denominator)
        
        print(numerator / denominator)
        summation = summation + (numerator / denominator)
        print(summation)

        if (summation % (10**-15)) > 0:
            break
        k += 1

    return multiply_sum_by * summation

#estimate_pi()

#value = 0.1234567890123456
#value_2 = 0.0000000000000006

#print(value % (10**15))
#print((value_2 % (10**15)) < (10**-15))

#print(estimate_pi())
#print(1/math.pi)


