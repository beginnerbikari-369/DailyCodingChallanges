def productArray(ls,n):
    left=[0]*n
    right=[0]*n
    prod=[0]*n
    left[0]=1
    right[n-1]=1
    for i in range(1,n):
        left[i]=ls[i-1]*left[i-1]
    for j in range(n-2,-1,-1):
        right[j]=ls[j+1]*right[j+1]
    for i in range(n):
        prod[i]=left[i]*right[i]
    print(prod)
ls=list(map(int,input().strip().split()))
n=len(ls)
print("the product array is:")
productArray(ls,n)