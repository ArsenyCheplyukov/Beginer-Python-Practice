import sys
import traceback
import logging
import collections

# Напишите программу, которая принимает текст и выводит два слова:
# наиболее часто встречающееся и самое длинное.

text = 'lorem ipsum dolor sit amet amet amet'

try:
    string = text.split()
    counter = collections.Counter(string)
    most_common, occurrences = counter.most_common()[0]
    longest = max(string, key=len)
    print("The common word is: ", most_common, ". And the longest is: ", longest)

except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")