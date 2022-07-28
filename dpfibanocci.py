#Using Dynamic Programming finding nth fibanocci number

Gowtham = {}
Gowtham[0]=0
Gowtham[1]=1
def fib(n):
    if n in Gowtham.keys():
        return Gowtham[n]
    else:
        Gowtham[n]= fib(n-1)+fib(n-2)
        return Gowtham[n]
print(fib(9))