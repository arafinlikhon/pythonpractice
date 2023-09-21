"""
calculator condition :

1. Functionality: The most critical aspect is whether the calculator functions correctly. 
   It should accurately perform arithmetic operations (addition, subtraction, multiplication,
   division) and handle more advanced functions if included (trigonometric, logarithmic, etc.).


2. Code Quality: The condition of the code is crucial. Well-structured, clean, and well-documented
   code is easier to maintain and less prone to bugs. Well-named variables and functions enhance code readability.


3. Error Handling: A good Python calculator should handle user input errors gracefully, providing clear error messages or prompts 
   when necessary.



 I'm gonna make a calculator within these condition 
 
"""


"""
addition
"""
def addition(*args):
    result = sum(args)
    return result

""" 
subtraction
"""


def subtraction(*args):
    if len(args) < 2:
        raise ValueError("Subtraction requires at least two numbers.")
    
    result = args[0] - sum(args[1:])
    return result


"""
multiplication
"""

def multiplication(*args):
    if len(args) < 2:
        raise ValueError("Multiplication requires at least two numbers.")
    
    result = 1
    for num in args:
        result *= num
    return result

"""
division
"""

def division(*args):
    if len(args) < 2:
        raise ValueError("Division requires at least two numbers.")
    
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("Division by zero is not allowed.")
        result /= num
    return result

print("Select an operation:")
print("0 - Addition")
print("1 - Subtraction")
print("2 - Multiplication")
print("3 - Division")
print("4 - Trigonometric functions (sin, cos, tan)")
print("5 - Logarithmic functions (log10, ln)")

action = int(input("Enter the number corresponding to your choice: "))

# Get the numbers to operate on
numbers = []
while True:
    num = input("Enter a number (or 'done' to calculate): ")
    if num == 'done':
        break
    try:
        num = float(num)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done' to calculate.")

# Perform the selected operation
if action == 0:
    result = addition(*numbers)
    print("The result of addition is:", result)
elif action == 1:
    result = subtraction(*numbers)
    print("The result of subtraction is:", result)
elif action == 2:
    result = multiplication(*numbers)
    print("The result of multiplication is:", result)
elif action == 3:
    result = division(*numbers)
    print("The result of division is:", result)
elif action == 4:
    if len(numbers) != 1:
        print("Trigonometric functions require exactly one number.")
    else:
        num = numbers[0]
        print("sin(", num, ") =", math.sin(num))
        print("cos(", num, ") =", math.cos(num))
        print("tan(", num, ") =", math.tan(num))
elif action == 5:
    if len(numbers) != 1:
        print("Logarithmic functions require exactly one number.")
    else:
        num = numbers[0]
        print("log10(", num, ") =", math.log10(num))
        print("ln(", num, ") =", math.log(num))



else:
    print("Invalid action. Please enter a valid operation (0, 1, 2, 3, 4, or 5).")