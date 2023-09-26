import sys
import traceback
import logging

# Нужно проверить, все ли числа в последовательности уникальны.

def transformation_lst(ints_as_strings):
    ints = map(int, ints_as_strings)
    lst = list(ints)
    return lst

def find_unique(some_list):
    return len(some_list) == len(set(some_list))

try:
    values = input("Enter numbers through comma ")
    ints_as_strings = values.split(',')
    string = transformation_lst(ints_as_strings)
    print("Is it list unique: ", find_unique(string))

except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")