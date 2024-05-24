try:
    a=10/0
    c=[]
    c[-1]
    print(c)
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except :
    print("some unknown error occurred")
finally:
    print("final block")

    