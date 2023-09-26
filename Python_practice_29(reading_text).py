import sys
import traceback
import logging
import numpy as np

string_width = 4

def read_from_txt():
    return np.loadtxt("INPUT.txt",  delimiter=' ', dtype="i")

try:
    lst = read_from_txt()
    print(lst[0][0])

except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")