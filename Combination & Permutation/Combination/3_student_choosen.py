"""
In how many ways can 3 students be chosen from a group of 10?
"""
# a function to calculate the factorial of a given number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)
    
# a function to calculate the combination
def combination(no_stu, group):
    return factorial(no_group) / (factorial(no_stu) * factorial(group-no_stu))

# intializing the total no. of student and the total number of group 
no_student = 3
no_group = 10

# calling the combination() function
result = combination(no_student, no_group)

# printing out the result
print(f"Combination C({no_group, no_student}) = {result}")