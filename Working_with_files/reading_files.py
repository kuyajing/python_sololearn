'''
Reading Files
You need to make a program to read the given number of characters of a file.
Take a number N as input and output the first N characters of the books.txt file.

The given code opens the books.txt file. Use the file object to read the content of the file.
'''

file = open("/usercode/files/books.txt")
#your code goes here

n=int(input())

reader=file.read(n)
print(reader)