#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer using recursion.
    
    Parameters:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of the number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = factorial(int(sys.argv[1]))
        print(f)
