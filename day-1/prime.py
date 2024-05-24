#advance(god damn my level)
import math
a=int(input())
prime=True
if a==1:
    print("not a prime number")
else:
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            print("not a prime number")
            prime=False
            break
if prime:
    print("prime number")
#normal
a=int(input())
prime=True
if a==1:
    print("not a prime number")
else:
    for i in range(2,a//2+1):
        if a%i==0:
            print("not a prime number")
            prime=False
            break
if prime:
    print("prime number")
# general
a=int(input())
prime=True
if a==1:
    print("not a prime number")
else:
    for i in range(2,a):
        if a%i==0:
            print("not a prime number")
            prime=False
            break
if prime and a!=1:
    print("prime number")

