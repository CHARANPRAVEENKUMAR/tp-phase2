# write a python program to accept a string as an input and print the character which occured maximum times withun given strnig 
a=input()
d=dict()
for i in a:
    if i.isalpha and i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
req=0
re=''
for i in d:
    if d[i]== req and ord(re)>ord(i):
        re=i
        req=d[i] 
    if d[i]> req:
        re=i
        req=d[i]
print(re)   