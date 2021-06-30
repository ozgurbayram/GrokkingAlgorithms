import sys
# solves RecursionError
sys.setrecursionlimit(1000000)
memo =[0 for i in range(1000000)]

# Fibonnaci calcualtion via memonization method 

def fib(n):
    if n<=1:
        return n
    if memo[n]!=0:
        return memo[n]
    else:
        memo[n] = fib(n-1)+fib(n-2)
        return memo[n]

print(fib(1500))