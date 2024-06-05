coins=[1,2,5]
amount=int(input())
memo=[0]*(amount+1)
for i in coins:
    for j in range(i,amount+1):
        memo[j]=memo[j-i]+1
print(memo[amount])
#possi el ways to get the required amount