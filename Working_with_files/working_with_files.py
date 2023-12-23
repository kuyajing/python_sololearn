'''
Working with Files
You are given a books.txt file, which includes book titles, each on a separate line.
Create a program to output how many words each title contains, in the following format:
Line 1: 3 words
Line 2: 5 words
...

Make sure to match the above mentioned format in the output.

To count the number of words in a given string, you can use the split() function, or, alternatively, 
count the number of spaces (for example, if a string contains 2 spaces, then it contains 3 words).'''


# Open the books.txt file
with open("/usercode/files/books.txt") as f:
   #your code goes here
   # Read the lines from the file
   lines = f.readlines()



# Process each line and count the words
for i, line in enumerate(lines, start=1):
    # Use split() to count the number of words
    word_count = len(line.split())
    
    # Output the result
    print(f"Line {i}: {word_count} words")
