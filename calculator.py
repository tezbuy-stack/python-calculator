#!/usr/bin/env python3
"""A beginner-friendly command-line calculator.

Supports addition, subtraction, multiplication, division, modulo and
power. Includes input validation, graceful handling of division by
zero, and an in-memory calculation history you can view at any time.

Run it with:

    python3 calculator.py

Standard library only — no third-party packages are needed.
"""

# The operators the calculator understands, mapped to their symbols.
OPERATORS = ("+", "-", "*", "/", "%", "**")


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return b subtracted from a."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b.

    Raises:
        ZeroDivisionError: if b is zero.
    """
    return a / b


def modulo(a, b):
    """Return the remainder of a divided by b.

    Raises:
        ZeroDivisionError: if b is zero.
    """
    return a % b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


# Map each operator symbol to the function that performs it.
OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "**": power,
}


def read_number(prompt):
    """Ask the user for a number and keep asking until it is valid.

    Returns:
        float: the number the user entered.
    """
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print(f"'{value}' is not a valid number. Please try again.")


def read_operator(prompt):
    """Ask the user for an operator and keep asking until it is valid.

    Returns:
        str: one of the supported operator symbols.
    """
    while True:
        operator = input(prompt).strip()
        if operator in OPERATORS:
            return operator
        print(
            f"'{operator}' is not a supported operator. "
            f"Choose one of: {', '.join(OPERATORS)}"
        )


def show_menu():
    """Print the main menu."""
    print("\n--- Calculator ---")
    print("1. New calculation")
    print("2. View history")
    print("3. Quit")
    print("------------------")


def show_history(history):
    """Print the calculation history, or a note if it is empty."""
    if not history:
        print("\nNo calculations yet. Do a calculation first!")
        return
    print("\n--- History ---")
    for index, entry in enumerate(history, start=1):
        print(f"{index}. {entry}")
    print("---------------")


def do_calculation(history):
    """Run one calculation: read two numbers and an operator, print the result."""
    first = read_number("Enter the first number: ")
    operator = read_operator(
        "Enter an operator (+, -, *, /, %, **): "
    )
    second = read_number("Enter the second number: ")

    try:
        result = OPERATIONS[operator](first, second)
    except ZeroDivisionError:
        print("Error: cannot divide by zero. Please try again.")
        return

    # Display whole numbers without a trailing ".0" for readability.
    def format_number(value):
        if value == int(value):
            return str(int(value))
        return str(value)

    entry = (
        f"{format_number(first)} {operator} {format_number(second)} "
        f"= {format_number(result)}"
    )
    print(f"\nResult: {entry}")
    history.append(entry)


def main():
    """Run the calculator menu loop until the user quits."""
    history = []
    print("Welcome to the Python Calculator!")
    print("Do simple arithmetic, and type 3 in the menu to quit.")

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            do_calculation(history)
        elif choice == "2":
            show_history(history)
        elif choice == "3":
            print("\nThanks for using the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
