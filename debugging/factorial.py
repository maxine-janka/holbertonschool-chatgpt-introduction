#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  
    return result

if len(sys.argv) > 1:
    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            f = factorial(number)
            print(f"The factorial of {number} is {f}")
    except ValueError:
        print("Please provide a valid integer.")
else:
    print("Usage: python script_name.py <number>")