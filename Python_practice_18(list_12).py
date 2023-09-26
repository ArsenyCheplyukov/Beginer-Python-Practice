import sys
import traceback
import logging

# Напишите программу, которая выводит чётные числа из введённого списка
# и останавливается, если встречает число 1

break_number = 1

def transformation_lst(ints_as_strings):
    ints = map(int, ints_as_strings)
    lst = list(ints)
    return lst

def breaking_printing(some_list):
    for x in some_list:
        if x == break_number:
            break
        elif x % 2 == 0:
            print(x)

try:
    values = input("Enter numbers through comma ")
    ints_as_strings = values.split(',')
    lst = transformation_lst(ints_as_strings)
    breaking_printing(lst)

except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")