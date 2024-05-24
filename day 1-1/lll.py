class Box:
    def __init__(self,data):
        self.data = data
        self.next = None
curr=Box(10)
curr.next = Box(20)
curr.next.next =Box(30)

def printLInkedList(curr):
    while curr!=None:
        print(curr.data)
        curr = curr.next

def insertAtEnd(curr,data):
    newObj= Box(data)
    head= curr
    if curr==None:
        return curr
    
    while curr.next!=None:
        curr = curr.next
    curr.next = newObj
    return head

def insertAtBegin(curr,data):
    newObj= Box(data)

    temp=curr
    if curr==None:
        curr = newObj
    else:
        curr=newObj
        curr.next = temp
    return curr

def deleteAtBegin(curr):
    temp=curr
    if curr==None:
        return curr
    else:
        curr=curr.next 
    return curr

def deleteAtEnd(curr):
    head=curr
    if curr==None:
        return curr
    seclast=None
    while curr.next!=None:
        seclast=curr
        curr =curr.next
    # print(seclast.data,"data")
    seclast.next = None
    return head

def deleteAtSpecificPosition(curr, position):
    i=1
    head=curr
    prev=None
    while curr.next!=None:
        if position==i :
            if prev.next!=None:
                prev.next=prev.next.next
        prev=curr
        curr =curr.next
        i+=1
    return head


def insertAtSpecificPosition(curr, position,data):
    i=1
    head=curr
    prev=None
    while curr.next!=None:
        if position==i:
            newObj=Box(data)
            prev.next=newObj
            newObj.next=curr
        prev=curr
        curr =curr.next
        i+=1
    return head

# printLInkedList(curr)

# curr=deleteAtSpecificPosition(curr,2)
# printLInkedList(curr)
# curr=insertAtEnd(curr,5)
# # printLInkedList(curr)

# curr=insertAtBegin(curr,3)

# curr=insertAtSpecificPosition(curr,2,123)
curr=deleteAtEnd(curr)

printLInkedList(curr)