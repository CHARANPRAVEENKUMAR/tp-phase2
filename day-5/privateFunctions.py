class A:
    def __init__(self):
        print("constructor")
    def fun1(self):
        print("funcrion1 from A")
    def __fun2(self): # to make a function private use double underscore before it.It restricts indirect calls from object 
        print("function2 from A")
class B(A):
    def __init__(self):
        print("constructor")
    def fun3(self):
        print("function3 from B")
b1=B()
b1.fun1() 
b1.fun2() #raises an error
