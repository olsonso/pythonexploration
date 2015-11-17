#!/usr/bin/python3
#Sonja Olson
#Program 5


import random
import string

#function that creates random letters for files
def rand_letters():
    return ''.join(random.choice(string.ascii_lowercase) for x in range(10))

#function that creates random interger 1-42
def rand_integer():
    return random.randint(1,42)

rand1 = rand_letters()
rand2 = rand_letters()
rand3 = rand_letters()

print("Creating three files and generating random input")

#printing out file 1

print("\nFirst File contents:")
file1 = open("mypython_file1", "w")
file1.write(rand1)
print(rand1)
file1.close() 

print("\nSecond File contents:")
file2 = open("mypython_file2", "w")
file2.write(rand1)
print(rand2)
file2.close() 

print("\nThird File contents:")
file3 = open("mypython_file3", "w")
file3.write(rand1)
print(rand3)
file3.close() 


print("\nRandom numbers:")
randInt1 = rand_integer()
print(randInt1)

randInt2 = rand_integer()
print(randInt2)

print("\nTheir product:")
product = randInt1 * randInt2
print(product)