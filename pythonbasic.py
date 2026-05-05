# name = "khalid"
# slice char
# print(name[0:3])

# Escape sequenses
# import math
# course = 'Python \"Programming '
# course = 'Python \'Programming '
# we can fix this by a \
# \" is is a escape sequense
# \\
# \n new line
# we use this to escape a char after


# print(course)


# formatet strings
# first = "khalid"
# last = "ghalib"
# full = f"{first} {last}"
# print(full)

# String methods
# course = "java programming"
# print(course.upper())
# print(course.rstrip())


# Numbers
# 1 int
# 1.1 float
# x = a + b i --> imagnary number
# print(round(2.9))

# print(math.ceil(2.2))


# type conversion
# x = input("x:")
# y = x + 1
# print(bool(""))

# number 0 and empty string and null object is 0 falsyyy


# condational statment
# temperature = 30
# if temperature > 40:
#     print("it' very warm")
#     print("Drink water")
# elif temperature > 35:

#     print("Done")


# age = 22
# if age >= 15:
#     print("eligible")
# else:
#     print("Not eligible")


# age = 17
# if age >= 18:
#     print('You Can Come')
# else:
#     print("We are sorry, Your Cannot Come!")


# Logical Opreators
# or \\ checks tow values if one of them is tue it will be true
# and  \\ if both values are true it will work otherwise it will be false
# not makes the bolian value false
# high_income = True
# good_credit = False
# students = False
# if (high_income or good_credit) and not students:
#     print("eligible")
# else:
#     print("not eligible")


# chaining comparaison operators
# age = 22
# if 18 <= age < 65:
#     print("Eligible")


# print(10 == "10")

# for loop
# for number in range(1, 10, 2):
#     print("Attept", number + 1, number * ".")


# for else
# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break

# else:
#     print("Attempted 3 times and failed")


# nested loops
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# iterables
# print(type(5))
# print(type(range(5)))
# range is an iterable but not a list and it is a complex types in python

# ............. example of iterables...........
# List
# numbers = [1, 2, 3, 4]

# String
# name = "Khalid"

# Tuple
# data = (10, 20, 30)

# Dictionary
# user = {"name": "Khalid", "age": 20}

# Set
# unique_numbers = {1, 2, 3}

# for x in "python":
#     print(x)

# python can iterate over any iterable object, which is an object that can return its elements one at a time. This includes lists, strings, tuples, dictionaries, sets, and more. The iter() function is used to create an iterator from an iterable object, and the next() function is used to retrieve the next element from the iterator.
# numbers = [1, 2, 3, 4]
# it = iter(numbers)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# while loops


# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
# print("echo", command)


# doing the exezise

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)

# print(f"we have {count} even numbers")


# function and arguments
# a prameter is the input that you define in the function definition, while an argument is the actual value you pass to the function when you call it. For example, in the function definition def greet(name):, name is a parameter. When you call the function with greet("Alice"), "Alice" is the argument.
# def greet(first_name, last_name):
#     print(f"hi {first_name} {last_name}")
#     print("hi there welcome aboard")


# greet("khalid", "ghalib")
# we have tow types of fanctions 1 perform a task 2 return a value


# def get_greeting(name):
#     return (f"hi(name)")


# print(get_greeting("khalid"))


# def increment(number, by):
#     return number + by


# print( increment(2, 1))


# default arguments
def increment(number, another, by=1):
    return number + by


print(increment(2, 5))
print(increment(2, 5, 3))
print(increment(2, 5, by=3))
