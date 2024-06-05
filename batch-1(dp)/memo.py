n=5
c=0
memo=[0]*(n+1)
def fib(n,memo):
    if memo[n]:
        return memo[n]
    if n<=1:
        return n
    else:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
        return memo[n]
print(fib(4,memo))
print(memo)