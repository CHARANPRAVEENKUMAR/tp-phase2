# 10 15 20 
class Box:
    def __init__(self,data):
        self.data=data
        lself.next=None

head=None
temp=head
obj1=None

for i in range(51,61):

    if obj1==None:
        obj1=Box(i)
        head=obj1
        temp=head
    else:
        obj1.next=Box(i)
        obj1=obj1.next

while(temp!=None):
    print(temp.data)
    temp=temp.next