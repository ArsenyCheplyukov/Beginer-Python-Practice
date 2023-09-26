import sys
import traceback
import logging

# Сложите цифры целого числа

def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

try:
    values = input("Print something ")
    print("You printed :")
    print("Sum of digits is: ", sum_digits(values))
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")