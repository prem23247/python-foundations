# loops.py
# This script demonstrates loops (for, while) and the for-else construct.

def main():
    print("--- Loops in Python ---")

    # 1. For Loop
    # Iterating over a range of numbers
    print("Counting from 1 to 5 using for loop:")
    for i in range(1, 6):
        print(i, end=" ")
    print("\n")

    # 2. While Loop
    # Repeating code while a condition is true
    print("Countdown using while loop:")
    count = 5
    while count > 0:
        print(count, end=" ")
        count -= 1
    print("\n")

    # 3. For-Else Loop
    # The else block runs if the loop completes normally (without break)
    print("Checking for even numbers in a list:")
    numbers = [1, 3, 5, 7, 9]
    for num in numbers:
        if num % 2 == 0:
            print(f"Found an even number: {num}")
            break
    else:
        print("No even numbers found in the list.")

if __name__ == "__main__":
    main()
