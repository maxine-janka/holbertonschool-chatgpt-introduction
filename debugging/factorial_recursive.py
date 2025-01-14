#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given integer n. If n is 0, returns 1 as 0! is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    # Convert the first command-line argument to an integer and calculate its factorial.
    f = factorial(int(sys.argv[1]))
    print(f)