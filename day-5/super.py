# class A:
#     def __init__(self,a):
#         self.a=a
#         print(self.a)
#     def fun1(self):
#         print("function1 from A")
#         print("a value is ",self.a)
#     def fun2(self):
#         print("function2 from A")
# class B(A):
#     def fun3(self):
#         print("function3 from B")
#         super().fun1() #call parent class functions
# b=B(3)
# b.fun3()
class A:
    abc=12 #static variable
    def fun1(self):
        c=5 #local variable
        self.d=10 #instance variable
a1=A()
a1.fun1() #intiailse the d value
print(a1.abc)
print(a1.d)




