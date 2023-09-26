import sys
import traceback
import logging

letter = 'o'

def counting_letter(some_string):
    return some_string.count(letter)

try:
    values = str(input("Print something "))
    print("You printed :")
    print("We have letter '", letter, "' there ", counting_letter(values), " times")
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")