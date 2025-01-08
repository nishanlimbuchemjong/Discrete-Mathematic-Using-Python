"""
Let A={1,2} and B={a,b,c}. Find AXB.
"""

# initializing the set
A = {1, 2}
B = {'a', 'b', 'c'}

# creating an empty set to store all the cartesian product
cartesian_product = []

# finding out the cartesian product of set A and set B
for a in A:
    for b in B:
        cartesian_product.append((a, b))

# finding the cartesian product of set A and B
print(cartesian_product)
