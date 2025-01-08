"""
How many ways can 6 people be arranged around a circular table
"""
# function to find the factorial of a number
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# initializing the no. of people
total_people = 6

# calling the function to find the total no. of arrangement on a circular table
result = factorial(total_people-1)

# printing out the result
print(f"Total no. of arrangement = {result}")

# output: Total no. of arrangement = 120