#!/bin/python

def div(a, b):
    return a / b


try:
    print(div(10,15))

except ZeroDivisionError:
    print("Zero error exception")
finally:
    print("Program exited successfully")

