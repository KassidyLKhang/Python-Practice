"""
Chapter 6 Exercise 1
"""

"""
x = 1
y = 2

c(1,5,3) ->
total = 1 + 5 + 3 = 9
square = b(9) ** 2

===

b(9)->
prod = a(9, 9)

==

a(9,9) ->
9 = 9 + 1 = 10
return 10 * 9 = 90

==

b(9)->
prod = a(9, 9) = 90
print(9, 90) #print "9 90"
return 90

===
square = b(9) ** 2 = 90 ** 2 = 8100
return 8100

print(8100)


Prints: 
9 90
8100

Yup, I'm right! <3

"""

#print(9,9) # prints "9 9"


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
    
x = 1
y = x + 1
#print(c(x, y+3, x+y)) #Check answer



"""
Exercise 2* 

Good example of how to write a recursive function mathematically and programmatically!

Also, if using larger arguments, it will cause a maximum recusion depth error.

"""

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

#print(ack(3,4))
#print(ack(300,400)) #Max depth reached


"""
Exercise 3
"""

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

empty = ""
b = "b"
at = "at"
hello = "Hello World!"
snake = "Snake"

odd_palindrome = "wasdqdsaw"
even_palindrome = "wasddsaw"

"""
print(first(b))
print(first(at))
#print(first(empty)) #Error out of index

print(last(b))
print(last(at))
#print(last(empty)) #Error out of index

#Prints nothing (print automatically adds \n)
print(middle(b) + ":O")
print(middle(at) + ":O")
print(middle(empty) + ":O")
print(middle(hello))


print(hello[:len(hello)])
print(hello[:(len(hello)//2)] + ":O")

print(snake[:(len(snake)//2)])
print(snake[(len(snake)//2):len(snake)])
print(snake[(len(snake)//2)+1:len(snake)])
"""

#Method 1: Check each string from start and end until they are next to each other or become the same index
#Method 2: If even compare string from 

#Oops, I need to either reverse the string or check the characters one by one.

def is_palidrome(string):
    is_palindrome = True
    string_length = len(string)
    half_index = len(string)//2

    first_half_even = string[:half_index]
    first_half_odd = string[:half_index + 1]
    second_half = "".join(reversed(string[half_index:string_length]))

    if len(string) % 2 == 0:
        if first_half_even != second_half:
            is_palindrome = False
    elif len(string) % 2 == 1:
        if first_half_odd != second_half: 
            is_palindrome = False

    return is_palindrome

"""
print(is_palidrome(hello))
print(is_palidrome(even_palindrome))
print(is_palidrome(odd_palindrome))
"""


"""
Exercise 4

a is power of b if:
a % b == 0 and a/b is a power of b

b**4

4/b?
4/2 True!
4/3 False!

a % b == 0

a/b % b == 0

a != 1

a == a/b

b != 0

3**2 = 9
9 % 3 = 0
9/3 % 3 = 3 % 3 = 0

3/3 % 3 = 1 % 3 = 

a = 1


8 = 2 ** 3
4 = 2 ** 2


(a/b) % b == 0


a = b 

2**3 = 8
8 % 2 = 0
4 % 2 = 0
2 % 2 = 0
1 % 2 = 1 #Have to stop here

5,2
5 % 2 = 1 #NOPE


(1,1)

1 % 1 = 0
1/1 % 1 = 0

if a >= b and b > 0:
    a % b == 0
    is power
"""

#1 is only power of 1, 0 is only power of 0, non zero num ** 0 == 1
def is_power(a, b):
    if a == 1:
        return True
    elif b == 0 and a == 0:
        return True
    elif b == 0:
        return False
    
    if a % b == 0:
        return is_power(a/b,b)
    else:
        return False

#print(is_power(9,3))
#print(is_power(16,4))
#print(is_power(15,4))
#print(is_power(1,1))
#print(is_power(0,0)) #Max Depth



"""
Exercise 5

a % b = r

gcd(a,0) = a        b = 0
gcd(a,b) = gcd(b,r)


E.G.

50 & 100
GCD = 50

Please put greater number as a.
a >= b please

"""

def gcd(a,b):
    if b == 0:
        return a

    return gcd(b, a%b)

print(gcd(100,50))
print(gcd(15,3))
print(gcd(15,12))
print(gcd(15,4))
