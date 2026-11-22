"""
Chapter 8
"""

string = "Strings are lists of characters!"

"""
print(string[0])
print(string[-1])
print(string[:8]) #Start to 8
print(string[5:8]) #This is called string slices
print(string[2:]) #Start from 2 to end
print(string[:]) #Print entire string
print(string[:-1]) #Prints everything but the last char
print(string[::-1]) #Prints everything reversed 




print("Start from index 0! Indexes can use expressions, just be sure the result is an integer. Also, avoid going out of range. You can use length - 1 or [-1]")

print(len(string))


for i in range(5):
    print(string[i])


def reverse_traverse(string):
    for i in range(len(string) + 1):
        print(string[-i])

reverse_traverse(string)

for i in string:
    print(i)   



prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == "Q" or letter == "O":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)


def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

#print(find(string, "s", 7))



def count_letter(string, char):
    count = 0
    for letter in string:
        if letter == char:
            count = count + 1
    print(count)

#count_letter(string, "s")


def find_count_letter(word, letter):
    count = 0
    find_value = 0

    while find_value > -1 and find_value <= (len(word)-1):
        find_value = find(word, letter, find_value+1)

        if find_value != -1:
            count += 1

        print(find_value)

    return count

print(find_count_letter(string, "s"))


print(string.find("s",6,15))

if "lists" in string:
    print("lists are in string!")



if "Hello World!" < string:
    print("'Hello World!' comes before string alphabetically!")

if "hello World!" > string:
    print("'hello World!' comes after string alphabetically due to being lowercase!")


"""

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1

    while j >= 0:
        print(word1[i],word2[j])
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
        
    return True


is_reverse("pots", "stop")