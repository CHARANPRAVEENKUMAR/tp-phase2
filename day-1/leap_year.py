year=int(input())
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it's a leap year")
        else:
            print("it's not a leap year")
    else:
        print("it's a leap year")
if year%4==0:
    print("")
else:
    print("")