# functions_intro.py
# This script demonstrates how to define and call simple functions.

def greet(name):
    """
    A simple function that prints a greeting.
    """
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """
    A function that takes two numbers and returns their sum.
    """
    return a + b

def calculate_area(length, width=1):
    """
    A function with a default parameter value.
    Calculates the area of a rectangle.
    """
    return length * width

def main():
    print("--- Functions in Python ---")

    # Calling a function with one argument
    greet("Python Learner")

    # Calling a function with return value
    sum_result = add_numbers(5, 7)
    print(f"Sum of 5 and 7 is: {sum_result}")

    # Calling a function with default arguments
    area1 = calculate_area(5, 3)
    print(f"Area with length 5 and width 3: {area1}")

    area2 = calculate_area(5) # usage of default width=1
    print(f"Area with length 5 (default width 1): {area2}")

if __name__ == "__main__":
    main()
