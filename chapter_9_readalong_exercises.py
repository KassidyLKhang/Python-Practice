fin = open("words.txt")
"""
line = fin.readline()
word = line.strip()

print(word)

line = fin.readline()
word = line.strip()

print(word)


for line in fin:
    word = line.strip()
    print(word)
"""

def twenty_only():
    for line in fin:
        line = fin.readline()
        word = "".join(line.split())
        if len(word) > 20:
            print(word)

#twenty_only()

def has_no_e(word):
    if "e" in word or "E" in word:
        return False
    else:
        return True

#print(has_no_e("Elf"))
#print(has_no_e("Glyph"))


def print_words_no_e():
    count = 0
    no_e_count = 0

    for line in fin:
        line = fin.readline()
        word = "".join(line.split())

        count += 1

        if has_no_e(word):
            no_e_count += 1
            print(word)
    print(f"Percentage of no 'e' words: {no_e_count/count}")

#print_words_no_e()


#This is case sensitive. Can use functions like .lower() to make it not case sensitive
def avoids(word, letters):
    no_forbidden_letters = True

    for letter in letters:
        if letter in word:
            #print(word, letter)
            no_forbidden_letters = False

    return no_forbidden_letters
    

#print(avoids("Entropy", "akl"))
#print(avoids("Serendipity", "S"))

def user_avoids():
    forbidden_letters = input("Input a string of forbidden letters.")

    count = 0

    for line in fin:
        line = fin.readline()
        word = "".join(line.split())

        if avoids(word, forbidden_letters):
            count += 1

    print(f"There are {count} words without those letters.")


#user_avoids() #aeiou results in 65 words. Pretty good, I'd say.

def uses_only(word, letters):
    uses_only = True

    for letter in letters:
        if letter not in word:
            #print(word, letter)
            uses_only = False

    return uses_only

#print("e" in "eucalyptus")
#print("e" not in "eucalyptus")

print(uses_only("ice","eci"))
print(uses_only("everest","eci"))
print(uses_only("fractal","eci"))


def uses_all(word, letters):
    pass
