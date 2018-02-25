
"""
Write a password generator in Python. Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
"""

import random
import string

words = ['dog', 'hockey', 'coffee', 'society', 'dinner', 'show', 'manchester', 'toronto', 'bastetball', 'misplay', 'mercedes', 'perrier']
digits = list(string.digits)
special = list(string.punctuation)


def passwordGenerator():

    count = int(input("Enter the amount of characters you would like for your password: \n"))
    
    characters = list(words + digits + special)

    password = ""

    for x in range(0,count):
        password += random.choice(characters)
    print(password)

passwordGenerator()