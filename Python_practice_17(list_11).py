import sys
import traceback
import logging

# При заданном целом числе n посчитайте n + nn + nnn

def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

try:
    solve(5)

except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")