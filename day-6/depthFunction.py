def upp(s):
    return s.upper()
def low(s):
    return s.lower() 
def myFun(anFun,s):
    return anFun(s)
a="Charan"
print("upper",myFun(upp,a))
print("lower",myFun(low,a))
