# Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.

def checkIfSumIs(k, ls):
    for i in range(len(ls)):
        base = ls[0]
        ls.pop(0)
        n = len(ls)
        for j in range(n):
            if(ls[j] + base == k):
                return "true"


if __name__ == "__main__":
    ls = list(map(int, input(
        "enter the space separated list values:").strip().split()))
    k = int(input("enter the sum value:"))
    str = checkIfSumIs(k, ls)
    if(str is not None):
        print(str)
    else:
        print("false")
