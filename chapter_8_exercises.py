"""
Exercise 1
"""

quote = " Sure, except I think I'm still a little too petrified to laugh. "

"""
print(quote.strip())
print(quote.lstrip())
print(quote.rstrip())

print(quote.split())
print("".join(quote.split()))
print(quote.replace(" ", ""))

print(quote.capitalize()) #Doesn't capitalize proper if the first char is a space
print(quote.casefold())
print(quote.lower())
print(quote.upper())
"""

"""
Exercise 2
"""

#print("banana".count("a"))


"""
Exercise 3

Oh hey, there's actually an explanation for the index reversal!

[start : end : step size]
"""

def is_palindrome(string_1, string_2):
    return True if string_1 == string_2[::-1] else False

#print(is_palindrome("wasd", "dsaw"))
#print(is_palindrome("wasd", "wasssap"))


"""
Exercise 4
"""

#Checks the first character in s and checks if it's lowercased. It will automatically escape the loop upon the first check due to return, so if the first letter is lowercase, it will return True. If it isn't, then even if there's a lowercase later on, it will return False.
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

#Variable c isn't actually checked proper. So actually, the lowercase letter c is being checked once, and then it returns True. It will return True every time.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

#Flag is assigned the boolean for whether or not c is a lowercase. It will be assigned the result of each check of each character, so it actually only returns the boolean of the last character's check. 
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

#Flag is preassigned False before the loop and given a condition to decide whether to change it as it goes through checking each char. The way the "or" conditional works, if one part is True, all will be True. So, if c is True even once, it will be assigned True even if the other checks are False. TLDR; It works!
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#The "not" keyword is actually a negator. So, if c was lowercase, it would be True, but the not keyword would make it False, and vice versa. It's going to terminate the first time it encounters a non-lowercase char, and only return True if the entire string is lowercase.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

if not True:
    print("Uh???")

#if not False:
#    print("What??")


"""
Exercise 5

Need to check if char code + int passes boundary for letter wrap.
check if char code + int surpasses char code a or z

if char is greater than z, wrap from a
if char is less than a, wrap from z

Let's assume that only letters are being used.


This works~ 
There's probably a cleaner way to do it. It'll get more interesting if special characters are involved. For now, I just assumed that only letters were used.
"""

def rotate_word(string, int):
    new_string = ""
    for letter in string:
        new_letter_code = ord(letter) + int

        if letter.islower():
            while new_letter_code < ord("a"):
                new_letter_code += 26
            while new_letter_code > ord("z"):
                new_letter_code -= 26

        if letter.isupper():
            while new_letter_code < ord("A"):
                new_letter_code += 26
            while new_letter_code > ord("Z"):
                new_letter_code -= 26

        new_string += chr(new_letter_code)
    return new_string

#Might try to write it with module

"""
#26 letters in the alphabet
#You could potentially hard code using the codes below. I'm just going to do what the book hinted.
print(ord("a")) # "1" actually 97
print(ord("z")) # "26" actually 122
print(ord("z") - ord("a")) #25, or 26 - 1

print(ord("A"))
print(ord("Z"))
print(ord("Z") - ord("A"))
"""

print(rotate_word("cheer", 7))
print(rotate_word("melon", -10))

print(rotate_word("Cheer", 7))
print(rotate_word("MELON", -260))