# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def swapf(x,cash,swap):
    i = 0
    j = len(x)-1
    while(i<j):
        if swap>cash:
            break
        if x[i]>x[j]:
            cash-=swap
            x[i]+=x[j]
            x[j]=x[i]-x[j]
            x[i]-=x[j]
            i+=1
        else:
            j-=1
    print(x,cash)
def flipf(x,cash,flip):
    for i,item in enumerate(x):
        if item == 1:
            if flip>cash:
                break
            x[i] = 0
            cash-=flip
    print(x,cash)
n = 4
x = [1,1,1,1]
cash = 7
swap = 1
flip = 2
cnt = x.count(0)
if swap < flip:
    swapf(x,cash,swap)
    flipf(x,cash,flip)
    s = ''.join(map(str,x))
    print(int(s,2))
else:
    flipf()
    swapf()
        