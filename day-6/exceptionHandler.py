def fun(l):
    try:
        n=len(l)
        a=l[0]//l[n]
    except ZeroDivisionError :
        print("zero divison error")
    finally:
        print("final from function called")
try:
    l=[1,2,3,4,5]
    fun(l)
except IndexError:
    print("index error")
finally:
    print("end of the finally")





