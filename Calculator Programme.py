from art import logo

# Add
def add(n1, n2):
  """Adds two numbers."""
  return n1 + n2

# Subtract
def subtract(n1, n2):
  """Subtracts the second number from the first number"""
  return n1 - n2

# Multiply
def multiply(n1, n2):
  """Multiplies both numbers"""
  return n1 * n2

# Divide
def divide(n1, n2):
  """Divides the first number by the second number."""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))

  want_to_continue = True
  while want_to_continue:
    for operation in operations:
      print(operation)
    operation_symbol = input("Pick an operation: ")

    num2 = float(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      want_to_continue = False
      calculator()

calculator()
