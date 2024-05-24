class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None
def dequeue(curr): #delete at the end of the queue\
    head=curr
    prev=None
    while curr.next!=None:
        prev=curr
        curr=curr.next
    prev.next=None
    return head
def enqueue(curr,data): #inseyr at begining of the queue
    head=curr
    newNode=Node(data)
    head=newNode
    head.next=curr
    return head
def printAll(curr):
    while curr!=None:
        print(curr.data)
        curr=curr.next
head=None
head=enqueue(head,4)
head=enqueue(head,5)
printAll(head)
head=dequeue(head)
printAll(head)