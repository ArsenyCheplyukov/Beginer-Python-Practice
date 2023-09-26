import sys
import traceback
import logging

# Напишите программу, которая принимает два списка и выводит все элементы первого,
# которых нет во втором.

set_1 = set(['White', 'Black', 'Red'])
set_2 = set(['Red', 'Green'])

def unique_from_two_lists(some_list_1, some_list_2):
    answer_list = some_list_1 - some_list_2
    return answer_list

try:
    print(unique_from_two_lists(set_1, set_2))
    
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")