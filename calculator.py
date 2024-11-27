def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers and return their sum
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Sum of the two numbers
    """
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers and return their product
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Product of the two numbers
    """
    return a * b

def main():
    # Get input from user
    print("Welcome to Simple Calculator!")
    print("\nOperations available:")
    print("1. Addition")
    print("2. Multiplication")
    
    try:
        # Get operation choice
        choice = input("\nEnter operation number (1/2): ")
        if choice not in ['1', '2']:
            raise ValueError("Invalid operation choice")
            
        # Get numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Perform calculation based on choice
        if choice == '1':
            result = add_numbers(num1, num2)
            operation = 'sum'
        else:
            result = multiply_numbers(num1, num2)
            operation = 'product'
        
        # Display result
        print(f"\nThe {operation} of {num1} and {num2} is: {result}")
        
    except ValueError as e:
        if str(e) == "Invalid operation choice":
            print("Error: Please select a valid operation (1 or 2)!")
        else:
            print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    main()