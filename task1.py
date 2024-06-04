def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Simple Calculator")
    
  
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
   
    print("Choose the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Enter the number of the operation (1/2/3/4): ")
    
    if operation == '1':
        print(f"The result is: {add(num1, num2)}")
    elif operation == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif operation == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid operation selected.")

calculator()
