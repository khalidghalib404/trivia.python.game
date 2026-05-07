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


def generate_password():
    length = int( input("input the desired password length: ").strip())
    include_uppercase = input(
        "include uppercase letters ? (yes/no): ").strip().lower()
    include_special = input(
        "include special characters ? (yes/no): ").strip().lower()
    include_digits = input(
        "include digits ? (yes/no): ").strip().lower()


generate_password()