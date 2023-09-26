import sys
import traceback
import logging

# С помощью анонимной функции извлеките из списка числа, делимые на 15.

num = 15
list_1 = [45, 55, 60, 37, 100, 105, 220]

def throw_numbers_that_divided_by_num(some_list):
    return list(filter(lambda x: not x % num, some_list))

try:
    print("New list is: ", throw_numbers_that_divided_by_num(list_1))
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")