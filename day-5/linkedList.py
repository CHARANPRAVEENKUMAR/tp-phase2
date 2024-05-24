class node:
    def __init__(self,a):
        self.a=a
        self.next=None
charan=node(36)
madhur=node(45)
sankar=node(54)
charan.next=madhur
madhur.next=sankar
print("madhurchod",charan.next.a,"sanku",charan.next.next.a)
