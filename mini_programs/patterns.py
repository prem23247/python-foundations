# patterns.py
# This script prints numeric and star patterns.

def print_star_pyramid(rows):
    """
    Prints a pyramid of stars.
    """
    print("\nStar Pyramid:")
    for i in range(1, rows + 1):
        # Print spaces
        print(" " * (rows - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

def print_numeric_pattern(rows):
    """
    Prints a right-angled triangle pattern of numbers.
    1
    1 2
    1 2 3
    """
    print("\nNumeric Pattern:")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    print("--- Pattern Printing ---")
    try:
        rows = int(input("Enter number of rows: "))
        print_star_pyramid(rows)
        print_numeric_pattern(rows)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
