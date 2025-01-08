"""
A committee of 4 members is to be formed from 6 men and 5 women. How many ways can this be done if the committee must include at least 2 women
"""

# a function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# a function to calculate the combination
def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

# From above question:
# Case I: 2 women out of 5 and 2 man out of 6
res1 = combination(5, 2) * combination(6, 2)
# case II: 3 women out of 5 and 1 man out of 6
res2 = combination(5, 3) * combination(6, 1)

# adding result 1 and result 2
result = res1 + res2

# printing out the total combinations
print(f"Total combination = {result}")