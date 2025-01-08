"""
How many 3-letter words can be formed from the alphabet (26 letters) where repetition of letters is allowed?
"""
# initializing the values
total_letters = 26
no_of_letters = 3

# the above questions says that 3-letter words can be formed from 26 letters of alphabets where repetition of letters is allowed
# calculating the permutation
result = total_letters**no_of_letters

# printing out the result
print(f"Total number of 3-letters words = {result}")

# output: Total number of 3-letters words = 17576