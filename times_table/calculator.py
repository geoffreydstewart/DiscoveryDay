import sys

def add(a, b):
    sum = a + b
    return sum

def multiply(a, b):
    product = a * b
    return product

def substract(a, b):
    difference = a - b
    return difference

def divide(a, b):
    quotient = a / b
    return quotient

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
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
    result = divide(a, b * 1.0)
    op_name = 'Quotient'
else:
    print(f'{op} is not a valid operation!')
    sys.exit()


print(f'{op_name} of {a} and {b} is {result}')
