# data_types.py
# This script demonstrates fundamental data types in Python: int, float, string, and list.

def main():
    print("--- Python Data Types ---")

    # 1. Integer (int)
    # Whole numbers, positive or negative, without decimals.
    my_int = 100
    print(f"Type of {my_int} is: {type(my_int)}")

    # 2. Floating-point number (float)
    # Numbers with a decimal point.
    my_float = 3.14
    print(f"Type of {my_float} is: {type(my_float)}")

    # 3. String (str)
    # Sequence of characters enclosed in quotes.
    my_string = "Python is fun"
    print(f"Type of '{my_string}' is: {type(my_string)}")

    # 4. List (list)
    # Ordered, mutable collection of items.
    my_list = [1, 2, 3, "four", 5.0]
    print(f"Type of {my_list} is: {type(my_list)}")
    print(f"List content: {my_list}")

    # Demonstrating simple type conversion (casting)
    print("\n--- Type Casting ---")
    float_from_int = float(my_int)
    print(f"Integer {my_int} cast to float: {float_from_int}")

    int_from_float = int(my_float)
    print(f"Float {my_float} cast to integer: {int_from_float}")

    str_from_int = str(my_int)
    print(f"Integer {my_int} cast to string: '{str_from_int}'")

if __name__ == "__main__":
    main()
