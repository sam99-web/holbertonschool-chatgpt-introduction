#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    
    The factorial of a number n is the product of all positive integers
    less than or equal to n. For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.
    This function uses a recursive approach where factorial(n) = n * factorial(n-1).
    
    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.
    
    Returns:
        int: The factorial of the input number n.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("The number must be non-negative.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except IndexError:
        print("Usage: ./script.py <number>")
    except ValueError as e:
        print("Error:", e)

