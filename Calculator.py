# calculator.py
# A simple command-line calculator using functions and loops

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers, handling division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    print("===== Simple Python Calculator =====")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Validate choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        # Take user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform the chosen operation
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print(f"Result: {result}")

if __name__ == "__main__":
    main()
