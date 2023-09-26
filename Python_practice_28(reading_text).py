import numpy as np
import sys
import traceback
import logging

string_width = 4

def reading():
    quarters = []
    for line in open("INPUT.txt", "r").read().split("\n"):
        for x in line[1:len(line)].split():
            quarters.append(sum(list(map(lambda c: int(c),x.split(",")))))
    return(quarters)

def qwerty():
    return np.loadtxt("INPUT.txt", dtype='i', delimiter=' ')

def tranformation_to_2d_string(some_list, elem_num):
    print("length of list is: ", len(some_list))
    print("list: ", some_list)
    print("number of elements is: ", elem_num)
    two_d_list = []
    for a in range(len(some_list) // elem_num):
        print(len(some_list) // elem_num)
        for b in range(elem_num):
            two_d_list[a].append(some_list[(a * elem_num) + b])
            print(two_d_list[a][b])
    return two_d_list

try:
    lst = reading()
    lst_2 = tranformation_to_2d_string(lst, string_width)

except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")