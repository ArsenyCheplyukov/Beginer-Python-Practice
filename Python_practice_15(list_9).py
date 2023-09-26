import sys
import traceback
import logging

# Вы принимаете от пользователя последовательность чисел,
# разделённых запятой. Составьте список и кортеж с этими числами.

def transformation_lst(ints_as_strings):
    ints = map(int, ints_as_strings)
    lst = list(ints)
    return lst

def transformation_tup(ints_as_strings):
    tup = tuple(transformation_lst(ints_as_strings))
    return tup

try:
    values = input("Enter numbers through comma ")
    ints_as_strings = values.split(',')
    lst = transformation_lst(ints_as_strings)
    tup = transformation_tup(ints_as_strings)
    print("List: ", lst)
    print("Tuple: ", tup)
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")