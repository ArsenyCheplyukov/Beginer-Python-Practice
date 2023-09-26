import sys
import traceback
import logging

try:
    list = []
    list.append('h')
    list.append(1)
    list_2 = ['a', 'b', 'c']
    list.append(list_2)
    tpi = ('str')
    list.append(tpi)
    for i in range(len(list)):
        print(list[i])
    list.remove('a')
    print(list.count('b'))
    list.reverse()
    list.clear()
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")



