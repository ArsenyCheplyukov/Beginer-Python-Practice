import sys
import traceback
import logging

num = 15
letter = 'o'
break_number = 1

def less_than_five(some_list):
    print(list(filter(lambda elem: elem < 5, some_list)))

def sorting_for_simmilar(some_list_1, some_list_2):
    return list(filter(lambda elem: elem in some_list_1, some_list_2))

def addition(*a):
    result = {}
    result.update(a)
    return result

def transform_to_int(some_string):
    return int(some_string, 16)

def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]

def is_palindrome(string):
    return string == string[::-1]

def convert(seconds):
    if seconds >= 86400:
        days = seconds // (24 * 3600)
        seconds %= 24 * 3600
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
    elif seconds >= 3600:
        days = 0
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
    elif seconds >= 60:
        days  = 0
        hours = 0
        minutes = seconds // 60
        seconds %= 60    
    else: 
        days    = 0
        hours   = 0
        minutes = 0
    print(f'{days}:{hours}:{minutes}:{seconds}')

def transformation_tup(ints_as_strings):
    ints = map(int, ints_as_strings)
    lst = list(ints)
    tup = tuple(lst)
    return tup

def print_last_and_first(some_list):
    print(f'First: {some_list[0]}; Last: {some_list[-1]}')

def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

def breaking_printing(some_list):
    for x in some_list:
        if x == break_number:
            break
        elif x % 2 == 0:
            print(x)

def unique_from_two_lists(some_list_1, some_list_2):
    answer_list = some_list_1 - some_list_2
    return answer_list

def sum_of_numbers_of_digit(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

def counting_letter(some_string):
    return some_string.count(letter)

def reading_list(ints_as_strings):
    values = input("Enter numbers through comma ")
    ints_as_strings = values.split(',')
    ints = map(int, ints_as_strings)
    lst = list(ints)
    return lst

def find_unique(some_list):
    return len(some_list) == len(set(some_list))

def throw_numbers_that_divided_by_num(some_list):
    return list(filter(lambda x: not x % num, some_list))

def trading_places(num_1, num_2):
    num_1, num_2 = num_2, num_1



try:
    values = input("Print something ")
    print("You printed :")
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")