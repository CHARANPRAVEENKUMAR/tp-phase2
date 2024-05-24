'''import random
a=input()
b=input()
c=["books","chess","anime","maanga","coding"]
print(a,b,"Friendship Percentage",random.randint(1,100),"%")
print(a,"likes",random.choice(c))'''
# year=int(input())
# a year divisible by 4 and not div by 100 if div by 400 and 100 then leap
# if year%4==0: #use 3 ifs
#     if year%100==0:
#         if year%400==0:
#             print("it's a leap year")
#         else:
#             print("not a leap year")
#     else:        
#         print("it's a leap year")
# #second logic use two ifs
# if year%4==0: #use 2 ifs
#     if year%100==0 and year%400==0 or True:
#         print("it's a leap year")
#     else:
#        print("not a leap year") 
# else:
#     print("not a leap year")
# # use 1 if 
# if year%4==0 and year%100!=0 or year%400==0:
#     print('its a leap year')
# else:
#     print('its not a leap year')
# print(2&1)
# a=int(input())
# if a&1==0:
#     print('even')
# else:
#     print('odd')
# number1=int(input())
# cop=number1
# number2=int(input())
# sum=0
# if number1>number2:
#     for i in range(number2):
#         sum+=number1
# else:
#     for i in range(number1):
#         sum+=number2
# print(sum)
# print(int(number1/(1/number2)))
number1=int(input())
cop=number1
number2=int(input())
divisor=0
rem=0
while number1-number2>=0:
    divisor+=1
    number1-=number2
    rem=number1
if cop-(divisor)*number2<0:
    print("rem",cop-(divisor-1)*number2)
    print("div",divisor-1)
else:
    print("rem",cop-(divisor)*number2)
    print("div",divisor)





