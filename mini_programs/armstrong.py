# armstrong.py
# This script checks if a given number is an Armstrong number.
# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

def is_armstrong(num):
    # Convert number to string to easily iterate over digits
    str_num = str(num)
    num_digits = len(str_num)
    
    sum_of_powers = 0
    for digit in str_num:
        sum_of_powers += int(digit) ** num_digits
        
    return sum_of_powers == num

def main():
    print("--- Armstrong Number Checker ---")
    try:
        number = int(input("Enter a number to check: "))
        if is_armstrong(number):
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is NOT an Armstrong number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
