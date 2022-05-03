# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
def productArray(ls, n):
    left = [0]*n
    right = [0]*n
    prod = [0]*n
    left[0] = 1
    right[n-1] = 1
    for i in range(1, n):
        left[i] = ls[i-1]*left[i-1]
    for j in range(n-2, -1, -1):
        right[j] = ls[j+1]*right[j+1]
    for i in range(n):
        prod[i] = left[i]*right[i]
    print(prod)


ls = list(map(int, input().strip().split()))
n = len(ls)
print("the product array is:")
productArray(ls, n)
