import os
os.system('cls')

# ----------------------------------------PASSWORD GENERATOR--------------------------------------------------

from random import choice,shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("WELCOME TO THE RANDOM PASSWORD GENERATOR PROGRAM")
nr_letters = int(input("Please enter the number of letters you want in your password - "))
nr_numbers = int(input("Please enter the number of numbers you want in your password - "))
nr_symbols = int(input("Please enter the number of symbols you want in your password - "))

# Printing it serial wise and using for loops

# password = ""

# for letter in range(0,nr_letters):
#     password += random.choice(letters)

# for number in range(0,nr_numbers):
#     password += random.choice(numbers)

# for symbol in range(0,nr_symbols):
#     password += random.choice(symbols)

# print(f"Your generated password is; {password}")

# Method 2: Using list comprehension and shuffle from random module and at last joining them 

password_letters = [choice(letters) for letter in range(0,nr_letters)]
password_numbers = [choice(numbers) for number in range(0,nr_numbers)]
password_symbols = [choice(symbols) for symbol in range(0,nr_symbols)]

password_list = password_letters + password_numbers + password_symbols
shuffle(password_list)

generated_password = "".join(password_list)

print(f"Your generated password is; {generated_password}")

 
