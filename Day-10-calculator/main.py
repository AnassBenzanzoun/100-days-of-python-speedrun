import re

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


expression = input("Enter the expression: ")

# Split the expression by any of the operation symbols
expression = re.split("(\+|-|\*|/)", expression)

# Remove any whitespace from the split results
expression = [item.strip() for item in expression if item.strip() != ""]
result = operations[expression[1]](int(expression[0]), int(expression[2]))
print(f"{expression[0]} {expression[1]} {expression[2]} = {result}")
