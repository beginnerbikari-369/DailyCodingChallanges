import math
if __name__ == "__main__":
    ls = []
    while(True):
        ls.append(int(input("enter any integer: ")))
        ls.sort()
        # print(ls)
        n = len(ls)
        if n % 2 == 0:
            print((ls[(n//2)-1] + ls[n//2])/2)
        else:
            n = int(math.floor(n/2))
            # print(n)
            print(ls[n])
