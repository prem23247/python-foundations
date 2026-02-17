# if_else.py
# This script demonstrates conditional logic using if, elif, and else statements.

def main():
    print("--- Conditional Logic (If/Else) ---")

    # Get user input for checking
    try:
        score = int(input("Enter a score (0-100): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Using if-elif-else to determine grade
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

    # Nested if statement example
    if score >= 60:
        if score == 100:
            print("Perfect score! Keep it up.")
        else:
            print("You passed.")
    else:
        print("You failed. Better luck next time.")

if __name__ == "__main__":
    main()
