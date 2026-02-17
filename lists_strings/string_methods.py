# string_methods.py
# This script demonstrates common string methods in Python.

def main():
    print("--- String Methods ---")

    text = "  Python Programming is Fun!  "
    print(f"Original string: '{text}'")

    # 1. strip(): Removes leading/trailing whitespace
    clean_text = text.strip()
    print(f"After strip(): '{clean_text}'")

    # 2. lower() and upper(): Case conversion
    print(f"Lowercase: {clean_text.lower()}")
    print(f"Uppercase: {clean_text.upper()}")

    # 3. replace(): Replaces constraints of a substring
    replaced_text = clean_text.replace("Fun", "Great")
    print(f"After replace('Fun', 'Great'): {replaced_text}")

    # 4. split(): Splits string into a list of substrings
    words = clean_text.split(" ")
    print(f"After split(): {words}")

    # 5. join(): Joins elements of a specific iterable into a single string
    joined_text = "-".join(words)
    print(f"After join('-'): {joined_text}")

    # 6. find(): Returns the index of the first occurrence of a substring
    index = clean_text.find("Program")
    print(f"Index of 'Program': {index}")

    # 7. count(): Occurrences of a substring
    count_o = clean_text.count("o")
    print(f"Count of 'o': {count_o}")

if __name__ == "__main__":
    main()
