import sys
import traceback
import logging

# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

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

try:
    input = int(input("Please enter something: "))
    print("You print: ", input)
    convert(input)
except ValueError:
    print("You entered incorrect data")
except Exception as e:
    print(e)
print("Ending program")