a=[1,34,5,2,345,3,5]
result=[]
for i in range(len(a)):
    great=-1
    for j in range(i,len(a)):
        if a[j]>a[i]:
            great=a[j]
            break
    result.append(great)
print(result)