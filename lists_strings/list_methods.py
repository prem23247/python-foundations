# list_methods.py
# This script demonstrates common list methods in Python.

def main():
    print("--- List Methods ---")
    
    # Initialize a list
    fruits = ["apple", "banana", "cherry"]
    print(f"Original list: {fruits}")

    # 1. append(): Adds an item to the end
    fruits.append("orange")
    print(f"After append('orange'): {fruits}")

    # 2. insert(): Inserts an item at a specific index
    fruits.insert(1, "blueberry")
    print(f"After insert(1, 'blueberry'): {fruits}")

    # 3. remove(): Removes the first occurrence of an item
    if "banana" in fruits:
        fruits.remove("banana")
    print(f"After remove('banana'): {fruits}")

    # 4. pop(): Removes and returns the item at a specific index (default is last)
    popped_fruit = fruits.pop()
    print(f"Popped item: {popped_fruit}")
    print(f"After pop(): {fruits}")

    # 5. sort(): Sorts the list in ascending order
    fruits.sort()
    print(f"After sort(): {fruits}")

    # 6. reverse(): Reverses the order of the list
    fruits.reverse()
    print(f"After reverse(): {fruits}")

    # 7. clear(): Removes all items
    fruits.clear()
    print(f"After clear(): {fruits}")

if __name__ == "__main__":
    main()
