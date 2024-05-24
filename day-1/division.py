num1=int(input())
num2=int(input())
quotient=0
while num1-num2>=0:
    num1-=num2;   
    quotient+=1
print("quotient",quotient) 
print("rem",num1)