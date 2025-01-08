"""
How many ways can 5 books be arranged on a shelf?
"""

# a function that return the total number of ways to arrange 
def permutation(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * permutation(n -1)

# initializing the number of books
no_books = 5

# calling the function
result = permutation(no_books)

# printing the result
print(f"{no_books} books can be arranged on a shelf in {result} ways")