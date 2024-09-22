# Calculator With Function            
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

# Function to display the menu and get user's choice
def get_operation():
    print("WellCome to the Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")

    choice = input("Enter choice (1/2/3/4/5/6): ")
    return choice

# Function to perform the selected operation
def perform_calculation(choice, num1, num2):
    if choice == '1':
        return add(num1, num2)
    elif choice == '2':
        return subtract(num1, num2)
    elif choice == '3':
        return multiply(num1, num2)
    elif choice == '4':
        return divide(num1, num2)
    elif choice == '5':
        return power(num1, num2)
    elif choice == '6':
        return modulus(num1, num2)
    else:
        return "Invalid Input"

# Main function to run the calculator
def calculator():
    while True:
        choice = get_operation()

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter numeric values.")
            continue

        result = perform_calculation(choice, num1, num2)
        print(f"Result: {result}")

        # Ask if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

# Run the calculator
if __name__ == "__main__":
    calculator()