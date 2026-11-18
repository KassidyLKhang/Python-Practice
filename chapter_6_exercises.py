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

#Method 1: Check each string from start and end until they are next to each other or become the same index
#Method 2: If even compare string from 

#Oops, I need to either reverse the string or check the characters one by one.

def is_palidrome(string):
    is_palindrome = True
    string_length = len(string)
    half_index = len(string)//2

    if len(string) % 2 == 0:
        if string[:half_index] != string[half_index:string_length]:
            is_palindrome = False
    elif len(string) % 2 == 1:
        if string[:half_index + 1] != string[half_index:string_length]: 
            is_palindrome = False

    return is_palindrome

print(is_palidrome(hello))
print(is_palidrome(even_palindrome))
print(is_palidrome(odd_palindrome))

        