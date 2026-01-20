def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers with zero division handling."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def main():
    """Main function to run the calculator."""
    operations = {
        '+': (add, '+'),
        '-': (subtract, '-'),
        '*': (multiply, '*'),
        '/': (divide, '/'),
    }
    
    print("=== Simple Calculator ===")
    print("Supported operations: + (add), - (subtract), * (multiply), / (divide)")
    print()
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ").strip()
            
            if operation not in operations:
                print("Invalid operation. Please use +, -, *, or /.\n")
                continue
            
            num2 = float(input("Enter second number: "))
            
            func, symbol = operations[operation]
            result = func(num1, num2)
            
            print(f"\n{num1} {symbol} {num2} = {result}\n")
            
        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Error: Invalid input. Please enter valid numbers.\n")
        
        again = input("Calculate again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()