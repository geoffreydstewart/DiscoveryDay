import sys

def add(a, b):
    return (a + b)

def multiply(a, b):
    return (a * b)

def substract(a, b):
    return (a - b)

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero!")
        return "Undefined"
    else:
        return (a / b)

a = float(input('Enter 1st number: '))
b = float(input('Enter 2nd number: '))
op = input('Enter the operation (+, *, -, /): ')

op_name = ''
result = 0

if op == '+':
    result = add(a, b)
    op_name = 'Sum'
elif op == '*':
    result = multiply(a, b)
    op_name = 'Product'
elif op == '-':
    result = substract(a, b)
    op_name = 'Difference'
elif op == '/':
    result = divide(a, b)
    op_name = 'Quotient'
else:
    print(f'{op} is not a valid operation!')


print(f'{op_name} of {a} and {b} is {result}')
