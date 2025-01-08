"""
Let 
A={1,2,3,4} and 
B={3,4,5,6}. Find:
a) AUB
b) A∩B
c) A-B

"""
# initializing values of A and B set
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# finding the union, intersection, and difference
union_result = A.union(B)
intersection_result = A.intersection(B)
difference_result = A.difference(B)

# printing all the result
print(f"AUB = {union_result}")
print(f"A∩B = {intersection_result}")
print(f"A-B = {difference_result}")

# output:
"""
AUB = {1, 2, 3, 4, 5, 6}
A∩B = {3, 4}
A-B = {1, 2}

"""
