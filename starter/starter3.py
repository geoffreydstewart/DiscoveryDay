# PROGRAMMING PROJECT #1

# 1. Change the function name from sum to add. Run the program to make sure your change worked.

# 2. Write a new function called multiply. It should be quite similar to your add function, but
#    multiplies 2 numbers instead. Hint: use the * character to multiply numbers.

# 3. Make a copy of the line at the bottom that starts with print and paste it on the next line
#    so there are two lines identical lines that start with print.

def add(a, b):
    return (a + b)

def multiply(a, b):
    return (a * b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {add(a, b)}')
print(f'Sum of {a} and {b} is {add(a, b)}')

# 4. Change the new second print statement to call the new multiply function. Run the program
#    to make sure everything is working.

