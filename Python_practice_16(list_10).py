import sys
import traceback
import logging

# Выведите первый и последний элемент списка

def transformation_lst(ints_as_strings):
    ints = map(int, ints_as_strings)
    lst = list(ints)
    return lst

def print_last_and_first(some_list):
    print(f'First: {some_list[0]}; Last: {some_list[-1]}')

try:
    values = input("Enter numbers through comma ")
    ints_as_strings = values.split(',')
    lst = transformation_lst(ints_as_strings)
    print("List: ", lst)
    print_last_and_first(lst)

except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")