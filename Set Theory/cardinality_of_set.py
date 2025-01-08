"""
If |A|=5 and |B|=3, find the number of elements in AUB, given |A∩B|=2

"""

# defining a function that returns a number of elements
def num_of_elements(a, b, common):
    return a + b - common

# given number of elements
a = 5       # |A|=5
b = 3       # |B|=3
common = 2  # |A∩B|=2

# calling the function
result = num_of_elements(a, b, common)

# printing out the total number of elements in AUB
print(f"Number of elements in AUB = {result}")      # output: Number of elements in AUB = 6
