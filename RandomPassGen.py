# collect user preferences for password generation
# length of password
# should contain uppercase letters
# should special
# should contain digits

# create all available characters based on user preferences
# randomly pick characters up to the length
# ensure we have at least one each character type


import random
import string
import sys


def generate_password():
    length = int( input("input the desired password length: ").strip())
    include_uppercase = input(
        "include uppercase letters ? (yes/no): ").strip().lower()
    include_special = input(
        "include special characters ? (yes/no): ").strip().lower()
    include_digits = input(
        "include digits ? (yes/no): ").strip().lower()
    if length < 1:
        print("password length must be at least 1")
        sys.exit(2.1)
        print("password length must be at least 4")
        
        
     


generate_password()