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
      
      
      
    if length < 4:
      print("password length must be at least 4 characters.")

      return
      
     
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else  ""
    special = string.punctuation if include_special == "yes" else  ""
    digits = string.digits if include_special == "yes" else  ""
    all_characters = lower + uppercase + special + digits 
    
    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

   
    remaining_length = length - len(required_characters)
    password = required_characters + random.choices(all_characters, k=remaining_length)
        
    for _ in range(remaining_length):
       character = random.choice(all_characters)
       password.append(character)
       
       random.shuffle(password)
       
       print(password)
        
        
  


generate_password()