def checkIfSumIs(k,ls):
    for i in range(len(ls)):
        base = ls[0]
        ls.pop(0)
        n=len(ls)
        for j in range(n):
            if(ls[j] + base == k):
                return "true"
if __name__=="__main__":
    ls = list(map(int,input("enter the space separated list values:").strip().split()))
    k = int(input("enter the sum value:"))
    str = checkIfSumIs(k,ls)
    if(str != None):
        print(str)
    else:
        print("false")