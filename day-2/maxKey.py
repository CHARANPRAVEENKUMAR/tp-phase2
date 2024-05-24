l=["i am charan","i am praveen","i am kumar","i am charan praveen kumar"]
for i in range(len(l)):
    l[i]=l[i].split()
print(max(l,key=len))

# a=[1,2,3,4,5,6,7,8,9,10]
# print(max(a))