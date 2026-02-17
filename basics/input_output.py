# input_output.py
# This script demonstrates how to take user input and format output.

def main():
    print("--- Input and Output ---")

    # Taking string input
    # input() always returns a string.
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

    # Taking integer input
    # We must convert (cast) the input string to an integer.
    try:
        age_str = input("Enter your age: ")
        age = int(age_str)
        print(f"You will be {age + 1} years old next year.")
    except ValueError:
        print("Invalid input! Please enter a number for your age.")
        return

    # Output formatting examples
    print("\n--- value Formatting ---")
    
    item = "Coffee"
    cost = 4.50
    
    # Using f-strings (Recommended)
    print(f"Item: {item}, Cost: ${cost:.2f}")
    
    # Using .format() method
    print("Item: {}, Cost: ${:.2f}".format(item, cost))
    
    # Using concatenation (Not recommended for mixing types)
    print("Item: " + item + ", Cost: $" + str(cost))

if __name__ == "__main__":
    main()
