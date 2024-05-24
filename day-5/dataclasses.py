from dataclasses import dataclass
@dataclass() #decorator
class A:
    a:int
    b:int 
    c:str 
d=A(1,2,"charan")
print(d.a,d.b,d.c)