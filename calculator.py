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

def main():
    # Get input from user
    print("Welcome to Simple Calculator!")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Calculate sum
        result = add_numbers(num1, num2)
        
        # Display result
        print(f"\nThe sum of {num1} and {num2} is: {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

if __name__ == "__main__":
    main()