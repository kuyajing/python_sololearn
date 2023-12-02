'''
You are given code that should calculate the corresponding percentage of a price.
Somebody wrote a lambda function to accomplish that, however the lambda is wrong.
Fix the code to output the given percentage of the price.

Sample Input
50
10

Sample Output
5.0

The first input is the price, while the second input is the percentage we need to calculate: 10% of 50 is 5.0.

    '''

price = int(input())
perc = int(input())

res = (lambda x,y: x*(y/100))(price, perc)

print(res)
