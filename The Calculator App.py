# Task 1: Create functions for each arithmetic operation.

# Answer:
# Task 1: Create functions for each arithmetic operation

#Answer:
# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    # Check if the denominator is zero
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


# Task 2: Use inputs to ask the user what operation they 
# want to perform, and what numbers they want to use.

# Answer:
# Display available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user for the operation
operation = input("Enter choice (1/2/3/4): ")

# Take input from the user for the numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# Task 3: Ensure your code can handle division by zero 
# and other potential errors. So if you divide by 0, 
# there is error handling set up to prevent an error 
# from showing in the console.

# Answer:
# Perform the selected operation and handle potential errors
if operation == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == '4':
    result = divide(num1, num2)
    if result == "Error! Division by zero.":
        print(result)
    else:
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid input! Please enter a valid operation choice.")

