# a={'name':'charan','favourite':"chess"}
# a['age']=27
# print(a)
# print(id(a))
# print(a.keys())
# print(a.values())
# print(a.items())
# print("dictionary items")
# for i in a:
#     print(i, a[i])
# print("dictionary items another way ")
# for i,j in a.items():
#     print(i,j)
dic={1:2,2:3,4:5,5:6}
print(dic.pop(1),dic) #delete the item with an index pass as argument
print(dic.popitem(),dic) #deletes and returns the last item 
print(dic.popitem(1),dic) #raises an error it wont take any arguments
print(dic.get(2),dic) #get the item with that index
print(dic.setdefault(0),dic) #create an item with index(argument)  leaving value None
