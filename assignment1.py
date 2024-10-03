#problem 1

def count_vowels(word):
    i = 0
    vowel_count = 0
    while i < len(word):
        if (word[i] in ["a","e","i","o","u"]):
            vowel_count += 1
        i += 1
    
    return vowel_count

print(count_vowels("hello")) #2
print(count_vowels(""))  # 0
print(count_vowels("aeiou")) #5


def print_animals():
    animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

    i = 0
    while (i < len(animals)):
        print(animals[i].upper())
        i += 1

print_animals()



def print_nums():
    i = 1
    while (i <= 20):
        oddEven = "even"
        if (i % 2 == 1):
            oddEven = "odd"

        print(i, oddEven)
        i += 1

print_nums()




def sum_of_integers(a,b):
    return a+b


a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))
print(sum_of_integers(a,b))