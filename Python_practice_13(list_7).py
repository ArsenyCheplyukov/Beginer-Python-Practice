import sys
import traceback
import logging

#Напишите проверку на то, является ли строка палиндромом.

def is_palindrome(string):
    return string == string[::-1]

try:
    var = input("Please enter something: ")
    print("You entered :", var)
    print("Is it palindrome :" , is_palindrome(var))
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")