"""
Prove that {2,3}⊆{1,2,3,4}. Find the power set of {1,2}.

"""
# initializing set A and B
A = {2, 3}
B = {1, 2, 3, 4}
S = {1, 2}

result = A.issubset(B)
if result == True:
    print(f"A = {A} is the subset of B = {B}")
else:
    print(f"A = {A} is not the subset of B = {B}")

# finding out the power of set (1, 2)
power_set=[[]]
for i in S:
    new_set = []
    for j in power_set:
        new_set.append(j + [i])
    power_set.extend(new_set)

print(power_set)
# output: [[], [1], [2], [1, 2]]