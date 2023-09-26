import sys
import traceback
import logging

# Напишите код, который переводит целое число в строку, 
# при том что его можно применить в любой системе счисления.

string_1 = 'ABC'

def transform_to_int(some_string):
    return int(some_string, 16)

try:
    print(transform_to_int(string_1))
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")