#stack can be implemented by array and linked list but highly prefer using array 
stacky=[]
def push(stacky,data):
    stacky.insert(0,data)
def pop(stacky):
    if len(stacky)==0:
        return 
    stacky.pop(0)
def printAll(stacky):
    for i in stacky:
        print(i)
stacky=push(stacky,3)
stacky=push(stacky,5)
stacky=pop(stacky)
printAll(stacky)