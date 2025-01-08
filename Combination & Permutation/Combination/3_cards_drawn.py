"""
How many ways can 3 cards be drawn from a deck of 52 cards if the order doesn't matter?
"""
# function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# function to calculate the combination 
def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))
    
# initializing the values
total_cards = 52
no_of_card = 3

# calling the combination() function
result = combination(total_cards, no_of_card)

# printing out the result
print(f"In {result} ways can {no_of_card} cards be drawn from a deck of {total_cards} cards if the order doesn't matter")

# output:
#   In 22100.0 ways can 3 cards be drawn from a deck of 52 cards if the order doesn't matter