# Calculator, making operations with floats


operations = ('+', '-', '*', '/') # tuple

# Ask for inputs and convert strings to floats
print("Welcome to Calculator!")
print("Operators: +, -, /, *")

def calculator():
    result = 0
    operator = ''

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        # loops until a valid operator:
        while operator not in operations:
            operator = input("Enter an operator: ")
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
        print(result)

    except ValueError: # catches error if input cannot be converted to float; starts over
        print("Invalid entry")
        calculator()

# Prompts user if they want to continue
while True:
    calculator()
    if input("Start over? (Y/N) ").lower() != 'y':
        break

