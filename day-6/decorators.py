# def decorator(fun):
#     def inner():
#         print("inner start")
#         fun()
#         print("inner finish")
#     return inner 
# def x():
#     print("function called")
# i=decorator(x)
# i()
def decorator(fun):
    def inner(a,b):
        print("entered inner")
        fun(a,b)
        print("completed inner")
    return inner
@decorator 
def x(a,b):
    print(a/b)
x(3,1)




