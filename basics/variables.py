# variables.py
# This script demonstrates how to declare and print variables in Python.

def main():
    print("--- Variable Declaration and Printing ---")

    # 1. String variable
    greeting = "Hello, Python world!"
    print(f"String variable: {greeting}")

    # 2. Integer variable
    age = 25
    print(f"Integer variable: {age}")

    # 3. Float variable
    price = 19.99
    print(f"Float variable: {price}")

    # 4. Boolean variable
    is_learning = True
    print(f"Boolean variable: {is_learning}")

    # 5. Multiple assignment
    x, y, z = 1, 2, 3
    print(f"Multiple assignment (x, y, z): {x}, {y}, {z}")

    # 6. Reassigning variables
    count = 10
    print(f"Initial count: {count}")
    count = count + 1
    print(f"Updated count: {count}")

if __name__ == "__main__":
    main()
