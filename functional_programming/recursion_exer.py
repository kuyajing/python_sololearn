'''factorial example'''
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

print(factorial(5))


'''Recursion exxam
Recursion
The given code defines a recursive function convert(), which needs to convert its argument from decimal to binary.
However, the code has an error.
Fix the code by adding the base case for the recursion, then take a number from user input and call the convert() function, to output the result.

Sample Input
8

Sample Output
1000

The binary representation of 8 is 1000.

PY
'''

def convert(num): 

    if num == 0:
        return "0"
    else:
        return num % 2 + 10 * int(convert(num // 2))

# Test the function
test=input()
a=int(test)
print(convert(a))