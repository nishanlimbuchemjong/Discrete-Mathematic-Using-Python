"""
How many different ways can the letters of the word "ALGORITHM" be arranged?
"""

# a function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# initializing the word   
word = "ALGORITHM"

# finding the total no. of letters in the given word
total_letters = len(word)

# finding the total no. of arrangement
result = factorial(total_letters)

# printing out the result
print(f"The letters of the word 'ALGORITHM' cam be arramged in {result} ways")