# prime_numbers.py
# This script prints prime numbers up to a specified number n using a for-else loop.

def is_prime(num):
    """
    Checks if a number is prime.
    """
    if num <= 1:
        return False
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_till_n(n):
    """
    Prints all prime numbers from 2 up to n.
    """
    print(f"Prime numbers up to {n}:")
    for num in range(2, n + 1):
        # Using for-else to find primes without a separate function call for demonstration
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            # This block executes if the loop completes without finding a factor
            print(num, end=" ")
    print()

def main():
    print("--- Prime Number Generator ---")
    try:
        limit = int(input("Enter the limit (n): "))
        print_primes_till_n(limit)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
