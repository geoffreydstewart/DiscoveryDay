# PROGRAMMING PROJECT #2

# 1. Delete all the code, except for your multiply function. Now, Type in the following code,
#    below the multiply function, which print the numbers from 0 to 12.

for i in range(13):
    print(f'{i} ')

# 2. Using your multiply function can you print out times table for 9?
#  0
#  9
#  18
# ...
#  108

# 3. In programming, parts of the code can be conditionally executed. For example:

if 10 > 5:
    print('Of course 10 is bigger than 5!')

#    How could you use this to change your program to only display results greater than 50?

def multiply(a, b):
    product = a * b
    return product

for i in range(13):
    product = multiply(i, 9)
    if product > 50:
        print(f'{product} ')

# 4. How could you write a calculator program?