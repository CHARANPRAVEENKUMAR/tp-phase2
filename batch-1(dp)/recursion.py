# n=int(input())
# for i in n:
#     print(i)
n=int(input())
def recursive(n):
    if n<=0:
        return 
    else:
        print(n%10)
        n=n//10
        recursive(n)
recursive(n)