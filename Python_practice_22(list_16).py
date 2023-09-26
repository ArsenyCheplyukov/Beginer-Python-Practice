import sys
import traceback
import logging

# Поменяйте значения переменных местами.

def trading_places(num_1, num_2):
    num_1, num_2 = num_2, num_1

try:
    num_1 = input("Print some number ")
    print("First number is :", num_1)
    num_2 = input("Print another number ")
    print("Second number is :", num_2)
    trading_places(num_1, num_2)
    print("Numbers change their places. Now number one is: ", num_1)
    print("and number two is: ", num_2)

except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")